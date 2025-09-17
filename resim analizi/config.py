import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# API Anahtarları
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

# Unsplash API URL'leri
UNSPLASH_BASE_URL = "https://api.unsplash.com"
UNSPLASH_SEARCH_URL = f"{UNSPLASH_BASE_URL}/search/photos"
UNSPLASH_RANDOM_URL = f"{UNSPLASH_BASE_URL}/photos/random"

# Hugging Face API URL'leri
HUGGINGFACE_BASE_URL = "https://api-inference.huggingface.co/models"
IMAGE_ANALYSIS_MODEL = "microsoft/DialoGPT-medium"  # Geçici, resim analizi için daha uygun model kullanacağız 