"""
Custom styling and design utilities for CarbonSeer - Awwwards-quality microsite.
Combines quantitative rigor with exceptional visual design.
"""


def get_custom_css(mode: str = "light"):
    """
    Return award-winning CSS for CarbonSeer microsite.
    Features: Glassmorphism, smooth animations, advanced typography, micro-interactions.

    Args:
        mode: "light" (default) or "seer" for a dark, neon, mystic Seer theme.
    """
    base_css = """
    <style>
    /* Import premium fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    /* ===== ROOT VARIABLES ===== */
    :root {
        /* Color Palette - Modern & Professional */
        /* Orange Accent Colors */
        --color-primary: #FBA834;
        --color-primary-light: #FCC266;
        --color-primary-dark: #E9762B;
        
        /* Blue Color Family */
        --color-secondary: #387ADF;
        --color-secondary-light: #50C4ED;
        --color-secondary-dark: #333A73;
        
        /* Light Blue */
        --color-tertiary: #D4EBF8;
        
        /* Neutrals */
        --color-dark: #1A1A1A;
        --color-gray-900: #2C2C2C;
        --color-gray-700: #4A4A4A;
        --color-gray-500: #666666;
        --color-gray-300: #CCCCCC;
        --color-gray-100: #F5F5F5;
        --color-white: #FFFFFF;
        
        /* Fallback Background */
        --color-fallback-bg: #F1F0E9;
        
        /* Semantic Colors */
        --color-success: #66BB6A;
        --color-warning: #FFA726;
        --color-error: #EF5350;
        --color-info: #42A5F5;
        
        /* Typography */
        --font-display: 'Plus Jakarta Sans', 'Inter', sans-serif;
        --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        
        /* Spacing System */
        --space-xs: 0.25rem;
        --space-sm: 0.5rem;
        --space-md: 1rem;
        --space-lg: 1.5rem;
        --space-xl: 2rem;
        --space-2xl: 3rem;
        --space-3xl: 4rem;
        --space-4xl: 6rem;
        
        /* Border Radius */
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        --radius-xl: 24px;
        --radius-full: 9999px;
        
        /* Shadows */
        --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.04);
        --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.06);
        --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.08);
        --shadow-xl: 0 16px 48px rgba(0, 0, 0, 0.12);
        --shadow-2xl: 0 24px 64px rgba(0, 0, 0, 0.16);
        
        /* Transitions */
        --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
        --transition-base: 300ms cubic-bezier(0.4, 0, 0.2, 1);
        --transition-slow: 500ms cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    /* ===== GLOBAL RESET & BASE STYLES ===== */
    * {
        font-family: var(--font-body);
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }
    
    html {
        scroll-behavior: smooth;
    }
    
    body {
        overflow-x: hidden;
    }
    
    /* Main container with animated gradient background */
    .main {
        background: linear-gradient(135deg, #F1F0E9 0%, #D4EBF8 50%, #F1F0E9 100%);
        background-size: 200% 200%;
        animation: gradientShift 15s ease infinite;
        min-height: 100vh;
        position: relative;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* ===== MODERN NAVIGATION & NAVBAR ===== */
    .navbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: var(--space-md) var(--space-lg);
        background: linear-gradient(180deg,
            rgba(255, 255, 255, 0.98) 0%,
            rgba(245, 243, 240, 0.95) 100%);
        backdrop-filter: blur(20px);
        border-bottom: 2px solid rgba(139, 125, 155, 0.1);
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
    }
    
    .navbar-brand {
        display: flex;
        align-items: center;
        gap: var(--space-md);
        font-weight: 700;
        color: var(--color-primary);
        font-family: var(--font-display);
        font-size: 1.3rem;
        text-decoration: none;
        transition: all var(--transition-fast);
    }
    
    .navbar-brand:hover {
        transform: translateY(-2px);
        color: var(--color-primary-dark);
    }
    
    .navbar-nav {
        display: flex;
        align-items: center;
        gap: var(--space-lg);
        list-style: none;
        margin: 0;
        padding: 0;
    }
    
    .nav-item {
        position: relative;
    }
    
    .nav-link {
        color: var(--color-primary);
        text-decoration: none;
        font-weight: 500;
        padding: var(--space-sm) var(--space-md);
        border-radius: var(--radius-md);
        transition: all var(--transition-fast);
        display: inline-flex;
        align-items: center;
        gap: 6px;
        position: relative;
    }
    
    .nav-link::after {
        content: '';
        position: absolute;
        bottom: -2px;
        left: var(--space-md);
        right: var(--space-md);
        height: 2px;
        background: linear-gradient(90deg, var(--color-secondary), var(--color-primary));
        border-radius: 1px;
        transform: scaleX(0);
        transform-origin: left;
        transition: transform var(--transition-fast);
    }
    
    .nav-link:hover {
        background: linear-gradient(135deg, rgba(139, 125, 155, 0.1), rgba(107, 155, 145, 0.05));
        color: var(--color-primary-dark);
    }
    
    .nav-link:hover::after {
        transform: scaleX(1);
    }
    
    .nav-link.active {
        background: linear-gradient(135deg, rgba(139, 125, 155, 0.15), rgba(107, 155, 145, 0.08));
        color: var(--color-primary-dark);
    }
    
    .nav-link.active::after {
        transform: scaleX(1);
    }
    
    .nav-badge {
        display: inline-block;
        background: rgba(107, 155, 145, 0.1);
        color: var(--color-secondary);
        font-size: 0.75rem;
        font-weight: 700;
        padding: 2px 8px;
        border-radius: var(--radius-full);
        margin-left: 4px;
        letter-spacing: 0.5px;
    }
    
    /* Navigation breadcrumbs */
    .breadcrumb {
        display: flex;
        align-items: center;
        gap: var(--space-sm);
        font-size: 0.9rem;
        color: var(--color-gray-500);
        margin: var(--space-md) 0;
        padding: var(--space-md);
        background: rgba(245, 243, 240, 0.5);
        border-radius: var(--radius-md);
        border: 1px solid rgba(139, 125, 155, 0.1);
    }
    
    .breadcrumb-item {
        transition: all var(--transition-fast);
    }
    
    .breadcrumb-item.active {
        color: var(--color-primary);
        font-weight: 600;
    }
    
    .breadcrumb-separator {
        color: var(--color-gray-300);
        margin: 0 var(--space-xs);
    }
    
    /* Page header with navigation context */
    .page-header {
        padding: var(--space-2xl) var(--space-xl);
        background: linear-gradient(135deg,
            rgba(139, 125, 155, 0.08) 0%,
            rgba(107, 155, 145, 0.04) 100%);
        border-bottom: 2px solid rgba(139, 125, 155, 0.1);
        border-radius: var(--radius-lg) var(--radius-lg) 0 0;
        margin-bottom: var(--space-2xl);
        animation: fadeInDown 0.6s ease-out;
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .page-header h1 {
        margin: 0;
        font-family: var(--font-display);
        font-size: 2rem;
        font-weight: 800;
        color: var(--color-primary);
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .page-header p {
        margin: var(--space-md) 0 0 0;
        color: var(--color-gray-700);
        font-size: 1.05rem;
        line-height: 1.6;
    }
    
    /* ===== HERO SECTION - Awwwards Quality ===== */
    .hero-section {
        background: linear-gradient(135deg, 
            #FBA834 0%,
            #FCC266 50%,
            #E9762B 100%);
        padding: var(--space-4xl) var(--space-2xl);
        border-radius: var(--radius-xl);
        margin-bottom: var(--space-2xl);
        box-shadow: var(--shadow-2xl);
        color: var(--color-white);
        position: relative;
        overflow: hidden;
        animation: fadeInUp 0.8s ease-out;
    }
    
    /* Glassmorphism overlay */
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 120%;
        height: 120%;
        background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 70%);
        animation: float 20s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translate(0, 0) rotate(0deg); }
        50% { transform: translate(-30px, -30px) rotate(5deg); }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(40px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .hero-title {
        font-family: var(--font-display);
        font-size: clamp(2.5rem, 6vw, 4.5rem);
        font-weight: 800;
        margin-bottom: var(--space-lg);
        line-height: 1.1;
        letter-spacing: -0.02em;
        position: relative;
        z-index: 1;
        text-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
    }
    
    .hero-subtitle {
        font-size: clamp(1.1rem, 2vw, 1.5rem);
        font-weight: 400;
        opacity: 0.95;
        line-height: 1.6;
        max-width: 800px;
        margin: 0 auto;
        position: relative;
        z-index: 1;
    }
    
    /* Scroll indicator */
    .scroll-indicator {
        position: absolute;
        bottom: 2rem;
        left: 50%;
        transform: translateX(-50%);
        animation: bounce 2s infinite;
        cursor: pointer;
        z-index: 2;
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateX(-50%) translateY(0); }
        40% { transform: translateX(-50%) translateY(-10px); }
        60% { transform: translateX(-50%) translateY(-5px); }
    }
    
    /* ===== GLASSMORPHISM METRIC CARDS ===== */
    .metric-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        padding: var(--space-xl);
        border-radius: var(--radius-lg);
        box-shadow: var(--shadow-lg);
        border: 1px solid rgba(255, 255, 255, 0.3);
        transition: all var(--transition-base);
        position: relative;
        overflow: hidden;
        animation: fadeInUp 0.6s ease-out backwards;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--color-primary), var(--color-secondary));
        transform: scaleX(0);
        transform-origin: left;
        transition: transform var(--transition-slow);
    }
    
    .metric-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: var(--shadow-2xl);
        border-color: rgba(139, 125, 155, 0.4);
    }
    
    .metric-card:hover::before {
        transform: scaleX(1);
    }
    
    .metric-value {
        font-family: var(--font-display);
        font-size: clamp(2rem, 4vw, 3rem);
        font-weight: 800;
        background: linear-gradient(135deg, var(--color-primary), var(--color-secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: var(--space-sm) 0;
        line-height: 1.2;
    }
    
    .metric-label {
        font-size: 0.85rem;
        color: var(--color-gray-500);
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 600;
        margin-bottom: var(--space-xs);
    }
    
    .metric-delta {
        font-size: 0.9rem;
        margin-top: var(--space-sm);
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        padding: var(--space-xs) var(--space-sm);
        border-radius: var(--radius-sm);
        background: rgba(0, 0, 0, 0.03);
    }
    
    /* ===== SECTION HEADERS WITH DECORATIVE ELEMENTS ===== */
    .section-header {
        font-family: var(--font-display);
        font-size: clamp(1.8rem, 3vw, 2.5rem);
        font-weight: 700;
        color: var(--color-gray-900);
        margin: var(--space-3xl) 0 var(--space-xl) 0;
        padding-left: var(--space-lg);
        border-left: 5px solid var(--color-primary);
        position: relative;
        animation: slideInLeft 0.6s ease-out;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, var(--color-primary), transparent);
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-40px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .section-subheader {
        font-family: var(--font-display);
        font-size: clamp(1.3rem, 2vw, 1.8rem);
        font-weight: 600;
        color: var(--color-gray-700);
        margin: var(--space-xl) 0 var(--space-md) 0;
        letter-spacing: -0.01em;
    }
    
    /* ===== ENHANCED INFO BOXES WITH DEPTH ===== */
    .info-box {
        background: linear-gradient(135deg, rgba(245, 243, 240, 0.95) 0%, rgba(255, 255, 255, 0.98) 100%);
        backdrop-filter: blur(10px);
        border-left: 4px solid var(--color-primary);
        padding: var(--space-xl);
        border-radius: var(--radius-md);
        margin: var(--space-xl) 0;
        box-shadow: var(--shadow-md);
        transition: all var(--transition-base);
        position: relative;
        overflow: hidden;
    }
    
    .info-box::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 100px;
        height: 100px;
        background: radial-gradient(circle, rgba(139, 125, 155, 0.08) 0%, transparent 70%);
        border-radius: 50%;
        transform: translate(30%, -30%);
    }
    
    .info-box:hover {
        transform: translateX(4px);
        box-shadow: var(--shadow-lg);
    }
    
    .success-box {
        background: linear-gradient(135deg, rgba(232, 245, 233, 0.95) 0%, rgba(241, 248, 233, 0.98) 100%);
        border-left: 4px solid var(--color-success);
        padding: var(--space-xl);
        border-radius: var(--radius-md);
        margin: var(--space-xl) 0;
        box-shadow: var(--shadow-md);
        transition: all var(--transition-base);
    }
    
    .success-box:hover {
        transform: scale(1.01);
        box-shadow: var(--shadow-lg);
    }
    
    .warning-box {
        background: linear-gradient(135deg, rgba(255, 243, 224, 0.95) 0%, rgba(255, 236, 179, 0.98) 100%);
        border-left: 4px solid var(--color-warning);
        padding: var(--space-xl);
        border-radius: var(--radius-md);
        margin: var(--space-xl) 0;
        box-shadow: var(--shadow-md);
        transition: all var(--transition-base);
    }
    
    .warning-box:hover {
        transform: scale(1.01);
        box-shadow: var(--shadow-lg);
    }
    
    /* ===== INTERACTIVE INSIGHT CARDS ===== */
    .insight-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(250, 250, 250, 0.95) 100%);
        backdrop-filter: blur(10px);
        padding: var(--space-xl);
        border-radius: var(--radius-lg);
        margin: var(--space-lg) 0;
        box-shadow: var(--shadow-md);
        border-top: 3px solid var(--color-primary);
        transition: all var(--transition-base);
        position: relative;
        overflow: hidden;
        cursor: pointer;
    }
    
    .insight-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, rgba(139, 125, 155, 0.03), rgba(107, 155, 145, 0.03));
        opacity: 0;
        transition: opacity var(--transition-base);
        pointer-events: none;
    }
    
    .insight-card:hover {
        transform: translateY(-4px) scale(1.01);
        box-shadow: var(--shadow-xl);
    }
    
    .insight-card:hover::after {
        opacity: 1;
    }
    
    .insight-number {
        font-family: var(--font-display);
        font-size: clamp(1.8rem, 3vw, 2.5rem);
        font-weight: 800;
        background: linear-gradient(135deg, var(--color-primary), var(--color-secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-right: var(--space-sm);
        display: inline-block;
    }
    
    /* ===== CHART CONTAINERS WITH DEPTH ===== */
    .chart-container {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(15px);
        padding: var(--space-xl);
        border-radius: var(--radius-lg);
        box-shadow: var(--shadow-lg);
        margin: var(--space-xl) 0;
        border: 1px solid rgba(255, 255, 255, 0.5);
        transition: all var(--transition-base);
        animation: fadeIn 0.6s ease-out;
    }
    
    .chart-container:hover {
        box-shadow: var(--shadow-xl);
        transform: scale(1.005);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    /* ===== STREAMLIT COMPONENT OVERRIDES ===== */
    
    /* Enhanced Metrics */
    .stMetric {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        padding: var(--space-lg);
        border-radius: var(--radius-md);
        box-shadow: var(--shadow-md);
        border: 1px solid rgba(139, 125, 155, 0.1);
        transition: all var(--transition-base);
    }
    
    .stMetric:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-lg);
    }
    
    /* Premium Buttons */
    .stButton > button {
        background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-light) 100%);
        color: var(--color-white);
        border: none;
        border-radius: var(--radius-md);
        padding: var(--space-md) var(--space-xl);
        font-weight: 600;
        font-size: 1rem;
        letter-spacing: 0.01em;
        transition: all var(--transition-base);
        box-shadow: 0 4px 16px rgba(139, 125, 155, 0.3);
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left var(--transition-slow);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 24px rgba(139, 125, 155, 0.4);
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 2px 8px rgba(139, 125, 155, 0.3);
    }
    
    /* Enhanced Sliders */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, var(--color-primary), var(--color-secondary));
    }
    
    .stSlider [data-baseweb="slider-track"] {
        height: 6px;
        border-radius: var(--radius-full);
    }
    
    .stSlider [role="slider"] {
        box-shadow: var(--shadow-md);
        transition: all var(--transition-base);
    }
    
    .stSlider [role="slider"]:hover {
        box-shadow: var(--shadow-lg);
        transform: scale(1.1);
    }
    
    /* Selectbox Styling */
    .stSelectbox > div > div {
        border-radius: var(--radius-sm);
        border: 2px solid rgba(139, 125, 155, 0.2);
        transition: all var(--transition-base);
        background: rgba(255, 255, 255, 0.95);
    }
    
    .stSelectbox > div > div:hover {
        border-color: var(--color-primary);
        box-shadow: var(--shadow-sm);
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: var(--color-primary);
        box-shadow: 0 0 0 3px rgba(139, 125, 155, 0.1);
    }
    
    /* Text Input Enhancement */
    .stTextInput > div > div > input {
        border-radius: var(--radius-sm);
        border: 2px solid rgba(139, 125, 155, 0.2);
        transition: all var(--transition-base);
        padding: var(--space-md);
        background: rgba(255, 255, 255, 0.95);
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--color-primary);
        box-shadow: 0 0 0 3px rgba(139, 125, 155, 0.1);
        outline: none;
    }
    
    /* Data Table Styling */
    .dataframe {
        border-radius: var(--radius-md);
        overflow: hidden;
        box-shadow: var(--shadow-md);
        border: 1px solid rgba(0, 0, 0, 0.05);
    }
    
    .dataframe thead tr th {
        background: linear-gradient(135deg, var(--color-primary), var(--color-primary-light)) !important;
        color: var(--color-white) !important;
        font-weight: 600;
        padding: var(--space-md) !important;
        letter-spacing: 0.02em;
    }
    
    .dataframe tbody tr:nth-child(even) {
        background-color: rgba(245, 243, 240, 0.5);
    }
    
    .dataframe tbody tr:hover {
        background-color: rgba(139, 125, 155, 0.08);
        transition: background-color var(--transition-fast);
    }
    
    .dataframe tbody td {
        padding: var(--space-md) !important;
    }
    
    /* ===== TABS WITH SMOOTH ANIMATIONS ===== */
    .stTabs [data-baseweb="tab-list"] {
        gap: var(--space-lg);
        border-bottom: 2px solid rgba(0, 0, 0, 0.05);
        padding-bottom: 0;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: var(--radius-sm) var(--radius-sm) 0 0;
        padding: var(--space-md) var(--space-xl);
        font-weight: 600;
        font-size: 1rem;
        color: var(--color-gray-500);
        background: transparent;
        border: none;
        transition: all var(--transition-base);
        position: relative;
    }
    
    .stTabs [data-baseweb="tab"]::after {
        content: '';
        position: absolute;
        bottom: -2px;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--color-primary), var(--color-secondary));
        transform: scaleX(0);
        transition: transform var(--transition-base);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        color: var(--color-primary);
        background: rgba(139, 125, 155, 0.05);
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: var(--color-primary);
        font-weight: 700;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"]::after {
        transform: scaleX(1);
    }
    
    /* ===== EXPANDER STYLING ===== */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, rgba(245, 243, 240, 0.8), rgba(255, 255, 255, 0.9));
        backdrop-filter: blur(10px);
        border-radius: var(--radius-sm);
        font-weight: 600;
        padding: var(--space-md) var(--space-lg);
        transition: all var(--transition-base);
        border: 1px solid rgba(139, 125, 155, 0.1);
    }
    
    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, rgba(139, 125, 155, 0.1), rgba(168, 155, 179, 0.05));
        border-color: var(--color-primary);
        box-shadow: var(--shadow-sm);
    }
    
    .streamlit-expanderContent {
        border: 1px solid rgba(0, 0, 0, 0.05);
        border-top: none;
        border-radius: 0 0 var(--radius-sm) var(--radius-sm);
        padding: var(--space-lg);
        background: rgba(255, 255, 255, 0.5);
    }
    
    /* ===== SIDEBAR STYLING - AWARD-WINNING NAVIGATION ===== */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: linear-gradient(180deg, 
            rgba(255, 255, 255, 0.99) 0%,
            rgba(245, 243, 240, 0.97) 50%,
            rgba(240, 237, 232, 0.95) 100%);
        backdrop-filter: blur(20px);
        border-right: 2px solid rgba(139, 125, 155, 0.15);
        box-shadow: inset -1px 0 0 rgba(0, 0, 0, 0.02);
    }

    /* Sidebar text and markdown containers */
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        padding: var(--space-lg) 0;
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3 {
        color: var(--color-primary);
        font-family: var(--font-display);
        font-weight: 700;
        letter-spacing: -0.5px;
        margin: var(--space-lg) 0 var(--space-md) 0;
        transition: all var(--transition-fast);
    }

    /* Sidebar links and nav items */
    [data-testid="stSidebar"] a {
        color: var(--color-primary) !important;
        text-decoration: none !important;
        font-weight: 500;
        transition: all var(--transition-fast);
        position: relative;
    }

    [data-testid="stSidebar"] a:hover {
        color: var(--color-primary-dark) !important;
        padding-left: 8px;
    }

    /* Navigation link styling with active state */
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] a::before {
        content: '▸ ';
        color: var(--color-secondary);
        margin-right: 4px;
        transition: all var(--transition-fast);
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] a:hover::before {
        color: var(--color-primary);
        margin-right: 8px;
    }

    /* Sidebar section dividers */
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] hr {
        margin: var(--space-lg) 0;
        border: none;
        border-top: 2px solid rgba(139, 125, 155, 0.1);
    }

    /* Sidebar button styling */
    [data-testid="stSidebar"] .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, 
            rgba(139, 125, 155, 0.1) 0%,
            rgba(107, 155, 145, 0.05) 100%);
        border: 2px solid rgba(139, 125, 155, 0.2);
        border-radius: var(--radius-md);
        color: var(--color-primary);
        font-weight: 600;
        padding: var(--space-md) var(--space-lg);
        transition: all var(--transition-fast);
        font-family: var(--font-display);
    }

    [data-testid="stSidebar"] .stButton > button:hover {
        background: linear-gradient(135deg, 
            rgba(139, 125, 155, 0.15) 0%,
            rgba(107, 155, 145, 0.1) 100%);
        border-color: rgba(139, 125, 155, 0.3);
        box-shadow: 0 4px 16px rgba(139, 125, 155, 0.1);
    }

    /* Sidebar expandable sections */
    [data-testid="stSidebar"] .streamlit-expanderHeader {
        background: linear-gradient(135deg,
            rgba(139, 125, 155, 0.08) 0%,
            rgba(107, 155, 145, 0.04) 100%);
        border: 1px solid rgba(139, 125, 155, 0.1);
        border-radius: var(--radius-md);
        padding: var(--space-md) var(--space-lg);
        margin: var(--space-sm) 0;
        transition: all var(--transition-fast);
        font-weight: 600;
        color: var(--color-primary);
    }

    [data-testid="stSidebar"] .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg,
            rgba(139, 125, 155, 0.12) 0%,
            rgba(107, 155, 145, 0.08) 100%);
        box-shadow: 0 2px 8px rgba(139, 125, 155, 0.08);
    }

    [data-testid="stSidebar"] .streamlit-expanderContent {
        background: rgba(245, 243, 240, 0.7);
        border: 1px solid rgba(139, 125, 155, 0.08);
        border-top: none;
        border-radius: 0 0 var(--radius-md) var(--radius-md);
        padding: var(--space-lg);
    }
    
    /* ===== FOOTER STYLING - STICKY ===== */
    .sticky-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(180deg,
            rgba(255, 255, 255, 0.98) 0%,
            rgba(241, 240, 233, 0.95) 100%);
        backdrop-filter: blur(20px);
        border-top: 2px solid rgba(251, 168, 52, 0.15);
        padding: var(--space-lg) var(--space-xl);
        z-index: 50;
        box-shadow: 0 -4px 16px rgba(0, 0, 0, 0.06);
    }
    
    .footer-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1400px;
        margin: 0 auto;
        flex-wrap: wrap;
        gap: var(--space-lg);
    }
    
    .footer-brand {
        font-family: var(--font-display);
        font-weight: 700;
        font-size: 1rem;
        color: var(--color-primary);
        letter-spacing: 0.5px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .footer-copyright {
        font-size: 0.85rem;
        color: var(--color-gray-500);
        display: flex;
        align-items: center;
        gap: 4px;
    }
    
    .footer-divider {
        width: 1px;
        height: 20px;
        background: rgba(251, 168, 52, 0.2);
        display: inline-block;
        margin: 0 var(--space-sm);
    }
    
    .footer-link {
        color: var(--color-secondary);
        text-decoration: none;
        font-weight: 500;
        font-size: 0.9rem;
        transition: all var(--transition-fast);
        display: inline-flex;
        align-items: center;
        gap: 6px;
        border-radius: var(--radius-sm);
        padding: 4px 8px;
    }
    
    .footer-link:hover {
        color: var(--color-secondary-dark);
        background: rgba(56, 122, 223, 0.08);
    }
    
    .dashboard-footer {
        text-align: center;
        padding: var(--space-2xl);
        padding-bottom: 120px;
        color: var(--color-gray-500);
        font-size: 0.9rem;
        margin-top: var(--space-4xl);
        border-top: 2px solid rgba(0, 0, 0, 0.05);
        background: linear-gradient(180deg, transparent, rgba(245, 243, 240, 0.5));
    }
    
    .dashboard-footer a {
        color: var(--color-primary);
        text-decoration: none;
        font-weight: 600;
        transition: all var(--transition-fast);
    }
    
    .dashboard-footer a:hover {
        color: var(--color-primary-dark);
        text-decoration: underline;
    }
    
    /* ===== UTILITY ANIMATIONS ===== */
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    @keyframes shimmer {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }
    
    .loading-shimmer {
        animation: shimmer 2s infinite linear;
        background: linear-gradient(
            90deg,
            rgba(255, 255, 255, 0) 0%,
            rgba(255, 255, 255, 0.6) 50%,
            rgba(255, 255, 255, 0) 100%
        );
        background-size: 1000px 100%;
    }
    
    /* ===== RESPONSIVE DESIGN ===== */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2rem;
        }
        
        .hero-subtitle {
            font-size: 1rem;
        }
        
        .section-header {
            font-size: 1.5rem;
            margin: var(--space-xl) 0 var(--space-md) 0;
        }
        
        .metric-card {
            padding: var(--space-md);
        }
        
        .metric-value {
            font-size: 1.8rem;
        }
        
        .chart-container {
            padding: var(--space-md);
        }
    }
    
    /* ===== HIDE STREAMLIT BRANDING ===== */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* ===== REDUCE BLANK SPACE ===== */
    /* Reduce padding in main container */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 1rem !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
    }
    
    /* Reduce spacing around horizontal rules */
    hr {
        margin-top: 1rem !important;
        margin-bottom: 1rem !important;
    }
    
    /* Reduce spacing around sections */
    .stMarkdown {
        margin-bottom: 0.5rem !important;
    }
    
    /* Reduce spacing between elements */
    .element-container {
        margin-bottom: 0.5rem !important;
    }
    
    /* Compact tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
    }
    
    /* Reduce dataframe spacing */
    .stDataFrame {
        margin-top: 0.5rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Compact expanders */
    .streamlit-expanderHeader {
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
    }
    
    /* Reduce chart spacing */
    .js-plotly-plot {
        margin-top: 0.5rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* ===== SCROLL PROGRESS INDICATOR ===== */
    .scroll-progress {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--color-primary), var(--color-secondary));
        transform-origin: left;
        z-index: 9999;
        box-shadow: 0 2px 8px rgba(139, 125, 155, 0.4);
    }
    
    /* ===== PERFORMANCE OPTIMIZATIONS ===== */
    * {
        will-change: auto;
    }
    
    .metric-card, .insight-card, .chart-container {
        will-change: transform;
    }
    
    /* ===== ACCESSIBILITY IMPROVEMENTS ===== */
    :focus-visible {
        outline: 3px solid var(--color-primary);
        outline-offset: 2px;
    }
    
    .sr-only {
        position: absolute;
        width: 1px;
        height: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        white-space: nowrap;
        border-width: 0;
    }
    
    </style>
    """

    return base_css


