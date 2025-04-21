import streamlit as st
from chatbot.rag_chatbot import RestaurantChatbot
from PIL import Image
import base64

# Custom CSS for styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Background image handling (updated)
def add_bg():
    try:
        with open("background.jpg", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url(data:image/jpg;base64,{encoded_string.decode()});
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                background-color: rgba(255, 255, 255, 0.9);
                background-blend-mode: lighten;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.markdown(
            """
            <style>
            .stApp {
                background-color: #f5f5f5;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.sidebar.warning("Background image not found. Using default theme.")

# Initialize chatbot
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = RestaurantChatbot('data/restaurants.json')
    st.session_state.history = []

# Apply custom styles
local_css("style.css")
add_bg()

# Main UI
st.title("🍽️ Restaurant Explorer")
st.markdown("""
    <div style='text-align: center; margin-bottom: 30px;'>
        <h3 style='color: #2E86AB;'>Ask me anything about restaurants, menus, and dietary options</h3>
    </div>
""", unsafe_allow_html=True)

# Sidebar for additional info
with st.sidebar:
    st.header("About")
    st.markdown("""
        This chatbot helps you find restaurant information including:
        - Menu items and prices
        - Dietary options (vegetarian, gluten-free, etc.)
        - Operating hours and locations
    """)
    
    st.header("Sample Questions")
    st.markdown("""
        - "Which restaurants have vegetarian thali options?"
        - "Show me restaurants with mild spice dishes"
        - "What's the best butter chicken in town?"
        - "Where can I find authentic South Indian food?"
        - "Which places have good biryani under ₹500?"
    """)

# Chat container
chat_container = st.container()

# User input
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("Your question:", key="input", 
                              placeholder="Ask about restaurants, menus, dietary options...")
    submit_button = st.form_submit_button(label='Send')

# Handle user input
if submit_button and user_input:
    with st.spinner("Finding restaurant information..."):
        response = st.session_state.chatbot.generate_response(user_input)
    
    # Add to history
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

# Display conversation history
with chat_container:
    for speaker, text in st.session_state.history:
        if speaker == "You":
            st.markdown(f"""
                <div style='background-color: #E3F2FD; 
                            padding: 10px; 
                            border-radius: 10px; 
                            margin: 5px 0; 
                            text-align: right;'>
                    <strong>You:</strong> {text}
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div style='background-color: #F5F5F5; 
                            padding: 10px; 
                            border-radius: 10px; 
                            margin: 5px 0;'>
                    <strong>🤖 Bot:</strong> {text}
                </div>
            """, unsafe_allow_html=True) 