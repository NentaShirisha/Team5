#!/usr/bin/env python3
"""
Setup script for Ai.lonso F1 Digital Companion
"""

import os
import sys
import subprocess

def create_directories():
    """Create necessary directories"""
    directories = [
        "assets/drivers",
        "assets/cars", 
        "assets/backgrounds",
        "assets/memes",
        "assets/reels",
        "assets/sign_language",
        "assets/emotions",
        "assets/ai_lonso",
        "assets/historical",
        "assets/ar_samples",
        "assets/logos",
        "assets/music"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

def install_dependencies():
    """Install required dependencies"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def check_streamlit():
    """Check if Streamlit is properly installed"""
    try:
        import streamlit
        print(f"✅ Streamlit {streamlit.__version__} is installed")
        return True
    except ImportError:
        print("❌ Streamlit is not installed")
        return False

def main():
    """Main setup function"""
    print("🏎️ Ai.lonso F1 Digital Companion - Setup")
    print("=" * 50)
    
    # Create directories
    print("\n📁 Creating directories...")
    create_directories()
    
    # Install dependencies
    print("\n📦 Installing dependencies...")
    if not install_dependencies():
        print("Please install dependencies manually: pip install -r requirements.txt")
        return False
    
    # Check Streamlit
    print("\n🔍 Checking installation...")
    if not check_streamlit():
        print("Please install Streamlit: pip install streamlit")
        return False
    
    print("\n✅ Setup completed successfully!")
    print("\n🚀 To run the application:")
    print("   streamlit run main.py")
    print("\n🎮 To run the demo:")
    print("   python demo.py")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)


