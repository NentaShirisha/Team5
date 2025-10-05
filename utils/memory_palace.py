import json
import random
from typing import Dict, List

class MemoryPalace:
    """Handles F1 historical context and memory palace functionality"""
    
    def __init__(self):
        self.historical_database = {
            "crash": [
                {
                    "year": 1994,
                    "driver": "Ayrton Senna",
                    "event": "Fatal crash at Imola",
                    "impact": "Led to major safety improvements in F1",
                    "similarity": "High-speed crash at challenging corner"
                },
                {
                    "year": 2014,
                    "driver": "Jules Bianchi",
                    "event": "Crash at Suzuka",
                    "impact": "Introduction of Virtual Safety Car",
                    "similarity": "Wet weather crash with heavy machinery"
                }
            ],
            "overtake": [
                {
                    "year": 2008,
                    "driver": "Lewis Hamilton",
                    "event": "Last corner overtake in Brazil",
                    "impact": "Won first world championship",
                    "similarity": "Championship-deciding overtake"
                },
                {
                    "year": 2019,
                    "driver": "Max Verstappen",
                    "event": "Overtake around the outside at Copse",
                    "impact": "Showcased new generation talent",
                    "similarity": "Aggressive overtaking move"
                }
            ],
            "pit_stop": [
                {
                    "year": 2019,
                    "team": "Red Bull Racing",
                    "event": "1.82 second pit stop",
                    "impact": "Fastest pit stop in F1 history",
                    "similarity": "Ultra-fast tire change"
                }
            ],
            "safety_car": [
                {
                    "year": 2014,
                    "event": "Introduction of Virtual Safety Car",
                    "impact": "Revolutionized race control",
                    "similarity": "Safety car deployment"
                }
            ],
            "weather": [
                {
                    "year": 2007,
                    "event": "Fuji rain race",
                    "impact": "One of the most chaotic wet races",
                    "similarity": "Weather affecting race outcome"
                }
            ]
        }
        
        self.periods = {
            "1950s-1960s": "Golden age of F1, dangerous but exciting",
            "1970s-1980s": "Ground effect era, turbo engines",
            "1990s-2000s": "Electronic aids, safety improvements",
            "2010s-Present": "Hybrid era, advanced aerodynamics"
        }
    
    def get_historical_context(self, current_event: str) -> Dict:
        """Get historical context for a current race event"""
        # Find the most relevant historical event
        event_key = self._categorize_event(current_event)
        
        if event_key in self.historical_database:
            historical_events = self.historical_database[event_key]
            selected_event = random.choice(historical_events)
        else:
            # Default historical event
            selected_event = {
                "year": 2008,
                "driver": "Lewis Hamilton",
                "event": "First world championship",
                "impact": "Marked the beginning of a new era",
                "similarity": "Significant moment in F1 history"
            }
        
        return {
            "similar_event": selected_event["event"],
            "year": selected_event["year"],
            "driver": selected_event.get("driver", "Multiple drivers"),
            "impact": selected_event["impact"],
            "similarity": selected_event["similarity"]
        }
    
    def _categorize_event(self, event: str) -> str:
        """Categorize current event to find relevant historical context"""
        event_lower = event.lower()
        
        if any(word in event_lower for word in ["crash", "accident", "collision"]):
            return "crash"
        elif any(word in event_lower for word in ["overtake", "pass", "overtaking"]):
            return "overtake"
        elif any(word in event_lower for word in ["pit", "stop", "tire"]):
            return "pit_stop"
        elif any(word in event_lower for word in ["safety", "car"]):
            return "safety_car"
        elif any(word in event_lower for word in ["weather", "rain", "wet"]):
            return "weather"
        else:
            return "general"
    
    def get_period_context(self, period: str) -> Dict:
        """Get context for a specific historical period"""
        return {
            "period": period,
            "description": self.periods.get(period, "Unknown period"),
            "key_events": self._get_period_events(period)
        }
    
    def _get_period_events(self, period: str) -> List[str]:
        """Get key events for a specific period"""
        period_events = {
            "1950s-1960s": ["First F1 championship", "Fangio's dominance", "British teams rise"],
            "1970s-1980s": ["Ground effect cars", "Turbo era", "Safety improvements"],
            "1990s-2000s": ["Schumacher era", "Electronic aids", "Global expansion"],
            "2010s-Present": ["Hybrid engines", "Hamilton dominance", "New regulations"]
        }
        
        return period_events.get(period, ["Significant F1 developments"])
    
    def create_memory_timeline(self) -> Dict:
        """Create a timeline of F1 historical events"""
        timeline = []
        
        for event_type, events in self.historical_database.items():
            for event in events:
                timeline.append({
                    "year": event["year"],
                    "type": event_type,
                    "event": event["event"],
                    "impact": event["impact"]
                })
        
        # Sort by year
        timeline.sort(key=lambda x: x["year"])
        
        return {
            "timeline": timeline,
            "total_events": len(timeline),
            "periods_covered": list(self.periods.keys())
        }


