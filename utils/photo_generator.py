from PIL import Image, ImageDraw, ImageFont
import random
from typing import Tuple, List

class PhotoGenerator:
    """Handles AR photo generation with F1 drivers and cars"""
    
    def __init__(self):
        self.drivers = {
            "Max Verstappen": {
                "image": "assets/drivers/max_verstappen.png",
                "team": "Red Bull",
                "number": "1"
            },
            "Lewis Hamilton": {
                "image": "assets/drivers/lewis_hamilton.png",
                "team": "Mercedes",
                "number": "44"
            },
            "Fernando Alonso": {
                "image": "assets/drivers/fernando_alonso.png",
                "team": "Aston Martin",
                "number": "14"
            },
            "Charles Leclerc": {
                "image": "assets/drivers/charles_leclerc.png",
                "team": "Ferrari",
                "number": "16"
            },
            "Lando Norris": {
                "image": "assets/drivers/lando_norris.png",
                "team": "McLaren",
                "number": "4"
            }
        }
        
        self.cars = {
            "Red Bull RB19": {
                "image": "assets/cars/red_bull_rb19.png",
                "color": "#1E41FF",
                "team": "Red Bull"
            },
            "Mercedes W14": {
                "image": "assets/cars/mercedes_w14.png",
                "color": "#00D2BE",
                "team": "Mercedes"
            },
            "Aston Martin AMR23": {
                "image": "assets/cars/aston_martin_amr23.png",
                "color": "#006F62",
                "team": "Aston Martin"
            },
            "Ferrari SF-23": {
                "image": "assets/cars/ferrari_sf23.png",
                "color": "#DC143C",
                "team": "Ferrari"
            },
            "McLaren MCL60": {
                "image": "assets/cars/mclaren_mcl60.png",
                "color": "#FF8700",
                "team": "McLaren"
            }
        }
        
        self.backgrounds = {
            "Race Track": "assets/backgrounds/race_track.jpg",
            "Pit Lane": "assets/backgrounds/pit_lane.jpg",
            "Podium": "assets/backgrounds/podium.jpg",
            "Garage": "assets/backgrounds/garage.jpg"
        }
        
        self.ar_scenes = {
            "Podium Celebration": {
                "driver_position": (200, 100),
                "car_position": (150, 300),
                "background": "Podium"
            },
            "Pit Stop Action": {
                "driver_position": (300, 150),
                "car_position": (100, 250),
                "background": "Pit Lane"
            },
            "Victory Lap": {
                "driver_position": (250, 120),
                "car_position": (200, 280),
                "background": "Race Track"
            },
            "Grid Walk": {
                "driver_position": (180, 140),
                "car_position": (120, 320),
                "background": "Race Track"
            }
        }
    
    def create_ar_photo(self, user_photo: Image.Image, driver: str, car: str, 
                       background: str) -> Image.Image:
        """Create AR photo with driver, car, and background"""
        try:
            # Load background
            bg_image = self._load_background(background)
            
            # Resize user photo to fit
            user_photo = self._resize_user_photo(user_photo, bg_image.size)
            
            # Create composite image
            composite = Image.new('RGBA', bg_image.size, (255, 255, 255, 255))
            composite.paste(bg_image, (0, 0))
            
            # Add user photo
            user_position = self._calculate_user_position(user_photo.size, bg_image.size)
            composite.paste(user_photo, user_position, user_photo if user_photo.mode == 'RGBA' else None)
            
            # Add driver overlay
            driver_image = self._load_driver_image(driver)
            if driver_image:
                driver_position = self._calculate_driver_position(driver_image.size, bg_image.size)
                composite.paste(driver_image, driver_position, driver_image)
            
            # Add car overlay
            car_image = self._load_car_image(car)
            if car_image:
                car_position = self._calculate_car_position(car_image.size, bg_image.size)
                composite.paste(car_image, car_position, car_image)
            
            # Add AR effects
            composite = self._add_ar_effects(composite, driver, car)
            
            return composite.convert('RGB')
            
        except Exception as e:
            print(f"Error creating AR photo: {e}")
            return self._create_fallback_ar_photo(user_photo, driver, car)
    
    def _load_background(self, background_name: str) -> Image.Image:
        """Load background image"""
        try:
            bg_path = self.backgrounds[background_name]
            return Image.open(bg_path)
        except:
            # Fallback: create colored background
            return Image.new('RGB', (800, 600), color='#2C3E50')
    
    def _resize_user_photo(self, user_photo: Image.Image, bg_size: Tuple[int, int]) -> Image.Image:
        """Resize user photo to appropriate size"""
        # Resize to fit in the background
        max_width = bg_size[0] // 3
        max_height = bg_size[1] // 2
        
        user_photo.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        return user_photo
    
    def _calculate_user_position(self, user_size: Tuple[int, int], bg_size: Tuple[int, int]) -> Tuple[int, int]:
        """Calculate position for user photo"""
        x = (bg_size[0] - user_size[0]) // 2
        y = bg_size[1] - user_size[1] - 50  # Bottom of image
        return (x, y)
    
    def _load_driver_image(self, driver_name: str) -> Image.Image:
        """Load driver image"""
        try:
            driver_path = self.drivers[driver_name]["image"]
            return Image.open(driver_path)
        except:
            return None
    
    def _calculate_driver_position(self, driver_size: Tuple[int, int], bg_size: Tuple[int, int]) -> Tuple[int, int]:
        """Calculate position for driver overlay"""
        x = bg_size[0] - driver_size[0] - 50  # Right side
        y = 50  # Top
        return (x, y)
    
    def _load_car_image(self, car_name: str) -> Image.Image:
        """Load car image"""
        try:
            car_path = self.cars[car_name]["image"]
            return Image.open(car_path)
        except:
            return None
    
    def _calculate_car_position(self, car_size: Tuple[int, int], bg_size: Tuple[int, int]) -> Tuple[int, int]:
        """Calculate position for car overlay"""
        x = 50  # Left side
        y = bg_size[1] - car_size[1] - 100  # Bottom
        return (x, y)
    
    def _add_ar_effects(self, image: Image.Image, driver: str, car: str) -> Image.Image:
        """Add AR effects to the image"""
        draw = ImageDraw.Draw(image)
        
        # Add driver info
        driver_info = self.drivers.get(driver, {})
        if driver_info:
            driver_text = f"{driver} #{driver_info.get('number', '?')}"
            self._add_text_with_outline(draw, driver_text, (10, 10), "#FFFFFF")
        
        # Add car info
        car_info = self.cars.get(car, {})
        if car_info:
            car_text = car_info.get('team', car)
            self._add_text_with_outline(draw, car_text, (10, 40), "#FFFFFF")
        
        # Add AR frame
        self._add_ar_frame(draw, image.size)
        
        return image
    
    def _add_text_with_outline(self, draw: ImageDraw.Draw, text: str, position: Tuple[int, int], color: str):
        """Add text with outline"""
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()
        
        x, y = position
        
        # Draw outline
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    draw.text((x + dx, y + dy), text, font=font, fill="black")
        
        # Draw main text
        draw.text((x, y), text, font=font, fill=color)
    
    def _add_ar_frame(self, draw: ImageDraw.Draw, size: Tuple[int, int]):
        """Add AR-style frame to image"""
        width, height = size
        
        # Draw corner brackets
        bracket_size = 30
        bracket_width = 3
        
        # Top-left
        draw.rectangle([10, 10, 10 + bracket_size, 10 + bracket_width], fill="white")
        draw.rectangle([10, 10, 10 + bracket_width, 10 + bracket_size], fill="white")
        
        # Top-right
        draw.rectangle([width - 10 - bracket_size, 10, width - 10, 10 + bracket_width], fill="white")
        draw.rectangle([width - 10 - bracket_width, 10, width - 10, 10 + bracket_size], fill="white")
        
        # Bottom-left
        draw.rectangle([10, height - 10 - bracket_width, 10 + bracket_size, height - 10], fill="white")
        draw.rectangle([10, height - 10 - bracket_size, 10 + bracket_width, height - 10], fill="white")
        
        # Bottom-right
        draw.rectangle([width - 10 - bracket_size, height - 10 - bracket_width, width - 10, height - 10], fill="white")
        draw.rectangle([width - 10 - bracket_width, height - 10 - bracket_size, width - 10, height - 10], fill="white")
    
    def _create_fallback_ar_photo(self, user_photo: Image.Image, driver: str, car: str) -> Image.Image:
        """Create fallback AR photo when assets are not available"""
        # Create a simple composite
        composite = Image.new('RGB', (800, 600), color='#2C3E50')
        
        # Resize and paste user photo
        user_photo.thumbnail((200, 200), Image.Resampling.LANCZOS)
        composite.paste(user_photo, (300, 200))
        
        # Add text overlays
        draw = ImageDraw.Draw(composite)
        
        try:
            font = ImageFont.truetype("arial.ttf", 30)
        except:
            font = ImageFont.load_default()
        
        draw.text((250, 50), f"AR Photo with {driver}", font=font, fill="white")
        draw.text((250, 450), f"and {car}", font=font, fill="white")
        
        return composite
    
    def apply_quick_ar_scene(self, user_photo: Image.Image, scene_name: str) -> Image.Image:
        """Apply a quick AR scene"""
        scene = self.ar_scenes.get(scene_name, self.ar_scenes["Podium Celebration"])
        
        # Get driver and car from scene
        driver = "Max Verstappen"  # Default
        car = "Red Bull RB19"  # Default
        background = scene["background"]
        
        return self.create_ar_photo(user_photo, driver, car, background)
    
    def get_available_drivers(self) -> List[str]:
        """Get list of available drivers"""
        return list(self.drivers.keys())
    
    def get_available_cars(self) -> List[str]:
        """Get list of available cars"""
        return list(self.cars.keys())
    
    def get_available_backgrounds(self) -> List[str]:
        """Get list of available backgrounds"""
        return list(self.backgrounds.keys())
    
    def get_ar_scenes(self) -> List[str]:
        """Get list of available AR scenes"""
        return list(self.ar_scenes.keys())


