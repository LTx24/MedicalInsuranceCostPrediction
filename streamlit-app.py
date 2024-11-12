import streamlit as st
import joblib
import os

def load_model():
    """Load the trained model"""
    return joblib.load("model_joblib_gr")

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
    # Set page config
    st.set_page_config(
        page_title="Insurance Cost Predictor",
        page_icon="💰",
        layout="centered"
    )
    
    # Create header
    create_page_header()
    
    try:
        # Load model
        model = load_model()
        
        # Get user input
        user_input = get_user_input()
        
        # Make prediction
        if st.button('Predict'):
            prediction = model.predict([user_input])
            st.success(f'Your Insurance Cost is ${round(prediction[0], 2):,.2f}')
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info("Please make sure the model file 'model_joblib_gr' is present in the same directory.")

if __name__ == "__main__":
    main()