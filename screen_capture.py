"""
Screen capture and OCR module
"""
import pyautogui
from PIL import Image
import pytesseract
from datetime import datetime
from pathlib import Path
from typing import Tuple, Optional
import cv2
import numpy as np

class ScreenCapture:
    """Handles screen capture and text extraction"""
    
    def __init__(self, screenshots_dir: Path, tesseract_cmd: str):
        self.screenshots_dir = screenshots_dir
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    
    def capture_screen(self, region: Optional[Tuple[int, int, int, int]] = None) -> Image.Image:
        """
        Capture screen or a region of the screen
        
        Args:
            region: Optional tuple (x, y, width, height) to capture specific region
            
        Returns:
            PIL Image object
        """
        if region:
            screenshot = pyautogui.screenshot(region=region)
        else:
            screenshot = pyautogui.screenshot()
        
        return screenshot
    
    def save_screenshot(self, image: Image.Image, prefix: str = 'capture') -> Path:
        """Save screenshot to file"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{prefix}_{timestamp}.png"
        filepath = self.screenshots_dir / filename
        image.save(filepath)
        return filepath
    
    def extract_text(self, image: Image.Image, preprocess: bool = True) -> str:
        """
        Extract text from image using OCR
        
        Args:
            image: PIL Image object
            preprocess: Whether to preprocess image for better OCR results
            
        Returns:
            Extracted text
        """
        if preprocess:
            image = self._preprocess_image(image)
        
        # Use pytesseract to extract text
        text = pytesseract.image_to_string(image, lang='eng')
        return text.strip()
    
    def _preprocess_image(self, image: Image.Image) -> Image.Image:
        """
        Preprocess image for better OCR results
        - Convert to grayscale
        - Apply thresholding
        - Denoise
        """
        # Convert PIL Image to OpenCV format
        img_array = np.array(image)
        
        # Convert to grayscale
        if len(img_array.shape) == 3:
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        else:
            gray = img_array
        
        # Apply thresholding to get binary image
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # Denoise
        denoised = cv2.fastNlMeansDenoising(thresh)
        
        # Convert back to PIL Image
        return Image.fromarray(denoised)
    
    def capture_and_extract(self, region: Optional[Tuple[int, int, int, int]] = None,
                          save: bool = True) -> Tuple[str, Optional[Path]]:
        """
        Capture screen and extract text in one operation
        
        Returns:
            Tuple of (extracted_text, screenshot_path)
        """
        screenshot = self.capture_screen(region)
        text = self.extract_text(screenshot)
        
        filepath = None
        if save:
            filepath = self.save_screenshot(screenshot)
        
        return text, filepath
    
    def get_screen_size(self) -> Tuple[int, int]:
        """Get screen dimensions"""
        return pyautogui.size()
