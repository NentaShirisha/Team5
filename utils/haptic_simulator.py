import numpy as np
import random
from typing import Dict, List

class HapticSimulator:
    """Handles haptic vibration patterns for F1 events"""
    
    def __init__(self):
        self.event_patterns = {
            "overtake": [0.8, 0.6, 0.9, 0.7, 0.5],
            "crash": [1.0, 0.3, 1.0, 0.2, 0.8, 0.4],
            "finish": [0.9, 0.9, 0.9, 0.9, 0.9],
            "pit_stop": [0.7, 0.5, 0.8, 0.6, 0.7],
            "safety_car": [0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
        }
        
        self.event_descriptions = {
            "overtake": "Quick succession of vibrations representing the overtaking maneuver",
            "crash": "Sharp, intense vibrations followed by silence, then gradual recovery",
            "finish": "Strong, sustained vibrations celebrating the finish",
            "pit_stop": "Rhythmic vibrations matching pit stop activities",
            "safety_car": "Steady, consistent vibrations representing safety car pace"
        }
    
    def trigger_event(self, event_type: str, intensity: float, duration: float) -> Dict:
        """Trigger a haptic event"""
        if event_type.lower() not in self.event_patterns:
            event_type = "overtake"  # Default fallback
        
        pattern = self.event_patterns[event_type.lower()]
        
        # Scale pattern based on intensity and duration
        scaled_pattern = [p * intensity for p in pattern]
        
        # Adjust pattern length based on duration
        pattern_duration = len(pattern) * 0.2  # Each vibration lasts 0.2 seconds
        if duration > pattern_duration:
            # Repeat pattern to fill duration
            repetitions = int(duration / pattern_duration)
            scaled_pattern = scaled_pattern * repetitions
        
        return {
            "event_type": event_type,
            "pattern": scaled_pattern,
            "duration": duration,
            "intensity": intensity,
            "description": self.event_descriptions.get(event_type.lower(), "Custom haptic event")
        }
    
    def get_pattern(self, event_type: str) -> List[float]:
        """Get vibration pattern for a specific event"""
        return self.event_patterns.get(event_type.lower(), [0.5, 0.5, 0.5])
    
    def simulate_race_sequence(self) -> List[Dict]:
        """Simulate a sequence of haptic events during a race"""
        events = []
        
        # Simulate race events
        race_events = [
            ("start", 0.8, 2.0),
            ("overtake", 0.9, 1.5),
            ("pit_stop", 0.7, 3.0),
            ("overtake", 0.8, 1.5),
            ("crash", 1.0, 2.5),
            ("safety_car", 0.6, 4.0),
            ("finish", 0.9, 3.0)
        ]
        
        for event_type, intensity, duration in race_events:
            event = self.trigger_event(event_type, intensity, duration)
            events.append(event)
        
        return events
    
    def create_haptic_timeline(self) -> Dict:
        """Create haptic timeline data for visualization"""
        events = self.simulate_race_sequence()
        
        timeline_data = {
            "timestamps": [],
            "intensities": [],
            "event_types": []
        }
        
        current_time = 0
        for event in events:
            timeline_data["timestamps"].append(current_time)
            timeline_data["intensities"].append(max(event["pattern"]))
            timeline_data["event_types"].append(event["event_type"])
            current_time += event["duration"]
        
        return timeline_data


