from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

class KnowledgeBase:
    def __init__(self, data_file):
        self.data = self._load_data(data_file)
        self.vectorizer = TfidfVectorizer()
        self._create_index()
    
    def _load_data(self, data_file):
        with open(data_file) as f:
            return json.load(f)
    
    def _create_index(self):
        self.documents = []
        self.metadata = []
        
        for restaurant in self.data:
            for item in restaurant['menu']:
                text = f"{item['name']} {item.get('description', '')}"
                self.documents.append(text)
                self.metadata.append({
                    'restaurant': restaurant['name'],
                    'item': item
                })
        
        self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)
    
    def search(self, query, top_k=3):
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix)[0]
        
        results = []
        for i, score in enumerate(similarities):
            if score > 0.2:  # Lower threshold for TF-IDF
                results.append({
                    **self.metadata[i],
                    'score': score
                })
        
        return sorted(results, key=lambda x: x['score'], reverse=True)[:top_k] 