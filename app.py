import streamlit as st
from story_logic import build_story, continue_story, generate_choices
from llm_engine import get_llm_response
from config import DEFAULT_GENRE, DEFAULT_STYLE

st.set_page_config(page_title="StoryCrafter", layout="wide")

if "story" not in st.session_state:
    st.session_state.story = []
if "choices" not in st.session_state:
    st.session_state.choices = []

st.title("📚 StoryCrafter: Co-Create a Story with AI")

with st.sidebar:
    st.header("🎨 Create Your Story")
    genre = st.selectbox("Choose a genre", ["Fantasy", "Mystery", "Sci-Fi", "Adventure", "Spooky"], index=DEFAULT_GENRE)
    main_character = st.text_input("Main character name", "Zara the Time Witch")
    twist = st.text_input("Story twist", "There’s a secret map hidden in the library")
    style = st.selectbox("Writing style", ["Whimsical", "Silly", "Spooky", "Epic"], index=DEFAULT_STYLE)

    if st.button("✨ Begin Story"):
        prompt = build_story(main_character, genre, twist, style)
        response = get_llm_response(prompt)
        st.session_state.story = [response]
        st.session_state.choices = generate_choices(response)

if st.session_state.story:
    for i, chunk in enumerate(st.session_state.story):
        st.markdown(f"### Scene {i + 1}")
        st.write(chunk)

    if st.session_state.choices:
        st.markdown("What should happen next?")
        for i, choice in enumerate(st.session_state.choices):
            if st.button(choice, key=i):
                prompt = continue_story(st.session_state.story, choice)
                response = get_llm_response(prompt)
                st.session_state.story.append(response)
                st.session_state.choices = generate_choices(response)
