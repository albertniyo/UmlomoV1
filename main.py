import streamlit as st
from streamlit_navigation_bar import st_navbar
import time
from PIL import Image

# ML components imports
from components import (
    load_oral_cancer_model, 
    CLASS_NAMES, 
    device,
    get_image_transform, 
    preprocess_image,
    predict_image_class, 
    get_prediction_feedback
)

# Set page configuration
st.set_page_config(
    page_title="Umlomo - Oral Health AI",
    page_icon="🦷",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize ML pipeline with caching
@st.cache_resource
def initialize_ml_pipeline():
    """Initialize the complete ML pipeline with optimizations"""
    model = load_oral_cancer_model('Model/UmlomoV1.pth')
    transform = get_image_transform()
    return model, transform

# Load model and transform
model, transform = initialize_ml_pipeline()

# Custom CSS for styling - ADDED NEW STYLES FOR ML RESULTS
st.markdown("""
<style>
    .main-header {
        font-size: 4rem !important;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f0f2f6;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .section-header {
        font-size: 2rem !important;
        color: #2e86ab;
        margin-top: 2rem;
        margin-bottom: 1rem;
        text-align: center;
    }
    .contributor-card {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f0f2f6;
        text-align: center;
        margin: 1rem 0;
        border-left: 4px solid #1f77b4;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .footer {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        text-align: center;
        padding: 15px 0;
        margin-top: 3rem;
        height: 60px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        position: static;
    }
    .upload-box {
        border: 2px dashed #1f77b4;
        border-radius: 10px;
        padding: 3rem;
        text-align: center;
        margin: 2rem 0;
        background-color: #f8f9fa;
        transition: all 0.3s ease;
    }
    .upload-box:hover {
        background-color: #e8f4fd;
        border-color: #2e86ab;
    }
    .result-high {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #ff4757;
    }
    .result-medium {
        background: linear-gradient(135deg, #ffa502 0%, #e67e22 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #ff7f50;
    }
    .result-low {
        background: linear-gradient(135deg, #2ed573 0%, #1dd1a1 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #00b894;
    }
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #1f77b4;
    }
    .stat-card {
        background: linear-gradient(135deg, #1f77b4 0%, #2e86ab 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
    }
    .benefit-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-top: 4px solid #1f77b4;
    }
    /* Navbar height matching */
    .css-1d391kg, [data-testid="stHeader"] {
        height: 60px;
    }
</style>
""", unsafe_allow_html=True)

def render_footer():
    """Render the static footer with same height as navbar"""
    st.markdown("""
    <div class="footer">
        <p style="margin: 0; font-size: 0.9em;">Developed with ♥ for Better Smiles</p>
        <p style="margin: 0; font-size: 0.7em;">© 2025 Umlomo Team. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

def render_home_tab():
    """Home tab content without videos"""
    
    # Big project name - home tab
    st.markdown('<div class="main-header">Umlomo</div>', unsafe_allow_html=True)
    
    # Introduction section
    st.markdown('<div class="section-header">Why Oral Health Matters</div>', unsafe_allow_html=True)
    
    # Three key features in columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>Preventive Care</h3>
            <p>Regular check-ups can prevent 85% of dental issues before they become serious problems. 
            Early intervention saves time, money, and discomfort while maintaining optimal oral health.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>Early Detection</h3>
            <p>AI-powered analysis helps detect potential issues months before they become visible to the naked eye. 
            Our advanced algorithms identify patterns that even trained professionals might miss.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>Personalized Insights</h3>
            <p>Get customized recommendations based on your unique oral health profile. 
            Our system adapts to your specific needs and provides actionable advice for improvement.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Key insights section
    st.markdown("---")
    st.markdown('<div class="section-header">Key Insights</div>', unsafe_allow_html=True)
    
    insight_col1, insight_col2, insight_col3 = st.columns(3)
    
    with insight_col1:
        st.markdown("""
        <div class="stat-card">
            <h2>90%</h2>
            <p>of systemic diseases have oral manifestations that can be detected early through proper screening</p>
        </div>
        """, unsafe_allow_html=True)
    
    with insight_col2:
        st.markdown("""
        <div class="stat-card">
            <h2>47%</h2>
            <p>reduction in dental emergencies achieved through regular AI monitoring and preventive care</p>
        </div>
        """, unsafe_allow_html=True)
    
    with insight_col3:
        st.markdown("""
        <div class="stat-card">
            <h2>5x Faster</h2>
            <p>diagnosis compared to traditional methods, enabling quicker treatment and better outcomes</p>
        </div>
        """, unsafe_allow_html=True)

def analyze_image_with_model(uploaded_file):
    """Analyze uploaded image using the ML model - REPLACED SIMULATED FUNCTION"""
    try:
        # Open and preprocess the image
        image = Image.open(uploaded_file)
        
        with st.spinner("Processing image and analyzing..."):
            # Preprocess image
            image_tensor = preprocess_image(image, transform)
            
            if image_tensor is None:
                return None, None, "Error processing image"
            
            # Make prediction
            predicted_class, probability = predict_image_class(
                image_tensor, model, CLASS_NAMES, device
            )
            
            # Get detailed feedback
            feedback = get_prediction_feedback(predicted_class, probability)
            
            return predicted_class, probability, feedback
            
    except Exception as e:
        return None, None, f"Analysis error: {str(e)}"

def render_test_tab():
    """Test tab with ACTUAL ML model integration - UPDATED"""
    st.markdown('<div class="section-header">Oral Health Analysis</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### AI-Powered Oral Screening
    Upload a clear photo of your oral cavity to get an AI-powered analysis. 
    Our model can help identify potential concerns that may require professional attention.
    
    **Note:** This is a screening tool, not a replacement for professional medical diagnosis.
    """)
    
    # Centered upload section
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
            <h3>Upload Oral Photo</h3>
            <p>Get AI analysis of your oral health</p>
        </div>
        """, unsafe_allow_html=True)
        
        # File uploader
        uploaded_file = st.file_uploader(
            "Upload a clear photo of your mouth area", 
            type=['jpg', 'jpeg', 'png'],
            help="Ensure good lighting and clear focus for best results",
            key="file_uploader"
        )
        
        if uploaded_file is not None:
            # Display the uploaded image
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
            
            # Analyze button - FIXED COLUMN NESTING
            if st.button("Analyze Oral Health", type="primary", use_container_width=True):
                # Perform analysis
                predicted_class, probability, feedback = analyze_image_with_model(uploaded_file)
                
                if predicted_class is not None and feedback is not None:
                    # Display results
                    st.markdown("---")
                    st.markdown("## Analysis Results")
                    
                    # Show prediction confidence - FIXED COLUMN STRUCTURE
                    result_col1, result_col2 = st.columns(2)
                    with result_col1:
                        st.metric("Prediction", predicted_class)
                    with result_col2:
                        st.metric("Confidence Level", f"{probability:.1%}")
                    
                    # Display appropriate result card based on urgency
                    if feedback['urgency_level'] == 'high':
                        st.markdown(f"""
                        <div class="result-high">
                            <h3>{feedback['main_message']}</h3>
                        </div>
                        """, unsafe_allow_html=True)
                    elif feedback['urgency_level'] == 'medium':
                        st.markdown(f"""
                        <div class="result-medium">
                            <h3>{feedback['main_message']}</h3>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class="result-low">
                            <h3>{feedback['main_message']}</h3>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Detailed advice
                    st.markdown("### Detailed Assessment")
                    for advice in feedback['detailed_advice']:
                        st.write(f"• {advice}")
                    
                    # Recommendations
                    st.markdown("### Recommendations")
                    for i, recommendation in enumerate(feedback['recommendations'], 1):
                        st.write(f"{i}. {recommendation}")
                    
                    # Disclaimer
                    st.markdown("---")
                    st.info(
                        "**Important Disclaimer:** This AI analysis is for screening purposes only. "
                        "It is not a substitute for professional medical diagnosis. Always consult "
                        "with qualified healthcare professionals for medical concerns."
                    )
                else:
                    st.error(feedback)  # Show error message

def render_about_tab():
    """About tab with project description"""
    st.markdown('<div class="section-header">About Umlomo</div>', unsafe_allow_html=True)
    
    # Project description
    st.markdown("""
    ## Our Mission
    
    **Umlomo** (which means "mouth" in Zulu) is an AI-powered oral health platform designed to make 
    dental care **accessible, preventive, and personalized** for everyone, everywhere.
    
    We believe that everyone deserves a healthy smile, and technology should make that easier, 
    not more complicated.
    """)

def render_contributor_card(name, role, description, github_url, github_handle):
    """Render a contributor card"""
    st.markdown(f"""
    <div class="contributor-card">
        <h3>{name}</h3>
        <h5>{role}</h5>
        <p>{description}</p>
        <p>GitHub: <a href="{github_url}" style="color: #1f77b4;">Profile</a></p>
    </div>
    """, unsafe_allow_html=True)

def render_us_tab():
    """Us tab - Contributors and Links in cards"""
    st.markdown('<div class="section-header">Our Team</div>', unsafe_allow_html=True)
    
    # Team introduction
    st.markdown("""
    We're a passionate team of AI engineers, dental professionals, and designers working together 
    to revolutionize oral healthcare through cutting-edge technology and compassionate design.
    """)
    
    # Core team section
    st.markdown("### Core Team")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        render_contributor_card(
            "Albert",
            "Niyonsenga",
            "Task",
            "https://github.com/Al04ni",
            "Albert"
        )
    with col2:
        render_contributor_card(
            "Albert",
            "Niyonsenga",
            "Task",
            "https://github.com/Al04ni",
            "Albert"
        )
    
    with col3:
        render_contributor_card(
            "Albert",
            "Niyonsenga",
            "Task",
            "https://github.com/Al04ni",
            "Albert"
        )
    
    with col4:
        render_contributor_card(
            "Albert",
            "Niyonsenga",
            "Task",
            "https://github.com/Al04ni",
            "Albert"
        )

def main():
    """Main application function"""
    
    # Navigation bar with 4 tabs
    selected_tab = st_navbar(
        ["Home", "Test", "About", "Us"],
        options={
            "show_menu": False,
            "show_sidebar": False,
        }
    )
    
    # Display content based on selected tab
    if selected_tab == "Home":
        render_home_tab()
    elif selected_tab == "Test":
        render_test_tab()
    elif selected_tab == "About":
        render_about_tab()
    elif selected_tab == "Us":
        render_us_tab()
    
    # Add footer to all pages
    render_footer()

if __name__ == "__main__":
    main()
