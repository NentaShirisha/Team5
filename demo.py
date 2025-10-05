#!/usr/bin/env python3
"""
Ai.lonso F1 Digital Companion - Demo Script

This script demonstrates the key features of the Ai.lonso prototype
without requiring the full Streamlit interface.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.sign_language import SignLanguageAvatar
from utils.emotion_detection import EmotionDetector
from utils.haptic_simulator import HapticSimulator
from utils.memory_palace import MemoryPalace
from utils.multilingual_commentary import MultilingualCommentary
from utils.meme_generator import MemeGenerator
from utils.reel_creator import ReelCreator
from utils.photo_generator import PhotoGenerator
from utils.pitstop_game import PitStopGame
from utils.chatbot import F1Chatbot
from utils.fan_polls import FanPolls

def demo_inclusive_companion():
    """Demonstrate Inclusive Companion features"""
    print("🧑‍🤝‍🧑 INCLUSIVE DIGITAL COMPANION DEMO")
    print("=" * 50)
    
    # Sign Language Avatar
    print("\n1. Sign Language Avatar")
    avatar = SignLanguageAvatar()
    commentary = "LAP 10: Max Verstappen leads, Lewis Hamilton in P2. Alonso crashes out!"
    result = avatar.generate_sign_language(commentary)
    print(f"Commentary: {commentary}")
    print(f"Detected words: {result['detected_words']}")
    print(f"Gestures: {result['gesture_descriptions']}")
    
    # Emotion Detection
    print("\n2. Emotional Mirror")
    detector = EmotionDetector()
    emotion, intensity = detector.detect_emotion_from_webcam()
    response = detector.get_ai_lonso_response(emotion)
    print(f"Detected emotion: {emotion} (intensity: {intensity:.2f})")
    print(f"Ai.lonso response: {response}")
    
    # Haptic Vibrations
    print("\n3. Haptic Vibrations")
    haptic = HapticSimulator()
    event = haptic.trigger_event("crash", 0.8, 2.0)
    print(f"Event: {event['event_type']}")
    print(f"Pattern: {event['pattern']}")
    print(f"Description: {event['description']}")
    
    # Memory Palace
    print("\n4. Memory Palace")
    memory = MemoryPalace()
    context = memory.get_historical_context("Alonso crashes at turn 3")
    print(f"Current event: Alonso crashes at turn 3")
    print(f"Historical context: {context['similar_event']} ({context['year']})")
    print(f"Driver: {context['driver']}")
    print(f"Impact: {context['impact']}")
    
    # Multilingual Commentary
    print("\n5. Multilingual Commentary")
    translator = MultilingualCommentary()
    result = translator.translate_and_simplify(commentary, "Spanish")
    print(f"Original: {result['original']}")
    print(f"Translated: {result['translation']}")
    print(f"Simplified: {result['simplified']}")

def demo_fan_engagement():
    """Demonstrate Fan Engagement Engine features"""
    print("\n🎉 VIRAL FAN ENGAGEMENT ENGINE DEMO")
    print("=" * 50)
    
    # Meme Generator
    print("\n1. Meme Generator")
    meme_gen = MemeGenerator()
    random_meme = meme_gen.generate_random_meme()
    print("Generated random F1 meme!")
    print(f"Meme templates available: {len(meme_gen.get_meme_templates())}")
    
    # Reel Creator
    print("\n2. Reel Creator")
    reel_creator = ReelCreator()
    templates = reel_creator.get_reel_templates()
    print(f"Available reel styles: {list(templates.keys())}")
    highlights = reel_creator.detect_highlights("sample_video.mp4")
    print(f"Detected highlights: {len(highlights)}")
    for highlight in highlights[:2]:
        print(f"  - {highlight['moment']} at {highlight['timestamp']}")
    
    # Photo Generator
    print("\n3. Photo Generator")
    photo_gen = PhotoGenerator()
    drivers = photo_gen.get_available_drivers()
    cars = photo_gen.get_available_cars()
    print(f"Available drivers: {drivers}")
    print(f"Available cars: {cars}")
    
    # Pit-Stop Game
    print("\n4. Pit-Stop Game")
    game = PitStopGame()
    game_state = game.start_game("Medium")
    print(f"Game started! Target time: {game_state['target_time']}s")
    
    # Perform some actions
    game_state = game.perform_action(game_state, "fix_tire")
    game_state = game.perform_action(game_state, "add_fuel")
    game_state = game.perform_action(game_state, "change_tire")
    game_state = game.end_game(game_state)
    
    print(f"Final score: {game_state['final_score']}")
    print(f"Performance: {game_state['performance']}")
    
    # Chatbot
    print("\n5. Live Chatbot")
    chatbot = F1Chatbot()
    questions = [
        "What's the current race status?",
        "Who's leading the championship?",
        "When is the next race?"
    ]
    
    for question in questions:
        response = chatbot.get_response(question)
        print(f"Q: {question}")
        print(f"A: {response}")
    
    # Fan Polls
    print("\n6. Fan Polls")
    polls = FanPolls()
    active_polls = polls.get_active_polls()
    print(f"Active polls: {len(active_polls)}")
    
    for poll in active_polls[:2]:
        print(f"Poll: {poll['question']}")
        print(f"Options: {poll['options']}")
        print(f"Votes: {poll['votes']}")

def demo_integration():
    """Demonstrate integrated features"""
    print("\n🔗 INTEGRATED FEATURES DEMO")
    print("=" * 50)
    
    # Simulate a race scenario
    print("\nSimulating a race scenario...")
    
    # 1. Race event occurs
    print("1. Race event: Alonso crashes at turn 3")
    
    # 2. Multiple systems respond
    haptic = HapticSimulator()
    memory = MemoryPalace()
    chatbot = F1Chatbot()
    
    # Haptic response
    haptic_event = haptic.trigger_event("crash", 1.0, 2.5)
    print(f"   Haptic: {haptic_event['description']}")
    
    # Historical context
    context = memory.get_historical_context("Alonso crashes at turn 3")
    print(f"   Memory Palace: Similar to {context['similar_event']} ({context['year']})")
    
    # Chatbot response
    response = chatbot.get_response("What happened to Alonso?")
    print(f"   Chatbot: {response}")
    
    # 3. Fan engagement
    print("\n2. Fan engagement triggered...")
    
    polls = FanPolls()
    meme_gen = MemeGenerator()
    
    # Create meme about the crash
    print("   Meme Generator: Creating crash meme...")
    
    # Update polls
    print("   Fan Polls: Updating predictions...")
    
    print("\n✅ Integrated response complete!")

def main():
    """Main demo function"""
    print("🏎️ Ai.lonso F1 Digital Companion - Feature Demo")
    print("=" * 60)
    
    try:
        demo_inclusive_companion()
        demo_fan_engagement()
        demo_integration()
        
        print("\n🎉 Demo completed successfully!")
        print("\nTo run the full Streamlit application:")
        print("  streamlit run main.py")
        
    except Exception as e:
        print(f"\n❌ Demo failed with error: {e}")
        print("Make sure all dependencies are installed: pip install -r requirements.txt")

if __name__ == "__main__":
    main()


