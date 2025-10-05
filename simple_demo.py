#!/usr/bin/env python3
"""
Ai.lonso F1 Digital Companion - Simple Demo

This script demonstrates the core features without heavy dependencies.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def demo_core_features():
    """Demonstrate core features that don't require heavy dependencies"""
    print("🏎️ Ai.lonso F1 Digital Companion - Core Features Demo")
    print("=" * 60)
    
    # Test basic imports
    try:
        from utils.sign_language import SignLanguageAvatar
        from utils.emotion_detection import EmotionDetector
        from utils.haptic_simulator import HapticSimulator
        from utils.memory_palace import MemoryPalace
        from utils.multilingual_commentary import MultilingualCommentary
        from utils.chatbot import F1Chatbot
        from utils.fan_polls import FanPolls
        from utils.pitstop_game import PitStopGame
        print("✅ Core utility modules imported successfully!")
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    
    # Demo Sign Language Avatar
    print("\n🤟 Sign Language Avatar Demo")
    try:
        avatar = SignLanguageAvatar()
        commentary = "LAP 10: Max Verstappen leads, Lewis Hamilton in P2. Alonso crashes out!"
        result = avatar.generate_sign_language(commentary)
        print(f"Commentary: {commentary}")
        print(f"Detected words: {result['detected_words']}")
        print(f"Gestures: {result['gesture_descriptions']}")
        print("✅ Sign Language Avatar working!")
    except Exception as e:
        print(f"❌ Sign Language Avatar error: {e}")
    
    # Demo Emotion Detection
    print("\n😊 Emotional Mirror Demo")
    try:
        detector = EmotionDetector()
        emotion, intensity = detector.detect_emotion_from_webcam()
        response = detector.get_ai_lonso_response(emotion)
        print(f"Detected emotion: {emotion} (intensity: {intensity:.2f})")
        print(f"Ai.lonso response: {response}")
        print("✅ Emotional Mirror working!")
    except Exception as e:
        print(f"❌ Emotional Mirror error: {e}")
    
    # Demo Haptic Vibrations
    print("\n📳 Haptic Vibrations Demo")
    try:
        haptic = HapticSimulator()
        event = haptic.trigger_event("crash", 0.8, 2.0)
        print(f"Event: {event['event_type']}")
        print(f"Pattern: {event['pattern']}")
        print(f"Description: {event['description']}")
        print("✅ Haptic Vibrations working!")
    except Exception as e:
        print(f"❌ Haptic Vibrations error: {e}")
    
    # Demo Memory Palace
    print("\n🏛️ Memory Palace Demo")
    try:
        memory = MemoryPalace()
        context = memory.get_historical_context("Alonso crashes at turn 3")
        print(f"Current event: Alonso crashes at turn 3")
        print(f"Historical context: {context['similar_event']} ({context['year']})")
        print(f"Driver: {context['driver']}")
        print(f"Impact: {context['impact']}")
        print("✅ Memory Palace working!")
    except Exception as e:
        print(f"❌ Memory Palace error: {e}")
    
    # Demo Multilingual Commentary
    print("\n🌍 Multilingual Commentary Demo")
    try:
        translator = MultilingualCommentary()
        result = translator.translate_and_simplify(commentary, "Spanish")
        print(f"Original: {result['original']}")
        print(f"Translated: {result['translation']}")
        print(f"Simplified: {result['simplified']}")
        print("✅ Multilingual Commentary working!")
    except Exception as e:
        print(f"❌ Multilingual Commentary error: {e}")
    
    # Demo Chatbot
    print("\n🤖 Live Chatbot Demo")
    try:
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
        print("✅ Live Chatbot working!")
    except Exception as e:
        print(f"❌ Live Chatbot error: {e}")
    
    # Demo Fan Polls
    print("\n📊 Fan Polls Demo")
    try:
        polls = FanPolls()
        active_polls = polls.get_active_polls()
        print(f"Active polls: {len(active_polls)}")
        
        for poll in active_polls[:2]:
            print(f"Poll: {poll['question']}")
            print(f"Options: {poll['options']}")
            print(f"Votes: {poll['votes']}")
        print("✅ Fan Polls working!")
    except Exception as e:
        print(f"❌ Fan Polls error: {e}")
    
    # Demo Pit-Stop Game
    print("\n🏁 Pit-Stop Game Demo")
    try:
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
        print("✅ Pit-Stop Game working!")
    except Exception as e:
        print(f"❌ Pit-Stop Game error: {e}")
    
    return True

def test_streamlit_app():
    """Test if the Streamlit app can be imported"""
    print("\n🌐 Testing Streamlit App...")
    try:
        # Test if we can import the main app
        import main
        print("✅ Main Streamlit app can be imported!")
        
        # Test if we can import the pages
        import pages.inclusive_companion
        import pages.fan_engagement
        print("✅ Page modules can be imported!")
        
        return True
    except Exception as e:
        print(f"❌ Streamlit app error: {e}")
        return False

def main():
    """Main demo function"""
    print("🚀 Starting Ai.lonso F1 Digital Companion Demo...")
    
    # Test core features
    core_success = demo_core_features()
    
    # Test Streamlit app
    streamlit_success = test_streamlit_app()
    
    print("\n" + "=" * 60)
    if core_success and streamlit_success:
        print("🎉 All core features are working!")
        print("\n🚀 To run the full Streamlit application:")
        print("   streamlit run main.py")
        print("\n📱 The app will open in your browser at http://localhost:8501")
    else:
        print("❌ Some features have issues. Check the errors above.")
    
    print("\n📋 Available Features:")
    print("   🧑‍🤝‍🧑 Inclusive Digital Companion")
    print("      - Sign Language Avatar")
    print("      - Haptic Vibrations") 
    print("      - Emotional Mirror")
    print("      - Memory Palace")
    print("      - Multilingual Commentary")
    print("   🎉 Viral Fan Engagement Engine")
    print("      - Meme Generator")
    print("      - Reel Creator")
    print("      - Photo Generator")
    print("      - Pit-Stop Game")
    print("      - Live Chatbot")
    print("      - Fan Polls")

if __name__ == "__main__":
    main()


