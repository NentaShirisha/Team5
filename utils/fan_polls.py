import random
from typing import Dict, List
import json

class FanPolls:
    """Handles fan polls and predictions functionality"""
    
    def __init__(self):
        self.active_polls = [
            {
                "id": 1,
                "question": "Who will win the next race?",
                "options": ["Max Verstappen", "Lewis Hamilton", "Fernando Alonso", "Charles Leclerc"],
                "votes": [45, 30, 15, 10],
                "total_votes": 100,
                "category": "race_prediction",
                "expires": "2024-12-31"
            },
            {
                "id": 2,
                "question": "Will there be a safety car?",
                "options": ["Yes", "No"],
                "votes": [60, 40],
                "total_votes": 100,
                "category": "race_event",
                "expires": "2024-12-31"
            },
            {
                "id": 3,
                "question": "Which team will have the fastest pit stop?",
                "options": ["Red Bull", "Mercedes", "Ferrari", "McLaren"],
                "votes": [35, 25, 20, 20],
                "total_votes": 100,
                "category": "team_performance",
                "expires": "2024-12-31"
            }
        ]
        
        self.poll_categories = {
            "race_prediction": "Race Predictions",
            "race_event": "Race Events",
            "team_performance": "Team Performance",
            "driver_performance": "Driver Performance",
            "championship": "Championship"
        }
        
        self.user_predictions = {}
        self.poll_history = []
    
    def get_active_polls(self) -> List[Dict]:
        """Get all active polls"""
        return self.active_polls
    
    def vote_on_poll(self, poll_id: int, option_index: int, user_id: str = "anonymous") -> Dict:
        """Vote on a poll"""
        poll = self._find_poll_by_id(poll_id)
        if not poll:
            return {"success": False, "message": "Poll not found"}
        
        if option_index >= len(poll["options"]):
            return {"success": False, "message": "Invalid option"}
        
        # Record vote
        poll["votes"][option_index] += 1
        poll["total_votes"] += 1
        
        # Record user prediction
        if user_id not in self.user_predictions:
            self.user_predictions[user_id] = []
        
        self.user_predictions[user_id].append({
            "poll_id": poll_id,
            "option": poll["options"][option_index],
            "timestamp": "2024-01-01T12:00:00Z"  # Would use actual timestamp
        })
        
        return {
            "success": True,
            "message": f"Vote recorded for {poll['options'][option_index]}",
            "poll_results": self._get_poll_results(poll)
        }
    
    def _find_poll_by_id(self, poll_id: int) -> Dict:
        """Find poll by ID"""
        for poll in self.active_polls:
            if poll["id"] == poll_id:
                return poll
        return None
    
    def _get_poll_results(self, poll: Dict) -> Dict:
        """Get poll results with percentages"""
        results = []
        for i, option in enumerate(poll["options"]):
            percentage = (poll["votes"][i] / poll["total_votes"]) * 100
            results.append({
                "option": option,
                "votes": poll["votes"][i],
                "percentage": round(percentage, 1)
            })
        
        return {
            "question": poll["question"],
            "total_votes": poll["total_votes"],
            "results": results
        }
    
    def create_poll(self, question: str, options: List[str], category: str = "general") -> Dict:
        """Create a new poll"""
        new_poll = {
            "id": len(self.active_polls) + 1,
            "question": question,
            "options": options,
            "votes": [0] * len(options),
            "total_votes": 0,
            "category": category,
            "expires": "2024-12-31"
        }
        
        self.active_polls.append(new_poll)
        
        return {
            "success": True,
            "message": "Poll created successfully",
            "poll_id": new_poll["id"]
        }
    
    def get_poll_statistics(self) -> Dict:
        """Get overall poll statistics"""
        total_polls = len(self.active_polls)
        total_votes = sum(poll["total_votes"] for poll in self.active_polls)
        
        category_counts = {}
        for poll in self.active_polls:
            category = poll["category"]
            category_counts[category] = category_counts.get(category, 0) + 1
        
        return {
            "total_polls": total_polls,
            "total_votes": total_votes,
            "active_users": len(self.user_predictions),
            "category_breakdown": category_counts
        }
    
    def get_user_predictions(self, user_id: str) -> Dict:
        """Get user's prediction history"""
        if user_id not in self.user_predictions:
            return {
                "user_id": user_id,
                "predictions": [],
                "accuracy": 0,
                "total_predictions": 0
            }
        
        predictions = self.user_predictions[user_id]
        
        # Calculate accuracy (simulated)
        accuracy = random.uniform(0.6, 0.9)  # 60-90% accuracy
        
        return {
            "user_id": user_id,
            "predictions": predictions,
            "accuracy": round(accuracy * 100, 1),
            "total_predictions": len(predictions)
        }
    
    def get_trending_predictions(self) -> List[Dict]:
        """Get trending predictions across all polls"""
        trending = []
        
        for poll in self.active_polls:
            # Find the most voted option
            max_votes = max(poll["votes"])
            max_index = poll["votes"].index(max_votes)
            
            trending.append({
                "poll_question": poll["question"],
                "trending_option": poll["options"][max_index],
                "votes": max_votes,
                "percentage": round((max_votes / poll["total_votes"]) * 100, 1)
            })
        
        return sorted(trending, key=lambda x: x["votes"], reverse=True)
    
    def get_prediction_leaderboard(self) -> List[Dict]:
        """Get prediction accuracy leaderboard"""
        leaderboard = []
        
        for user_id, predictions in self.user_predictions.items():
            # Simulate accuracy based on number of predictions
            accuracy = random.uniform(0.5, 0.95)
            
            leaderboard.append({
                "user_id": user_id,
                "accuracy": round(accuracy * 100, 1),
                "total_predictions": len(predictions),
                "correct_predictions": int(len(predictions) * accuracy)
            })
        
        return sorted(leaderboard, key=lambda x: x["accuracy"], reverse=True)
    
    def get_achievements(self, user_id: str) -> List[str]:
        """Get user achievements"""
        achievements = []
        
        if user_id in self.user_predictions:
            predictions = self.user_predictions[user_id]
            prediction_count = len(predictions)
            
            if prediction_count >= 10:
                achievements.append("🎯 Prediction Master")
            if prediction_count >= 25:
                achievements.append("🏆 Poll Champion")
            if prediction_count >= 50:
                achievements.append("📈 Trend Spotter")
            if prediction_count >= 100:
                achievements.append("🔮 Future Seer")
        
        return achievements
    
    def get_poll_categories(self) -> Dict:
        """Get available poll categories"""
        return self.poll_categories
    
    def get_random_poll_question(self) -> str:
        """Get a random poll question for inspiration"""
        sample_questions = [
            "Who will get pole position?",
            "Will there be a red flag?",
            "Which driver will have the fastest lap?",
            "How many overtakes will there be?",
            "Will it rain during the race?",
            "Which team will score the most points?",
            "Who will win the championship?",
            "Will there be a crash in the first lap?"
        ]
        
        return random.choice(sample_questions)
    
    def export_poll_data(self) -> str:
        """Export poll data as JSON"""
        data = {
            "active_polls": self.active_polls,
            "user_predictions": self.user_predictions,
            "statistics": self.get_poll_statistics()
        }
        
        return json.dumps(data, indent=2)
    
    def simulate_live_voting(self) -> Dict:
        """Simulate live voting updates"""
        # Simulate new votes coming in
        for poll in self.active_polls:
            if poll["total_votes"] < 1000:  # Cap at 1000 votes
                # Randomly add votes
                if random.random() < 0.3:  # 30% chance of new vote
                    random_option = random.randint(0, len(poll["options"]) - 1)
                    poll["votes"][random_option] += 1
                    poll["total_votes"] += 1
        
        return {
            "message": "Live voting simulation updated",
            "total_active_votes": sum(poll["total_votes"] for poll in self.active_polls)
        }


