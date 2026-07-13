import os

header_html = """<!DOCTYPE html>
<html lang="en-GB">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Restek UK Ltd - Your Rock for Remediation</title>
    <meta name="description" content="Restek UK Ltd - Specialist ground remediation, structural repair, waterproofing, and GPR services across infrastructure, commercial, and residential sectors. Your rock for remediation.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <!-- Top Bar -->
    <div class="top-bar">
        <div class="container">
            <div class="top-bar-content">
                <div class="top-bar-left">
                    <a href="tel:+441773438905" class="top-bar-link" id="top-phone">
                        <i class="fas fa-phone"></i>
                        <span>01773 438905</span>
                    </a>
                    <a href="mailto:info@restekltd.com" class="top-bar-link" id="top-email">
                        <i class="fas fa-envelope"></i>
                        <span>info@restekltd.com</span>
                    </a>
                </div>
                <div class="top-bar-right">
                    <div class="social-links">
                        <a href="https://www.facebook.com/RestekLTD/" target="_blank" rel="noopener" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                        <a href="https://twitter.com/RestekUKLTD" target="_blank" rel="noopener" aria-label="Twitter"><i class="fab fa-x-twitter"></i></a>
                        <a href="https://www.instagram.com/restek_ukltd/" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                        <a href="https://www.youtube.com/channel/UCi-WhqzECs9Lo9z_r0eNfmw" target="_blank" rel="noopener" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
                        <a href="https://www.linkedin.com/company/restek-uk-limited/" target="_blank" rel="noopener" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Header -->
    <header class="header" id="main-header">
      <div class="container">
        <div class="header-content" style="display: contents;">
          <a href="index.html" class="header__logo" id="site-logo">
            <img src="images/logo.png" alt="Restek Logo" style="height: 76px; width: auto; object-fit: contain;">
          </a>
          <nav class="nav" id="main-nav">
            <ul class="nav__list">
              <li class="nav__item {home_active}">
                <a href="index.html" class="nav__link">Home</a>
              </li>
              <li class="nav__item {about_active}">
                <a href="about.html" class="nav__link">About Us</a>
              </li>
              <li class="nav__dropdown">
                <a href="services.html" class="nav__link {services_active}">Solutions & Services <i class="fas fa-chevron-down"></i></a>
                <div class="nav__dropdown-menu">
                  <div class="mega-dropdown-inner" style="display: flex; gap: 20px; padding: 20px;">
                    <div class="mega-col">
                      <h4 class="mega-heading"><i class="fas fa-road"></i> Infrastructure</h4>
                      <ul class="mega-list">
                        <li><a href="services.html#ground-remediation">Ground Remediation</a></li>
                        <li><a href="services.html#gpr">Ground Penetrating Radar (GPR)</a></li>
                        <li><a href="services.html#surface-coatings">Surface Coatings</a></li>
                        <li><a href="services.html#crack-repair">Crack Repair</a></li>
                        <li><a href="services.html#structural-strengthening">Structural Strengthening</a></li>
                        <li><a href="services.html#waterproofing">Waterproofing</a></li>
                      </ul>
                    </div>
                    <div class="mega-col">
                      <h4 class="mega-heading"><i class="fas fa-building"></i> Commercial</h4>
                      <ul class="mega-list">
                        <li><a href="services.html#ground-remediation">Ground Remediation</a></li>
                        <li><a href="services.html#gpr">Ground Penetrating Radar – GPR</a></li>
                        <li><a href="services.html#crack-repair">Crack Repair</a></li>
                        <li><a href="services.html#surface-coatings">Surface Coatings</a></li>
                        <li><a href="services.html#structural-strengthening">Structural Strengthening</a></li>
                        <li><a href="services.html#waterproofing">Waterproofing</a></li>
                      </ul>
                    </div>
                    <div class="mega-col">
                      <h4 class="mega-heading"><i class="fas fa-house"></i> Residential</h4>
                      <ul class="mega-list">
                        <li><a href="services.html#subsidence">Subsidence & Ground Stabilisation</a></li>
                        <li><a href="services.html#crack-repair">Crack Repair</a></li>
                      </ul>
                    </div>
                  </div>
                </div>
              </li>
              <li class="nav__item {projects_active}">
                <a href="projects.html" class="nav__link">Projects</a>
              </li>
              <li class="nav__item {contact_active}">
                <a href="contact.html" class="nav__link">Contact</a>
              </li>
            </ul>
          </nav>
          <a href="contact.html" class="btn btn-primary header-cta" id="header-cta">Get a Quote</a>
          <button class="mobile-toggle" id="mobile-toggle" aria-label="Toggle Menu">
            <span></span><span></span><span></span>
          </button>
        </div>
      </div>
    </header>

    <!-- Mobile Menu Overlay -->
    <div class="mobile-menu-overlay" id="mobile-menu">
      <div class="mobile-menu-content">
        <ul class="mobile-nav-list">
          <li><a href="index.html">Home</a></li>
          <li><a href="about.html">About Us</a></li>
          <li><a href="services.html">Solutions & Services</a></li>
          <li><a href="projects.html">Projects</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
        <a href="contact.html" class="btn btn-primary mobile-cta">Get a Quote</a>
      </div>
    </div>
"""

