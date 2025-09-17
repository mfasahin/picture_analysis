# 🖼️ Akıllı Resim Analiz Uygulaması

Yapay zeka ve ücretsiz API'ler kullanarak geliştirilmiş modern bir resim analiz uygulaması. Bu uygulama Unsplash API'den resimler çeker ve Hugging Face API ile detaylı analiz yapar.

## ✨ Özellikler

- 🔍 **Akıllı Resim Arama**: Unsplash API ile anahtar kelime bazlı resim arama
- 🎲 **Rastgele Resimler**: Kategori bazlı rastgele resim getirme
- 🤖 **AI Analizi**: Hugging Face API ile detaylı resim analizi
- 🏷️ **Otomatik Etiketleme**: Resimler için AI destekli etiket oluşturma
- 🎨 **Modern Arayüz**: Streamlit ile güzel ve kullanıcı dostu tasarım
- 📱 **Responsive Tasarım**: Mobil ve masaüstü uyumlu
- 🆓 **Tamamen Ücretsiz**: Tüm API'ler ücretsiz!

## 🚀 Kurulum

### 1. Gereksinimler

- Python 3.8+
- Hugging Face API Key (ücretsiz)
- Unsplash API Key (ücretsiz)

### 2. Projeyi İndirin

```bash
git clone <repository-url>
cd akilli-resim-analiz
```

### 3. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### 4. API Anahtarlarını Ayarlayın

1. **Hugging Face API Key** alın: https://huggingface.co/settings/tokens
2. **Unsplash API Key** alın: https://unsplash.com/developers
3. Proje dizininde `.env` dosyası oluşturun:

```env
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
UNSPLASH_ACCESS_KEY=your_unsplash_access_key_here
```

### 5. Uygulamayı Çalıştırın

```bash
streamlit run app.py
```

## 📖 Kullanım

### Resim Arama
1. "📸 Resim Arama" sekmesine gidin
2. Arama terimi girin (örn: doğa, şehir, portre)
3. Resim sayısını belirleyin
4. "🔍 Ara" butonuna tıklayın
5. İstediğiniz resmi seçip "🔍 Analiz Et" butonuna tıklayın

### Rastgele Resimler
1. "🎲 Rastgele Resimler" sekmesine gidin
2. İsteğe bağlı kategori belirtin
3. Resim sayısını seçin
4. "🎲 Rastgele Getir" butonuna tıklayın

### Analiz Türleri
- **Genel Analiz**: Kapsamlı resim analizi
- **Nesne Tespiti**: Resimdeki nesneleri listeler
- **Basit Açıklama**: Kısa resim açıklaması

## 🛠️ Teknolojiler

- **Frontend**: Streamlit
- **AI**: Hugging Face API (Açık kaynak modeller)
- **Resim API**: Unsplash API
- **Python Kütüphaneleri**:
  - `streamlit`: Web arayüzü
  - `transformers`: Hugging Face modelleri
  - `torch`: PyTorch backend
  - `requests`: HTTP istekleri
  - `Pillow`: Resim işleme
  - `python-dotenv`: Environment değişkenleri

## 📁 Proje Yapısı

```
akilli-resim-analiz/
├── app.py                 # Ana Streamlit uygulaması
├── config.py              # Konfigürasyon ve API anahtarları
├── unsplash_api.py        # Unsplash API entegrasyonu
├── huggingface_vision.py  # Hugging Face API entegrasyonu
├── requirements.txt       # Python bağımlılıkları
├── README.md             # Proje dokümantasyonu
└── .env                  # API anahtarları (kullanıcı oluşturur)
```

## 🔧 API Limitleri

### Hugging Face API
- Ücretsiz plan: 30,000 istek/ay
- Açık kaynak modeller
- Tamamen ücretsiz!

### Unsplash API
- Ücretsiz plan: 5,000 istek/ay
- Resim indirme: 50/ay
- Demo uygulamalar için yeterli

## 🎯 Gelecek Özellikler

- [ ] Kendi resim yükleme özelliği
- [ ] Resim karşılaştırma
- [ ] Analiz geçmişi
- [ ] Çoklu dil desteği
- [ ] Resim filtreleme
- [ ] Analiz raporu indirme
- [ ] Daha fazla AI modeli entegrasyonu

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 🙏 Teşekkürler

- [Hugging Face](https://huggingface.co/) - Açık kaynak AI modelleri
- [Unsplash](https://unsplash.com/) - Resim API
- [Streamlit](https://streamlit.io/) - Web framework

## 📞 İletişim

Sorularınız için issue açabilir veya iletişime geçebilirsiniz.

---

**Not**: Bu uygulama tamamen ücretsiz API'ler kullanır ve eğitim amaçlı geliştirilmiştir. 

```python
from PIL import Image

raw_image = Image.open("kendi_resminiz.jpg").convert('RGB')
``` 