def get_plotly_theme():
    """
    Return award-winning Plotly theme configuration matching the design system.
    Features modern colors, smooth animations, and professional typography.
    """
    return {
        "layout": {
            "paper_bgcolor": "rgba(255, 255, 255, 0.95)",
            "plot_bgcolor": "rgba(245, 243, 240, 0.5)",
            "font": {
                "family": "Inter, -apple-system, BlinkMacSystemFont, sans-serif",
                "size": 13,
                "color": "#2C2C2C",
            },
            "colorway": [
                "#8B7D9B",  # Primary Purple
                "#6B9B91",  # Secondary Teal
                "#C9A9A6",  # Accent Dusty Rose
                "#A68B7D",  # Earth Brown
                "#D4C5B9",  # Warm Beige
                "#98887D",  # Taupe
                "#8BA8A3",  # Sage Green
                "#B8A5C4",  # Light Purple
            ],
            "title": {
                "font": {
                    "size": 24,
                    "family": "Plus Jakarta Sans, Inter, sans-serif",
                    "color": "#2C2C2C",
                    "weight": 700,
                },
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {
                "gridcolor": "rgba(0, 0, 0, 0.05)",
                "linecolor": "#CCCCCC",
                "zerolinecolor": "rgba(0, 0, 0, 0.1)",
                "tickfont": {"size": 12},
                "title": {"font": {"size": 14, "weight": 600}},
            },
            "yaxis": {
                "gridcolor": "rgba(0, 0, 0, 0.05)",
                "linecolor": "#CCCCCC",
                "zerolinecolor": "rgba(0, 0, 0, 0.1)",
                "tickfont": {"size": 12},
                "title": {"font": {"size": 14, "weight": 600}},
            },
            "hoverlabel": {
                "bgcolor": "rgba(255, 255, 255, 0.98)",
                "font": {"family": "Inter, sans-serif", "size": 13},
                "bordercolor": "#8B7D9B",
                "align": "left",
            },
            "legend": {
                "bgcolor": "rgba(255, 255, 255, 0.95)",
                "bordercolor": "rgba(139, 125, 155, 0.2)",
                "borderwidth": 1,
                "font": {"size": 12},
                "orientation": "v",
                "yanchor": "top",
                "y": 1,
                "xanchor": "right",
                "x": 1,
            },
            "margin": {"l": 80, "r": 80, "t": 100, "b": 80},
            "autosize": True,
            "hovermode": "closest",
            "showlegend": True,
        },
        "data": {
            "scatter": [
                {"marker": {"line": {"width": 0.5, "color": "white"}, "opacity": 0.8}}
            ],
            "bar": [{"marker": {"line": {"width": 0}, "opacity": 0.9}}],
            "box": [{"marker": {"opacity": 0.7}, "line": {"width": 2}}],
        },
    }


def create_metric_card_html(value, label, delta=None, delta_color="normal"):
    """
    Create a custom HTML metric card.
    """
    delta_html = ""
    if delta:
        color_map = {"normal": "#666", "positive": "#66BB6A", "negative": "#EF5350"}
        color = color_map.get(delta_color, "#666")
        delta_html = f'<div class="metric-delta" style="color: {color};">{delta}</div>'

    return f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        {delta_html}
    </div>
    """


def render_global_branding(
    hult_asset: str = "assets/Hult_logo.png", hult_width: int = 110
):
    """Render a small top-right Hult 'Developed at' lockup.

    This function is intentionally small and safe to call at the top of any page.
    It uses Streamlit layout primitives so it renders consistently across pages.
    """
    try:
        import streamlit as st
        from pathlib import Path

        # Use two columns so the branding sits on the right
        cols = st.columns([6, 1])
        with cols[1]:
            st.caption(
                "Developed at", help="Developed at Hult International Business School"
            )
            asset_path = Path(__file__).parent.parent / hult_asset
            if asset_path.exists():
                # use_container_width deprecated -> use width param
                st.image(str(asset_path), width=hult_width)
    except Exception:
        return


def render_page_lockup(
    lockup_asset: str = "assets/Carbonseer.png",
    facemark_asset: str = "assets/CarbonSeer_png.png",
    width: int = 240,
):
    """Render the CarbonSeer lockup (used on homepage splash and page headers).

    By default this centers the lockup for a neat header. Pages can call this where
    they want the CarbonSeer lockup to appear.
    """
    try:
        import streamlit as st
        from pathlib import Path

        # Center the lockup using columns
        col_left, col_center, col_right = st.columns([1, 2, 1])
        with col_center:
            asset_path = Path(__file__).parent.parent / lockup_asset
            if asset_path.exists():
                # use_container_width deprecated -> use width param
                st.image(str(asset_path), width=width)
    except Exception:
        return


def sanitize_df_for_display(df):
    """Return a copy of df with column types coerced to Arrow-friendly types.

    Strategy:
    - For object dtype columns: try to convert to numeric (int/float)
    - If numeric conversion fails, try to parse datetimes
    - If that fails, convert values to plain strings; if values are lists/dicts, JSON-serialize
    - Preserve NaNs and None

    This function intentionally does not modify the original DataFrame.
    """
    import pandas as pd
    import numpy as np
    import json

    df_copy = df.copy()

    for col in df_copy.columns:
        if pd.api.types.is_object_dtype(df_copy[col].dtype):
            series = df_copy[col]

            # 1) Try numeric - convert inf to NaN explicitly
            coerced_num = pd.to_numeric(series, errors="coerce")
            # Replace inf values with NaN as recommended by pandas
            coerced_num = coerced_num.replace([np.inf, -np.inf], np.nan)
            if (
                coerced_num.notna().sum() > 0
                and coerced_num.isna().sum() < series.notna().sum()
            ):
                # Use numeric where possible, keep original NAs
                df_copy[col] = coerced_num
                continue

            # 2) Try datetime
            coerced_dt = pd.to_datetime(series, errors="coerce", format="mixed")
            if (
                coerced_dt.notna().sum() > 0
                and coerced_dt.isna().sum() < series.notna().sum()
            ):
                df_copy[col] = coerced_dt
                continue

            # 3) Fallback: stringify, but ensure JSON for lists/dicts
            def _safe_serialize(x):
                if pd.isna(x):
                    return None
                if isinstance(x, (list, dict)):
                    try:
                        return json.dumps(x, ensure_ascii=False)
                    except Exception:
                        return str(x)
                try:
                    return str(x)
                except Exception:
                    return json.dumps(x, default=str, ensure_ascii=False)

            df_copy[col] = series.apply(_safe_serialize).astype(object)

    # For completeness, replace Python objects like numpy types with native Python types
    for col in df_copy.columns:
        if pd.api.types.is_integer_dtype(
            df_copy[col].dtype
        ) or pd.api.types.is_float_dtype(df_copy[col].dtype):
            # ensure numpy types cast to native
            df_copy[col] = df_copy[col].apply(
                lambda x: None
                if pd.isna(x)
                else (
                    int(x)
                    if pd.api.types.is_integer_dtype(df_copy[col].dtype)
                    else float(x)
                )
            )

    return df_copy


def render_navbar(current_page: str = "Home"):
    """
    Render a modern, award-winning navbar with navigation links and page indicator.

    Args:
        current_page: The name of the current page for active state highlighting

    Usage:
        render_navbar("Analysis")
    """
    import streamlit as st

    pages = {
        "🏠 Home": "Home",
        "📊 Analysis": "Analysis",
    }

    navbar_html = """
    <div class='navbar'>
        <div class='navbar-brand'>
            🌍 CarbonSeer
        </div>
        <nav class='navbar-nav'>
    """

    for display_name, page_name in pages.items():
        is_active = page_name == current_page
        active_class = "active" if is_active else ""
        navbar_html += f"""
            <li class='nav-item'>
                <a href='#' class='nav-link {active_class}' title='{page_name}'>
                    {display_name}
                </a>
            </li>
        """

    navbar_html += """
        </nav>
    </div>
    """

    st.markdown(navbar_html, unsafe_allow_html=True)


def render_page_header(
    page_title: str, page_emoji: str = "📊", page_description: str = ""
):
    """
    Render a beautiful page header with title, emoji, and optional description.

    Args:
        page_title: The title of the page
        page_emoji: An emoji to display before the title
        page_description: Optional description text below the title
    """
    import streamlit as st

    header_html = f"""
    <div class='page-header'>
        <h1>{page_emoji} {page_title}</h1>
    """

    if page_description:
        header_html += f"<p>{page_description}</p>"

    header_html += "</div>"

    st.html(header_html)


def render_breadcrumbs(breadcrumb_items: list):
    """
    Render a breadcrumb navigation trail.

    Args:
        breadcrumb_items: List of tuples (name, is_active)
                         Example: [("Home", False), ("Analysis", True)]
    """
    import streamlit as st

    breadcrumb_html = '<div class="breadcrumb">'

    for i, (item_name, is_active) in enumerate(breadcrumb_items):
        active_class = "active" if is_active else ""
        breadcrumb_html += (
            f'<span class="breadcrumb-item {active_class}">{item_name}</span>'
        )

        if i < len(breadcrumb_items) - 1:
            breadcrumb_html += '<span class="breadcrumb-separator">/</span>'

    breadcrumb_html += "</div>"

    st.markdown(breadcrumb_html, unsafe_allow_html=True)


def render_sticky_footer():
    """
    Render a professional, sticky footer with copyright, branding, and contact information.

    Features:
    - Fixed to bottom of viewport
    - Contains copyright symbol
    - CarbonSeer-Demo branding
    - Contact link to portfolio
    - Modern glassmorphism design
    """
    import streamlit as st

    # Helper: try to load the logo lockup and embed as base64; fall back to text if missing
    def _logo_data_url(asset_path: str = "assets/CarbonSeer_png.png") -> str:
        from pathlib import Path
        import base64

        p = Path(__file__).parent.parent / asset_path
        if not p.exists():
            return ""

        try:
            data = p.read_bytes()
            b64 = base64.b64encode(data).decode("utf-8")
            # infer mime type from suffix
            suffix = p.suffix.lower().lstrip(".")
            mime = f"image/{suffix if suffix != 'png' else 'png'}"
            return f"data:{mime};base64,{b64}"
        except Exception:
            return ""

    logo_url = _logo_data_url()
    if logo_url:
        logo_img = f"<img src='{logo_url}' alt='CarbonSeer logo' style='height:32px; vertical-align:middle; margin-right:8px;'/>"
        brand_html = f"<div class='footer-brand'>{logo_img}<span style='vertical-align:middle;'>CarbonSeer</span></div>"
    else:
        brand_html = "<div class='footer-brand'>CarbonSeer</div>"

    footer_html = f"""
    <div class='sticky-footer'>
        <div class='footer-content' style='align-items: center; display: flex; justify-content: space-between; flex-wrap: wrap;'>
            {brand_html}
            
            <div class='footer-copyright'>
                © 2025 <b>CarbonSeer</b>
                <span class='footer-divider'></span>
                Data-Driven Carbon Analytics for Businesses
                <span class='footer-divider'></span>
                Built by
                <a href='https://kartavya-jharwal.github.io' target='_blank' rel='noopener noreferrer' class='footer-link'>
                Kartavya Jharwal
            </a>
            </div>
        </div>
    </div>
    """

    st.html(footer_html)


def render_sidebar_resources():
    """Render sidebar with PDF viewer and notebook download links."""
    import streamlit as st
    from pathlib import Path
    import uuid

    # Generate truly unique keys with UUID for each button
    pdf_key = f"pdf_btn_{uuid.uuid4()}"
    notebook_key = f"nb_btn_{uuid.uuid4()}"

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📚 Resources")

    # Check if PDF exists
    pdf_path = Path(__file__).parent.parent / "assignment_report.pdf"
    notebook_path = Path(__file__).parent.parent / "CarbonSeer_Analysis.ipynb"

    if pdf_path.exists():
        st.sidebar.markdown("#### 📄 Analysis Report")

        # PDF viewer using streamlit-extras
        try:
            from streamlit_extras.pdf_viewer import pdf_viewer

            with st.sidebar.expander("📖 View Report", expanded=False):
                with open(pdf_path, "rb") as f:
                    pdf_bytes = f.read()
                pdf_viewer(pdf_bytes, height=400)
        except ImportError:
            st.sidebar.info("Install `streamlit-extras` to view PDF inline")

        # Download link
        with open(pdf_path, "rb") as f:
            st.sidebar.download_button(
                label="⬇️ Download PDF Report",
                data=f.read(),
                file_name="CarbonSeer_Analysis_Report.pdf",
                mime="application/pdf",
                width="stretch",
                key=pdf_key,
            )

    if notebook_path.exists():
        st.sidebar.markdown("#### 📓 Jupyter Notebook")

        # Download link for notebook
        with open(notebook_path, "rb") as f:
            st.sidebar.download_button(
                label="⬇️ Download Notebook (.ipynb)",
                data=f.read(),
                file_name="CarbonSeer_Analysis.ipynb",
                mime="application/x-ipynb+json",
                width="stretch",
                key=notebook_key,
            )

        # Optional: Link to nbviewer
        st.sidebar.markdown(
            "[🔗 View on GitHub](https://github.com/Kartavya-Jharwal/Kartavya_Business_Analytics2025/blob/main/A1/assignment.ipynb)",
            unsafe_allow_html=True,
        )