footer_html = """
    <!-- Footer -->
    <footer class="footer">
      <div class="container">
        <div class="footer__top" style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 40px; padding-bottom: 40px; border-bottom: 1px solid var(--clr-border-subtle);">
          <div class="footer-col">
            <a href="index.html" class="footer__logo">
              <img src="images/logo.png" alt="Restek Logo" style="height: 60px; width: auto; object-fit: contain;">
            </a>
            <p class="footer__about">Your rock for remediation. Specialist contractors serving the UK with industry-leading solutions.</p>
            <div class="footer__social" style="display: flex; gap: 15px; margin-top: 20px;">
              <a href="#"><i class="fab fa-facebook-f"></i></a>
              <a href="#"><i class="fab fa-twitter"></i></a>
              <a href="#"><i class="fab fa-linkedin-in"></i></a>
              <a href="#"><i class="fab fa-instagram"></i></a>
            </div>
          </div>
          <div class="footer-col">
            <h4 class="footer-heading">Quick Links</h4>
            <ul class="footer__links">
              <li><a href="about.html">About Us</a></li>
              <li><a href="projects.html">Projects</a></li>
              <li><a href="contact.html">Contact Us</a></li>
              <li><a href="#">Health & Safety</a></li>
              <li><a href="#">Privacy Policy</a></li>
              <li><a href="#">Anti-Slavery Policy</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4 class="footer-heading">Our Services</h4>
            <ul class="footer__links">
              <li><a href="services.html#ground-remediation">Ground Remediation</a></li>
              <li><a href="services.html#gpr">Ground Penetrating Radar</a></li>
              <li><a href="services.html#crack-repair">Crack Repair</a></li>
              <li><a href="services.html#surface-coatings">Surface Coatings</a></li>
              <li><a href="services.html#structural-strengthening">Structural Strengthening</a></li>
              <li><a href="services.html#waterproofing">Waterproofing</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4 class="footer-heading">Newsletter</h4>
            <p class="footer__newsletter-text">Subscribe to our newsletter for the latest news and insights.</p>
            <form class="newsletter-form">
              <div class="newsletter-input-group" style="display: flex;">
                <input type="email" placeholder="Your email address" required style="padding: 10px; flex-grow: 1; border: 2px solid #000;">
                <button type="submit" class="btn btn-primary"><i class="fas fa-paper-plane"></i></button>
              </div>
            </form>
          </div>
        </div>
        <div class="footer__bottom" style="padding-top: 20px; text-align: center; color: var(--clr-text-muted);">
          <p>&copy; 2022-2026 <strong><a href="index.html">Restek UK Ltd</a></strong>. All rights reserved.</p>
          <p>Specialist Remediation Contractors</p>
        </div>
      </div>
    </footer>
    <script src="js/main.js"></script>
</body>
</html>
"""

