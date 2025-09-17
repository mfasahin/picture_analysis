import streamlit as st
import requests
from PIL import Image
import io
from unsplash_api import UnsplashAPI
from huggingface_vision import HuggingFaceVision
from config import HUGGINGFACE_API_KEY, UNSPLASH_ACCESS_KEY
from transformers import BlipProcessor, BlipForConditionalGeneration

# Sayfa konfigürasyonu
st.set_page_config(
    page_title="Akıllı Resim Analiz Uygulaması",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS stilleri
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .photo-card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        background: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .analysis-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .tag-box {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #1f77b4;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    .free-badge {
        background: #28a745;
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Ana başlık
st.markdown('<h1 class="main-header">🖼️ Akıllı Resim Analiz Uygulaması</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Yapay Zeka ile Resim Analizi ve Etiketleme <span class="free-badge">ÜCRETSİZ</span></p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Ayarlar")
    
    # API anahtarları kontrolü
    if not HUGGINGFACE_API_KEY:
        st.error("❌ Hugging Face API anahtarı bulunamadı!")
        st.info("Lütfen .env dosyasına HUGGINGFACE_API_KEY ekleyin")
    
    if not UNSPLASH_ACCESS_KEY:
        st.error("❌ Unsplash API anahtarı bulunamadı!")
        st.info("Lütfen .env dosyasına UNSPLASH_ACCESS_KEY ekleyin")
    
    if HUGGINGFACE_API_KEY and UNSPLASH_ACCESS_KEY:
        st.success("✅ API anahtarları hazır!")
    
    st.divider()
    
    # Analiz türü seçimi
    st.subheader("🔍 Analiz Türü")
    analysis_type = st.selectbox(
        "Hangi tür analiz yapmak istiyorsunuz?",
        ["Genel Analiz", "Nesne Tespiti", "Basit Açıklama"],
        help="Genel Analiz: Kapsamlı resim analizi\nNesne Tespiti: Resimdeki nesneleri listeler\nBasit Açıklama: Kısa resim açıklaması"
    )
    
    # Analiz türü mapping
    analysis_mapping = {
        "Genel Analiz": "general",
        "Nesne Tespiti": "objects", 
        "Basit Açıklama": "simple"
    }
    
    st.divider()
    
    # Bilgi kutusu
    st.info("""
    **🆓 Ücretsiz API Kullanımı:**
    - Hugging Face: 30,000 istek/ay
    - Unsplash: 5,000 istek/ay
    - Tamamen ücretsiz!
    """)

# Ana içerik
if HUGGINGFACE_API_KEY and UNSPLASH_ACCESS_KEY:
    # Tab'lar
    tab1, tab2, tab3 = st.tabs(["📸 Resim Arama", "🎲 Rastgele Resimler", "📤 Kendi Resminizi Yükleyin"])
    
    with tab1:
        st.header("🔍 Resim Arama")
        
        # Arama formu
        col1, col2 = st.columns([3, 1])
        with col1:
            search_query = st.text_input("Arama terimi girin:", placeholder="örn: doğa, şehir, portre...")
        with col2:
            search_count = st.number_input("Resim sayısı:", min_value=1, max_value=20, value=6)
        
        if st.button("🔍 Ara", use_container_width=True):
            if search_query:
                with st.spinner("Resimler aranıyor..."):
                    unsplash = UnsplashAPI()
                    photos = unsplash.search_photos(search_query, search_count)
                    
                    if photos:
                        st.success(f"✅ {len(photos)} resim bulundu!")
                        
                        # Resimleri grid halinde göster
                        cols = st.columns(3)
                        for i, photo in enumerate(photos):
                            with cols[i % 3]:
                                with st.container():
                                    st.image(photo["thumb"], caption=f"📸 {photo['photographer']}", use_container_width=True)
                                    
                                    if st.button(f"🔍 Analiz Et", key=f"analyze_{i}"):
                                        with st.spinner("Resim analiz ediliyor..."):
                                            vision = HuggingFaceVision()
                                            
                                            if analysis_mapping[analysis_type] == "simple":
                                                result = vision.simple_image_description(photo["url"])
                                                if result["success"]:
                                                    st.markdown('<div class="analysis-box">', unsafe_allow_html=True)
                                                    st.markdown("### 🤖 AI Açıklaması")
                                                    st.write(result["description"])
                                                    st.markdown('</div>', unsafe_allow_html=True)
                                                else:
                                                    st.error(f"Analiz hatası: {result['error']}")
                                            else:
                                                response = requests.get(photo["url"])
                                                image = Image.open(io.BytesIO(response.content)).convert('RGB')
                                                
                                                analysis = vision.analyze_image_from_url(
                                                    photo["url"], 
                                                    analysis_mapping[analysis_type]
                                                )
                                                
                                                if analysis["success"]:
                                                    st.markdown('<div class="analysis-box">', unsafe_allow_html=True)
                                                    st.markdown("### 🤖 AI Analizi")
                                                    st.write(analysis["analysis"])
                                                    st.markdown('</div>', unsafe_allow_html=True)
                                                    
                                                    # Etiketler
                                                    tags_result = vision.generate_tags(photo["url"])
                                                    if tags_result["success"]:
                                                        st.markdown('<div class="tag-box">', unsafe_allow_html=True)
                                                        st.markdown("### 🏷️ Etiketler")
                                                        st.write(tags_result["tags"])
                                                        st.markdown('</div>', unsafe_allow_html=True)
                                                else:
                                                    st.error(f"Analiz hatası: {analysis['error']}")
                                                    st.write(analysis)  # Hata detayını göster
                    else:
                        st.warning("❌ Arama sonucu bulunamadı.")
            else:
                st.warning("Lütfen bir arama terimi girin.")
    
    with tab2:
        st.header("🎲 Rastgele Resimler")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            random_query = st.text_input("Kategori (opsiyonel):", placeholder="örn: manzara, hayvan...")
        with col2:
            random_count = st.number_input("Resim sayısı:", min_value=1, max_value=10, value=6, key="random_count")
        
        if st.button("🎲 Rastgele Getir", use_container_width=True):
            with st.spinner("Rastgele resimler getiriliyor..."):
                unsplash = UnsplashAPI()
                photos = unsplash.get_random_photos(random_count, random_query if random_query else None)
                
                if photos:
                    st.success(f"✅ {len(photos)} rastgele resim getirildi!")
                    
                    # Resimleri grid halinde göster
                    cols = st.columns(3)
                    for i, photo in enumerate(photos):
                        with cols[i % 3]:
                            with st.container():
                                st.image(photo["thumb"], caption=f"📸 {photo['photographer']}", use_container_width=True)
                                
                                if st.button(f"🔍 Analiz Et", key=f"random_analyze_{i}"):
                                    with st.spinner("Resim analiz ediliyor..."):
                                        vision = HuggingFaceVision()
                                        
                                        if analysis_mapping[analysis_type] == "simple":
                                            result = vision.simple_image_description(photo["url"])
                                            if result["success"]:
                                                st.markdown('<div class="analysis-box">', unsafe_allow_html=True)
                                                st.markdown("### 🤖 AI Açıklaması")
                                                st.write(result["description"])
                                                st.markdown('</div>', unsafe_allow_html=True)
                                            else:
                                                st.error(f"Analiz hatası: {result['error']}")
                                        else:
                                            response = requests.get(photo["url"])
                                            image = Image.open(io.BytesIO(response.content)).convert('RGB')
                                            
                                            analysis = vision.analyze_image_from_url(
                                                photo["url"], 
                                                analysis_mapping[analysis_type]
                                            )
                                            
                                            if analysis["success"]:
                                                st.markdown('<div class="analysis-box">', unsafe_allow_html=True)
                                                st.markdown("### 🤖 AI Analizi")
                                                st.write(analysis["analysis"])
                                                st.markdown('</div>', unsafe_allow_html=True)
                                                
                                                # Etiketler
                                                tags_result = vision.generate_tags(photo["url"])
                                                if tags_result["success"]:
                                                    st.markdown('<div class="tag-box">', unsafe_allow_html=True)
                                                    st.markdown("### 🏷️ Etiketler")
                                                    st.write(tags_result["tags"])
                                                    st.markdown('</div>', unsafe_allow_html=True)
                                            else:
                                                st.error(f"Analiz hatası: {analysis['error']}")
                                                st.write(analysis)  # Hata detayını göster
                else:
                    st.warning("❌ Rastgele resimler getirilemedi.")
    
    with tab3:
        st.header("📤 Kendi Resminizi Yükleyin")
        
        uploaded_file = st.file_uploader(
            "Resim dosyası seçin:",
            type=['png', 'jpg', 'jpeg'],
            help="PNG, JPG veya JPEG formatında resim yükleyebilirsiniz"
        )
        
        if uploaded_file is not None:
            # Resmi göster
            image = Image.open(uploaded_file)
            st.image(image, caption="Yüklenen resim", use_container_width=True)
            
            if st.button("🔍 Resmi Analiz Et", use_container_width=True):
                with st.spinner("Resim analiz ediliyor..."):
                    st.warning("⚠️ Bu özellik için resmin bir URL'de olması gerekiyor. Lütfen resmi bir URL'ye yükleyip o URL'yi kullanın.")
                    
                    st.info("Bu özellik geliştirme aşamasında. Lütfen şimdilik URL tabanlı resimler kullanın.")

else:
    st.error("❌ API anahtarları eksik!")
    st.markdown("""
    ### 🔑 API Anahtarlarını Ayarlayın
    
    1. **Hugging Face API Key** alın: https://huggingface.co/settings/tokens
    2. **Unsplash API Key** alın: https://unsplash.com/developers
    3. Proje dizininde `.env` dosyası oluşturun:
    
    ```
    HUGGINGFACE_API_KEY=your_huggingface_api_key_here
    UNSPLASH_ACCESS_KEY=your_unsplash_access_key_here
    ```
    
    4. Uygulamayı yeniden başlatın
    
    **🆓 Her iki API de ücretsizdir!**
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem;">
    🤖 Hugging Face API + 📸 Unsplash API ile geliştirildi<br>
    💡 Yapay zeka destekli resim analizi uygulaması - <strong>ÜCRETSİZ!</strong>
</div>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_model()

st.title("Yerel BLIP Görsel Açıklama Uygulaması")

uploaded_file = st.file_uploader("Bir resim yükleyin", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Yüklenen Resim", use_container_width=True)
    if st.button("Analiz Et"):
        with st.spinner("Analiz ediliyor..."):
            try:
                inputs = processor(image, return_tensors="pt")
                out = model.generate(**inputs)
                caption = processor.decode(out[0], skip_special_tokens=True)
                st.success("Açıklama: " + caption)
            except Exception as e:
                st.error(f"Bir hata oluştu: {e}") 