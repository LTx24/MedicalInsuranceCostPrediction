import streamlit as st
import os
import sys
import traceback
pip install joblib
# Add error handling for imports


@st.cache_resource
def load_model():
    """Load the trained model with error handling"""
    try:
        model_path = "model_joblib_gr"
        if not os.path.exists(model_path):
            st.error(f"Model file not found at: {model_path}")
            st.info("Please ensure the model file is uploaded to the repository")
            return None
        return joblib.load(model_path)
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        st.info("Check logs for more details")
        return None

def create_page_header():
    """Create the page header with styling"""
    st.markdown(
        """
        <div style="background-color:lightblue;padding:16px">
            <h2 style="color:black;text-align:center">Medical Insurance Cost Prediction using ML</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

def get_user_input():
    """Collect user inputs through Streamlit widgets"""
    age = st.slider('Enter Your Age', 18, 100)
    sex = st.selectbox('Sex', ('Male', 'Female'))
    sex_encoded = 1 if sex == 'Male' else 0
    
    bmi = st.number_input('Enter Your BMI Value')
    children = st.slider("Enter Number Of Children", 0, 4)
    
    smoker = st.selectbox("Smoker", ('Yes', 'No'))
    smoker_encoded = 1 if smoker == 'Yes' else 0
    
    region = st.slider("Enter Your Region", 1, 4)
    
    return [age, sex_encoded, bmi, children, smoker_encoded, region]

def main():
    try:
        # Set page config
        st.set_page_config(
            page_title="Insurance Cost Predictor",
            page_icon="💰",
            layout="centered"
        )
        
        # Create header
        create_page_header()
        
        # Debug information
        st.sidebar.write("Debug Information:")
        st.sidebar.write(f"Python Version: {sys.version}")
        st.sidebar.write(f"Working Directory: {os.getcwd()}")
        st.sidebar.write(f"Directory Contents: {os.listdir()}")
        
        # Load model
        model = load_model()
        if model is None:
            st.stop()
        
        # Get user input
        user_input = get_user_input()
        
        # Make prediction
        if st.button('Predict'):
            try:
                prediction = model.predict([user_input])
                st.success(f'Your Insurance Cost is ${round(prediction[0], 2):,.2f}')
            except Exception as e:
                st.error(f"Prediction error: {str(e)}")
                st.info("Please check if all input values are valid")
                
    except Exception as e:
        st.error("An unexpected error occurred")
        st.code(traceback.format_exc())

if __name__ == "__main__":
    main()
