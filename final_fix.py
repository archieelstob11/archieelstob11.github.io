import glob
import re

# 1. Add missing grid classes to styles.css
css_append = """
/* Automatic Layout Fixes */
.news-grid, .projects-grid, .services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--sp-6);
}

.news-card__link {
    color: var(--clr-accent-orange);
    font-weight: var(--fw-bold);
}
"""

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()
if '.news-grid' not in css:
    with open('css/styles.css', 'a', encoding='utf-8') as f:
        f.write(css_append)

# 2. Fix wrappers and news classes in HTML files
html_files = glob.glob('*.html')
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Bypass the flex-breaking wrappers
    html = html.replace('class="header-content"', 'class="header-content" style="display: contents;"')
    html = html.replace('class="top-bar__content"', 'class="top-bar__content" style="display: contents;"')
    
    # Fix news classes
    html = html.replace('class="news-image"', 'class="news-card__image"')
    html = html.replace('class="news-date"', 'class="news-card__meta"')
    html = html.replace('class="news-content"', 'class="news-card__body"')
    html = html.replace('class="news-title"', 'class="news-card__title"')
    html = html.replace('class="news-excerpt"', 'class="news-card__excerpt"')
    html = html.replace('class="news-link"', 'class="news-card__link"')
    
    # Check stats counters: data-count is not showing because they are zero in html and animated?
    # Actually wait, they probably don't have the base value or the JS fails. Let's ensure they have a baseline.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Final HTML fixes applied.")
