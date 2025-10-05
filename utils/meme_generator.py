from PIL import Image, ImageDraw, ImageFont
import random
from typing import Tuple, List

class MemeGenerator:
    """Handles meme generation functionality"""
    
    def __init__(self):
        self.meme_templates = [
            "assets/meme_template_1.jpg",
            "assets/meme_template_2.jpg",
            "assets/meme_template_3.jpg"
        ]
        
        self.f1_meme_texts = {
            "top_texts": [
                "MY WEEKEND PLANS",
                "WHEN YOU'RE LEADING",
                "QUALIFYING P1",
                "RACE STRATEGY",
                "PIT STOP TIME"
            ],
            "bottom_texts": [
                "vs REALITY",
                "BUT SEE SAFETY CAR",
                "vs RACE P20",
                "vs ACTUAL RACE",
                "vs ACTUAL TIME"
            ]
        }
        
        self.font_sizes = {
            "small": 30,
            "medium": 40,
            "large": 50,
            "extra_large": 60
        }
    
    def create_meme(self, image: Image.Image, top_text: str, bottom_text: str, 
                   font_size: int, text_color: str) -> Image.Image:
        """Create a meme with top and bottom text"""
        # Create a copy of the image
        meme_image = image.copy()
        
        # Get image dimensions
        width, height = meme_image.size
        
        # Create drawing context
        draw = ImageDraw.Draw(meme_image)
        
        # Try to load a font, fallback to default if not available
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()
        
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
        self._add_text_with_outline(draw, top_text, (top_x, top_y), font, text_color)
        self._add_text_with_outline(draw, bottom_text, (bottom_x, bottom_y), font, text_color)
        
        return meme_image
    
    def _add_text_with_outline(self, draw: ImageDraw.Draw, text: str, position: Tuple[int, int], 
                              font: ImageFont.ImageFont, text_color: str):
        """Add text with black outline for better visibility"""
        x, y = position
        
        # Draw black outline
        for dx in [-2, -1, 0, 1, 2]:
            for dy in [-2, -1, 0, 1, 2]:
                if dx != 0 or dy != 0:
                    draw.text((x + dx, y + dy), text, font=font, fill="black")
        
        # Draw main text
        draw.text((x, y), text, font=font, fill=text_color)
    
    def generate_random_meme(self) -> Image.Image:
        """Generate a random F1-themed meme"""
        # Select random template
        template_path = random.choice(self.meme_templates)
        
        # Select random texts
        top_text = random.choice(self.f1_meme_texts["top_texts"])
        bottom_text = random.choice(self.f1_meme_texts["bottom_texts"])
        
        # Select random font size and color
        font_size = random.choice(list(self.font_sizes.values()))
        text_color = random.choice(["#FFFFFF", "#FFFF00", "#FF0000", "#00FF00"])
        
        # Create meme
        try:
            template_image = Image.open(template_path)
            meme = self.create_meme(template_image, top_text, bottom_text, font_size, text_color)
            return meme
        except:
            # Fallback: create a simple colored image
            return self._create_fallback_meme(top_text, bottom_text)
    
    def _create_fallback_meme(self, top_text: str, bottom_text: str) -> Image.Image:
        """Create a fallback meme when template is not available"""
        # Create a simple colored background
        image = Image.new('RGB', (500, 400), color='#1f77b4')
        draw = ImageDraw.Draw(image)
        
        # Add text
        try:
            font = ImageFont.truetype("arial.ttf", 30)
        except:
            font = ImageFont.load_default()
        
        # Center text
        top_bbox = draw.textbbox((0, 0), top_text, font=font)
        bottom_bbox = draw.textbbox((0, 0), bottom_text, font=font)
        
        top_width = top_bbox[2] - top_bbox[0]
        bottom_width = bottom_bbox[2] - bottom_bbox[0]
        
        top_x = (500 - top_width) // 2
        bottom_x = (500 - bottom_width) // 2
        
        draw.text((top_x, 50), top_text, font=font, fill="white")
        draw.text((bottom_x, 300), bottom_text, font=font, fill="white")
        
        return image
    
    def get_meme_templates(self) -> List[str]:
        """Get list of available meme templates"""
        return self.meme_templates
    
    def create_custom_meme(self, image: Image.Image, texts: List[str], 
                          positions: List[Tuple[int, int]], 
                          font_size: int, text_color: str) -> Image.Image:
        """Create a custom meme with multiple text elements"""
        meme_image = image.copy()
        draw = ImageDraw.Draw(meme_image)
        
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()
        
        for text, position in zip(texts, positions):
            self._add_text_with_outline(draw, text, position, font, text_color)
        
        return meme_image


