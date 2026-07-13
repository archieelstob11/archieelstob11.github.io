import os
import glob

# Mappings from generic HTML classes to BEM classes in styles.css
REPLACEMENTS = {
    'class="top-bar-left"': 'class="top-bar__left"',
    'class="top-bar-right"': 'class="top-bar__right"',
    'class="top-bar-link"': 'class="top-bar__item"',
    'class="social-links"': 'class="top-bar__social"',
    
    'class="logo"': 'class="header__logo"',
    'class="logo-text"': 'class="header__logo-text"',
    'class="main-nav"': 'class="nav"',
    'class="nav-list"': 'class="nav__list"',
    'class="nav-link"': 'class="nav__link"',
    'class="nav-item has-dropdown"': 'class="nav__dropdown"',
    'class="nav-item active"': 'class="nav__item active"',
    'class="nav-item"': 'class="nav__item"',
    'class="mega-dropdown"': 'class="nav__dropdown-menu"',
    
    'class="hero-bg"': 'class="hero__bg"',
    'class="page-header-bg"': 'class="page-header__bg"',
    'class="page-header-content animate-on-scroll"': 'class="page-header__content animate-on-scroll"',
    'class="page-header-overlay"': 'class="page-header__overlay"'
}

JS_REPLACEMENTS = {
    '".nav-link"': '".nav__link"',
}

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in REPLACEMENTS.items():
        content = content.replace(old, new)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file}")

js_files = glob.glob('js/*.js')
for file in js_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in JS_REPLACEMENTS.items():
        content = content.replace(old, new)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file}")

print("Formatting classes synced.")
