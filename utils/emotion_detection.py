import cv2
import numpy as np
from typing import Dict, List, Tuple
import random

class EmotionDetector:
    """Handles emotion detection and mirroring functionality"""
    
    def __init__(self):
        self.emotions = ["happy", "excited", "worried", "neutral", "surprised", "stressed"]
        self.emotion_intensities = {
            "happy": 0.8,
            "excited": 0.9,
            "worried": 0.6,
            "neutral": 0.4,
            "surprised": 0.7,
            "stressed": 0.5
        }
        
        self.ai_lonso_responses = {
            "happy": "😊 Ai.lonso is smiling with joy!",
            "excited": "🤩 Ai.lonso is jumping with excitement!",
            "worried": "😟 Ai.lonso looks concerned",
            "neutral": "😐 Ai.lonso is calm and focused",
            "surprised": "😲 Ai.lonso is surprised!",
            "stressed": "😰 Ai.lonso feels the pressure too"
        }
    
    def detect_emotion_from_image(self, image: np.ndarray) -> Tuple[str, float]:
        """Detect emotion from an image (simulated)"""
        # In a real implementation, this would use a trained emotion detection model
        # For demo purposes, we'll return random emotions
        emotion = random.choice(self.emotions)
        intensity = self.emotion_intensities[emotion]
        
        return emotion, intensity
    
    def detect_emotion_from_webcam(self) -> Tuple[str, float]:
        """Detect emotion from webcam feed (simulated)"""
        # Simulate webcam emotion detection
        emotion = random.choice(self.emotions)
        intensity = random.uniform(0.3, 1.0)
        
        return emotion, intensity
    
    def get_ai_lonso_response(self, emotion: str) -> str:
        """Get Ai.lonso's response to detected emotion"""
        return self.ai_lonso_responses.get(emotion, "😊 Ai.lonso is here with you!")
    
    def get_emotion_history(self) -> List[Dict]:
        """Get recent emotion detection history"""
        # Simulate emotion history
        history = []
        for i in range(10):
            emotion = random.choice(self.emotions)
            intensity = random.uniform(0.3, 1.0)
            timestamp = f"14:{30+i}:{random.randint(0, 59):02d}"
            
            history.append({
                "timestamp": timestamp,
                "emotion": emotion,
                "intensity": intensity
            })
        
        return sorted(history, key=lambda x: x["timestamp"])
    
    def create_emotion_timeline(self) -> Dict:
        """Create emotion timeline data for visualization"""
        history = self.get_emotion_history()
        
        return {
            "timestamps": [item["timestamp"] for item in history],
            "emotions": [item["emotion"] for item in history],
            "intensities": [item["intensity"] for item in history]
        }


