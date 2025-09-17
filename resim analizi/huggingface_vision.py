import requests
import base64
import json
from config import HUGGINGFACE_API_KEY, HUGGINGFACE_BASE_URL

class HuggingFaceVision:
    def __init__(self):
        self.api_key = "HUGGINGFACE_API_KEY"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def analyze_image_from_url(self, image_url, analysis_type="general"):
        """URL'den resim analizi yap"""
        try:
            # Resmi URL'den indir
            response = requests.get(image_url)
            response.raise_for_status()
            
            # Resmi base64'e çevir
            image_data = base64.b64encode(response.content).decode('utf-8')
            
            # Analiz türüne göre model seç
            if analysis_type == "objects":
                model = "microsoft/git-base-coco"  # Nesne tespiti için
            elif analysis_type == "emotions":
                model = "microsoft/DialoGPT-medium"  # Duygu analizi için (geçici)
            else:
                model = "microsoft/git-base-coco"  # Genel analiz için
            
            # Hugging Face API'ye istek gönder
            api_url = f"{HUGGINGFACE_BASE_URL}/{model}"
            
            payload = {
                "inputs": f"data:image/jpeg;base64,{image_data}",
                "parameters": {
                    "max_length": 100,
                    "do_sample": True,
                    "temperature": 0.7
                }
            }
            
            response = requests.post(api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            
            # Sonucu işle
            if isinstance(result, list) and len(result) > 0:
                analysis = result[0].get('generated_text', 'Analiz tamamlandı.')
            else:
                analysis = str(result)
            
            return {
                "success": True,
                "analysis": analysis,
                "model": model
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "analysis": "Resim analizi sırasında bir hata oluştu."
            }
    
    def generate_tags(self, image_url):
        """Resim için etiketler oluştur"""
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            
            image_data = base64.b64encode(response.content).decode('utf-8')
            
            # Etiket oluşturma için uygun model
            model = "microsoft/git-base-coco"
            api_url = f"{HUGGINGFACE_BASE_URL}/{model}"
            
            payload = {
                "inputs": f"data:image/jpeg;base64,{image_data}",
                "parameters": {
                    "max_length": 50,
                    "do_sample": True,
                    "temperature": 0.5
                }
            }
            
            response = requests.post(api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            
            if isinstance(result, list) and len(result) > 0:
                tags = result[0].get('generated_text', 'Etiketler oluşturulamadı.')
            else:
                tags = str(result)
            
            return {
                "success": True,
                "tags": tags
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "tags": "Etiket oluşturulamadı."
            }
    
    def simple_image_description(self, image_url):
        """Basit resim açıklaması"""
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            
            image_data = base64.b64encode(response.content).decode('utf-8')
            
            # Basit açıklama için model
            model = "microsoft/git-base-coco"
            api_url = f"{HUGGINGFACE_BASE_URL}/{model}"
            
            payload = {
                "inputs": f"data:image/jpeg;base64,{image_data}"
            }
            
            response = requests.post(api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            
            if isinstance(result, list) and len(result) > 0:
                description = result[0].get('generated_text', 'Açıklama oluşturulamadı.')
            else:
                description = str(result)
            
            return {
                "success": True,
                "description": description
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "description": "Açıklama oluşturulamadı."
            } 