import re

css_file = 'css/styles.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace Theme Variables
# 1. Colors
css = css.replace('--clr-primary-dark: #0a0e17;', '--clr-primary-dark: #f8f9fa;') # Light primary background
css = css.replace('--clr-secondary-dark: #111827;', '--clr-secondary-dark: #e9ecef;') # Light secondary background
css = css.replace('--clr-text-light: #f1f5f9;', '--clr-text-light: #212529;') # Dark text
css = css.replace('--clr-text-muted: #94a3b8;', '--clr-text-muted: #495057;') # Dark muted text
css = css.replace('--clr-text-heading: #ffffff;', '--clr-text-heading: #111827;') # Dark heading text
css = css.replace('--clr-white: #ffffff;', '--clr-white: #ffffff;') # Keep white as white
css = css.replace('--clr-card-bg: rgba(17, 24, 39, 0.7);', '--clr-card-bg: #ffffff;') # Solid white cards
css = css.replace('--clr-card-bg-solid: #111827;', '--clr-card-bg-solid: #ffffff;') # Solid white background for overlays
css = css.replace('--clr-border-subtle: rgba(204, 0, 0, 0.15);', '--clr-border-subtle: #000000;') # Solid black borders
css = css.replace('--clr-border-hover: rgba(204, 0, 0, 0.45);', '--clr-border-hover: #cc0000;') # Red border on hover
css = css.replace('--clr-glass-bg: rgba(10, 14, 23, 0.72);', '--clr-glass-bg: #ffffff;') # No glass, solid white
css = css.replace('--clr-glass-border: rgba(255, 255, 255, 0.06);', '--clr-glass-border: #000000;') # Solid black borders
css = css.replace('--clr-overlay: rgba(10, 14, 23, 0.65);', '--clr-overlay: rgba(255, 255, 255, 0.85);') # Light overlay

# 2. Shadows (Rugged, solid offsets instead of blurs)
css = css.replace('--shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);', '--shadow-sm: 2px 2px 0px rgba(0, 0, 0, 1);')
css = css.replace('--shadow-md: 0 4px 12px rgba(0, 0, 0, 0.4);', '--shadow-md: 4px 4px 0px rgba(0, 0, 0, 1);')
css = css.replace('--shadow-lg: 0 8px 30px rgba(0, 0, 0, 0.45);', '--shadow-lg: 8px 8px 0px rgba(0, 0, 0, 1);')
css = css.replace('--shadow-xl: 0 16px 50px rgba(0, 0, 0, 0.5);', '--shadow-xl: 12px 12px 0px rgba(0, 0, 0, 1);')
css = css.replace('--shadow-glow: 0 0 25px rgba(var(--clr-accent-orange-rgb), 0.25);', '--shadow-glow: none;')
css = css.replace('--shadow-glow-lg: 0 0 50px rgba(var(--clr-accent-orange-rgb), 0.18);', '--shadow-glow-lg: none;')
css = re.sub(r'--shadow-card-hover:[\s\S]*?;', '--shadow-card-hover: 6px 6px 0px rgba(0, 0, 0, 1);', css)

# 3. Border Radii (Blocky, sharp corners)
css = css.replace('--radius-sm: 0.375rem;', '--radius-sm: 0px;')
css = css.replace('--radius-md: 0.5rem;', '--radius-md: 0px;')
css = css.replace('--radius-lg: 0.75rem;', '--radius-lg: 0px;')
css = css.replace('--radius-xl: 1rem;', '--radius-xl: 0px;')
css = css.replace('--radius-2xl: 1.5rem;', '--radius-2xl: 0px;')
css = css.replace('--radius-full: 9999px;', '--radius-full: 0px;') # Optional, but keeps it rugged

# 4. Remove backdrop filters for glassmorphism
css = re.sub(r'backdrop-filter:\s*blur\([^)]+\);', '', css)

# 5. Fix footer heading and mega heading color
css = css.replace('color: var(--clr-white);', 'color: var(--clr-text-heading);')

# 6. Buttons
# Let's add a solid border to buttons for the rugged look
css = css.replace('.btn {', '.btn {\n  border: 2px solid #000;')

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

print("Theme updated to Light & Rugged.")
