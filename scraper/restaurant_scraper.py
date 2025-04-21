from bs4 import BeautifulSoup
import requests
import json
from urllib.robotparser import RobotFileParser
import time

class RestaurantScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.data = []
    
    def check_robots_txt(self, base_url):
        rp = RobotFileParser()
        rp.set_url(f"{base_url}/robots.txt")
        rp.read()
        return rp
    
    def scrape_restaurant(self, url):
        try:
            rp = self.check_robots_txt(url)
            if not rp.can_fetch('*', url):
                print(f"Skipping {url} due to robots.txt restrictions")
                return None
            
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            restaurant = {
                'name': self._extract_name(soup),
                'location': self._extract_location(soup),
                'menu': self._extract_menu(soup),
                'hours': self._extract_hours(soup),
                'contact': self._extract_contact(soup)
            }
            
            self.data.append(restaurant)
            time.sleep(2)  # Be polite with delay between requests
            return restaurant
            
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return None
    
    def _extract_name(self, soup):
        # Implementation for specific website
        pass
    
    def _extract_location(self, soup):
        # Implementation for specific website
        pass
    
    def _extract_menu(self, soup):
        menu_items = []
        # Common patterns for Indian restaurant menus
        for item in soup.find_all(class_=['menu-item', 'dish-card']):
            try:
                menu_items.append({
                    'name': self._clean_text(item.find(['h3', '.dish-name'])),
                    'description': self._clean_text(item.find(['p', '.dish-desc'])),
                    'price': self._clean_text(item.find(['span', '.price'])),
                    'tags': self._extract_indian_tags(item)
                })
            except Exception as e:
                continue
        return menu_items
    
    def _extract_indian_tags(self, item):
        tags = []
        # Common Indian food tags
        for tag_class in ['veg', 'non-veg', 'spicy', 'mild', 'jain', 'gluten-free']:
            if item.find(class_=tag_class):
                tags.append(tag_class.replace('-', ' '))
        return tags
    
    def _extract_hours(self, soup):
        # Implementation for specific website
        pass
    
    def _extract_contact(self, soup):
        # Implementation for specific website
        pass
    
    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=2) 