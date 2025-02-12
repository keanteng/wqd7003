import streamlit as st
from backend.utils import *
import pandas as pd
from datetime import datetime, timedelta
import time
import joblib
import google.generativeai as genai
import matplotlib.pyplot as plt

# page layout
st.set_page_config(page_title="Telco Churn Engine", page_icon="🧊", layout="wide")

# title
st.title("Telco Churn Engine")
st.write("Speed up predicting customer churn in the telecommunications industry. Powered by Generative AI and Job Schedule Function.") 

# sidebar
with st.sidebar:
    with st.expander("⏰ Schedule Run (Demo)", expanded=False):
        st.caption("Schedule a run for the app.")
        run_date = st.date_input("Select Date")
        run_time = st.time_input("Select Time")
        countdown_placeholder = st.empty()
        if st.button("Schedule Run", type='secondary'):
            run_datetime = datetime.combine(run_date, run_time)
            # scheduler.add_job(scheduled_task, 'date', run_date=run_datetime)
            st.success(f"App scheduled to run on {run_datetime}.")
            
            # Countdown logic
            while True:
                now = datetime.now()
                time_left = run_datetime - now
                if time_left.total_seconds() <= 0:
                    countdown_placeholder.write("Scheduled task is running!")
                    break
                countdown_placeholder.write(f"Time left: {time_left}")
                time.sleep(1)
    
    with st.expander("⚙️ Generative AI", expanded=True):
        st.caption("API token can be obtained at https://aistudio.google.com/.")
        gemini_api = st.text_input("Gemini Token", "", type='password')
        if authenticate_gemini(gemini_api):
            st.success("Gemini API token is valid.")
        else:
            st.error("Gemini API token is invalid.")
            
    with st.expander("🗳️ Sample Data Download", expanded=False):
        st.caption("Download sample data for testing.")
        sample_data = load_data("data/sample_data.csv")
        st.download_button("Download Sample Data", sample_data.to_csv(), "sample_data.csv", "text/csv")
            
    st.divider()
    
    st.caption("MIT License 2025 © Khor Kean Teng, Loong Shih-Wai, Tioh Zi Cong, Yee See Marn")
    

# main content
with st.chat_message("assistant", avatar="https://static.vecteezy.com/system/resources/previews/035/010/451/non_2x/bionic-zombie-infusion-design-zombie-cyborg-evolution-icon-vector.jpg"):
    response = st.write("Hello admin! I am Arnold. How can I automate so that you might lost your job?")
    st.caption("If you use predefined data, the file upload step will be hidden.")
    toggle = st.toggle('Use Predefined Data', True)
    data = load_data("data/sample_data.csv")
    
    if toggle == False:
        uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
    
    submit = st.button("Execute", type='primary')

    if submit:
        # show preview in table in expander
        with st.status("Preview Data", expanded=True):
            st.write(data.head())

        model = joblib.load("model/model.pkl")
        prediction = model.predict(data)
        data["Churn Prediction"] = prediction
        
        # count how many churn
        churn_count = data["Churn Prediction"].value_counts()
        
        # show prview in table in expander
        with st.status("Prediction", expanded=True):
            st.write("The prediction is done. There are {} churn customers out of the total {} customers.".format(churn_count[1], len(data)))
            st.write(data.head())
        
        # plot a pie chart
        with st.status("Churn Pie Chart", expanded=True):
            st.write("The pie chart shows the distribution of churn customers.")
            fig, ax = plt.subplots()
            # resize the pie chart
            fig.set_size_inches(3, 3)
            ax.pie(churn_count, labels=["Churn", "Non-Churn"], autopct='%1.1f%%', startangle=90)
            st.pyplot(fig)
        
        with st.status("AI Opinion", expanded=True):
            try:
                ai_model = genai.GenerativeModel("gemini-1.5-flash")
                response = ai_model.generate_content(f"Give some opinions in about 100 word based on the prediction results where there are {churn_count[1]} cases of attrition out of the total {len(data)} number of customers.")
                st.write(response.text)
            except Exception as e:
                st.write("You don't have access to this feature. Please authenticate to use this feature.")