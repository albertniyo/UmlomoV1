import torch
import torch.nn as nn
import torchvision.models as models
import time
import sys

# define the device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def load_oral_cancer_model(model_save_path='Model/UmlomoV1.pth'):
    """
    Load the pre-trained MobileNetV2 model for oral cancer detection with compatibility fixes
    """
    num_classes = 2  # normal and Oral Cancer classes
    
    try:
        start_time = time.time()
        
        # fix: Use new weights parameter instead of deprecated pretrained
        model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.IMAGENET1K_V1)
        
        # classifier for the specific number of classes modified
        model.classifier[1] = nn.Linear(model.last_channel, num_classes)
        model = model.to(device)
        
        # load the trained weights with compatibility fixes
        checkpoint = torch.load(model_save_path, map_location=device)
        model.load_state_dict(checkpoint)
        model.eval()  # Set to evaluation mode
        
        # fix: Remove torch.compile() for Python 3.12+ compatibilit-  it was under Dynamo 
        # go for alternative optimization if available and compatible
        if hasattr(torch, 'compile') and sys.version_info < (3, 12):
            try:
                model = torch.compile(model)
                optimization_status = "Yes (torch.compile)"
            except Exception as e:
                optimization_status = f"No (compile failed: {e})"
        else:
            # alternative optimization: set optimizations for inference
            torch.backends.cudnn.benchmark = True
            optimization_status = "Yes (cudnn benchmark)"
        
        load_time = time.time() - start_time
        
        print(f"Model loaded successfully from {model_save_path}")
        print(f"Using device: {device}")
        print(f"⏱Model loading time: {load_time:.2f} seconds")
        print(f"Model optimized for inference: {optimization_status}")
        print(f"Python version: {sys.version.split()[0]}")
        print(f"PyTorch version: {torch.__version__}") # no need kweli
        
        return model
        
    except FileNotFoundError:
        print(f"Error: Model file not found at {model_save_path}")
        print("Please ensure the model file exists in the Model/ directory")
        return None
    except Exception as e:
        print(f"Error loading model: {e}")
        print("Time for documentation then - Pytorch compatibility")
        return None

# class names (should match your training)
CLASS_NAMES = ['Normal', 'Oral Cancer']

print("Model loader module updated with compatibility fixes")