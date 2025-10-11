import torch
import torch.nn as nn
import torchvision.models as models
import time

# define the device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def load_oral_cancer_model(model_save_path='Model/UmlomoV1.pth'):
    """
    Load the pre-trained MobileNetV2 model for oral cancer detection with optimization
    """
    num_classes = 2  # Normal and Oral Cancer
    
    try:
        start_time = time.time()
        
        # load pre-trained MobileNetV2
        model = models.mobilenet_v2(pretrained=True)
        
        # modify classifier for the specific number of classes
        model.classifier[1] = nn.Linear(model.last_channel, num_classes)
        model = model.to(device)
        
        # load the trained weights with optimized settings
        checkpoint = torch.load(model_save_path, map_location=device, weights_only=True)
        model.load_state_dict(checkpoint)
        model.eval()  # evaluation mode
        
        # optimize for inference
        if torch.__version__ >= '2.0.0':
            model = torch.compile(model)  # PyTorch 2.0 compilation for faster inference
        
        load_time = time.time() - start_time
        
        print(f"Model loaded successfully from {model_save_path}")
        print(f"Using device: {device}")
        print(f"Model loading time: {load_time:.2f} seconds")
        print(f"Model optimized for inference: {'Yes' if torch.__version__ >= '2.0.0' else 'No'}")
        
        return model
        
    except FileNotFoundError:
        print(f"Error: Model file not found at {model_save_path}")
        print("Please ensure the model file exists in the Model/ directory")
        return None
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# class names
CLASS_NAMES = ['Normal', 'Oral Cancer']

print("Model loader module optimized and ready")