# helper_functions.py
import cv2

def resize_image(image, width, height):
    """Resize an image to the specified width and height."""
    return cv2.resize(image, (width, height))

def convert_to_grayscale(image):
    """Convert an image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
