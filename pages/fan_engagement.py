import streamlit as st
try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False

import numpy as np
from PIL import Image, ImageDraw, ImageFont

try:
    import moviepy.editor as mp
    MOVIEPY_AVAILABLE = True
except ImportError:
    MOVIEPY_AVAILABLE = False

import random
import time
import json
from utils.meme_generator import MemeGenerator
from utils.reel_creator import ReelCreator
from utils.photo_generator import PhotoGenerator
from utils.pitstop_game import PitStopGame
from utils.chatbot import F1Chatbot
from utils.fan_polls import FanPolls

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
            image = Image.open(uploaded_image)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            # Meme text
            top_text = st.text_input("Top text:", value="MY WEEKEND PLANS")
            bottom_text = st.text_input("Bottom text:", value="vs REALITY")
            
            # Style options
            font_size = st.slider("Font Size", 20, 80, 40)
            text_color = st.color_picker("Text Color", "#FFFFFF")
            
            if st.button("Generate Meme", key="meme_btn"):
                meme_gen = MemeGenerator()
                meme_image = meme_gen.create_meme(image, top_text, bottom_text, font_size, text_color)
                
                st.success("Meme generated!")
                st.image(meme_image, caption="Your F1 Meme", use_column_width=True)
                
                # Download option
                st.download_button(
                    label="Download Meme",
                    data=meme_image.tobytes(),
                    file_name="f1_meme.png",
                    mime="image/png"
                )
        
        # Template gallery
        st.subheader("F1 Meme Templates")
        templates = [
            "assets/meme_template_1.jpg",
            "assets/meme_template_2.jpg", 
            "assets/meme_template_3.jpg"
        ]
        
        selected_template = st.selectbox("Choose template:", ["Template 1", "Template 2", "Template 3"])
        template_index = int(selected_template.split()[-1]) - 1
        
        if st.button("Use Template", key="template_btn"):
            st.image(templates[template_index], caption=f"Using {selected_template}")
    
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
        
        # Quick meme buttons
        st.markdown("### Quick Memes")
        if st.button("Generate Random Meme"):
            random_meme = MemeGenerator().generate_random_meme()
            st.image(random_meme, caption="Random F1 Meme")

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
                reel_creator = ReelCreator()
                
                with st.spinner("Creating your reel..."):
                    if MOVIEPY_AVAILABLE:
                        reel_video = reel_creator.create_reel(uploaded_video, duration, style, music)
                    else:
                        reel_video = "assets/reels/demo_reel.mp4"
                        st.info("🎬 Video processing features require moviepy. Using demo reel.")
                
                st.success("Reel created!")
                st.video(reel_video)
                
                # Share options
                st.subheader("Share Options")
                col_share1, col_share2, col_share3 = st.columns(3)
                
                with col_share1:
                    st.button("📱 Share to Instagram")
                with col_share2:
                    st.button("🐦 Share to Twitter")
                with col_share3:
                    st.button("📘 Share to Facebook")
        
        # Auto-highlight detection
        st.subheader("Auto-Highlight Detection")
        if st.button("Find Highlights", key="highlight_btn"):
            highlights = ReelCreator().detect_highlights(uploaded_video)
            
            st.write("Detected highlights:")
            for i, highlight in enumerate(highlights):
                st.write(f"{i+1}. {highlight['moment']} at {highlight['timestamp']}")
    
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
            if st.button(f"Use {template['name']}", key=f"template_{template['name']}"):
                st.success(f"Applied {template['name']} template!")

