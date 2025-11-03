import streamlit as st
from pathlib import Path


def show_splash_overlay(logo_path: Path | None = None):
    """
    Renders a simple loading message while data loads.
    """
    # Only show if it hasn't been shown or if data isn't loaded
    if st.session_state.get("splash_shown", False) and st.session_state.get(
        "data_loaded", False
    ):
        return

    st.session_state.splash_shown = True
    
    # Simple text-based loading message
    st.info("⏳ Loading data...")


def clear_splash():
    """Mark splash as complete - data is now loaded."""
    if "data_loaded" not in st.session_state:
        st.session_state.data_loaded = True
