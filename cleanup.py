import os
import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Fix the double class issue for mobile-toggle
    # It might look like: class="mobile-toggle" id="mobile-toggle" class="hamburger"
    # or similar due to multiple replacements
    
    # We want the button to have exactly one class attribute: class="hamburger" id="mobile-toggle"
    # Let's just use regex to clean up the button
    html = re.sub(r'<button[^>]*id="mobile-toggle"[^>]*>', '<button class="hamburger" id="mobile-toggle" aria-label="Toggle Menu">', html)
    
    # Also fix mobile-menu-overlay double classes if any
    html = re.sub(r'<div[^>]*id="mobile-menu"[^>]*>', '<div class="mobile-nav" id="mobile-menu">', html)
    
    # Let's fix the nav list problem by making ul class="nav" instead of nav__list,
    # OR we can just use nav__list and fix it in CSS. Let's fix the HTML:
    # Instead of <nav class="nav" id="main-nav"> <ul class="nav__list">
    # Let's just make the ul the flex container by adding a style to styles.css.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        
# Add .nav__list and .mega-list styles to styles.css
with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.nav__list {' not in css:
    css += """

/* --- Fixes injected automatically --- */
.nav__list {
  display: flex;
  align-items: center;
  gap: var(--sp-1);
  margin: 0;
  padding: 0;
}

.mega-list {
  display: flex;
  flex-direction: column;
  gap: var(--sp-2);
  margin: 0;
  padding: 0;
}

.mega-heading {
  font-family: var(--ff-heading);
  font-size: var(--fs-base);
  color: var(--clr-white);
  margin-bottom: var(--sp-4);
  display: flex;
  align-items: center;
  gap: var(--sp-2);
}

.mega-heading i {
  color: var(--clr-accent-orange);
}
"""
    with open('css/styles.css', 'w', encoding='utf-8') as f:
        f.write(css)

print("HTML cleanup and CSS append completed.")
