import random
import time
from typing import Dict, List, Tuple

class PitStopGame:
    """Handles pit stop mini-game functionality"""
    
    def __init__(self):
        self.game_states = {
            "waiting": "Waiting to start",
            "active": "Game in progress",
            "finished": "Game completed",
            "paused": "Game paused"
        }
        
        self.actions = {
            "fix_tire": {"points": 10, "time": 0.5, "description": "Fix tire"},
            "add_fuel": {"points": 15, "time": 0.8, "description": "Add fuel"},
            "change_tire": {"points": 20, "time": 1.0, "description": "Change tire"},
            "adjust_wings": {"points": 12, "time": 0.6, "description": "Adjust wings"},
            "clean_visor": {"points": 5, "time": 0.3, "description": "Clean visor"}
        }
        
        self.difficulty_levels = {
            "Easy": {"time_multiplier": 1.5, "point_multiplier": 1.2},
            "Medium": {"time_multiplier": 1.0, "point_multiplier": 1.0},
            "Hard": {"time_multiplier": 0.7, "point_multiplier": 0.8},
            "Expert": {"time_multiplier": 0.5, "point_multiplier": 0.6}
        }
        
        self.leaderboard = [
            {"name": "SpeedDemon", "score": 1250, "time": 2.3, "difficulty": "Hard"},
            {"name": "PitMaster", "score": 1180, "time": 2.1, "difficulty": "Expert"},
            {"name": "TireKing", "score": 1100, "time": 2.5, "difficulty": "Medium"},
            {"name": "FastLane", "score": 1050, "time": 2.8, "difficulty": "Medium"},
            {"name": "QuickStop", "score": 980, "time": 3.1, "difficulty": "Easy"}
        ]
    
    def start_game(self, difficulty: str = "Medium") -> Dict:
        """Start a new pit stop game"""
        game_state = {
            "state": "active",
            "score": 0,
            "start_time": time.time(),
            "current_time": 0,
            "difficulty": difficulty,
            "actions_completed": [],
            "target_time": self._get_target_time(difficulty)
        }
        
        return game_state
    
    def _get_target_time(self, difficulty: str) -> float:
        """Get target time based on difficulty"""
        base_time = 3.0  # Base target time in seconds
        multiplier = self.difficulty_levels[difficulty]["time_multiplier"]
        return base_time * multiplier
    
    def perform_action(self, game_state: Dict, action: str) -> Dict:
        """Perform an action in the game"""
        if game_state["state"] != "active":
            return game_state
        
        if action not in self.actions:
            return game_state
        
        action_data = self.actions[action]
        difficulty_data = self.difficulty_levels[game_state["difficulty"]]
        
        # Calculate points with difficulty multiplier
        points = int(action_data["points"] * difficulty_data["point_multiplier"])
        
        # Add points to score
        game_state["score"] += points
        
        # Record action
        game_state["actions_completed"].append({
            "action": action,
            "points": points,
            "timestamp": time.time() - game_state["start_time"]
        })
        
        return game_state
    
    def end_game(self, game_state: Dict) -> Dict:
        """End the game and calculate final results"""
        if game_state["state"] != "active":
            return game_state
        
        end_time = time.time()
        total_time = end_time - game_state["start_time"]
        
        game_state["state"] = "finished"
        game_state["total_time"] = total_time
        game_state["final_score"] = game_state["score"]
        
        # Calculate bonus points for speed
        target_time = game_state["target_time"]
        if total_time <= target_time:
            speed_bonus = int((target_time - total_time) * 100)
            game_state["speed_bonus"] = speed_bonus
            game_state["final_score"] += speed_bonus
        
        # Determine performance level
        game_state["performance"] = self._calculate_performance(game_state)
        
        return game_state
    
    def _calculate_performance(self, game_state: Dict) -> str:
        """Calculate performance level based on score and time"""
        score = game_state["final_score"]
        time_taken = game_state["total_time"]
        target_time = game_state["target_time"]
        
        if score >= 1000 and time_taken <= target_time:
            return "World Class"
        elif score >= 800 and time_taken <= target_time * 1.2:
            return "Excellent"
        elif score >= 600 and time_taken <= target_time * 1.5:
            return "Good"
        elif score >= 400:
            return "Average"
        else:
            return "Needs Practice"
    
    def get_leaderboard(self) -> List[Dict]:
        """Get current leaderboard"""
        return sorted(self.leaderboard, key=lambda x: x["score"], reverse=True)
    
    def add_to_leaderboard(self, player_name: str, score: int, time_taken: float, difficulty: str) -> bool:
        """Add new score to leaderboard"""
        new_entry = {
            "name": player_name,
            "score": score,
            "time": time_taken,
            "difficulty": difficulty
        }
        
        # Add to leaderboard
        self.leaderboard.append(new_entry)
        
        # Sort and keep top 10
        self.leaderboard = sorted(self.leaderboard, key=lambda x: x["score"], reverse=True)[:10]
        
        # Check if new entry made it to top 10
        return new_entry in self.leaderboard
    
    def get_game_stats(self) -> Dict:
        """Get overall game statistics"""
        total_games = len(self.leaderboard)
        if total_games == 0:
            return {"total_games": 0, "average_score": 0, "best_time": 0}
        
        total_score = sum(entry["score"] for entry in self.leaderboard)
        best_time = min(entry["time"] for entry in self.leaderboard)
        
        return {
            "total_games": total_games,
            "average_score": total_score / total_games,
            "best_time": best_time,
            "top_player": self.leaderboard[0]["name"] if self.leaderboard else "None"
        }
    
    def get_random_challenge(self) -> Dict:
        """Get a random pit stop challenge"""
        challenges = [
            {
                "name": "Speed Challenge",
                "description": "Complete pit stop in under 2.5 seconds",
                "target_time": 2.5,
                "bonus_points": 200
            },
            {
                "name": "Precision Challenge",
                "description": "Score 1000+ points with perfect timing",
                "target_score": 1000,
                "bonus_points": 150
            },
            {
                "name": "Endurance Challenge",
                "description": "Complete 10 actions in sequence",
                "target_actions": 10,
                "bonus_points": 100
            }
        ]
        
        return random.choice(challenges)
    
    def simulate_ai_opponent(self, difficulty: str) -> Dict:
        """Simulate an AI opponent for comparison"""
        ai_stats = {
            "Easy": {"score": 600, "time": 3.5},
            "Medium": {"score": 800, "time": 3.0},
            "Hard": {"score": 1000, "time": 2.5},
            "Expert": {"score": 1200, "time": 2.0}
        }
        
        return ai_stats.get(difficulty, ai_stats["Medium"])
    
    def get_sponsor_branding(self) -> Dict:
        """Get sponsor branding information"""
        return {
            "primary_sponsor": "TURBO OIL",
            "logo": "assets/turbo_oil_logo.png",
            "slogan": "Powering Champions",
            "secondary_sponsors": ["SpeedTire", "FuelMax", "GearPro"]
        }
    
    def create_training_mode(self) -> Dict:
        """Create training mode with guided instructions"""
        return {
            "mode": "training",
            "instructions": [
                "Click 'Fix Tire' to repair tire damage (+10 points)",
                "Click 'Add Fuel' to refuel the car (+15 points)",
                "Click 'Change Tire' for new tires (+20 points)",
                "Complete actions quickly for bonus points",
                "Target time: 3.0 seconds for medium difficulty"
            ],
            "practice_actions": ["fix_tire", "add_fuel", "change_tire"]
        }


