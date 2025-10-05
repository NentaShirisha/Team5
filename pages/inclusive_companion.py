import streamlit as st
import cv2
import numpy as np
from PIL import Image
import requests
import json
import time
import random
from utils.sign_language import SignLanguageAvatar
from utils.emotion_detection import EmotionDetector
from utils.haptic_simulator import HapticSimulator
from utils.memory_palace import MemoryPalace
from utils.multilingual_commentary import MultilingualCommentary

def show_inclusive_companion():
    st.title("🧑‍🤝‍🧑 Ai.lonso - Inclusive Digital Companion")
    st.markdown("Making F1 racing accessible for everyone!")
    
    # Feature selection
    feature = st.selectbox(
        "Choose a feature to explore:",
        ["Sign Language Avatar", "Haptic Vibrations", "Emotional Mirror", 
         "Memory Palace", "Multilingual Commentary"]
    )
    
    if feature == "Sign Language Avatar":
        show_sign_language_avatar()
    elif feature == "Haptic Vibrations":
        show_haptic_vibrations()
    elif feature == "Emotional Mirror":
        show_emotional_mirror()
    elif feature == "Memory Palace":
        show_memory_palace()
    elif feature == "Multilingual Commentary":
        show_multilingual_commentary()

def show_sign_language_avatar():
    st.header("🤟 Sign Language Avatar")
    st.markdown("Experience F1 commentary in sign language with expressive gestures!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Live Commentary Input")
        
        # Sample race commentary
        sample_commentary = st.text_area(
            "Enter race commentary or use sample:",
            value="LAP 10: Max Verstappen leads, Lewis Hamilton in P2. Alonso crashes out at turn 3!",
            height=100
        )
        
        if st.button("Generate Sign Language", key="sign_lang_btn"):
            with st.spinner("Generating sign language animation..."):
                # Simulate sign language generation
                avatar = SignLanguageAvatar()
                result = avatar.generate_sign_language(sample_commentary)
                
                st.success("Sign language animation generated!")
                
                # Display the avatar
                try:
                    st.image("assets/sign_language_demo.gif", caption="Ai.lonso signing the commentary")
                except:
                    st.info("🎭 Sign language animation would be displayed here")
                
                # Show word mapping
                st.subheader("Word Mapping")
                words = sample_commentary.split()
                for word in words[:10]:  # Show first 10 words
                    st.write(f"**{word}** → {random.choice(['Hand gesture A', 'Hand gesture B', 'Hand gesture C'])}")
    
    with col2:
        st.subheader("Avatar Controls")
        
        # Avatar customization
        avatar_style = st.selectbox("Avatar Style", ["Professional", "Casual", "Expressive"])
        speed = st.slider("Animation Speed", 0.5, 2.0, 1.0)
        
        # Demo features
        st.markdown("### Demo Features")
        if st.button("Demo: 'Start'"):
            try:
                st.image("assets/sign_start.gif", caption="Sign for 'Start'")
            except:
                st.info("🤟 Start gesture: Hands moving forward")
        
        if st.button("Demo: 'Win'"):
            try:
                st.image("assets/sign_win.gif", caption="Sign for 'Win'")
            except:
                st.info("🏆 Win gesture: Victory gesture with both hands")
        
        if st.button("Demo: 'Crash'"):
            try:
                st.image("assets/sign_crash.gif", caption="Sign for 'Crash'")
            except:
                st.info("💥 Crash gesture: Hands colliding motion")

