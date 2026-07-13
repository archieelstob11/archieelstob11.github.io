import glob
import re

# 1. Update CSS colors
css_file = 'css/styles.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace hex and RGB
css = css.replace('#f97316', '#cc0000') # Orange to Deep Red
css = css.replace('#f59e0b', '#ff1a1a') # Amber to Bright Red
css = css.replace('249, 115, 22', '204, 0, 0')
css = css.replace('245, 158, 11', '255, 26, 26')

# Additionally check if gradient variable name needs renaming, but it's safe to keep it
with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Include logo in HTML files
html_files = glob.glob('*.html')
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace the text logo with the image
    # The original is:
    # <a href="index.html" class="header__logo" id="site-logo">
    #   <span class="header__logo-text">RESTEK</span>
    #   <span class="logo-tagline">UK LTD</span>
    # </a>
    # We will use regex to find the inner contents of header__logo and replace it.
    
    pattern = r'(<a[^>]*class="header__logo"[^>]*>)\s*<span class="header__logo-text">[^<]*</span>\s*<span class="logo-tagline">[^<]*</span>\s*(</a>)'
    replacement = r'\1\n            <img src="images/logo.png" alt="Restek Logo" style="height: 60px; width: auto;">\n          \2'
    
    html = re.sub(pattern, replacement, html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Theme and logo updated successfully.")
