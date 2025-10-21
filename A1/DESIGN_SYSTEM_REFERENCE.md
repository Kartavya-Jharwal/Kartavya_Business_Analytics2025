# CarbonSeer Design System - Quick Reference

## 🎨 Color Variables

```css
/* Primary Colors */
--color-primary: #8B7D9B          /* Purple - Main brand */
--color-primary-light: #A89BB3    /* Light purple */
--color-primary-dark: #6B5D7B     /* Dark purple */
--color-secondary: #6B9B91        /* Teal - Accent */
--color-accent: #C9A9A6           /* Dusty rose */
--color-earth: #A68B7B            /* Earth brown */
--color-beige: #F5F3F0            /* Warm beige */

/* Semantic Colors */
--color-success: #66BB6A          /* Green */
--color-warning: #FFA726          /* Orange */
--color-error: #EF5350            /* Red */
--color-info: #42A5F5             /* Blue */
```

## 📏 Spacing Scale

```css
--space-xs: 0.25rem    /* 4px */
--space-sm: 0.5rem     /* 8px */
--space-md: 1rem       /* 16px */
--space-lg: 1.5rem     /* 24px */
--space-xl: 2rem       /* 32px */
--space-2xl: 3rem      /* 48px */
--space-3xl: 4rem      /* 64px */
--space-4xl: 6rem      /* 96px */
```

## 🔤 Typography

```css
/* Font Families */
--font-display: 'Plus Jakarta Sans', 'Inter', sans-serif
--font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif

/* Font Sizes */
Hero Title: clamp(2.5rem, 6vw, 4.5rem)
Section Header: clamp(1.8rem, 3vw, 2.5rem)
Subheader: clamp(1.3rem, 2vw, 1.8rem)
Body Large: 1.1rem
Body: 1rem
Small: 0.9rem
Label: 0.85rem
```

## 🔲 Border Radius

```css
--radius-sm: 8px
--radius-md: 12px
--radius-lg: 16px
--radius-xl: 24px
--radius-full: 9999px
```

## 🌑 Shadows

```css
--shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.04)
--shadow-md: 0 4px 16px rgba(0, 0, 0, 0.06)
--shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.08)
--shadow-xl: 0 16px 48px rgba(0, 0, 0, 0.12)
--shadow-2xl: 0 24px 64px rgba(0, 0, 0, 0.16)
```

## ⏱️ Transitions

```css
--transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1)
--transition-base: 300ms cubic-bezier(0.4, 0, 0.2, 1)
--transition-slow: 500ms cubic-bezier(0.4, 0, 0.2, 1)
```

## 🎬 Key Animations

```css
/* Fade In Up */
animation: fadeInUp 0.8s ease-out;

/* Slide In Left */
animation: slideInLeft 0.6s ease-out;

/* Fade In Scale */
animation: fadeInScale 0.8s ease-out;

/* With Delay (stagger) */
animation: fadeInUp 0.6s ease-out 0.2s backwards;
```

## 📦 Component Classes

### Metric Card
```html
<div class='metric-card'>
    <div class='metric-label'>LABEL</div>
    <div class='metric-value'>123</div>
    <div class='metric-delta'>Change text</div>
</div>
```

### Section Header
```html
<div class='section-header'>
    📊 Section Title
</div>
```

### Info Box (4 variants)
```html
<div class='info-box'>Content</div>
<div class='success-box'>Success message</div>
<div class='warning-box'>Warning message</div>
<!-- Info with custom gradient -->
<div class='info-box' style='background: linear-gradient(135deg, rgba(66, 165, 245, 0.08), rgba(66, 165, 245, 0.05));'>
```

### Insight Card
```html
<div class='insight-card'>
    <span class='insight-number'>01</span>
    <p>Insight text</p>
</div>
```

### Chart Container
```html
<div class='chart-container'>
    <!-- Plotly chart here -->
</div>
```

### Hero Section
```html
<div class='hero-section'>
    <div class='hero-title'>Title</div>
    <div class='hero-subtitle'>Subtitle</div>
</div>
```

## 🎨 Utility Classes

```css
/* Colors */
.color-purple { color: #8B7D9B; }
.color-teal { color: #6B9B91; }
.color-accent { color: #C9A9A6; }

/* Backgrounds */
.bg-purple { background-color: #8B7D9B; }
.bg-teal { background-color: #6B9B91; }
.bg-beige { background-color: #F5F3F0; }
```

