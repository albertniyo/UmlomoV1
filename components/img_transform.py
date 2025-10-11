from PIL import Image
import torch
from torchvision import transforms
import functools

@functools.lru_cache(maxsize=1)
def get_image_transform():
    """
    Define the image transformation pipeline that matches model training
    Uses the same transform as validation during training
    Cached for performance
    """
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  # match validation transform size
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    return transform

def preprocess_image(image, transform=None):
    """
    Preprocesses a PIL image for model prediction
    Uses the same transformation as validation during training
    """
    try:
        # use cached transform if not provided
        if transform is None:
            transform = get_image_transform()
        
        # convert to RGB if needed
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # apply transformations (same as validation transform during training)
        image_tensor = transform(image)
        
        # add batch dimension (B, C, H, W)
        image_tensor = image_tensor.unsqueeze(0)
        
        return image_tensor
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

def preprocess_image_for_display(image, size=(224, 224)):
    """
    Preprocess image for display purposes (without normalization)
    Optimized for performance
    """
    try:
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # simple resize for display - no need for full transform
        image.thumbnail(size, Image.Resampling.LANCZOS)
        return image
    except Exception as e:
        print(f"Error processing image for display: {e}")
        return None

print("Image transformation module optimized with caching")