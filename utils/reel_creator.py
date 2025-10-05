try:
    import moviepy.editor as mp
    MOVIEPY_AVAILABLE = True
except ImportError:
    MOVIEPY_AVAILABLE = False
    print("Warning: moviepy not available. Video features will be limited.")

import random
from typing import List, Dict, Tuple
import os

class ReelCreator:
    """Handles video reel creation and highlight detection"""
    
    def __init__(self):
        self.reel_templates = {
            "Action Packed": {
                "duration": 30,
                "style": "fast_cuts",
                "music": "epic",
                "effects": ["zoom", "speed_up"]
            },
            "Emotional": {
                "duration": 45,
                "style": "slow_motion",
                "music": "emotional",
                "effects": ["fade", "slow_motion"]
            },
            "Funny": {
                "duration": 20,
                "style": "quick_cuts",
                "music": "upbeat",
                "effects": ["zoom", "freeze_frame"]
            },
            "Dramatic": {
                "duration": 60,
                "style": "cinematic",
                "music": "dramatic",
                "effects": ["fade", "zoom", "slow_motion"]
            }
        }
        
        self.music_tracks = {
            "Epic": "assets/music/epic.mp3",
            "Electronic": "assets/music/electronic.mp3",
            "Rock": "assets/music/rock.mp3",
            "None": None
        }
        
        self.highlight_keywords = [
            "overtake", "crash", "finish", "victory", "championship",
            "pole", "fastest", "record", "spectacular", "amazing"
        ]
    
    def create_reel(self, video_path: str, duration: int, style: str, music: str) -> str:
        """Create a reel from uploaded video"""
        if not MOVIEPY_AVAILABLE:
            return "assets/reels/demo_reel.mp4"  # Return placeholder path
        
        try:
            # Load video
            video = mp.VideoFileClip(video_path)
            
            # Get template settings
            template = self.reel_templates.get(style, self.reel_templates["Action Packed"])
            
            # Adjust duration
            if duration > video.duration:
                duration = video.duration
            
            # Create reel
            reel = self._process_video(video, duration, template)
            
            # Add music if specified
            if music != "None" and music in self.music_tracks:
                reel = self._add_music(reel, music)
            
            # Save reel
            output_path = f"assets/reels/reel_{random.randint(1000, 9999)}.mp4"
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            reel.write_videofile(output_path, temp_audiofile='temp-audio.m4a', remove_temp=True)
            
            return output_path
            
        except Exception as e:
            print(f"Error creating reel: {e}")
            return "assets/reels/demo_reel.mp4"  # Return placeholder path
    
    def _process_video(self, video, duration: int, template: Dict):
        """Process video according to template style"""
        if not MOVIEPY_AVAILABLE:
            return None
            
        # Cut video to desired duration
        if video.duration > duration:
            start_time = random.uniform(0, video.duration - duration)
            processed_video = video.subclip(start_time, start_time + duration)
        else:
            processed_video = video
        
        # Apply effects based on style
        if template["style"] == "fast_cuts":
            processed_video = self._apply_fast_cuts(processed_video)
        elif template["style"] == "slow_motion":
            processed_video = self._apply_slow_motion(processed_video)
        elif template["style"] == "cinematic":
            processed_video = self._apply_cinematic_effects(processed_video)
        
        return processed_video
    
    def _apply_fast_cuts(self, video):
        """Apply fast cutting effects"""
        if not MOVIEPY_AVAILABLE:
            return video
            
        # Simulate fast cuts by creating multiple short clips
        clips = []
        segment_duration = video.duration / 10  # 10 segments
        
        for i in range(10):
            start = i * segment_duration
            end = min((i + 1) * segment_duration, video.duration)
            clip = video.subclip(start, end)
            clips.append(clip)
        
        return mp.concatenate_videoclips(clips)
    
    def _apply_slow_motion(self, video):
        """Apply slow motion effects"""
        if not MOVIEPY_AVAILABLE:
            return video
            
        # Slow down the video
        return video.fx(mp.vfx.speedx, 0.5)
    
    def _apply_cinematic_effects(self, video):
        """Apply cinematic effects"""
        if not MOVIEPY_AVAILABLE:
            return video
            
        # Add fade in/out
        return video.fadein(1).fadeout(1)
    
    def _add_music(self, video, music_type: str):
        """Add background music to video"""
        if not MOVIEPY_AVAILABLE:
            return video
            
        try:
            music_path = self.music_tracks[music_type]
            if music_path and os.path.exists(music_path):
                audio = mp.AudioFileClip(music_path)
                # Match audio duration to video
                audio = audio.subclip(0, video.duration)
                return video.set_audio(audio)
        except:
            pass
        
        return video
    
    def detect_highlights(self, video_path: str) -> List[Dict]:
        """Detect highlights in video (simulated)"""
        # In a real implementation, this would use computer vision
        # to detect exciting moments, crashes, overtakes, etc.
        
        highlights = [
            {
                "timestamp": "00:15",
                "moment": "Spectacular overtake",
                "confidence": 0.9,
                "type": "overtake"
            },
            {
                "timestamp": "01:30",
                "moment": "Close call at turn 3",
                "confidence": 0.8,
                "type": "near_miss"
            },
            {
                "timestamp": "02:45",
                "moment": "Victory celebration",
                "confidence": 0.95,
                "type": "victory"
            },
            {
                "timestamp": "03:20",
                "moment": "Pit stop drama",
                "confidence": 0.7,
                "type": "pit_stop"
            }
        ]
        
        return highlights
    
    def create_highlight_reel(self, video_path: str, highlight_type: str) -> str:
        """Create a reel focusing on specific highlight types"""
        if not MOVIEPY_AVAILABLE:
            return f"assets/reels/highlight_{highlight_type}_demo.mp4"
            
        highlights = self.detect_highlights(video_path)
        
        # Filter highlights by type
        filtered_highlights = [h for h in highlights if h["type"] == highlight_type]
        
        if not filtered_highlights:
            return f"assets/reels/highlight_{highlight_type}_demo.mp4"
        
        try:
            # Create reel from highlights
            video = mp.VideoFileClip(video_path)
            clips = []
            
            for highlight in filtered_highlights:
                # Convert timestamp to seconds
                time_parts = highlight["timestamp"].split(":")
                seconds = int(time_parts[0]) * 60 + int(time_parts[1])
                
                # Create 5-second clip around highlight
                start = max(0, seconds - 2.5)
                end = min(video.duration, seconds + 2.5)
                clip = video.subclip(start, end)
                clips.append(clip)
            
            if clips:
                highlight_reel = mp.concatenate_videoclips(clips)
                output_path = f"assets/reels/highlight_{highlight_type}_{random.randint(1000, 9999)}.mp4"
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                highlight_reel.write_videofile(output_path, temp_audiofile='temp-audio.m4a', remove_temp=True)
                return output_path
        except Exception as e:
            print(f"Error creating highlight reel: {e}")
        
        return f"assets/reels/highlight_{highlight_type}_demo.mp4"
    
    def get_reel_templates(self) -> Dict:
        """Get available reel templates"""
        return self.reel_templates
    
    def create_auto_reel(self, video_path: str) -> str:
        """Automatically create the best reel based on video content"""
        highlights = self.detect_highlights(video_path)
        
        # Determine best style based on highlights
        if any(h["type"] == "crash" for h in highlights):
            style = "Dramatic"
        elif any(h["type"] == "victory" for h in highlights):
            style = "Emotional"
        elif len(highlights) > 5:
            style = "Action Packed"
        else:
            style = "Funny"
        
        # Create reel with determined style
        template = self.reel_templates[style]
        return self.create_reel(video_path, template["duration"], style, "Epic")
