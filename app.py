import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📩 Spam Mail Detector")

user_input = st.text_area("Enter your email message:")

if st.button("Check"):
    input_data = vectorizer.transform([user_input])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Ham Mail")
    else:
        st.error("🚨 Spam Mail")