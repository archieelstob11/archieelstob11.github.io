import urllib.request
import re
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.record = False

    def handle_starttag(self, tag, attrs):
        if tag in ['p', 'h1', 'h2', 'h3']:
            self.record = True

    def handle_endtag(self, tag):
        if tag in ['p', 'h1', 'h2', 'h3']:
            self.record = False
            self.text.append('\n')

    def handle_data(self, data):
        if self.record:
            self.text.append(data.strip())

def fetch_and_extract(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
        parser = TextExtractor()
        parser.feed(html)
        
        raw = " ".join(parser.text).replace('\n ', '\n').replace(' \n', '\n')
        lines = [line.strip() for line in raw.split('\n') if len(line.strip()) > 20 and "Subscribe to our newsletter" not in line]
        
        seen = set()
        unique = []
        for line in lines:
            if line not in seen:
                seen.add(line)
                unique.append(line)
                
        return "\n\n".join(unique[:12])
    except Exception as e:
        return f"Error fetching {url}: {e}"

pages = {
    'Services': 'https://restekltd.com/solutions-services/',
    'Projects': 'https://restekltd.com/case-studies/',
    'Contact': 'https://restekltd.com/contact-us/'
}

for name, url in pages.items():
    print(f"--- {name} ---")
    print(fetch_and_extract(url))
    print("\n")