def show_photo_generator():
    st.header("📸 Photo Generator")
    st.markdown("Create AR selfies with F1 drivers and cars!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("AR Selfie Creator")
        
        # Photo upload
        uploaded_photo = st.file_uploader("Upload your selfie:", type=['png', 'jpg', 'jpeg'])
        
        if uploaded_photo is not None:
            photo = Image.open(uploaded_photo)
            st.image(photo, caption="Your Selfie", use_column_width=True)
            
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
                photo_gen = PhotoGenerator()
                
                with st.spinner("Creating AR photo..."):
                    ar_photo = photo_gen.create_ar_photo(photo, driver, car, background)
                
                st.success("AR photo created!")
                st.image(ar_photo, caption="Your AR F1 Photo", use_column_width=True)
                
                # Download
                st.download_button(
                    label="Download AR Photo",
                    data=ar_photo.tobytes(),
                    file_name="f1_ar_photo.png",
                    mime="image/png"
                )
        
        # Quick AR options
        st.subheader("Quick AR Options")
        quick_options = [
            "Podium Celebration",
            "Pit Stop Action",
            "Victory Lap",
            "Grid Walk"
        ]
        
        selected_option = st.selectbox("Quick AR Scene:", quick_options)
        if st.button("Apply Quick AR", key="quick_ar_btn"):
            st.success(f"Applied {selected_option} AR scene!")
    
    with col2:
        st.subheader("AR Gallery")
        
        # Sample AR photos
        st.markdown("### Sample AR Photos")
        sample_photos = [
            "assets/ar_sample_1.jpg",
            "assets/ar_sample_2.jpg",
            "assets/ar_sample_3.jpg"
        ]
        
        for i, photo in enumerate(sample_photos):
            st.image(photo, caption=f"Sample AR Photo {i+1}")
        
        # AR Stats
        st.markdown("### Your AR Stats")
        st.write("Photos created: 12")
        st.write("Favorite driver: Max Verstappen")
        st.write("Most used car: Red Bull RB19")

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
        
        # Game display
        game_placeholder = st.empty()
        
        if st.session_state.game_active:
            # Show game interface
            game_placeholder.markdown("""
            <div style="text-align: center; padding: 20px; border: 2px solid #1f77b4; border-radius: 10px;">
                <h3>🏎️ Pit Stop Challenge</h3>
                <p>Click the buttons as fast as you can!</p>
                <div style="display: flex; justify-content: space-around; margin: 20px;">
                    <button style="padding: 10px 20px; font-size: 16px;">🔧</button>
                    <button style="padding: 10px 20px; font-size: 16px;">⚡</button>
                    <button style="padding: 10px 20px; font-size: 16px;">🛞</button>
                </div>
                <p>Score: {}</p>
                <p>Time: {}s</p>
            </div>
            """.format(st.session_state.game_score, st.session_state.game_time), unsafe_allow_html=True)
        else:
            game_placeholder.markdown("""
            <div style="text-align: center; padding: 40px; border: 2px dashed #ccc; border-radius: 10px;">
                <h3>🏁 Ready to Race?</h3>
                <p>Click "Start Game" to begin the pit stop challenge!</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Game controls
        col_start, col_stop = st.columns(2)
        
        with col_start:
            if st.button("Start Game", key="start_game_btn"):
                st.session_state.game_active = True
                st.session_state.game_score = 0
                st.session_state.game_time = 0
                st.rerun()
        
        with col_stop:
            if st.button("Stop Game", key="stop_game_btn"):
                st.session_state.game_active = False
                st.rerun()
        
        # Quick actions
        if st.session_state.game_active:
            st.subheader("Quick Actions")
            col_action1, col_action2, col_action3 = st.columns(3)
            
            with col_action1:
                if st.button("🔧 Fix Tire", key="fix_tire_btn"):
                    st.session_state.game_score += 10
                    st.success("Tire fixed! +10 points")
            
            with col_action2:
                if st.button("⚡ Add Fuel", key="add_fuel_btn"):
                    st.session_state.game_score += 15
                    st.success("Fuel added! +15 points")
            
            with col_action3:
                if st.button("🛞 Change Tire", key="change_tire_btn"):
                    st.session_state.game_score += 20
                    st.success("Tire changed! +20 points")
    
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
        
        # Game stats
        st.subheader("Game Stats")
        st.write("Best time: 2.1s")
        st.write("Average time: 3.2s")
        st.write("Games played: 45")
        
        # Sponsor branding
        st.markdown("### Sponsored by")
        try:
            st.image("assets/turbo_oil_logo.png", caption="TURBO OIL")
        except:
            st.info("🏁 TURBO OIL - Official Sponsor")

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
        chat_container = st.container()
        with chat_container:
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
            
            # Get AI response
            chatbot = F1Chatbot()
            response = chatbot.get_response(user_input)
            
            # Add AI response
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            
            st.rerun()
        
        # Quick questions
        st.subheader("Quick Questions")
        quick_questions = [
            "What's the current race status?",
            "Who's leading the championship?",
            "When is the next race?",
            "What are the weather conditions?"
        ]
        
        for question in quick_questions:
            if st.button(question, key=f"quick_{question}"):
                chatbot = F1Chatbot()
                response = chatbot.get_response(question)
                st.session_state.chat_history.append({"role": "user", "content": question})
                st.session_state.chat_history.append({"role": "assistant", "content": response})
                st.rerun()
    
    with col2:
        st.subheader("Chat Features")
        
        # Chat settings
        st.markdown("### Chat Settings")
        chat_mode = st.selectbox("Chat Mode", ["General", "Technical", "Beginner", "Expert"])
        response_style = st.selectbox("Response Style", ["Friendly", "Professional", "Casual"])
        
        # Live updates
        st.markdown("### Live Updates")
        if st.button("Enable Live Updates"):
            st.success("Live updates enabled!")
        
        # Chat history
        st.markdown("### Chat History")
        if st.button("Clear Chat"):
            st.session_state.chat_history = [
                {"role": "assistant", "content": "Hello! I'm Ai.lonso, your F1 digital companion. How can I help you today?"}
            ]
            st.rerun()
        
        # Export chat
        if st.button("Export Chat"):
            chat_data = json.dumps(st.session_state.chat_history, indent=2)
            st.download_button(
                label="Download Chat",
                data=chat_data,
                file_name="chat_history.json",
                mime="application/json"
            )

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
        
        # Create new poll
        st.subheader("Create New Poll")
        new_question = st.text_input("Poll Question:")
        new_options = st.text_area("Options (one per line):")
        
        if st.button("Create Poll", key="create_poll_btn"):
            if new_question and new_options:
                st.success("Poll created successfully!")
            else:
                st.error("Please fill in both question and options.")
    
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
        
        # Your predictions
        st.markdown("### Your Predictions")
        st.write("Accuracy: 78%")
        st.write("Predictions made: 23")
        st.write("Correct predictions: 18")
        
        # Gamification
        st.markdown("### Achievements")
        achievements = [
            "🎯 Prediction Master",
            "🏆 Poll Champion", 
            "📈 Trend Spotter",
            "🔮 Future Seer"
        ]
        
        for achievement in achievements:
            st.write(achievement)
