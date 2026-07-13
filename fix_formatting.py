import glob
import re

# 1. Update CSS file
css_file = 'css/styles.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix logo height in CSS
css = re.sub(r'\.header__logo img\s*\{\s*height:\s*42px;', '.header__logo img {\n  height: 76px;', css)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Fix HTML files
html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove inline style for logo
    html = re.sub(r'style="height:\s*76px;\s*width:\s*auto;\s*object-fit:\s*contain;"', '', html)

    # Fix mobile menu classes
    html = html.replace('class="mobile-toggle"', 'class="hamburger"')
    html = html.replace('id="mobile-toggle"', 'id="hamburger"')
    html = html.replace('<span></span><span></span><span></span>', '<span class="hamburger__line"></span><span class="hamburger__line"></span><span class="hamburger__line"></span>')

    html = html.replace('class="mobile-menu-overlay"', 'class="mobile-nav"')
    html = html.replace('id="mobile-menu"', 'id="mobile-nav"')
    
    # Fix mobile nav links
    html = html.replace('class="mobile-nav-list"', 'class="mobile-nav__list"')
    html = re.sub(r'<li><a href="([^"]+)">([^<]+)</a></li>', r'<li><a href="\1" class="mobile-nav__link">\2</a></li>', html)
    html = re.sub(r'<li><a href="([^"]+)" class="active">([^<]+)</a></li>', r'<li><a href="\1" class="mobile-nav__link active">\2</a></li>', html)

    # Fix mega menu styling since the old CSS is gone
    # If the user sees formatting issues, they might be referring to the mega-menu dropdown or footer.
    # We already have inline flex styling for the dropdown, but let's make sure it's clean.

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("CSS and HTML formatting issues fixed.")
