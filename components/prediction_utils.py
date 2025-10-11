import torch
import time

def predict_image_class(image_tensor, model, class_names, device):
    """
    Makes a prediction on a single preprocessed image tensor
    Optimized for performance
    """
    if image_tensor is None:
        return "Error: Could not process image", 0.0

    try:
        start_time = time.time()
        
        # move the image tensor to the correct device
        image_tensor = image_tensor.to(device)

        # set the model to evaluation mode
        model.eval()

        with torch.no_grad():
            # get the model's output (logits)
            outputs = model(image_tensor)

            # apply softmax to get probabilities
            probabilities = torch.softmax(outputs, dim=1)

            # get the predicted class index and the corresponding probability
            predicted_prob, predicted_idx = torch.max(probabilities, 1)

            # get the predicted class name
            predicted_class = class_names[predicted_idx.item()]
            
            inference_time = time.time() - start_time
            print(f"Prediction completed in {inference_time:.3f} seconds")

            return predicted_class, predicted_prob.item()
            
    except Exception as e:
        return f"Prediction error: {str(e)}", 0.0

def get_prediction_feedback(predicted_class, predicted_probability):
    """
    Generate detailed feedback based on prediction results
    Optimized with pre-defined templates
    """
    
    # pre-defined feedback templates(as dict) for better performance
    # better since we didn't use LLM for feedback *_*
    FEEDBACK_TEMPLATES = {
        'normal_high': {
            'main_message': "Your oral health appears to be good based on the image analysis.",
            'urgency_level': 'low',
            'detailed_advice': [
                "Keep up the good work with your oral hygiene!",
                "Continue with regular dental check-ups."
            ],
            'recommendations': [
                "Brush your teeth twice a day with fluoride toothpaste.",
                "Floss daily to remove food particles and plaque between teeth.",
                "Visit your dentist regularly for checkups and cleanings.",
                "Maintain a healthy diet and limit sugary snacks and drinks.",
                "Avoid smoking and excessive alcohol consumption."
            ]
        },
        'normal_moderate': {
            'main_message': "The analysis shows no clear signs of oral cancer, but confidence is moderate.",
            'urgency_level': 'medium', 
            'detailed_advice': [
                "While the image doesn't clearly show signs of oral cancer, it's always best to consult a healthcare professional for a definitive diagnosis.",
                "Be aware of any persistent sores, lumps, or unusual changes in your mouth."
            ],
            'recommendations': [
                "Consult a dentist or doctor if you notice any changes in your oral health.",
                "Schedule a professional dental examination for comprehensive assessment."
            ]
        },
        'cancer_high': {
            'main_message': "The analysis suggests potential signs that require immediate professional attention.",
            'urgency_level': 'high',
            'detailed_advice': [
                "This is a serious finding that requires immediate professional evaluation.",
                "Do not rely solely on this analysis; professional medical evaluation is essential."
            ],
            'recommendations': [
                "Contact a healthcare professional (dentist or oral surgeon) immediately.",
                "Schedule an appointment for further examination and diagnosis.",
                "Be prepared to discuss your medical history and any symptoms you've experienced.", 
                "Do not delay seeking professional medical advice."
            ]
        },
        'cancer_moderate': {
            'main_message': "The analysis shows some features that warrant professional evaluation.",
            'urgency_level': 'medium',
            'detailed_advice': [
                "While this finding warrants attention, it's important not to panic.",
                "Professional evaluation is needed to confirm any diagnosis."
            ],
            'recommendations': [
                "Schedule an appointment with a dentist or doctor for evaluation.",
                "Share this analysis result with your healthcare professional.",
                "Monitor for any changes in your oral health and report them to your doctor."
            ]
        },
        'error': {
            'main_message': "Could not make a clear prediction from the image.",
            'urgency_level': 'low',
            'detailed_advice': [
                "Please ensure the image is clear and well-lit.",
                "Try again with a different image or consult a healthcare professional."
            ],
            'recommendations': [
                "Ensure good lighting and clear focus when taking oral photos.",
                "Make sure the entire area of concern is visible in the image.",
                "Consult a healthcare professional for a definitive diagnosis.",
                "And don't complicate things fam, haha."
            ]
        }
    }
    
    if predicted_class == 'Normal':
        if predicted_probability > 0.8:
            return FEEDBACK_TEMPLATES['normal_high']
        else:
            return FEEDBACK_TEMPLATES['normal_moderate']
            
    elif predicted_class == 'Oral Cancer':
        if predicted_probability > 0.7:
            return FEEDBACK_TEMPLATES['cancer_high']
        else:
            return FEEDBACK_TEMPLATES['cancer_moderate']
    else:
        return FEEDBACK_TEMPLATES['error']

print("Prediction utilities optimized with performance enhancements")