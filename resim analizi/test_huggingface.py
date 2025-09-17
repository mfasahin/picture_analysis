import requests
import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# Token'ı al
token = os.getenv("HUGGINGFACE_API_KEY")

print(f"Token bulundu mu: {'Evet' if token else 'Hayır'}")
if token:
    print(f"Token uzunluğu: {len(token)} karakter")
    print(f"Token başlangıcı: {token[:10]}...")

# Test isteği gönder
if token:
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # Basit bir test isteği
    model = "nlpconnect/vit-gpt2-image-captioning"
    api_url = f"https://api-inference.huggingface.co/nlpconnect/vit-gpt2-image-captioning"
    
    try:
        response = requests.get(api_url, headers=headers)
        print(f"API yanıt kodu: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Token geçerli!")
        elif response.status_code == 401:
            print("❌ Token geçersiz veya yetkisiz")
        elif response.status_code == 403:
            print("❌ Token yetkisi yetersiz")
        else:
            print(f"❌ Beklenmeyen hata: {response.status_code}")
            print(f"Hata mesajı: {response.text}")
            
    except Exception as e:
        print(f"❌ Bağlantı hatası: {e}")
else:
    print("❌ Token bulunamadı! .env dosyasını kontrol edin.")

# Yeni test için yeni kod
if token:
    headers = {"Authorization": f"Bearer {token}"}
    api_url = f"https://api-inference.huggingface.co/nlpconnect/vit-gpt2-image-captioning"
    response = requests.get(api_url, headers=headers)
    print(response.status_code)
    print(response.text) 