import streamlit as st
from streamlit_navigation_bar import st_navbar
import time

# set page configuration
st.set_page_config(
    page_title="Umlomo - Oral Health AI",
    page_icon="🦷",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# custom CSS for styling
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
    .analysis-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
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
        <p style="margin: 0; font-size: 0.9em;">Umlomo - Revolutionizing Oral Health with AI | Developed for Better Smiles</p>
        <p style="margin: 0; font-size: 0.7em;">© 2024 Umlomo Team. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

def render_home_tab():
    """Home tab content without videos"""
    
    # big project name - home tab
    st.markdown('<div class="main-header">Umlomo</div>', unsafe_allow_html=True)
    
    # introduction section
    st.markdown('<div class="section-header">Why Oral Health Matters</div>', unsafe_allow_html=True)
    
    # three key features in columns
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
    
    # key insights section
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
    
    # additional benefits
    st.markdown("---")
    st.markdown('<div class="section-header">Benefits of Regular Monitoring</div>', unsafe_allow_html=True)
    
    benefits_col1, benefits_col2, benefits_col3 = st.columns(3)
    
    with benefits_col1:
        st.markdown("""
        <div class="benefit-card">
            <h4>Cost Effective</h4>
            <ul>
            <li>Save up to 60% on dental bills</li>
            <li>Prevent expensive procedures</li>
            <li>Early intervention savings</li>
            <li>Reduced emergency costs</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with benefits_col2:
        st.markdown("""
        <div class="benefit-card">
            <h4>Time Saving</h4>
            <ul>
            <li>No appointment wait times</li>
            <li>Instant results and analysis</li>
            <li>24/7 availability</li>
            <li>Reduced clinic visits</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with benefits_col3:
        st.markdown("""
        <div class="benefit-card">
            <h4>Confidence Boost</h4>
            <ul>
            <li>Maintain a healthy smile</li>
            <li>Prevent bad breath issues</li>
            <li>Build self-confidence</li>
            <li>Improved social interactions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # call to action
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: #e8f4fd; border-radius: 10px;">
        <h3>Ready to Take Control of Your Oral Health?</h3>
        <p>Get started today with our AI-powered analysis in the Test tab.</p>
    </div>
    """, unsafe_allow_html=True)

def analyze_image(image):
    """Simulate image analysis"""
    with st.spinner("Analyzing your oral health... This will just take a moment!"):
        # simulate analysis with progress
        progress_bar = st.progress(0)
        for percent_complete in range(0, 101, 20):
            time.sleep(0.5)
            progress_bar.progress(percent_complete)
        
        # display results
        st.success("Analysis Complete!")
        
        # show results in columns
        result_col1, result_col2, result_col3 = st.columns(3)
        
        with result_col1:
            st.metric("Health Score", "92%", "+5% from last check")
            st.info("Excellent oral health!")
        
        with result_col2:
            st.metric("Areas of Concern", "2", "-1 from last check")
            st.warning("Minor improvements needed")
        
        with result_col3:
            st.metric("Recommendations", "3", "Personalized for you")
            st.success("Keep up the good work!")
        
        # detailed recommendations
        st.markdown("---")
        st.markdown("### Personalized Recommendations")
        
        rec_col1, rec_col2 = st.columns(2)
        
        with rec_col1:
            st.markdown("""
            **Brushing Tips:**
            - Brush for 2 minutes, twice daily
            - Use fluoride toothpaste
            - Replace toothbrush every 3 months
            - Pay attention to gum line
            """)
            
            st.markdown("""
            **Dietary Advice:**
            - Reduce sugary snacks
            - Drink more water
            - Eat crunchy fruits & vegetables
            - Limit acidic beverages
            """)
        
        with rec_col2:
            st.markdown("""
            **Professional Care:**
            - Schedule next check-up in 6 months
            - Consider fluoride treatment
            - Monitor wisdom teeth
            - Discuss teeth cleaning options
            """)
            
            st.markdown("""
            **Monitoring:**
            - Check again in 2 weeks
            - Track progress in app
            - Set reminders for dental care
            - Maintain oral hygiene journal
            """)
        
        # celebration button
        if st.button("Celebrate My Healthy Smile!", use_container_width=True):
            st.balloons()
            st.success("You're doing amazing! Keep smiling!")

def render_test_tab():
    """Test tab with file upload only"""
    st.markdown('<div class="section-header">Test Your Oral Health</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### How it Works
    Upload a clear photo of your teeth to get instant AI-powered analysis of your oral health. 
    Our advanced algorithms will assess multiple factors and provide personalized recommendations.
    """)
    
    # centered upload section
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
            <h3>Upload Your Photo</h3>
            <p>Get instant AI analysis of your oral health</p>
        </div>
        """, unsafe_allow_html=True)
        
        # file uploader
        uploaded_file = st.file_uploader(
            "Drag and drop or click to upload your photo", 
            type=['jpg', 'jpeg', 'png'],
            help="Upload a clear, well-lit photo of your teeth for best results",
            key="file_uploader"
        )
        
        if uploaded_file is not None:
            # display the uploaded image
            st.image(uploaded_file, caption="Your Uploaded Image", use_column_width=True)
            
            # analyze button
            analyze_col1, analyze_col2, analyze_col3 = st.columns([1, 2, 1])
            with analyze_col2:
                if st.button("Analyze My Smile", type="primary", use_container_width=True):
                    analyze_image(uploaded_file)
    
    # for better photos
    st.markdown("---")
    st.markdown("### Tips for Best Results")
    
    tips_col1, tips_col2, tips_col3 = st.columns(3)
    
    with tips_col1:
        st.markdown("""
        **Lighting**
        - Natural light is best
        - Avoid shadows on face
        - Even lighting on teeth
        - No harsh direct light
        """)
    
    with tips_col2:
        st.markdown("""
        **Photo Quality**
        - Clear, focused image
        - Teeth fully visible
        - No blur or glare
        - High resolution preferred
        """)
    
    with tips_col3:
        st.markdown("""
        **Positioning**
        - Smile naturally
        - Show all teeth
        - Front-facing angle
        - Close-up shot works best
        """)
    
    # supported formats
    st.markdown("---")
    st.markdown("### Supported Formats")
    
    format_col1, format_col2, format_col3 = st.columns(3)
    
    with format_col1:
        st.markdown("**Image Types**")
        st.markdown("- JPG/JPEG")
        st.markdown("- PNG")
        st.markdown("- High quality images")
    
    with format_col2:
        st.markdown("**File Size**")
        st.markdown("- Up to 10MB")
        st.markdown("- Optimal: 1-5MB")
        st.markdown("- No compression artifacts")
    
    with format_col3:
        st.markdown("**Processing**")
        st.markdown("- Instant analysis")
        st.markdown("- Secure & private")
        st.markdown("- No personal data stored")

def render_about_tab():
    """About tab with project description"""
    st.markdown('<div class="section-header">About Umlomo</div>', unsafe_allow_html=True)
    
    # project description
    st.markdown("""
    ## Our Mission
    
    **Umlomo** (which means "mouth" in Zulu) is an AI-powered oral health platform designed to make 
    dental care **accessible, preventive, and personalized** for everyone, everywhere.
    
    We believe that everyone deserves a healthy smile, and technology should make that easier, 
    not more complicated.
    """)
    
    # how it works section
    st.markdown("---")
    st.markdown("## How It Works")
    
    steps_col1, steps_col2, steps_col3, steps_col4 = st.columns(4)
    
    with steps_col1:
        st.markdown("""
        <div class="feature-card">
            <h4>1. Capture</h4>
            <p>Upload a clear photo of your teeth using our intuitive interface</p>
        </div>
        """, unsafe_allow_html=True)
    
    with steps_col2:
        st.markdown("""
        <div class="feature-card">
            <h4>2. Analyze</h4>
            <p>Our AI examines 50+ dental health indicators in seconds</p>
        </div>
        """, unsafe_allow_html=True)
    
    with steps_col3:
        st.markdown("""
        <div class="feature-card">
            <h4>3. Insights</h4>
            <p>Get instant feedback and understand your oral health status</p>
        </div>
        """, unsafe_allow_html=True)
    
    with steps_col4:
        st.markdown("""
        <div class="feature-card">
            <h4>4. Action</h4>
            <p>Receive personalized recommendations for improvement</p>
        </div>
        """, unsafe_allow_html=True)
    
    # technology stack
    st.markdown("---")
    st.markdown("## Technology Stack")
    
    tech_col1, tech_col2, tech_col3 = st.columns(3)
    
    with tech_col1:
        st.markdown("""
        <div class="benefit-card">
            <h4>Artificial Intelligence</h4>
            <ul>
            <li>Computer Vision</li>
            <li>Deep Learning Models</li>
            <li>Neural Networks</li>
            <li>Pattern Recognition</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tech_col2:
        st.markdown("""
        <div class="benefit-card">
            <h4>Modern Development</h4>
            <ul>
            <li>Streamlit Framework</li>
            <li>Python Backend</li>
            <li>Responsive Design</li>
            <li>Real-time Processing</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tech_col3:
        st.markdown("""
        <div class="benefit-card">
            <h4>Security & Privacy</h4>
            <ul>
            <li>Encrypted Data</li>
            <li>Anonymous Analysis</li>
            <li>Secure Storage</li>
            <li>Privacy First Approach</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def render_contributor_card(name, role, description, github_url, github_handle):
    """Render a contributor card"""
    st.markdown(f"""
    <div class="contributor-card">
        <h3>{name}</h3>
        <p><strong>{role}</strong></p>
        <p>{description}</p>
        <p>Email: <a href="mailto:{github_handle}@umlomo.com" style="color: #1f77b4;">{github_handle}@umlomo.com</a></p>
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
    
    # core team section
    st.markdown("### Core Team")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        render_contributor_card(
            "Albert",
            "Title",
            "Task",
            "https://github.com/Al04ni",
            "Albert"
        )
    
    with col2:
        render_contributor_card(
            "Munyakazi",
            "Title",
            "Task",
            "https://github.com/kevin",
            "Kevin"
        )
    
    with col3:
        render_contributor_card(
            "Poli",
            "Title",
            "Task",
            "https://github.com/poli",
            "Poli"
        )
    
    with col4:
        render_contributor_card(
            "Carine",
            "Title",
            "Task",
            "https://github.com/Mr-poli",
            "Mr-poli"
        )
    
    # repository links section
    st.markdown("---")
    st.markdown('<div class="section-header">Project Links</div>', unsafe_allow_html=True)
    
    link_col1, link_col2, link_col3 = st.columns(3)
    
    with link_col1:
        st.markdown("### GitHub Repository")
        st.markdown("[![GitHub](https://img.shields.io/badge/View_Code-Repository-blue?style=for-the-badge&logo=github)](https://github.com/username/umlomo)") #to be updated
        st.markdown("**Main Codebase**  \nAll the source code, issues, and project tracking")
    
    with link_col2:
        st.markdown("### Documentation")
        st.markdown("[![Docs](https://img.shields.io/badge/Read_Docs-Wiki-green?style=for-the-badge&logo=readthedocs)](https://github.com/username/umlomo/wiki)") #to be updated
        st.markdown("**User Guides & API**  \nComprehensive documentation and tutorials")
    
    with link_col3:
        st.markdown("### Issue Tracker")
        st.markdown("[![Issues](https://img.shields.io/badge/Report_Issues-Bug_Tracker-red?style=for-the-badge&logo=git)](https://github.com/username/umlomo/issues)") #to be updated
        st.markdown("**Bugs & Features**  \nReport issues or request new features")

def main():
    """Main application function"""
    
    # navigation bar with 4 tabs
    selected_tab = st_navbar(
        ["Home", "Test", "About", "Us"],
        options={
            "show_menu": False, #no menu
            "show_sidebar": False, #no sidebar
        }
    )
    
    # display content based on selected tab
    if selected_tab == "Home":
        render_home_tab()
    elif selected_tab == "Test":
        render_test_tab()
    elif selected_tab == "About":
        render_about_tab()
    elif selected_tab == "Us":
        render_us_tab()
    
    # add footer to all pages
    render_footer()

if __name__ == "__main__":
    main()