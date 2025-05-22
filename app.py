import os
from dotenv import load_dotenv
import streamlit as st
import json
from profile_manager import *
from utils import *

st.set_page_config(page_title="Smart AI Agent", layout="wide")
st.title("🤖 Smart AI Agent Builder")

# Configure API
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if (gemini_api_key is None) or (gemini_api_key == ""):
    api_key = st.text_input("🔑 Enter your Google API Key", type="password")
    if api_key:
        configure_api(api_key)
else:
    configure_api(gemini_api_key)
# api_key = st.sidebar.text_input("🔑 Enter your Gemini API Key", type="password")
# if api_key:
#     configure_api(api_key)
# else:
#     st.warning("Please enter your Gemini API key.")
#     st.stop()

# Load templates
with st.sidebar.expander("📁 Load Template Profile"):
    template_name = st.selectbox("Choose a template", list_template_profiles())
    if st.button("Load Template"):
        st.session_state.current_profile = get_template_profile(template_name)
        st.session_state.profile_name = template_name

# Profile editor
with st.sidebar.expander("🛠️ Edit Current Profile"):
    current_profile = st.session_state.get("current_profile", None)
    if current_profile:
        for key in current_profile:
            if isinstance(current_profile[key], list):
                current_profile[key] = st.text_input(key, ", ".join(current_profile[key])).split(",")
            elif isinstance(current_profile[key], int):
                current_profile[key] = st.number_input(key, value=current_profile[key])
            else:
                current_profile[key] = st.text_input(key, value=current_profile[key])

        name_to_save = st.text_input("Save Profile As", st.session_state.get("profile_name", "CustomAgent"))
        if st.button("💾 Save Profile"):
            save_profile(name_to_save, current_profile)
            st.success(f"Profile '{name_to_save}' saved.")
            st.session_state.profile_name = name_to_save
    else:
        st.info("No profile loaded.")

# Tabs for all saved profiles
profiles = list_profiles()
tabs = st.tabs(profiles if profiles else ["General Assistant"])

for i, name in enumerate(profiles if profiles else ["General Assistant"]):
    with tabs[i]:
        profile = load_profile(name) if name in profiles else None

        # Memory per profile
        if f"chat_{name}" not in st.session_state:
            st.session_state[f"chat_{name}"] = []

        st.subheader(f"💬 Chat with: {name}")

        user_input = st.text_input(f"Type your prompt to {name}:", key=f"input_{name}")
        if st.button("Send", key=f"send_{name}") and user_input:
            response = ask_gemini(user_input, profile)
            if response == "EXIT_SIGNAL":
                st.warning("🔚 User wants to exit.")
            else:
                st.session_state[f"chat_{name}"].append({
                    "input": user_input,
                    "response": response,
                    "profile": name,
                    "feedback": None
                })

        # Show chat
        st.markdown("### 🕘 Chat History")
        for idx, chat in enumerate(st.session_state[f"chat_{name}"]):
            st.markdown(f"**You:** {chat['input']}")
            st.markdown(f"**{name}:** {chat['response']}")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("👍", key=f"up_{name}_{idx}"):
                    chat["feedback"] = "👍"
            with col2:
                if st.button("👎", key=f"down_{name}_{idx}"):
                    chat["feedback"] = "👎"

        # Download
        st.download_button(
            label="📤 Export Chat",
            data=json.dumps(st.session_state[f"chat_{name}"], indent=2),
            file_name=f"{name}_chat_history.json",
            mime="application/json"
        )

        # Reset
        if st.button("🧹 Clear Chat", key=f"clear_{name}"):
            st.session_state[f"chat_{name}"] = []
