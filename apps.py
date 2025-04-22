import streamlit as st
import base64

# --- Page Configuration ---
st.set_page_config(page_title="Home - Gyaan Apps", layout="wide")

# --- Inject Custom CSS ---
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #FFFFFF 0%, #F9FAFB 100%);
        height: 100vh;
        min-height: 100vh;
        display: block;
        margin: 0; /* Ensure no default body margin */
        padding: 0; /* Ensure no default body padding */
        padding-bottom: 0 !important; /* Force no bottom padding */
    }

    # Main Streamlit container
    [data-testid="stAppViewContainer"] > .main {
        min-height: 0 !important;
        height: auto !important;
        flex: unset !important;
        display: block !important;
        padding-bottom: 0 !important; /* Force no bottom padding */
        margin-bottom: 0 !important; /* Force no bottom margin */
    }

    /* Remove top padding from main block container */
    .block-container {
        padding-top: 0 !important;
    }

    .announcement {
        background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%);
        color: #166534;
        padding: 15px 20px;
        border-radius: 12px;
        border: 2px solid #16A34A;
        box-shadow: 0 4px 15px rgba(22, 163, 74, 0.15);
        animation: slideDown 0.5s ease-out, pulse 2s ease-in-out infinite;
        position: relative;
        overflow: hidden;
        font-weight: 500;
        font-size: 1.1em;
        margin-bottom: 25px;
    }

    .stCard {
        background: white;
        border-radius: 15px;
        box-shadow: 0 6px 10px rgba(17, 24, 39, 0.08);
        text-align: center;
        overflow: hidden;
        border: 1px solid #E5E7EB;
        transition: all 0.3s ease;
        height: 100%;
        display: block;
        cursor: pointer;
        text-decoration: none;
        color: inherit;
        margin-bottom: 20px;
    }

    .stCard:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 20px rgba(17, 24, 39, 0.12);
        border-color: #6B7280;
    }

    .card-title {
        font-size: 1.25em;
        font-weight: 600;
        background: #4B5563;
        color: white;
        padding: 15px;
        margin: 0;
        text-align: center;
    }

    .card-image {
        width: 100%;
        padding: 15px;
        background: #F9FAFB;
        height: 200px;
        object-fit: contain;
        max-width: 100%;
        max-height: 100%;
        display: block;
        margin: 0 auto;
    }

    .footer {
        text-align: center;
        font-size: 14px;
        padding: 10px;
        margin-top: 0;
        border-top: 1px solid #E5E7EB;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
        position: fixed !important;
        left: 0 !important;
        bottom: 0 !important;
        width: 100% !important;
        background: #fff !important;
        z-index: 9999 !important;
        margin-bottom: 0 !important; /* Ensure footer itself has no bottom margin */
    }

    .footer img {
        height: 35px;
        object-fit: contain;
    }

    .footer-text {
        font-weight: bold;
        color: #222; /* Ensure text is visible on white background */
        font-size: 1.1em; /* Slightly larger for clarity */
    }

    @keyframes slideDown {
        from {
            transform: translateY(-20px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }

    @keyframes pulse {
        0% { box-shadow: 0 4px 15px rgba(22, 163, 74, 0.15); }
        50% { box-shadow: 0 4px 20px rgba(22, 163, 74, 0.25); }
        100% { box-shadow: 0 4px 15px rgba(22, 163, 74, 0.15); }
    }

    /* Hide Streamlit header */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewContainer"] > .main {
        height: 100vh !important;
        min-height: 100vh !important;
        padding-bottom: 0 !important;
        margin-bottom: 0 !important;
        box-sizing: border-box;
    }
    .footer {
        margin-bottom: 0 !important;
        padding-bottom: 0 !important;
        position: fixed !important;
        left: 0 !important;
        bottom: 0 !important;
        width: 100% !important;
        background: #fff !important;
        z-index: 9999 !important;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# --- Announcement ---
st.markdown('<div class="announcement">🔔 Latest updates and announcements will appear here</div>', unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 style='text-align: center;'>Gyaan Apps</h1>", unsafe_allow_html=True)

# --- App Cards ---
cards = [
    {"name": "Coder", "img": "artifacts/1.jpg", "link": "#"},
    {"name": "Document", "img": "artifacts/2.jpg", "link": "#"},
    {"name": "Meeting", "img": "artifacts/3.jpg", "link": "#"},
    {"name": "Admin", "img": "artifacts/4.jpg", "link": "admin-login.html"},
    {"name": "X-ray", "img": "artifacts/5.jpg", "link": "#"},
]

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Create columns for cards - using Streamlit's column system instead of HTML grid
cols = st.columns(3)  # Adjust the number based on how many cards you want per row

# Render Cards as clickable elements
for i, card in enumerate(cards):
    with cols[i % 3]:  # This distributes cards across columns
        img_base64 = get_base64_image(card['img'])
        card_html = f'''
        <a href="{card['link']}" class="stCard" target="_self">
            <img src="data:image/jpeg;base64,{img_base64}" class="card-image">
            <p class="card-title">{card["name"]}</p>
        </a>
        '''
        st.markdown(card_html, unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<div class="footer">
    <div class="footer-text">🚀 Built by Team GYAAN</div>
</div>
""", unsafe_allow_html=True)
