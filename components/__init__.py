"""
Components Package
Optimized module initialization for oral cancer detection
"""

import sys
import os

# Add the components directory to the Python path
sys.path.append(os.path.dirname(__file__))

# Import key functions and classes for easy access
from .img_transform import get_image_transform, preprocess_image, preprocess_image_for_display
from .model_loader import load_oral_cancer_model, CLASS_NAMES, device
from .prediction_utils import predict_image_class, get_prediction_feedback

# package version
__version__ = "1.0.0"
__author__ = "Umlomo Team"
__description__ = "AI components for oral health analysis"

# export public interface
__all__ = [
    # image transformation
    'get_image_transform',
    'preprocess_image', 
    'preprocess_image_for_display',
    
    # model loading
    'load_oral_cancer_model',
    'CLASS_NAMES',
    'device',
    
    # prediction utilities
    'predict_image_class',
    'get_prediction_feedback',
]

print(f"Components v{__version__} initialized successfully")