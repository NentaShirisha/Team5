import random
from typing import Dict, List

class MultilingualCommentary:
    """Handles multilingual commentary translation and simplification"""
    
    def __init__(self):
        self.language_codes = {
            "Spanish": "es",
            "French": "fr", 
            "German": "de",
            "Italian": "it",
            "Portuguese": "pt",
            "Japanese": "ja",
            "Simplified": "simple"
        }
        
        self.translations = {
            "Safety car deployed": {
                "Spanish": "Coche de seguridad desplegado",
                "French": "Voiture de sécurité déployée",
                "German": "Safety Car eingesetzt",
                "Italian": "Safety car schierato",
                "Portuguese": "Carro de segurança implantado",
                "Japanese": "セーフティカーが展開されました",
                "Simplified": "Safety car is out"
            },
            "Driver in the lead": {
                "Spanish": "Piloto en el liderato",
                "French": "Pilote en tête",
                "German": "Fahrer in Führung",
                "Italian": "Pilota in testa",
                "Portuguese": "Piloto na liderança",
                "Japanese": "リーダーのドライバー",
                "Simplified": "Driver is winning"
            },
            "Pit stop required": {
                "Spanish": "Parada en boxes requerida",
                "French": "Arrêt au stand requis",
                "German": "Boxenstopp erforderlich",
                "Italian": "Pit stop richiesto",
                "Portuguese": "Parada nos boxes necessária",
                "Japanese": "ピットストップが必要",
                "Simplified": "Need to pit"
            },
            "Race finished": {
                "Spanish": "Carrera terminada",
                "French": "Course terminée",
                "German": "Rennen beendet",
                "Italian": "Gara finita",
                "Portuguese": "Corrida terminada",
                "Japanese": "レース終了",
                "Simplified": "Race over"
            }
        }
        
        self.simplification_rules = {
            "technical_terms": {
                "aerodynamics": "car shape",
                "downforce": "car grip",
                "differential": "car gears",
                "telemetry": "car data",
                "fuel load": "car fuel"
            },
            "complex_phrases": {
                "overtaking maneuver": "passing",
                "championship points": "points",
                "grid position": "starting place",
                "race strategy": "race plan"
            }
        }
    
    def translate_and_simplify(self, commentary: str, target_language: str) -> Dict:
        """Translate commentary and create simplified version"""
        # Simulate translation (in real implementation, would use translation API)
        translated = self._simulate_translation(commentary, target_language)
        
        # Create simplified version
        simplified = self._simplify_commentary(commentary)
        
        return {
            "translation": translated,
            "simplified": simplified,
            "original": commentary,
            "language": target_language
        }
    
    def _simulate_translation(self, text: str, target_language: str) -> str:
        """Simulate translation (placeholder for real translation API)"""
        # In a real implementation, this would call a translation service
        # For demo purposes, we'll return a simulated translation
        
        if target_language == "Spanish":
            return f"[ES] {text}"
        elif target_language == "French":
            return f"[FR] {text}"
        elif target_language == "German":
            return f"[DE] {text}"
        elif target_language == "Italian":
            return f"[IT] {text}"
        elif target_language == "Portuguese":
            return f"[PT] {text}"
        elif target_language == "Japanese":
            return f"[JA] {text}"
        elif target_language == "Simplified":
            return self._simplify_commentary(text)
        else:
            return text
    
    def _simplify_commentary(self, commentary: str) -> str:
        """Simplify commentary for easier understanding"""
        simplified = commentary
        
        # Replace technical terms
        for technical, simple in self.simplification_rules["technical_terms"].items():
            simplified = simplified.replace(technical, simple)
        
        # Replace complex phrases
        for complex_phrase, simple_phrase in self.simplification_rules["complex_phrases"].items():
            simplified = simplified.replace(complex_phrase, simple_phrase)
        
        # Simplify sentence structure
        simplified = simplified.replace("LAP", "Lap")
        simplified = simplified.replace("P1", "1st place")
        simplified = simplified.replace("P2", "2nd place")
        
        return simplified
    
    def generate_summary(self, commentary: str) -> str:
        """Generate a summary of the commentary"""
        # Extract key information
        words = commentary.split()
        
        # Find key elements
        lap_info = [word for word in words if "LAP" in word]
        position_info = [word for word in words if word.startswith("P")]
        driver_info = [word for word in words if word.isupper() and len(word) > 2]
        
        # Create summary
        summary_parts = []
        
        if lap_info:
            summary_parts.append(f"At {lap_info[0]}")
        
        if driver_info:
            summary_parts.append(f"{driver_info[0]} is leading")
        
        if position_info:
            summary_parts.append(f"Positions: {', '.join(position_info[:3])}")
        
        return ". ".join(summary_parts) + "."
    
    def quick_translate(self, phrase: str, target_language: str) -> str:
        """Quick translation for common phrases"""
        if phrase in self.translations:
            return self.translations[phrase].get(target_language, phrase)
        else:
            return self._simulate_translation(phrase, target_language)
    
    def get_supported_languages(self) -> List[str]:
        """Get list of supported languages"""
        return list(self.language_codes.keys())
    
    def create_language_comparison(self, text: str) -> Dict:
        """Create comparison of text in multiple languages"""
        comparison = {}
        
        for language in self.language_codes.keys():
            comparison[language] = self._simulate_translation(text, language)
        
        return comparison