## 📱 Responsive Breakpoints

```css
/* Mobile */
@media (max-width: 768px) {
    /* Mobile styles */
}

/* Tablet and up */
@media (min-width: 768px) {
    /* Tablet styles */
}

/* Desktop */
@media (min-width: 1024px) {
    /* Desktop styles */
}
```

## ✨ Glassmorphism Recipe

```css
background: rgba(255, 255, 255, 0.95);
backdrop-filter: blur(20px);
-webkit-backdrop-filter: blur(20px);
border: 1px solid rgba(255, 255, 255, 0.3);
box-shadow: var(--shadow-lg);
```

## 🎯 Hover Effects

```css
/* Lift & Scale */
transition: all var(--transition-base);
&:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: var(--shadow-2xl);
}

/* Slide Right */
&:hover {
    transform: translateX(4px);
}

/* Glow */
&:hover {
    box-shadow: 0 0 0 3px rgba(139, 125, 155, 0.1);
}
```

## 📊 Chart Theme Integration

```python
import plotly.graph_objects as go
from utils.styling import get_plotly_theme

theme = get_plotly_theme()
fig = go.Figure(...)
fig.update_layout(**theme['layout'])
```

## 🔧 Common Patterns

### Staggered Animations
```html
<div style='animation: fadeInUp 0.6s ease-out 0.1s backwards;'>Item 1</div>
<div style='animation: fadeInUp 0.6s ease-out 0.2s backwards;'>Item 2</div>
<div style='animation: fadeInUp 0.6s ease-out 0.3s backwards;'>Item 3</div>
```

### Gradient Text
```html
<div style='background: linear-gradient(135deg, var(--color-primary), var(--color-secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 800;'>
    Gradient Text
</div>
```

### Stat Grid
```html
<div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem;'>
    <div>Stat 1</div>
    <div>Stat 2</div>
    <div>Stat 3</div>
</div>
```

## 🎭 Animation Choreography

### Page Load Sequence
1. Hero (0s) - Immediate
2. Branding (0.2s) - Slight delay
3. First content section (0.4s)
4. Subsequent sections (0.6s, 0.8s, etc.)

### Card Stagger
- Each card: +0.1s delay
- Example: 0.1s, 0.2s, 0.3s, 0.4s

### Scroll Reveal
- Trigger at: 20% visible
- Duration: 0.6-0.8s
- Easing: ease-out

## 🔍 Accessibility Checklist

- [ ] Focus states visible (3px outline)
- [ ] Color contrast ≥ 4.5:1
- [ ] Alt text on images
- [ ] Semantic HTML
- [ ] Keyboard navigation
- [ ] ARIA labels where needed
- [ ] Skip links for navigation

## 💡 Pro Tips

1. **Consistent Spacing:** Use spacing variables, not hardcoded values
2. **Animation Performance:** Prefer transform/opacity over position/dimensions
3. **Color Usage:** Primary for CTAs, secondary for accents, neutrals for text
4. **Typography:** Max 2-3 font weights per font family
5. **Shadows:** Increase shadow depth with elevation
6. **Gradients:** Subtle (5-10% opacity difference) for backgrounds
7. **Border Radius:** Consistent within component types
8. **Hover States:** Always provide visual feedback
9. **Loading States:** Shimmer or skeleton screens
10. **Mobile First:** Design for mobile, enhance for desktop

## 📚 Resources

- **Fonts:** [Google Fonts](https://fonts.google.com/)
- **Colors:** [Coolors](https://coolors.co/)
- **Gradients:** [uiGradients](https://uigradients.com/)
- **Shadows:** [ShadowBrumm](https://shadows.brumm.af/)
- **Animations:** [Animista](https://animista.net/)
- **Accessibility:** [WAVE](https://wave.webaim.org/)

---

**Quick Start:**
```python
# Import design system
from utils.styling import get_custom_css, get_plotly_theme

# Apply global styles
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Use components
st.markdown("<div class='metric-card'>...</div>", unsafe_allow_html=True)
```

**File Location:** `utils/styling.py`

**Documentation:** `DESIGN_UPGRADE_COMPLETE.md`
