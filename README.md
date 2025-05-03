## Restaurant Explorer

**README**

---

### Overview

Restaurant Explorer is an interactive Streamlit web application that helps users discover and explore restaurants. The app features a modern UI, custom background, and a conversational chatbot interface to assist users with restaurant recommendations and queries. It leverages a local restaurant dataset and provides a visually engaging experience with custom CSS and background imagery.
Deployed link of the project: https://zomatodatascrapper.streamlit.app/

---

### Features

- **Conversational Chatbot:** Ask questions about restaurants, get recommendations, and explore options using an AI-powered chatbot.
- **Custom Styling:** Enhanced UI with a custom CSS file for rounded input fields, styled buttons, and a polished sidebar.
- **Background Image:** Visually appealing background image for a premium look (auto-downloads if not present).
- **Session Management:** Uses Streamlit’s session state to maintain conversation history and chatbot state.
- **Easy Deployment:** All dependencies managed via `requirements.txt`.

---

### Project Structure

```
.
├── app.py                # Main Streamlit application
├── chatbot/
│   └── rag_chatbot.py    # Chatbot logic (RAG-based)
├── data/
│   └── restaurants.json  # Restaurant dataset
├── style.css             # Custom CSS for UI styling
├── background.jpg        # Background image (auto-downloaded if missing)
├── download_background.py# Script to fetch default background image
└── requirements.txt      # Python dependencies
```

---

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone 
   cd 
   ```

2. **Install Dependencies**
   Ensure you have Python 3.8+ installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```
   The main dependencies are:
   - streamlit
   - Pillow
   - requests
   - beautifulsoup4
   - scikit-learn[4]

3. **Prepare Assets**
   - If `background.jpg` is missing, it will be automatically downloaded via `download_background.py` or when you run the app[3].
   - Ensure `data/restaurants.json` exists with your restaurant data.

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

---

### Customization

- **Background Image:** Replace `background.jpg` with your preferred image for a different look.
- **CSS Styling:** Edit `style.css` to further customize input fields, buttons, sidebar, and chat bubbles[5].
- **Restaurant Data:** Update `data/restaurants.json` to reflect your dataset.

---

### File Descriptions

| File                  | Purpose                                                |
|-----------------------|--------------------------------------------------------|
| app.py                | Main Streamlit app, UI logic, and chatbot integration  |
| chatbot/rag_chatbot.py| Restaurant chatbot backend (retrieval-augmented)       |
| style.css             | Custom CSS for UI enhancements                         |
| background.jpg        | Background image for the app                           |
| download_background.py| Script to fetch background image if missing            |
| requirements.txt      | List of Python dependencies                            |

---

### Notes

- The app uses Streamlit session state to maintain chatbot state and conversation history.
- If the background image is missing, a warning is shown in the sidebar and the default Streamlit theme is used[1].
- For deployment on Streamlit Cloud or similar platforms, ensure all required files are present and listed in your repository root[7].

---



### Credits

- Built with [Streamlit][6].
- Background image sourced from Unsplash (see `download_background.py` for attribution)[3].

---

Enjoy exploring restaurants with Restaurant Explorer!





