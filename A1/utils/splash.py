import streamlit as st
from pathlib import Path
import base64


def show_splash_overlay(logo_path: Path | None = None):
    """
    Renders a modern overlay splash screen that waits for data to load.
    Removal is triggered by calling `clear_splash()` from the main app.
    """
    # Only show if it hasn't been shown or if data isn't loaded
    if st.session_state.get("splash_shown", False) and st.session_state.get(
        "data_loaded", False
    ):
        return

    st.session_state.splash_shown = True

    logo_html = ""
    if logo_path and logo_path.exists():
        logo_b64 = base64.b64encode(logo_path.read_bytes()).decode()
        logo_html = f"""
        <img src='data:image/png;base64,{logo_b64}' 
             alt='CarbonSeer Logo'
             class='splash-logo'>
        """
    else:
        logo_html = "<div class='splash-logo-text'>CarbonSeer</div>"

    splash_html = f"""
    <style>
    @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @keyframes fadeOut {{ from {{ opacity: 1; }} to {{ opacity: 0; }} }}
    @keyframes scaleIn {{
        from {{ opacity: 0; transform: scale(0.9); }}
        to {{ opacity: 1; transform: scale(1); }}
    }}
    @keyframes spin {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
    }}
    .splash-overlay {{
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background: linear-gradient(135deg, 
            rgba(251, 168, 52, 0.97) 0%,
            rgba(252, 194, 102, 0.95) 50%,
            rgba(233, 118, 43, 0.97) 100%);
        backdrop-filter: blur(20px);
        z-index: 999999;
        display: flex; justify-content: center; align-items: center; flex-direction: column;
        animation: fadeIn 0.4s ease-out;
    }}
    .splash-overlay.fade-out {{
        animation: fadeOut 0.4s ease-out forwards;
    }}
    .splash-content {{
        text-align: center;
        animation: scaleIn 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .splash-logo {{
        max-width: 400px; width: 80vw; height: auto; margin-bottom: 2rem;
        filter: drop-shadow(0 8px 24px rgba(0, 0, 0, 0.15));
    }}
    .splash-logo-text {{
        font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
        font-size: clamp(3rem, 8vw, 5rem); font-weight: 800; color: white;
        margin-bottom: 2rem; text-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        letter-spacing: -0.02em;
    }}
    .spinner {{
        width: 56px; height: 56px;
        border: 5px solid rgba(255, 255, 255, 0.25);
        border-top-color: white;
        border-radius: 50%;
        animation: spin 1s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite;
        margin: 0 auto;
    }}
    .splash-message {{
        font-family: 'Inter', sans-serif; font-size: 1.25rem;
        color: rgba(255, 255, 255, 0.95); margin-top: 1.5rem;
        font-weight: 500; letter-spacing: 0.02em;
    }}
    </style>
    
    <div class='splash-overlay' id='splashOverlay'>
        <div class='splash-content'>
            {logo_html}
            <div class='spinner-container'>
                <div class='spinner'></div>
            </div>
            <div class='splash-message'>Loading Carbon Analytics...</div>
        </div>
    </div>
    
    <script>
    function removeSplash() {{
        var splash = document.getElementById('splashOverlay');
        if (splash) {{
            splash.classList.add('fade-out');
            setTimeout(function() {{
                if (splash.parentNode) {{
                    splash.parentNode.removeChild(splash);
                }}
            }}, 400);
        }}
    }}
    // This function will be called by Streamlit when data is ready
    window.clearSplash = removeSplash;
    </script>
    """
    st.markdown(splash_html, unsafe_allow_html=True)


def clear_splash():
    """Injects JavaScript to remove the splash screen."""
    st.markdown(
        """
        <script>
            if (window.clearSplash) {
                window.clearSplash();
            }
        </script>
    """,
        unsafe_allow_html=True,
    )
