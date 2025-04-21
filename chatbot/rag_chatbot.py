from knowledge_base.processor import KnowledgeBase
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

class RestaurantChatbot:
    def __init__(self, knowledge_base_path):
        self.kb = KnowledgeBase(knowledge_base_path)
        self.conversation_history = []
    
    def generate_response(self, query):
        retrieved_info = self.kb.search(query)
        
        if not retrieved_info:
            return "I couldn't find any relevant information about Indian restaurants matching your query."
        
        response = "Here are some Indian restaurants that match your query:\n"
        for item in retrieved_info:
            response += f"\n🍛 **{item['restaurant']}** - {item['item']['name']}"
            
            if 'description' in item['item']:
                response += f"\n   _{item['item']['description']}_"
            
            if 'price' in item['item']:
                response += f"\n   💵 Price: {item['item']['price']}"
            
            if 'tags' in item['item']:
                tags = " | ".join([f"#{tag}" for tag in item['item']['tags']])
                response += f"\n   🏷️ {tags}"
        
        # Update conversation history
        self.conversation_history.append({
            'query': query,
            'response': response,
            'context': retrieved_info
        })
        
        return response
    
    def get_history(self):
        return self.conversation_history 