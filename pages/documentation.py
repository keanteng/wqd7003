import streamlit as st

st.set_page_config(page_title='Documentation', layout='wide')

with st.sidebar:
    with st.expander("⚠️ Disclaimer", expanded=True):
        st.write("This web app is intended for prediction purposes only. The results are based on the input data provided and \
        the performance of the machine learning model. The accuracy of the predictions may vary depending on data quality \
        and model reliability.")
        
    st.caption("MIT License 2025 © Khor Kean Teng, Loong Shih-Wai, Tioh Zi Cong, Yee See Marn")

st.title("📄 Documentation")
st.markdown("""
            To learn more about the project, please refer to the sections below.
            """)
st.subheader("About Telco Churn")
st.write("""Customer churn is a critical issue in the telecommunications industry. \
    It refers to the percentage of customers who discontinue their services with a company within a given time period. 
    The churn rate is a key metric for businesses to measure customer satisfaction and loyalty.""")