import random
from typing import Dict, List

class F1Chatbot:
    """Handles F1 chatbot functionality and responses"""
    
    def __init__(self):
        self.responses = {
            "race_status": [
                "The race is currently in progress with Max Verstappen leading.",
                "Lewis Hamilton is closing the gap on the leader.",
                "Safety car has been deployed due to an incident.",
                "The race is under red flag conditions.",
                "All drivers have completed their pit stops."
            ],
            "championship": [
                "Max Verstappen leads the championship with 350 points.",
                "Lewis Hamilton is second with 280 points.",
                "Fernando Alonso is third with 250 points.",
                "The championship battle is heating up!",
                "Only 3 races left in the season."
            ],
            "next_race": [
                "The next race is the Brazilian Grand Prix in São Paulo.",
                "Race weekend starts on Friday with practice sessions.",
                "Qualifying is scheduled for Saturday afternoon.",
                "The race will be held on Sunday at 2:00 PM local time.",
                "Weather forecast shows sunny conditions."
            ],
            "weather": [
                "Current track temperature is 35°C.",
                "Air temperature is 28°C with light winds.",
                "Weather conditions are perfect for racing.",
                "Rain is expected in the next hour.",
                "Track is dry with good grip levels."
            ],
            "rules": [
                "Drivers must use two different tire compounds during the race.",
                "Minimum pit stop time is 2.3 seconds.",
                "Safety car speed limit is 60 km/h.",
                "DRS zones are active on the main straight.",
                "Virtual Safety Car can be deployed for incidents."
            ],
            "drivers": [
                "Max Verstappen is known for his aggressive driving style.",
                "Lewis Hamilton has 7 world championships.",
                "Fernando Alonso is the most experienced driver on the grid.",
                "Charles Leclerc is Ferrari's lead driver.",
                "Lando Norris is McLaren's rising star."
            ],
            "teams": [
                "Red Bull Racing is currently leading the constructors' championship.",
                "Mercedes has won 8 consecutive constructors' titles.",
                "Ferrari is the most successful team in F1 history.",
                "McLaren is making a strong comeback this season.",
                "Aston Martin has improved significantly this year."
            ],
            "general": [
                "Formula 1 is the pinnacle of motorsport.",
                "F1 cars can reach speeds of over 350 km/h.",
                "The season consists of 23 races around the world.",
                "F1 drivers are some of the fittest athletes in the world.",
                "Technology in F1 drives innovation in road cars."
            ]
        }
        
        self.keywords = {
            "race": "race_status",
            "status": "race_status",
            "leading": "race_status",
            "championship": "championship",
            "points": "championship",
            "next": "next_race",
            "when": "next_race",
            "schedule": "next_race",
            "weather": "weather",
            "temperature": "weather",
            "rain": "weather",
            "rules": "rules",
            "regulation": "rules",
            "driver": "drivers",
            "verstappen": "drivers",
            "hamilton": "drivers",
            "alonso": "drivers",
            "team": "teams",
            "red bull": "teams",
            "mercedes": "teams",
            "ferrari": "teams"
        }
    
    def get_response(self, user_input: str) -> str:
        """Get response based on user input"""
        user_input_lower = user_input.lower()
        
        # Determine response category
        category = self._categorize_input(user_input_lower)
        
        # Get appropriate response
        if category in self.responses:
            response = random.choice(self.responses[category])
        else:
            response = random.choice(self.responses["general"])
        
        # Add personality to response
        response = self._add_personality(response)
        
        return response
    
    def _categorize_input(self, user_input: str) -> str:
        """Categorize user input to determine response type"""
        for keyword, category in self.keywords.items():
            if keyword in user_input:
                return category
        
        return "general"
    
    def _add_personality(self, response: str) -> str:
        """Add Ai.lonso's personality to responses"""
        personality_prefixes = [
            "🏎️ ",
            "🤖 ",
            "⚡ ",
            "🏁 ",
            "💨 "
        ]
        
        personality_suffixes = [
            " That's what makes F1 so exciting!",
            " I love sharing F1 knowledge!",
            " The action never stops in F1!",
            " What a sport!",
            " Keep following the action!"
        ]
        
        # Add prefix
        response = random.choice(personality_prefixes) + response
        
        # Sometimes add suffix
        if random.random() < 0.3:
            response += random.choice(personality_suffixes)
        
        return response
    
    def get_quick_facts(self) -> List[str]:
        """Get quick F1 facts"""
        facts = [
            "F1 cars can accelerate from 0 to 100 km/h in 2.6 seconds",
            "The fastest pit stop ever was 1.82 seconds by Red Bull",
            "F1 drivers can lose up to 3kg during a race",
            "The G-force in corners can reach 5G",
            "F1 cars have over 80,000 components",
            "The fuel used in F1 is similar to regular gasoline",
            "F1 cars can brake from 200 km/h to 0 in 55 meters",
            "The cockpit temperature can reach 50°C during races"
        ]
        
        return random.sample(facts, 3)
    
    def get_race_updates(self) -> Dict:
        """Get current race updates"""
        return {
            "current_lap": random.randint(1, 60),
            "leader": random.choice(["Max Verstappen", "Lewis Hamilton", "Fernando Alonso"]),
            "gap": f"{random.uniform(0.5, 5.0):.1f}s",
            "fastest_lap": random.choice(["Max Verstappen", "Lewis Hamilton", "Charles Leclerc"]),
            "safety_car": random.choice([True, False]),
            "weather": random.choice(["Sunny", "Cloudy", "Light Rain"])
        }
    
    def get_driver_info(self, driver_name: str) -> Dict:
        """Get information about a specific driver"""
        driver_info = {
            "Max Verstappen": {
                "team": "Red Bull Racing",
                "number": "1",
                "nationality": "Dutch",
                "championships": 3,
                "wins": 54,
                "poles": 30
            },
            "Lewis Hamilton": {
                "team": "Mercedes",
                "number": "44",
                "nationality": "British",
                "championships": 7,
                "wins": 103,
                "poles": 104
            },
            "Fernando Alonso": {
                "team": "Aston Martin",
                "number": "14",
                "nationality": "Spanish",
                "championships": 2,
                "wins": 32,
                "poles": 22
            }
        }
        
        return driver_info.get(driver_name, {
            "team": "Unknown",
            "number": "?",
            "nationality": "Unknown",
            "championships": 0,
            "wins": 0,
            "poles": 0
        })
    
    def get_team_info(self, team_name: str) -> Dict:
        """Get information about a specific team"""
        team_info = {
            "Red Bull": {
                "drivers": ["Max Verstappen", "Sergio Perez"],
                "championships": 6,
                "headquarters": "Milton Keynes, UK",
                "engine": "Honda RBPT"
            },
            "Mercedes": {
                "drivers": ["Lewis Hamilton", "George Russell"],
                "championships": 8,
                "headquarters": "Brackley, UK",
                "engine": "Mercedes"
            },
            "Ferrari": {
                "drivers": ["Charles Leclerc", "Carlos Sainz"],
                "championships": 16,
                "headquarters": "Maranello, Italy",
                "engine": "Ferrari"
            }
        }
        
        return team_info.get(team_name, {
            "drivers": ["Unknown"],
            "championships": 0,
            "headquarters": "Unknown",
            "engine": "Unknown"
        })
    
    def get_help_topics(self) -> List[str]:
        """Get list of help topics"""
        return [
            "Race Status",
            "Championship Standings",
            "Next Race Schedule",
            "Weather Conditions",
            "F1 Rules and Regulations",
            "Driver Information",
            "Team Information",
            "General F1 Facts"
        ]
    
    def get_chat_history_summary(self, chat_history: List[Dict]) -> str:
        """Get summary of chat history"""
        if not chat_history:
            return "No chat history available."
        
        topics_discussed = []
        for message in chat_history:
            if message["role"] == "user":
                category = self._categorize_input(message["content"].lower())
                if category not in topics_discussed:
                    topics_discussed.append(category)
        
        if topics_discussed:
            return f"We discussed: {', '.join(topics_discussed)}"
        else:
            return "We had a general conversation about F1."


