import streamlit as st
import sys
import os

# Add backend folder to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.profile_analyzer import ProfileAnalyzer
from backend.conversation_generator import ConversationGenerator
st.set_page_config(page_title="Personalized Networking Assistant", layout="centered")

st.title("🤝 Personalized Networking Assistant")

st.write("Generate personalized networking introductions and conversation starters using AI.")

name = st.text_input("Your Name")
profession = st.text_input("Profession")
interests = st.text_area("Interests")
event = st.text_input("Event Name")
profile_analyzer = ProfileAnalyzer()
conversation_generator = ConversationGenerator()

if st.button("Generate"):
    try:
        profile = profile_analyzer.analyze_profile(name, interests, event)
        result = conversation_generator.generate_conversation(profile)

        st.subheader("Generated Networking Content")
        st.write(result)

    except Exception as e:
        st.error(f"Error: {e}")