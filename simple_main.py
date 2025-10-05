import streamlit as st
import os

# Page configuration
st.set_page_config(
    page_title="Ai.lonso - F1 Digital Companion",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .feature-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">🏎️ Ai.lonso - F1 Digital Companion</h1>', unsafe_allow_html=True)
    
    # Simple navigation
    st.sidebar.markdown("### 🏎️ Ai.lonso")
    st.sidebar.markdown("*F1 Digital Companion*")
    
    # Navigation buttons
    page = st.sidebar.selectbox(
        "Choose a section:",
        ["Home", "Inclusive Companion", "Fan Engagement"]
    )
    
    # Main content based on selection
    if page == "Home":
        show_home_page()
    elif page == "Inclusive Companion":
        show_inclusive_companion()
    elif page == "Fan Engagement":
        show_fan_engagement()

def show_home_page():
    st.markdown("""
    ## Welcome to Ai.lonso - The Future of F1 Fan Experience! 🏁
    
    Ai.lonso is a revolutionary AI-powered digital companion designed to make Formula 1 racing accessible, 
    engaging, and inclusive for fans of all backgrounds and abilities.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🧑‍🤝‍🧑 Inclusive Digital Companion
        
        Making F1 accessible for everyone:
        - **Sign Language Avatar**: Live race commentary in sign language
        - **Haptic Vibrations**: Feel the race through vibrations
        - **Emotional Mirror**: AI reflects your emotions in real-time
        - **Memory Palace**: Connect current events with F1 history
        - **Multilingual Commentary**: Simplified commentary for all fans
        """)
    
    with col2:
        st.markdown("""
        ### 🎉 Viral Fan Engagement Engine
        
        Creating shareable F1 moments:
        - **Meme Generator**: Turn race moments into viral memes
        - **Reel Creator**: Auto-generate highlight videos
        - **Photo Generator**: AR selfies with drivers and cars
        - **Pit-Stop Game**: Fun mini-games with leaderboards
        - **Live Chatbot**: Real-time Q&A with AI.lonso
        - **Fan Polls**: Gamified predictions and voting
        """)

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
    
    with col2:
        st.subheader("Avatar Controls")
        
        # Avatar customization
        avatar_style = st.selectbox("Avatar Style", ["Professional", "Casual", "Expressive"])
        speed = st.slider("Animation Speed", 0.5, 2.0, 1.0)
    
    with col1:
        st.subheader("Live Commentary Input")
        
        # Sample race commentary
        sample_commentary = st.text_area(
            "Enter race commentary or use sample:",
            value="LAP 10: Max Verstappen leads, Lewis Hamilton in P2. Alonso crashes out at turn 3!",
            height=100
        )
        
        if st.button("Generate Sign Language", key="sign_lang_btn"):
            st.success("Sign language animation generated!")
            
            # Create a visual representation of sign language
            st.subheader("Sign Language Analysis")
            
            # Analyze the commentary
            words = sample_commentary.split()
            f1_keywords = ["LAP", "VERSTAPPEN", "HAMILTON", "ALONSO", "CRASH", "LEADS", "P2", "TURN"]
            
            detected_words = []
            for word in words:
                if word.upper() in f1_keywords:
                    detected_words.append(word.upper())
            
            st.write(f"**Detected F1 Keywords:** {', '.join(detected_words)}")
            
            # Show word mapping with actual gestures
            st.subheader("Word Mapping")
            gesture_database = {
                "LAP": "Circular motion with both hands",
                "VERSTAPPEN": "V-sign with victory gesture",
                "HAMILTON": "H-shape with both hands",
                "ALONSO": "A-shape with one hand",
                "CRASH": "Hands colliding motion",
                "LEADS": "Pointing forward motion",
                "P2": "Two fingers up",
                "TURN": "Steering wheel motion"
            }
            
            for word in words[:10]:  # Show first 10 words
                word_upper = word.upper()
                if word_upper in gesture_database:
                    st.write(f"**{word}** → {gesture_database[word_upper]}")
                else:
                    st.write(f"**{word}** → Generic gesture")
            
            # Create a simple visualization
            st.subheader("Animation Sequence")
            if detected_words:
                st.write("**Animation Order:**")
                for i, word in enumerate(detected_words[:5]):
                    st.write(f"{i+1}. {word} - {gesture_database.get(word, 'Generic gesture')}")
            else:
                st.write("No specific F1 gestures detected. Using general commentary gestures.")
            
            # Show avatar settings
            st.subheader("Avatar Settings Applied")
            st.write(f"**Style:** {avatar_style}")
            st.write(f"**Speed:** {speed}x")
            st.write(f"**Animation Duration:** {len(words) * 0.5:.1f} seconds")
    
    with col2:
        # Demo features
        st.markdown("### Demo Features")
        if st.button("Demo: 'Start'"):
            st.info("🤟 Start gesture: Hands moving forward")
        
        if st.button("Demo: 'Win'"):
            st.info("🏆 Win gesture: Victory gesture with both hands")
        
        if st.button("Demo: 'Crash'"):
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
            st.success(f"Triggered {event_type} vibration!")
            
            # Generate specific vibration patterns based on event type
            vibration_patterns = {
                "Overtake": [0.8, 0.6, 0.9, 0.7, 0.5],
                "Crash": [1.0, 0.3, 1.0, 0.2, 0.8, 0.4],
                "Finish Line": [0.9, 0.9, 0.9, 0.9, 0.9],
                "Pit Stop": [0.7, 0.5, 0.8, 0.6, 0.7],
                "Safety Car": [0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
            }
            
            pattern = vibration_patterns.get(event_type, [0.5, 0.5, 0.5])
            
            # Scale pattern based on intensity
            scaled_pattern = [p * (intensity / 10) for p in pattern]
            
            # Show vibration pattern
            st.subheader("Vibration Pattern")
            st.write(f"**Event:** {event_type}")
            st.write(f"**Intensity:** {intensity}/10")
            st.write(f"**Duration:** {duration} seconds")
            st.write(f"**Pattern:** {[round(p, 2) for p in scaled_pattern]}")
            
            # Show pattern visualization
            import matplotlib.pyplot as plt
            import numpy as np
            
            # Create time array
            time_points = np.linspace(0, duration, len(scaled_pattern))
            
            # Create the plot
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(time_points, scaled_pattern, 'b-o', linewidth=2, markersize=6)
            ax.fill_between(time_points, scaled_pattern, alpha=0.3)
            ax.set_title(f"{event_type} Vibration Pattern")
            ax.set_xlabel("Time (seconds)")
            ax.set_ylabel("Vibration Intensity")
            ax.set_ylim(0, 1)
            ax.grid(True, alpha=0.3)
            
            st.pyplot(fig)
            
            # Show haptic description
            descriptions = {
                "Overtake": "Quick succession of vibrations representing the overtaking maneuver",
                "Crash": "Sharp, intense vibrations followed by silence, then gradual recovery",
                "Finish Line": "Strong, sustained vibrations celebrating the finish",
                "Pit Stop": "Rhythmic vibrations matching pit stop activities",
                "Safety Car": "Steady, consistent vibrations representing safety car pace"
            }
            
            st.write(f"**Description:** {descriptions.get(event_type, 'Custom vibration pattern')}")
            
            # Show device compatibility
            st.subheader("Device Compatibility")
            devices = ["📱 Phone", "🎮 Controller", "⌚ Wearable"]
            for device in devices:
                st.write(f"✅ {device} - Compatible")
    
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
            st.info("🤖 Ai.lonso is feeling: **excited**")
        
        # Manual emotion input
        st.subheader("Manual Emotion Input")
        manual_emotion = st.selectbox(
            "How are you feeling?",
            ["Happy", "Excited", "Worried", "Neutral", "Surprised", "Stressed"]
        )
        
        if st.button("Mirror Emotion", key="mirror_btn"):
            st.success(f"Ai.lonso is now reflecting: {manual_emotion}")
            
            # Simulate emotion detection and mirroring
            import random
            
            # Generate emotion confidence
            confidence = random.uniform(0.7, 0.95)
            
            # Show emotion analysis
            st.subheader("Emotion Analysis")
            st.write(f"**Detected Emotion:** {manual_emotion}")
            st.write(f"**Confidence:** {confidence:.1%}")
            st.progress(confidence)
            
            # Show avatar response
            st.subheader("Avatar Response")
            avatar_responses = {
                "Happy": "😊 Avatar shows cheerful expression with bright eyes",
                "Excited": "🤩 Avatar displays excited animation with energetic movements",
                "Worried": "😟 Avatar shows concerned look with furrowed brow",
                "Neutral": "😐 Avatar maintains calm, composed expression",
                "Surprised": "😲 Avatar shows surprise reaction with wide eyes",
                "Stressed": "😰 Avatar displays tension with subtle facial changes"
            }
            
            st.write(avatar_responses.get(manual_emotion, "🤖 Avatar responds to emotion"))
            
            # Show emotion visualization
            import matplotlib.pyplot as plt
            import numpy as np
            
            # Create emotion wheel
            fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
            
            emotions = ["Happy", "Excited", "Worried", "Neutral", "Surprised", "Stressed"]
            values = [random.uniform(0.1, 0.9) for _ in emotions]
            
            # Highlight selected emotion
            selected_idx = emotions.index(manual_emotion)
            values[selected_idx] = confidence
            
            # Create the plot
            theta = np.linspace(0, 2*np.pi, len(emotions), endpoint=False)
            theta = np.concatenate((theta, [theta[0]]))
            values_plot = values + [values[0]]
            
            ax.plot(theta, values_plot, 'o-', linewidth=2, color='#FF2D01')
            ax.fill(theta, values_plot, alpha=0.25, color='#FF2D01')
            ax.set_xticks(theta[:-1])
            ax.set_xticklabels(emotions)
            ax.set_ylim(0, 1)
            ax.set_title("Emotion Detection Wheel", pad=20)
            
            plt.tight_layout()
            st.pyplot(fig)
            
            # Show mirror settings
            st.subheader("Mirror Settings")
            st.write(f"**Sensitivity:** High")
            st.write(f"**Update Frequency:** Real-time")
            st.write(f"**Detection Method:** Facial Expression Analysis")
    
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
            st.success("Historical context found!")
            
            # Historical F1 database
            historical_events = {
                "Alonso crashes at turn 3": {
                    "year": "2003",
                    "event": "Brazilian GP - Alonso's first F1 crash",
                    "driver": "Fernando Alonso",
                    "description": "Fernando Alonso crashed at turn 3 during his rookie season, similar to today's incident.",
                    "significance": "This crash marked Alonso's learning curve in F1, leading to his future success.",
                    "impact": "Alonso went on to win 2 World Championships",
                    "similarity": 0.85
                },
                "Verstappen overtakes Hamilton": {
                    "year": "2021",
                    "event": "Brazilian GP - Verstappen's aggressive overtake",
                    "driver": "Max Verstappen",
                    "description": "Max Verstappen made a controversial overtake on Lewis Hamilton, similar to today's move.",
                    "significance": "This moment defined the 2021 championship battle.",
                    "impact": "Verstappen won his first World Championship that year",
                    "similarity": 0.92
                },
                "Safety car deployed": {
                    "year": "2019",
                    "event": "German GP - Multiple safety car periods",
                    "driver": "Multiple drivers",
                    "description": "The 2019 German GP had multiple safety car periods, creating chaos and opportunities.",
                    "significance": "This race showed how safety cars can completely change race outcomes.",
                    "impact": "Race had 5 safety car periods",
                    "similarity": 0.78
                },
                "Pit stop strategy change": {
                    "year": "2016",
                    "event": "Monaco GP - Strategic pit stop gamble",
                    "driver": "Lewis Hamilton",
                    "description": "Hamilton's team made a strategic pit stop that changed the race outcome.",
                    "significance": "Demonstrated the importance of pit stop strategy in F1.",
                    "impact": "Hamilton won the race despite starting from pole",
                    "similarity": 0.73
                },
                "Weather conditions worsen": {
                    "year": "2007",
                    "event": "Japanese GP - Typhoon conditions",
                    "driver": "Lewis Hamilton",
                    "description": "Extreme weather conditions led to race delays and strategy changes.",
                    "significance": "One of the most weather-affected races in F1 history.",
                    "impact": "Race was shortened due to safety concerns",
                    "similarity": 0.81
                }
            }
            
            # Get historical data
            historical_data = historical_events.get(selected_event, {
                "year": "2020",
                "event": "Generic F1 event",
                "driver": "Multiple drivers",
                "description": "Similar event in F1 history",
                "significance": "Important moment in F1",
                "impact": "Changed F1 regulations",
                "similarity": 0.65
            })
            
            # Display historical information
            st.subheader("Historical Context")
            st.write(f"**Current Event:** {selected_event}")
            st.write(f"**Historical Event:** {historical_data['event']}")
            st.write(f"**Year:** {historical_data['year']}")
            st.write(f"**Driver:** {historical_data['driver']}")
            st.write(f"**Description:** {historical_data['description']}")
            st.write(f"**Significance:** {historical_data['significance']}")
            st.write(f"**Impact:** {historical_data['impact']}")
            
            # Show similarity score
            st.subheader("Connection Analysis")
            similarity = historical_data['similarity']
            st.write(f"**Similarity Score:** {similarity:.1%}")
            st.progress(similarity)
            
            if similarity > 0.8:
                st.success("Strong historical connection!")
            elif similarity > 0.6:
                st.warning("Moderate historical connection.")
            else:
                st.info("Weak historical connection.")
            
            # Show timeline
            st.subheader("F1 Timeline")
            timeline_years = ["2003", "2007", "2016", "2019", "2021", "2024"]
            timeline_events = [
                "Alonso's rookie season",
                "Typhoon conditions",
                "Strategic pit stops",
                "Safety car chaos",
                "Championship battle",
                "Current race"
            ]
            
            for year, event in zip(timeline_years, timeline_events):
                if year == historical_data['year']:
                    st.write(f"🎯 **{year}** - {event} (Selected)")
                else:
                    st.write(f"📅 **{year}** - {event}")
            
            # Show AR/VR experience
            st.subheader("AR/VR Experience")
            st.write("**Spatial Audio:** Historical commentary from the era")
            st.write("**Visual Overlay:** Side-by-side comparison of events")
            st.write("**Interactive Elements:** Touch to explore different angles")
            st.write("**3D Reconstruction:** Recreate the historical moment")
    
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
            import random
            st.info(random.choice(facts))

def show_multilingual_commentary():
    st.header("🌍 Multilingual Commentary")
    st.markdown("Simplified commentary in multiple languages for all fans!")
    
    # Import comprehensive translation function
    from utils.translation import translate_text_comprehensive
    import random
    
    # Simple translation function for user input
    def translate_text(text, target_language):
        # Use the comprehensive translation function
        return translate_text_comprehensive(text, target_language)
    
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
            st.success("Translation complete!")
            
            # Translate the user's input
            translated_text = translate_text(commentary_input, target_language)
            
            # Show results
            st.subheader("Translated Commentary")
            st.write(f"**Language:** {target_language}")
            st.write(f"**Original:** {commentary_input}")
            st.write(f"**Translated:** {translated_text}")
            
            # Show if translation actually changed anything
            if translated_text == commentary_input:
                st.warning("⚠️ Translation didn't change the text. This might indicate an issue with the translation function.")
            else:
                st.success("✅ Translation successful!")
            
        
        # Summary generator
        st.subheader("Auto Summary Generator")
        if st.button("Generate Summary", key="summary_btn"):
            # Generate intelligent summary based on commentary
            words = commentary_input.split()
            key_actions = []
            
            # Extract key information
            if "leads" in commentary_input.lower():
                key_actions.append("Leader identified")
            if "closing" in commentary_input.lower() or "gap" in commentary_input.lower():
                key_actions.append("Chase in progress")
            if "pits" in commentary_input.lower() or "pit" in commentary_input.lower():
                key_actions.append("Pit stop occurred")
            if "lap" in commentary_input.lower():
                lap_number = next((word for word in words if word.isdigit()), "Unknown")
                key_actions.append(f"Lap {lap_number}")
            
            # Create summary
            if key_actions:
                summary = f"Key events: {', '.join(key_actions)}"
            else:
                summary = "Verstappen leads, Hamilton chasing, Alonso pits for tires."
            
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
            # Quick translations for common phrases
            quick_translations = {
                "Safety car deployed": {
                    "Spanish": "Coche de seguridad desplegado",
                    "French": "Voiture de sécurité déployée",
                    "German": "Safety Car eingesetzt",
                    "Italian": "Safety car schierato",
                    "Portuguese": "Carro de segurança implantado",
                    "Japanese": "セーフティカーが投入されました"
                },
                "Driver in the lead": {
                    "Spanish": "Piloto en el liderato",
                    "French": "Pilote en tête",
                    "German": "Fahrer in Führung",
                    "Italian": "Pilota in testa",
                    "Portuguese": "Piloto na liderança",
                    "Japanese": "リーダーのドライバー"
                },
                "Pit stop required": {
                    "Spanish": "Pit stop requerido",
                    "French": "Arrêt aux stands requis",
                    "German": "Boxenstopp erforderlich",
                    "Italian": "Pit stop richiesto",
                    "Portuguese": "Pit stop necessário",
                    "Japanese": "ピットストップが必要"
                },
                "Race finished": {
                    "Spanish": "Carrera terminada",
                    "French": "Course terminée",
                    "German": "Rennen beendet",
                    "Italian": "Gara finita",
                    "Portuguese": "Corrida terminada",
                    "Japanese": "レース終了"
                }
            }
            
            translations = quick_translations.get(selected_phrase, {})
            
            st.write(f"**Original:** {selected_phrase}")
            st.write("**Translations:**")
            
            for language, translation in translations.items():
                st.write(f"• **{language}:** {translation}")
            
            if not translations:
                st.write("Translation not available for this phrase.")

def show_fan_engagement():
    st.title("🎉 Ai.lonso - Viral Fan Engagement Engine")
    st.markdown("Creating shareable F1 moments and viral content!")
    
    # Feature selection
    feature = st.selectbox(
        "Choose a feature to explore:",
        ["Meme Generator", "Reel Creator", "Photo Generator", 
         "Pit-Stop Game", "Live Chatbot", "Fan Polls"]
    )
    
    if feature == "Meme Generator":
        show_meme_generator()
    elif feature == "Reel Creator":
        show_reel_creator()
    elif feature == "Photo Generator":
        show_photo_generator()
    elif feature == "Pit-Stop Game":
        show_pitstop_game()
    elif feature == "Live Chatbot":
        show_live_chatbot()
    elif feature == "Fan Polls":
        show_fan_polls()

def show_meme_generator():
    st.header("😂 Meme Generator")
    st.markdown("Turn F1 race moments into viral memes instantly!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Create Your Meme")
        
        # Image upload
        uploaded_image = st.file_uploader("Upload an image:", type=['png', 'jpg', 'jpeg'])
        
        if uploaded_image is not None:
            st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
            
            # Meme text
            top_text = st.text_input("Top text:", value="MY WEEKEND PLANS")
            bottom_text = st.text_input("Bottom text:", value="vs REALITY")
            
            # Style options
            font_size = st.slider("Font Size", 20, 80, 40)
            text_color = st.color_picker("Text Color", "#FFFFFF")
            
            if st.button("Generate Meme", key="meme_btn"):
                st.success("Meme generated!")
                
                # Create a simple meme using PIL
                from PIL import Image, ImageDraw, ImageFont
                import io
                
                # Open the uploaded image
                image = Image.open(uploaded_image)
                
                # Create a drawing context
                draw = ImageDraw.Draw(image)
                
                # Try to use a font, fallback to default
                try:
                    font = ImageFont.truetype("arial.ttf", font_size)
                except:
                    font = ImageFont.load_default()
                
                # Get image dimensions
                width, height = image.size
                
                # Calculate text positions
                top_text_bbox = draw.textbbox((0, 0), top_text, font=font)
                bottom_text_bbox = draw.textbbox((0, 0), bottom_text, font=font)
                
                top_text_width = top_text_bbox[2] - top_text_bbox[0]
                bottom_text_width = bottom_text_bbox[2] - bottom_text_bbox[0]
                
                # Center text horizontally
                top_x = (width - top_text_width) // 2
                bottom_x = (width - bottom_text_width) // 2
                
                # Position text vertically
                top_y = 20
                bottom_y = height - font_size - 20
                
                # Add text with outline for better visibility
                # Draw black outline
                for dx in [-2, -1, 0, 1, 2]:
                    for dy in [-2, -1, 0, 1, 2]:
                        if dx != 0 or dy != 0:
                            draw.text((top_x + dx, top_y + dy), top_text, font=font, fill="black")
                            draw.text((bottom_x + dx, bottom_y + dy), bottom_text, font=font, fill="black")
                
                # Draw main text
                draw.text((top_x, top_y), top_text, font=font, fill=text_color)
                draw.text((bottom_x, bottom_y), bottom_text, font=font, fill=text_color)
                
                # Display the meme
                st.image(image, caption="Your F1 Meme", use_container_width=True)
                
                # Download option
                img_buffer = io.BytesIO()
                image.save(img_buffer, format='PNG')
                img_buffer.seek(0)
                
                st.download_button(
                    label="Download Meme",
                    data=img_buffer.getvalue(),
                    file_name="f1_meme.png",
                    mime="image/png"
                )
    
    with col2:
        st.subheader("Popular F1 Memes")
        
        # Trending memes
        trending_memes = [
            {"text": "When you're leading but see a safety car", "likes": 1250},
            {"text": "Pit stop in 2.3 seconds", "likes": 980},
            {"text": "Qualifying P1 vs Race P20", "likes": 756},
            {"text": "When your teammate crashes", "likes": 654}
        ]
        
        for meme in trending_memes:
            st.write(f"**{meme['text']}**")
            st.write(f"👍 {meme['likes']} likes")
            st.write("---")

def show_reel_creator():
    st.header("🎬 Reel Creator")
    st.markdown("Auto-generate short shareable videos from race highlights!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Create Reel")
        
        # Video upload
        uploaded_video = st.file_uploader("Upload race video:", type=['mp4', 'avi', 'mov'])
        
        if uploaded_video is not None:
            st.video(uploaded_video)
            
            # Reel settings
            st.subheader("Reel Settings")
            
            duration = st.slider("Reel Duration (seconds)", 15, 60, 30)
            style = st.selectbox("Style", ["Action Packed", "Emotional", "Funny", "Dramatic"])
            music = st.selectbox("Background Music", ["Epic", "Electronic", "Rock", "None"])
            
            if st.button("Generate Reel", key="reel_btn"):
                st.success("Reel created!")
                
                # Show video information
                st.subheader("Video Analysis")
                st.write(f"**Duration:** {duration} seconds")
                st.write(f"**Style:** {style}")
                st.write(f"**Music:** {music}")
                
                # Simulate highlight detection
                st.subheader("Detected Highlights")
                highlights = [
                    {"timestamp": "00:15", "moment": "Spectacular overtake", "confidence": 0.9},
                    {"timestamp": "01:30", "moment": "Close call at turn 3", "confidence": 0.8},
                    {"timestamp": "02:45", "moment": "Victory celebration", "confidence": 0.95}
                ]
                
                for highlight in highlights:
                    st.write(f"**{highlight['timestamp']}** - {highlight['moment']} (Confidence: {highlight['confidence']*100:.0f}%)")
                
                # Show reel preview
                st.subheader("Reel Preview")
                st.info("🎬 Your F1 highlight reel would be displayed here")
                st.write("**Reel Features:**")
                st.write("• Auto-detected exciting moments")
                st.write("• Dynamic music synchronization")
                st.write("• Professional transitions")
                st.write("• Social media optimized")
                
                # Share options
                st.subheader("Share Options")
                col_share1, col_share2, col_share3 = st.columns(3)
                
                with col_share1:
                    if st.button("📱 Share to Instagram"):
                        st.success("Ready to share on Instagram!")
                with col_share2:
                    if st.button("🐦 Share to Twitter"):
                        st.success("Ready to share on Twitter!")
                with col_share3:
                    if st.button("📘 Share to Facebook"):
                        st.success("Ready to share on Facebook!")
    
    with col2:
        st.subheader("Reel Templates")
        
        # Popular templates
        templates = [
            {"name": "Crash Compilation", "duration": 30, "style": "Action"},
            {"name": "Overtake Moments", "duration": 45, "style": "Dramatic"},
            {"name": "Funny Moments", "duration": 20, "style": "Funny"},
            {"name": "Championship Moments", "duration": 60, "style": "Emotional"}
        ]
        
        for template in templates:
            st.write(f"**{template['name']}**")
            st.write(f"Duration: {template['duration']}s")
            st.write(f"Style: {template['style']}")

def show_photo_generator():
    st.header("📸 Photo Generator")
    st.markdown("Create AR selfies with F1 drivers and cars!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("AR Selfie Creator")
        
        # Photo upload
        uploaded_photo = st.file_uploader("Upload your selfie:", type=['png', 'jpg', 'jpeg'])
        
        if uploaded_photo is not None:
            st.image(uploaded_photo, caption="Your Selfie", use_column_width=True)
            
            # AR elements
            st.subheader("Add AR Elements")
            
            # Driver selection
            driver = st.selectbox("Choose driver:", 
                                ["Max Verstappen", "Lewis Hamilton", "Fernando Alonso", 
                                 "Charles Leclerc", "Lando Norris"])
            
            # Car selection
            car = st.selectbox("Choose car:", 
                             ["Red Bull RB19", "Mercedes W14", "Aston Martin AMR23", 
                              "Ferrari SF-23", "McLaren MCL60"])
            
            # Background
            background = st.selectbox("Background:", 
                                    ["Race Track", "Pit Lane", "Podium", "Garage"])
            
            if st.button("Generate AR Photo", key="ar_btn"):
                st.success("AR photo created!")
                
                # Create AR photo using PIL
                from PIL import Image, ImageDraw, ImageFont
                import io
                
                # Open the uploaded photo
                user_photo = Image.open(uploaded_photo)
                
                # Resize user photo to fit
                user_photo.thumbnail((300, 300), Image.Resampling.LANCZOS)
                
                # Create a background
                bg_width, bg_height = 600, 400
                composite = Image.new('RGB', (bg_width, bg_height), color='#2C3E50')
                
                # Paste user photo
                user_x = (bg_width - user_photo.width) // 2
                user_y = bg_height - user_photo.height - 50
                composite.paste(user_photo, (user_x, user_y))
                
                # Add AR elements
                draw = ImageDraw.Draw(composite)
                
                # Add driver info
                driver_text = f"{driver} - F1 Driver"
                try:
                    font = ImageFont.truetype("arial.ttf", 20)
                except:
                    font = ImageFont.load_default()
                
                # Add text with outline
                text_x, text_y = 10, 10
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx != 0 or dy != 0:
                            draw.text((text_x + dx, text_y + dy), driver_text, font=font, fill="black")
                
                draw.text((text_x, text_y), driver_text, font=font, fill="white")
                
                # Add car info
                car_text = f"{car} - F1 Car"
                car_y = text_y + 30
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx != 0 or dy != 0:
                            draw.text((text_x + dx, car_y + dy), car_text, font=font, fill="black")
                
                draw.text((text_x, car_y), car_text, font=font, fill="white")
                
                # Add AR frame
                frame_color = "white"
                frame_width = 3
                # Top-left corner
                draw.rectangle([10, 10, 40, 40], outline=frame_color, width=frame_width)
                draw.rectangle([10, 10, 10 + frame_width, 40], fill=frame_color)
                draw.rectangle([10, 10, 40, 10 + frame_width], fill=frame_color)
                
                # Top-right corner
                draw.rectangle([bg_width - 40, 10, bg_width - 10, 40], outline=frame_color, width=frame_width)
                draw.rectangle([bg_width - 10 - frame_width, 10, bg_width - 10, 40], fill=frame_color)
                draw.rectangle([bg_width - 40, 10, bg_width - 10, 10 + frame_width], fill=frame_color)
                
                # Bottom-left corner
                draw.rectangle([10, bg_height - 40, 40, bg_height - 10], outline=frame_color, width=frame_width)
                draw.rectangle([10, bg_height - 40, 10 + frame_width, bg_height - 10], fill=frame_color)
                draw.rectangle([10, bg_height - 10 - frame_width, 40, bg_height - 10], fill=frame_color)
                
                # Bottom-right corner
                draw.rectangle([bg_width - 40, bg_height - 40, bg_width - 10, bg_height - 10], outline=frame_color, width=frame_width)
                draw.rectangle([bg_width - 10 - frame_width, bg_height - 40, bg_width - 10, bg_height - 10], fill=frame_color)
                draw.rectangle([bg_width - 40, bg_height - 10 - frame_width, bg_width - 10, bg_height - 10], fill=frame_color)
                
                # Display the AR photo
                st.image(composite, caption="Your AR F1 Photo", use_container_width=True)
                
                # Download option
                img_buffer = io.BytesIO()
                composite.save(img_buffer, format='PNG')
                img_buffer.seek(0)
                
                st.download_button(
                    label="Download AR Photo",
                    data=img_buffer.getvalue(),
                    file_name="f1_ar_photo.png",
                    mime="image/png"
                )
    
    with col2:
        st.subheader("AR Gallery")
        
        # Sample AR photos
        st.markdown("### Sample AR Photos")
        st.info("📸 Sample AR Photo 1")
        st.info("📸 Sample AR Photo 2")
        st.info("📸 Sample AR Photo 3")

def show_pitstop_game():
    st.header("🏁 Pit-Stop Game")
    st.markdown("Test your reflexes in our tire-changing mini-game!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Game Arena")
        
        # Game state
        if 'game_score' not in st.session_state:
            st.session_state.game_score = 0
        if 'game_time' not in st.session_state:
            st.session_state.game_time = 0
        if 'game_active' not in st.session_state:
            st.session_state.game_active = False
        if 'game_start_time' not in st.session_state:
            st.session_state.game_start_time = None
        
        # Update game time if game is active
        if st.session_state.game_active and st.session_state.game_start_time is not None:
            import time
            current_time = time.time()
            elapsed_time = current_time - st.session_state.game_start_time
            st.session_state.game_time = round(elapsed_time, 1)
        
        # Game display
        if st.session_state.game_active:
            st.info("🏎️ Pit Stop Challenge - Click the buttons as fast as you can!")
            st.write(f"Score: {st.session_state.game_score}")
            st.write(f"Time: {st.session_state.game_time}s")
            
            # Add refresh button to update timer
            if st.button("🔄 Update Timer", key="refresh_timer_btn"):
                st.rerun()
        else:
            st.info("🏁 Ready to Race? Click 'Start Game' to begin!")
        
        # Game controls
        col_start, col_stop = st.columns(2)
        
        with col_start:
            if st.button("Start Game", key="start_game_btn"):
                import time
                st.session_state.game_active = True
                st.session_state.game_score = 0
                st.session_state.game_time = 0
                st.session_state.game_start_time = time.time()
                st.rerun()
        
        with col_stop:
            if st.button("Stop Game", key="stop_game_btn"):
                st.session_state.game_active = False
                st.session_state.game_start_time = None
                st.rerun()
        
        # Quick actions
        if st.session_state.game_active:
            st.subheader("Quick Actions")
            col_action1, col_action2, col_action3 = st.columns(3)
            
            with col_action1:
                if st.button("🔧 Fix Tire", key="fix_tire_btn"):
                    st.session_state.game_score += 10
                    st.success("Tire fixed! +10 points")
                    # Update timer when action is performed
                    if st.session_state.game_start_time is not None:
                        import time
                        current_time = time.time()
                        elapsed_time = current_time - st.session_state.game_start_time
                        st.session_state.game_time = round(elapsed_time, 1)
                    st.rerun()
            
            with col_action2:
                if st.button("⚡ Add Fuel", key="add_fuel_btn"):
                    st.session_state.game_score += 15
                    st.success("Fuel added! +15 points")
                    # Update timer when action is performed
                    if st.session_state.game_start_time is not None:
                        import time
                        current_time = time.time()
                        elapsed_time = current_time - st.session_state.game_start_time
                        st.session_state.game_time = round(elapsed_time, 1)
                    st.rerun()
            
            with col_action3:
                if st.button("🛞 Change Tire", key="change_tire_btn"):
                    st.session_state.game_score += 20
                    st.success("Tire changed! +20 points")
                    # Update timer when action is performed
                    if st.session_state.game_start_time is not None:
                        import time
                        current_time = time.time()
                        elapsed_time = current_time - st.session_state.game_start_time
                        st.session_state.game_time = round(elapsed_time, 1)
                    st.rerun()
    
    with col2:
        st.subheader("Leaderboard")
        
        # Top scores
        leaderboard = [
            {"name": "SpeedDemon", "score": 1250, "time": "2.3s"},
            {"name": "PitMaster", "score": 1180, "time": "2.1s"},
            {"name": "TireKing", "score": 1100, "time": "2.5s"},
            {"name": "FastLane", "score": 1050, "time": "2.8s"},
            {"name": "You", "score": st.session_state.game_score, "time": f"{st.session_state.game_time}s"}
        ]
        
        for i, player in enumerate(leaderboard):
            if i < 4:
                st.write(f"**{i+1}.** {player['name']} - {player['score']} pts ({player['time']})")
            else:
                st.write(f"**Your Score:** {player['score']} pts ({player['time']})")

def show_live_chatbot():
    st.header("🤖 Live Chatbot")
    st.markdown("Chat with Ai.lonso for real-time F1 updates and answers!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Chat with Ai.lonso")
        
        # Chat history
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = [
                {"role": "assistant", "content": "Hello! I'm Ai.lonso, your F1 digital companion. How can I help you today?"}
            ]
        
        # Display chat history
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.write(f"**You:** {message['content']}")
            else:
                st.write(f"**Ai.lonso:** {message['content']}")
        
        # Chat input
        user_input = st.text_input("Ask Ai.lonso anything about F1:", key="chat_input")
        
        if st.button("Send", key="send_btn") and user_input:
            # Add user message
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            
            # Smart AI response based on question
            import random
            
            # F1 knowledge base
            f1_responses = {
                "race status": [
                    "🏎️ The race is currently in progress with Max Verstappen leading!",
                    "🏁 Lewis Hamilton is closing the gap on the leader.",
                    "⚡ Safety car has been deployed due to an incident.",
                    "🚩 The race is under red flag conditions."
                ],
                "championship": [
                    "🏆 Max Verstappen leads the championship with 350 points.",
                    "🥈 Lewis Hamilton is second with 280 points.",
                    "🥉 Fernando Alonso is third with 250 points.",
                    "📊 The championship battle is heating up!"
                ],
                "next race": [
                    "🗓️ The next race is the Brazilian Grand Prix in São Paulo.",
                    "🏁 Race weekend starts on Friday with practice sessions.",
                    "⏰ Qualifying is scheduled for Saturday afternoon.",
                    "🌤️ Weather forecast shows sunny conditions."
                ],
                "weather": [
                    "🌡️ Current track temperature is 35°C.",
                    "💨 Air temperature is 28°C with light winds.",
                    "☀️ Weather conditions are perfect for racing.",
                    "🌧️ Rain is expected in the next hour."
                ],
                "default": [
                    "🏎️ That's a great question about F1!",
                    "🏁 I love talking about Formula 1 racing!",
                    "⚡ F1 is such an exciting sport!",
                    "🤖 Let me help you with that F1 question!"
                ]
            }
            
            # Determine response category
            user_input_lower = user_input.lower()
            if any(word in user_input_lower for word in ["race", "status", "leading"]):
                response = random.choice(f1_responses["race status"])
            elif any(word in user_input_lower for word in ["championship", "points", "leader"]):
                response = random.choice(f1_responses["championship"])
            elif any(word in user_input_lower for word in ["next", "when", "schedule"]):
                response = random.choice(f1_responses["next race"])
            elif any(word in user_input_lower for word in ["weather", "temperature", "rain"]):
                response = random.choice(f1_responses["weather"])
            else:
                response = random.choice(f1_responses["default"])
            
            # Add AI response
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            
            st.rerun()
    
    with col2:
        st.subheader("Quick Questions")
        quick_questions = [
            "What's the current race status?",
            "Who's leading the championship?",
            "When is the next race?",
            "What are the weather conditions?"
        ]
        
        for question in quick_questions:
            if st.button(question, key=f"quick_{question}"):
                st.session_state.chat_history.append({"role": "user", "content": question})
                
                # Provide specific answers for quick questions
                if "race status" in question.lower():
                    response = "🏎️ The race is currently in progress with Max Verstappen leading by 2.3 seconds!"
                elif "championship" in question.lower():
                    response = "🏆 Max Verstappen leads the championship with 350 points, followed by Lewis Hamilton with 280 points."
                elif "next race" in question.lower():
                    response = "🗓️ The next race is the Brazilian Grand Prix in São Paulo, scheduled for this weekend."
                elif "weather" in question.lower():
                    response = "🌡️ Current track temperature is 35°C with sunny conditions and light winds."
                else:
                    response = "🏎️ " + question + " - Great question!"
                
                st.session_state.chat_history.append({"role": "assistant", "content": response})
                st.rerun()

def show_fan_polls():
    st.header("📊 Fan Polls & Predictions")
    st.markdown("Vote on predictions and see what other fans think!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Active Polls")
        
        # Poll data
        polls = [
            {
                "id": 1,
                "question": "Who will win the next race?",
                "options": ["Max Verstappen", "Lewis Hamilton", "Fernando Alonso", "Charles Leclerc"],
                "votes": [45, 30, 15, 10],
                "total_votes": 100
            },
            {
                "id": 2,
                "question": "Will there be a safety car?",
                "options": ["Yes", "No"],
                "votes": [60, 40],
                "total_votes": 100
            },
            {
                "id": 3,
                "question": "Which team will have the fastest pit stop?",
                "options": ["Red Bull", "Mercedes", "Ferrari", "McLaren"],
                "votes": [35, 25, 20, 20],
                "total_votes": 100
            }
        ]
        
        for poll in polls:
            st.markdown(f"**{poll['question']}**")
            
            # Display poll results
            for i, option in enumerate(poll['options']):
                percentage = (poll['votes'][i] / poll['total_votes']) * 100
                st.write(f"{option}: {poll['votes'][i]} votes ({percentage:.1f}%)")
                
                # Progress bar
                st.progress(poll['votes'][i] / poll['total_votes'])
            
            st.write("---")
    
    with col2:
        st.subheader("Poll Statistics")
        
        # Overall stats
        st.markdown("### Overall Stats")
        st.write("Total polls: 15")
        st.write("Total votes: 2,450")
        st.write("Active users: 156")
        
        # Top predictions
        st.markdown("### Top Predictions")
        predictions = [
            "Max Verstappen wins (45%)",
            "Safety car deployed (60%)",
            "Red Bull fastest pit (35%)",
            "Lewis Hamilton podium (70%)"
        ]
        
        for prediction in predictions:
            st.write(f"• {prediction}")

if __name__ == "__main__":
    main()