# Now the page specific content
index_content = """
    <!-- Hero Section -->
    <section class="hero" id="hero-section" style="position: relative; padding: 120px 0; min-height: 80vh; display: flex; align-items: center;">
      <div class="hero__bg" style="position: absolute; inset: 0; z-index: 0;">
        <img src="images/hero-bg.png" alt="Restek UK ground remediation project" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.2;"/>
      </div>
      <div class="container" style="position: relative; z-index: 2;">
        <div class="hero-content">
          <div class="hero-badge" style="display: inline-block; padding: 5px 15px; border: 2px solid #000; margin-bottom: 20px; font-weight: bold;">
            <span class="badge-dot" style="display: inline-block; width: 8px; height: 8px; background: #cc0000; border-radius: 50%; margin-right: 8px;"></span>
            Your Rock for Remediation
          </div>
          <h1 class="hero__title" style="font-size: 4rem; font-weight: 900; line-height: 1.1; margin-bottom: 30px; color: #111827;">
            Specialist Ground Remediation &<br>Structural Repair
          </h1>
          <p class="hero__description" style="font-size: 1.25rem; color: #495057; max-width: 600px; margin-bottom: 40px;">
            Industry-leading solutions in ground stabilisation, structural strengthening, waterproofing, crack repair, and ground penetrating radar across infrastructure, commercial, and residential sectors.
          </p>
          <div class="hero__actions" style="display: flex; gap: 20px;">
            <a href="services.html" class="btn btn-primary" style="padding: 15px 30px; font-weight: bold; background: #cc0000; color: #fff; border: 2px solid #000; box-shadow: 4px 4px 0px #000; text-decoration: none;">Our Services <i class="fas fa-arrow-right"></i></a>
            <a href="contact.html" class="btn btn-outline" style="padding: 15px 30px; font-weight: bold; background: transparent; color: #000; border: 2px solid #000; box-shadow: 4px 4px 0px #000; text-decoration: none;">Get a Quote</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Overview -->
    <section class="section" style="padding: 80px 0; background: #fff;">
        <div class="container">
            <p style="font-weight: bold; margin-bottom: 10px; color: #cc0000;">What We Do</p>
            <h2 style="font-size: 3rem; font-weight: 900; margin-bottom: 40px;">Our Solutions & Services</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
                <div class="service-card" style="border: 2px solid #000; padding: 30px; box-shadow: 6px 6px 0px #000; background: #f8f9fa;">
                    <i class="fas fa-road" style="font-size: 2.5rem; color: #cc0000; margin-bottom: 20px;"></i>
                    <h3 style="font-size: 1.5rem; margin-bottom: 15px;">Infrastructure</h3>
                    <p style="margin-bottom: 20px; color: #495057;">Specialist remediation for roads, rail, and utilities.</p>
                    <a href="services.html" style="font-weight: bold; color: #000; text-decoration: none;">Learn More <i class="fas fa-arrow-right"></i></a>
                </div>
                <div class="service-card" style="border: 2px solid #000; padding: 30px; box-shadow: 6px 6px 0px #000; background: #f8f9fa;">
                    <i class="fas fa-building" style="font-size: 2.5rem; color: #cc0000; margin-bottom: 20px;"></i>
                    <h3 style="font-size: 1.5rem; margin-bottom: 15px;">Commercial</h3>
                    <p style="margin-bottom: 20px; color: #495057;">Structural repairs and waterproofing for commercial buildings.</p>
                    <a href="services.html" style="font-weight: bold; color: #000; text-decoration: none;">Learn More <i class="fas fa-arrow-right"></i></a>
                </div>
                <div class="service-card" style="border: 2px solid #000; padding: 30px; box-shadow: 6px 6px 0px #000; background: #f8f9fa;">
                    <i class="fas fa-house" style="font-size: 2.5rem; color: #cc0000; margin-bottom: 20px;"></i>
                    <h3 style="font-size: 1.5rem; margin-bottom: 15px;">Residential</h3>
                    <p style="margin-bottom: 20px; color: #495057;">Subsidence and ground stabilisation for homes.</p>
                    <a href="services.html" style="font-weight: bold; color: #000; text-decoration: none;">Learn More <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>
        </div>
    </section>

    <!-- Statistics Section -->
    <section class="stats" id="stats-section" style="padding: 80px 0; background: #e9ecef;">
      <div class="container">
        <div class="stats-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 40px; text-align: center;">
          <div class="stat-card" style="border: 2px solid #000; padding: 40px; background: #fff; box-shadow: 8px 8px 0px #000;">
            <p style="font-weight: bold; color: #495057;">YEARS EXPERIENCE</p>
            <div class="stat__number" data-count="25" style="font-size: 4rem; font-weight: 900; color: #cc0000; margin: 10px 0;">0</div>
            <p style="font-weight: bold;">+</p>
          </div>
          <div class="stat-card" style="border: 2px solid #000; padding: 40px; background: #fff; box-shadow: 8px 8px 0px #000;">
            <p style="font-weight: bold; color: #495057;">PROJECTS COMPLETED</p>
            <div class="stat__number" data-count="500" style="font-size: 4rem; font-weight: 900; color: #cc0000; margin: 10px 0;">0</div>
            <p style="font-weight: bold;">+</p>
          </div>
          <div class="stat-card" style="border: 2px solid #000; padding: 40px; background: #fff; box-shadow: 8px 8px 0px #000;">
            <p style="font-weight: bold; color: #495057;">EXPERT TEAM MEMBERS</p>
            <div class="stat__number" data-count="50" style="font-size: 4rem; font-weight: 900; color: #cc0000; margin: 10px 0;">0</div>
            <p style="font-weight: bold;">+</p>
          </div>
          <div class="stat-card" style="border: 2px solid #000; padding: 40px; background: #fff; box-shadow: 8px 8px 0px #000;">
            <p style="font-weight: bold; color: #495057;">SECTORS SERVED</p>
            <div class="stat__number" data-count="3" style="font-size: 4rem; font-weight: 900; color: #cc0000; margin: 10px 0;">0</div>
            <p style="font-weight: bold;">+</p>
          </div>
        </div>
      </div>
    </section>

    <div style="position: fixed; bottom: 30px; right: 30px; z-index: 999;">
        <a href="#top" style="display: flex; align-items: center; justify-content: center; width: 50px; height: 50px; background: #fff; color: #cc0000; border: 2px solid #000; box-shadow: 4px 4px 0px #000; font-size: 1.5rem;"><i class="fas fa-chevron-up"></i></a>
    </div>
"""