def show_haptic_vibrations():
    st.header("📳 Haptic Vibrations")
    st.markdown("Feel the race through vibrations - experience overtakes, crashes, and finishes!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Race Event Simulator")
        
        # Event selection
        event_type = st.selectbox(
            "Select race event:",
            ["Overtake", "Crash", "Finish Line", "Pit Stop", "Safety Car"]
        )
        
        intensity = st.slider("Vibration Intensity", 1, 10, 5)
        duration = st.slider("Duration (seconds)", 0.5, 3.0, 1.0)
        
        if st.button("Trigger Haptic Event", key="haptic_btn"):
            haptic = HapticSimulator()
            haptic.trigger_event(event_type, intensity, duration)
            
            # Visual feedback
            st.success(f"Triggered {event_type} vibration!")
            
            # Show vibration pattern
            st.subheader("Vibration Pattern")
            pattern = haptic.get_pattern(event_type)
            
            # Create a simple visualization
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(figsize=(10, 3))
            ax.plot(pattern)
            ax.set_title(f"{event_type} Vibration Pattern")
            ax.set_xlabel("Time")
            ax.set_ylabel("Intensity")
            st.pyplot(fig)
    
    with col2:
        st.subheader("Haptic Settings")
        
        # Device selection
        device = st.selectbox("Device", ["Phone", "Controller", "Wearable"])
        
        # Accessibility options
        st.markdown("### Accessibility Options")
        reduced_motion = st.checkbox("Reduce motion intensity")
        audio_cues = st.checkbox("Add audio cues")
        
        # Demo events
        st.markdown("### Quick Demo")
        if st.button("Quick Overtake"):
            st.success("💥 Overtake vibration triggered!")
        
        if st.button("Quick Crash"):
            st.success("💥💥 Crash vibration triggered!")
        
        if st.button("Quick Finish"):
            st.success("🏁 Finish line vibration triggered!")

def show_emotional_mirror():
    st.header("😊 Emotional Mirror")
    st.markdown("Ai.lonso reflects your emotions in real-time during the race!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Live Emotion Detection")
        
        # Camera input
        if st.button("Start Camera", key="camera_btn"):
            st.info("Camera started! Looking for emotions...")
            
            # Simulate emotion detection
            detector = EmotionDetector()
            
            # Create a placeholder for camera feed
            camera_placeholder = st.empty()
            
            for i in range(10):  # Simulate 10 frames
                # Simulate different emotions
                emotions = ["happy", "excited", "worried", "neutral", "surprised"]
                current_emotion = random.choice(emotions)
                
                # Show emotion
                camera_placeholder.image(f"assets/emotion_{current_emotion}.jpg", 
                                       caption=f"Detected: {current_emotion}")
                
                # Show Ai.lonso's response
                st.write(f"🤖 Ai.lonso is feeling: **{current_emotion}**")
                
                time.sleep(1)
        
        # Manual emotion input
        st.subheader("Manual Emotion Input")
        manual_emotion = st.selectbox(
            "How are you feeling?",
            ["Happy", "Excited", "Worried", "Neutral", "Surprised", "Stressed"]
        )
        
        if st.button("Mirror Emotion", key="mirror_btn"):
            st.success(f"Ai.lonso is now reflecting: {manual_emotion}")
            try:
                st.image(f"assets/ai_lonso_{manual_emotion.lower()}.jpg", 
                        caption=f"Ai.lonso feeling {manual_emotion}")
            except:
                st.info(f"🤖 Ai.lonso is now reflecting: {manual_emotion}")
    
    with col2:
        st.subheader("Emotion History")
        
        # Show emotion timeline
        st.markdown("### Recent Emotions")
        emotions_data = [
            {"time": "14:32:15", "emotion": "Excited", "intensity": 8},
            {"time": "14:31:45", "emotion": "Worried", "intensity": 6},
            {"time": "14:31:20", "emotion": "Happy", "intensity": 9},
            {"time": "14:30:55", "emotion": "Neutral", "intensity": 4},
        ]
        
        for data in emotions_data:
            st.write(f"**{data['time']}** - {data['emotion']} ({data['intensity']}/10)")

