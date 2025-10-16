import streamlit as st
from pathlib import Path
import time


def show_splash_overlay(logo_path: Path | None = None, duration: float = 2.0, wait_for_data: bool = False):
    """Render a modern overlay splash screen with spinner during app loading.

    Features:
    - Full-screen overlay with backdrop blur
    - Animated logo with fade-in
    - Modern spinner with brand colors
    - Can wait for data loading to complete before dismissing
    - Only shows once per session
    
    Args:
        logo_path: Path to CarbonSeer logo PNG
        duration: How long to show splash (seconds) - minimum display time
        wait_for_data: If True, keep splash visible until data_loaded is True in session state
    """
    # Check if splash has already been shown this session
    if "splash_shown" in st.session_state:
        return
    
    # Mark splash as shown immediately
    st.session_state.splash_shown = True
    
    # Initialize data loading state if waiting for data
    if wait_for_data and "data_loaded" not in st.session_state:
        st.session_state.data_loaded = False
    
    # Build logo HTML if path provided
    logo_html = ""
    if logo_path and logo_path.exists():
        # Use base64 encoding for embedded image
        import base64
        with open(logo_path, "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()
        logo_html = f"""
        <img src='data:image/png;base64,{logo_b64}' 
             alt='CarbonSeer Logo'
             class='splash-logo'>
        """
    else:
        # Fallback to text logo
        logo_html = """
        <div class='splash-logo-text'>CarbonSeer</div>
        """

    splash_html = f"""
    <style>
    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}
    
    @keyframes fadeOut {{
        from {{ opacity: 1; }}
        to {{ opacity: 0; }}
    }}
    
    @keyframes scaleIn {{
        from {{
            opacity: 0;
            transform: scale(0.9);
        }}
        to {{
            opacity: 1;
            transform: scale(1);
        }}
    }}
    
    @keyframes spin {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
    }}
    
    .splash-overlay {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: linear-gradient(135deg, 
            rgba(251, 168, 52, 0.97) 0%,
            rgba(252, 194, 102, 0.95) 50%,
            rgba(233, 118, 43, 0.97) 100%);
        backdrop-filter: blur(20px);
        z-index: 999999;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
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
        max-width: 400px;
        width: 80vw;
        height: auto;
        margin-bottom: 2rem;
        filter: drop-shadow(0 8px 24px rgba(0, 0, 0, 0.15));
    }}
    
    .splash-logo-text {{
        font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
        font-size: clamp(3rem, 8vw, 5rem);
        font-weight: 800;
        color: white;
        margin-bottom: 2rem;
        text-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        letter-spacing: -0.02em;
    }}
    
    .spinner-container {{
        margin-top: 2rem;
    }}
    
    .spinner {{
        width: 56px;
        height: 56px;
        border: 5px solid rgba(255, 255, 255, 0.25);
        border-top-color: white;
        border-radius: 50%;
        animation: spin 1s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite;
        margin: 0 auto;
    }}
    
    .splash-message {{
        font-family: 'Inter', sans-serif;
        font-size: 1.25rem;
        color: rgba(255, 255, 255, 0.95);
        margin-top: 1.5rem;
        font-weight: 500;
        letter-spacing: 0.02em;
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
                splash.remove();
            }}, 400);
        }}
    }}
    
    // For data-driven splash: keep showing until data is loaded
    window.splashRemovalTimer = null;
    
    // If wait_for_data is true, this will be called from Python when data is ready
    // Otherwise, timer will remove splash after minimum duration
    window.removeSplashAfterDelay = function(ms) {{
        if (window.splashRemovalTimer) clearTimeout(window.splashRemovalTimer);
        window.splashRemovalTimer = setTimeout(removeSplash, ms);
    }};
    
    window.removeSplashNow = function() {{
        removeSplash();
    }};
    
    // Set minimum display time
    window.removeSplashAfterDelay({int(duration * 1000)});
    </script>
    """
    
    # Render the splash overlay
    st.markdown(splash_html, unsafe_allow_html=True)
    
    # For data-driven splash: keep checking until data is loaded
    if wait_for_data:
        # Wait for data to load (will be marked by app.py)
        start_time = time.time()
        while not st.session_state.get("data_loaded", False):
            time.sleep(0.1)
            # Timeout after 30 seconds (safety)
            if time.time() - start_time > 30:
                break
        
        # Trigger splash removal via JavaScript
        st.markdown("""
        <script>
        if (window.removeSplashNow) {
            window.removeSplashNow();
        }
        </script>
        """, unsafe_allow_html=True)
    
    return


def clear_splash():
    """Mark splash as ready to be removed."""
    st.session_state.data_loaded = True