about_content = """
    <div style="padding: 120px 0 80px; background: #f8f9fa; text-align: center; border-bottom: 2px solid #000;">
        <h1 style="font-size: 4rem; font-weight: 900;">About Us</h1>
        <p style="font-size: 1.25rem; color: #495057;">Your rock for remediation.</p>
    </div>
    <div class="container" style="padding: 80px 0;">
        <p style="font-size: 1.2rem; line-height: 1.6;">Restek UK Ltd is a specialist remediation contractor...</p>
    </div>
"""

services_content = """
    <div style="padding: 120px 0 80px; background: #f8f9fa; text-align: center; border-bottom: 2px solid #000;">
        <h1 style="font-size: 4rem; font-weight: 900;">Solutions & Services</h1>
        <p style="font-size: 1.25rem; color: #495057;">Expert remediation tailored to your sector.</p>
    </div>
    <div class="container" style="padding: 80px 0; min-height: 50vh;">
        <h2 style="font-size: 2.5rem; font-weight: 900;">Our Services</h2>
    </div>
"""

projects_content = """
    <div style="padding: 120px 0 80px; background: #f8f9fa; text-align: center; border-bottom: 2px solid #000;">
        <h1 style="font-size: 4rem; font-weight: 900;">Our Projects</h1>
        <p style="font-size: 1.25rem; color: #495057;">See our remediation expertise in action.</p>
    </div>
    <div class="container" style="padding: 80px 0; min-height: 50vh;">
        <h2 style="font-size: 2.5rem; font-weight: 900;">Recent Work</h2>
    </div>
"""

contact_content = """
    <div style="padding: 120px 0 80px; background: #f8f9fa; text-align: center; border-bottom: 2px solid #000;">
        <h1 style="font-size: 4rem; font-weight: 900;">Contact Us</h1>
        <p style="font-size: 1.25rem; color: #495057;">Get in touch for a quote or consultation.</p>
    </div>
    <div class="container" style="padding: 80px 0; min-height: 50vh;">
        <h2 style="font-size: 2.5rem; font-weight: 900;">Send us a message</h2>
    </div>
"""

def build_page(filename, content, active_nav):
    # Set up active nav states
    nav_states = {
        'home_active': 'active' if active_nav == 'home' else '',
        'about_active': 'active' if active_nav == 'about' else '',
        'services_active': 'active' if active_nav == 'services' else '',
        'projects_active': 'active' if active_nav == 'projects' else '',
        'contact_active': 'active' if active_nav == 'contact' else ''
    }
    
    html = header_html.format(**nav_states) + content + footer_html
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {filename}")

build_page('index.html', index_content, 'home')
build_page('about.html', about_content, 'about')
build_page('services.html', services_content, 'services')
build_page('projects.html', projects_content, 'projects')
build_page('contact.html', contact_content, 'contact')

print("All HTML files reconstructed successfully!")