def show_memory_palace():
    st.header("🏛️ Memory Palace")
    st.markdown("Connect current race events with F1 history using AR/VR and Spatial Audio!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Race Event Explorer")
        
        # Current race events
        current_events = [
            "Alonso crashes at turn 3",
            "Verstappen overtakes Hamilton",
            "Safety car deployed",
            "Pit stop strategy change",
            "Weather conditions worsen"
        ]
        
        selected_event = st.selectbox("Select current race event:", current_events)
        
        if st.button("Explore Historical Context", key="memory_btn"):
            memory_palace = MemoryPalace()
            historical_data = memory_palace.get_historical_context(selected_event)
            
            st.success("Historical context found!")
            
            # Display historical information
            st.subheader("Historical Context")
            st.write(f"**Event:** {selected_event}")
            st.write(f"**Similar Historical Event:** {historical_data['similar_event']}")
            st.write(f"**Year:** {historical_data['year']}")
            st.write(f"**Driver:** {historical_data['driver']}")
            st.write(f"**Impact:** {historical_data['impact']}")
            
            # Show historical video/image
            try:
                st.image(f"assets/historical_{historical_data['year']}.jpg", 
                        caption=f"Historical event from {historical_data['year']}")
            except:
                st.info(f"📸 Historical image from {historical_data['year']} would be displayed here")
    
    with col2:
        st.subheader("Memory Palace Settings")
        
        # AR/VR options
        st.markdown("### Experience Mode")
        experience_mode = st.selectbox("Mode", ["AR Overlay", "VR Immersion", "Audio Only"])
        
        # Historical periods
        st.markdown("### Historical Periods")
        periods = ["1950s-1960s", "1970s-1980s", "1990s-2000s", "2010s-Present"]
        selected_period = st.multiselect("Select periods:", periods, default=["2010s-Present"])
        
        # Quick historical facts
        st.markdown("### Quick Facts")
        if st.button("Random F1 Fact"):
            facts = [
                "Ayrton Senna won his first championship in 1988",
                "Michael Schumacher has 7 world championships",
                "Lewis Hamilton holds the record for most pole positions",
                "Max Verstappen is the youngest F1 winner ever"
            ]
            st.info(random.choice(facts))

def show_multilingual_commentary():
    st.header("🌍 Multilingual Commentary")
    st.markdown("Simplified commentary in multiple languages for all fans!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Commentary Translator")
        
        # Input commentary
        commentary_input = st.text_area(
            "Enter F1 commentary:",
            value="LAP 15: Max Verstappen leads by 2.3 seconds. Lewis Hamilton is closing the gap. Fernando Alonso pits for fresh tires.",
            height=100
        )
        
        # Language selection
        target_language = st.selectbox(
            "Translate to:",
            ["Spanish", "French", "German", "Italian", "Portuguese", "Japanese", "Simplified"]
        )
        
        if st.button("Generate Translation", key="translate_btn"):
            translator = MultilingualCommentary()
            
            with st.spinner("Translating and simplifying..."):
                result = translator.translate_and_simplify(commentary_input, target_language)
            
            st.success("Translation complete!")
            
            # Show results
            st.subheader("Translated Commentary")
            st.write(f"**Language:** {target_language}")
            st.write(f"**Original:** {commentary_input}")
            st.write(f"**Translated:** {result['translation']}")
            
            if result.get('simplified'):
                st.write(f"**Simplified:** {result['simplified']}")
        
        # Summary generator
        st.subheader("Auto Summary Generator")
        if st.button("Generate Summary", key="summary_btn"):
            summary = translator.generate_summary(commentary_input)
            st.write(f"**Summary:** {summary}")
    
    with col2:
        st.subheader("Language Settings")
        
        # Complexity level
        complexity = st.selectbox("Complexity Level", ["Beginner", "Intermediate", "Advanced"])
        
        # Target audience
        audience = st.selectbox("Target Audience", ["Kids", "Seniors", "New Fans", "General"])
        
        # Quick translations
        st.markdown("### Quick Translations")
        quick_phrases = [
            "Safety car deployed",
            "Driver in the lead",
            "Pit stop required",
            "Race finished"
        ]
        
        selected_phrase = st.selectbox("Quick phrase:", quick_phrases)
        if st.button("Translate Phrase"):
            quick_translation = translator.quick_translate(selected_phrase, target_language)
            st.write(f"**{selected_phrase}** → **{quick_translation}**")
