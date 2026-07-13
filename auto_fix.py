import os
import re
import glob

# Read all classes from styles.css
with open('css/styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Find all CSS classes
css_classes = set(re.findall(r'\.([a-zA-Z0-9_-]+)', css_content))

# Hardcoded mappings for things that don't follow the exact rule
HARDCODED = {
    'logo': 'header__logo',
    'logo-text': 'header__logo-text',
    'main-nav': 'nav',
    'nav-list': 'nav__list',
    'nav-link': 'nav__link',
    'has-dropdown': 'nav__dropdown',
    'mega-dropdown': 'nav__dropdown-menu',
    'header-cta': 'header__cta',
    'mobile-toggle': 'hamburger',
    'mobile-menu-overlay': 'mobile-nav',
    'mobile-nav-list': 'mobile-nav__list',
    'mobile-cta': 'mobile-nav__cta',
    'hero-badge': 'hero__label',
    'badge-dot': 'dot',
    'hero-subtitle': 'hero__description',
    'gradient-text': 'gradient-text', # if it exists
    'services-grid': 'services__grid',
    'service-card': 'service-card',
    'service-icon': 'service-card__icon',
    'service-content': 'service-card__content',
    'service-title': 'service-card__title',
    'service-desc': 'service-card__description',
    'service-link': 'service-card__link',
    'cookie-banner': 'cookie-banner',
    'btn-primary': 'btn btn-primary',
}

def auto_map(cls_name):
    if cls_name in css_classes:
        return cls_name
    
    if cls_name in HARDCODED:
        return HARDCODED[cls_name]
    
    # Try replacing first hyphen with __
    parts = cls_name.split('-', 1)
    if len(parts) == 2:
        candidate = f"{parts[0]}__{parts[1]}"
        if candidate in css_classes:
            return candidate
            
    # Try replacing all hyphens with __
    candidate = cls_name.replace('-', '__')
    if candidate in css_classes:
        return candidate
        
    return cls_name

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Find all class="..."
    def replacer(match):
        classes = match.group(1).split()
        new_classes = []
        for c in classes:
            mapped = auto_map(c)
            # avoid duplicates if hardcoded mapped to two classes
            for mc in mapped.split():
                if mc not in new_classes:
                    new_classes.append(mc)
        return f'class="{" ".join(new_classes)}"'
        
    new_html = re.sub(r'class="([^"]+)"', replacer, html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Processed {filepath}")

# Process JS
js_files = glob.glob('js/*.js')
for filepath in js_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        js = f.read()
        
    # We can just manually replace some known ones for JS
    js = js.replace('.nav-link', '.nav__link')
    js = js.replace('#mobile-toggle', '.hamburger')
    js = js.replace('#mobile-menu', '.mobile-nav')
    js = js.replace('.mobile-toggle', '.hamburger')
    js = js.replace('.mobile-menu-overlay', '.mobile-nav')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(js)
    print(f"Processed {filepath}")
