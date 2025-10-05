import random
import json
from typing import Dict, List

class SignLanguageAvatar:
    """Handles sign language avatar functionality for F1 commentary"""
    
    def __init__(self):
        self.sign_database = {
            "start": "assets/sign_start.gif",
            "win": "assets/sign_win.gif", 
            "crash": "assets/sign_crash.gif",
            "overtake": "assets/sign_overtake.gif",
            "pit": "assets/sign_pit.gif",
            "finish": "assets/sign_finish.gif",
            "safety": "assets/sign_safety.gif",
            "car": "assets/sign_car.gif",
            "race": "assets/sign_race.gif",
            "fast": "assets/sign_fast.gif"
        }
        
        self.gesture_mapping = {
            "start": "Hands moving forward",
            "win": "Victory gesture with both hands",
            "crash": "Hands colliding motion",
            "overtake": "One hand passing another",
            "pit": "Circular motion with hands",
            "finish": "Hands crossing finish line",
            "safety": "Hands forming safety symbol",
            "car": "Steering wheel motion",
            "race": "Running motion",
            "fast": "Quick hand movements"
        }
    
    def generate_sign_language(self, commentary: str) -> Dict:
        """Generate sign language animation for commentary"""
        words = commentary.lower().split()
        detected_words = []
        
        for word in words:
            if word in self.sign_database:
                detected_words.append(word)
        
        return {
            "detected_words": detected_words,
            "animation_sequence": [self.sign_database[word] for word in detected_words],
            "gesture_descriptions": [self.gesture_mapping[word] for word in detected_words]
        }
    
    def get_word_mapping(self, word: str) -> str:
        """Get gesture description for a specific word"""
        return self.gesture_mapping.get(word.lower(), "Generic gesture")
    
    def create_avatar_animation(self, words: List[str]) -> str:
        """Create a combined animation for multiple words"""
        # This would combine multiple sign language animations
        return "assets/combined_sign_animation.gif"


