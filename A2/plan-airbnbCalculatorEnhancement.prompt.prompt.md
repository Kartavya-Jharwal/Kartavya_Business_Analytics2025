## Plan: Airbnb Price Calculator Microsite Enhancement

**Quality Target:** Awwwards-level visual polish — a spectacular, attention-grabbing experience that feels premium and delightful. Prioritize fast loading (minimal external dependencies, inline critical CSS, lightweight animations).

This plan upgrades the calculator from a functional prototype to a showcase-quality microsite by unifying design systems with the landing page, adding stunning micro-interactions, and ensuring the UI scales beautifully across all devices.

### Steps

1. **Unify design system with landing page** — Adopt the landing page's complete design language:
   - Add `Space Mono` font for labels, numbers, and data displays
   - Align CSS variable names (`--accent`, `--success`, `--bg-dark`, `--bg-card`, `--border`)
   - Replicate typographic hierarchy: monospace section labels with `letter-spacing: 0.1em`, tight leading, bold data callouts
   - Match the dark theme palette (`#0a0a0a`, `#111111`, `#FF5A5F`, `#00A699`)
   - Consistent card styling with subtle borders and hover states

2. **Elevate visual hierarchy & layout** — Create a more impactful information architecture:
   - Add numbered section labels (e.g., "01 · PROPERTY DETAILS") in monospace
   - Larger, bolder price display with animated number transitions
   - Visual separation between input and output sections using gradients/borders
   - Premium card shadows and layering depth
   - Consider split-screen or asymmetric layouts for desktop

3. **Add spectacular micro-interactions & animations** — Make every interaction feel intentional and delightful:
   - Smooth hover lift effects (`translateY(-2px)`) on all interactive elements
   - Button press feedback with scale transforms
   - Price update animation with counting/morphing numbers
   - Subtle parallax or floating elements in background
   - Input focus states with glowing borders and smooth transitions
   - Staggered fade-in animations on page load
   - Consider: particle effects, gradient shifts, or liquid glass morphism

4. **Implement smart form logic** — Add JavaScript enforcing logical property configurations:
   - `beds >= bedrooms` (at least 1 bed per bedroom, except studios)
   - `accommodates <= beds × 2` (reasonable guest-to-bed ratio)
   - Room-type-specific caps (Private/Shared rooms limit capacity)
   - Auto-adjust related fields gracefully with subtle toast notifications

5. **Perfect responsive scaling** — Ensure the experience is premium on every device:
   - Fluid typography with `clamp()` for seamless scaling
   - Touch-optimized controls (min 44×44px targets)
   - Mobile-first layout that expands elegantly on desktop
   - Consider horizontal layout or side-by-side panels on wide screens

6. **Enhance accessibility without compromising aesthetics** — WCAG AA compliance:
   - Proper `aria-label` on all interactive elements
   - Sufficient color contrast (especially on dark backgrounds)
   - Keyboard navigation support with visible focus indicators
   - Reduced motion media query support for animations
