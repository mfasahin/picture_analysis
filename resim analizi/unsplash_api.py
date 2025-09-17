import requests
from config import UNSPLASH_ACCESS_KEY, UNSPLASH_SEARCH_URL, UNSPLASH_RANDOM_URL

class UnsplashAPI:
    def __init__(self):
        self.access_key = UNSPLASH_ACCESS_KEY
        self.headers = {
            "Authorization": f"Client-ID {self.access_key}"
        }
    
    def search_photos(self, query, per_page=10):
        """Belirli bir arama terimi ile fotoğraf ara"""
        params = {
            "query": query,
            "per_page": per_page,
            "orientation": "landscape"
        }
        
        try:
            response = requests.get(UNSPLASH_SEARCH_URL, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            photos = []
            for photo in data.get("results", []):
                photos.append({
                    "id": photo["id"],
                    "url": photo["urls"]["regular"],
                    "thumb": photo["urls"]["thumb"],
                    "alt": photo.get("alt_description", "No description"),
                    "photographer": photo["user"]["name"],
                    "download_url": photo["links"]["download"]
                })
            
            return photos
        except requests.RequestException as e:
            print(f"Unsplash API hatası: {e}")
            return []
    
    def get_random_photos(self, count=10, query=None):
        """Rastgele fotoğraflar getir"""
        params = {
            "count": count,
            "orientation": "landscape"
        }
        
        if query:
            params["query"] = query
        
        try:
            response = requests.get(UNSPLASH_RANDOM_URL, headers=self.headers, params=params)
            response.raise_for_status()
            photos = response.json()
            
            result = []
            for photo in photos:
                result.append({
                    "id": photo["id"],
                    "url": photo["urls"]["regular"],
                    "thumb": photo["urls"]["thumb"],
                    "alt": photo.get("alt_description", "No description"),
                    "photographer": photo["user"]["name"],
                    "download_url": photo["links"]["download"]
                })
            
            return result
        except requests.RequestException as e:
            print(f"Unsplash API hatası: {e}")
            return [] 