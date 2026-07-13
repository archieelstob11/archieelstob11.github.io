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
            <img src="images/logo.png" alt="Restek Logo">
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
                <a href="services.html" class="nav__link {services_active}">
                    <span class="nav__dropdown-toggle">Solutions & Services <i class="chevron"></i></span>
                </a>
                <div class="nav__dropdown-menu">
                  <a href="services.html#ground-remediation"><i class="fas fa-road"></i> Ground Remediation</a>
                  <a href="services.html#gpr"><i class="fas fa-satellite-dish"></i> Ground Penetrating Radar</a>
                  <a href="services.html#surface-coatings"><i class="fas fa-paint-roller"></i> Surface Coatings</a>
                  <a href="services.html#crack-repair"><i class="fas fa-tools"></i> Crack Repair</a>
                  <a href="services.html#structural-strengthening"><i class="fas fa-building"></i> Structural Strengthening</a>
                  <a href="services.html#waterproofing"><i class="fas fa-water"></i> Waterproofing</a>
                  <a href="services.html#subsidence"><i class="fas fa-house-damage"></i> Subsidence</a>
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
          <a href="contact.html" class="btn btn-primary header__cta" id="header-cta">Get a Quote</a>
          <button class="hamburger" id="mobile-toggle" aria-label="Toggle Menu">
            <span class="hamburger__line"></span>
            <span class="hamburger__line"></span>
            <span class="hamburger__line"></span>
          </button>
        </div>
      </div>
    </header>

    <!-- Mobile Menu Overlay -->
    <div class="mobile-nav" id="mobile-menu">
      <ul class="mobile-nav__list">
        <li><a href="index.html" class="mobile-nav__link">Home</a></li>
        <li><a href="about.html" class="mobile-nav__link">About Us</a></li>
        <li><a href="services.html" class="mobile-nav__link">Solutions & Services</a></li>
        <li><a href="projects.html" class="mobile-nav__link">Projects</a></li>
        <li><a href="contact.html" class="mobile-nav__link">Contact</a></li>
      </ul>
      <a href="contact.html" class="btn btn-primary mobile-cta">Get a Quote</a>
    </div>
"""

footer_html = """
    <!-- Footer -->
    <footer class="footer">
      <div class="container">
        <div class="footer-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: var(--sp-8); padding-bottom: var(--sp-10); border-bottom: 1px solid var(--clr-border-subtle);">
          <div class="footer-col">
            <a href="index.html" class="footer__logo">
              <img src="images/logo.png" alt="Restek Logo" style="height: 60px; width: auto; object-fit: contain;">
            </a>
            <p class="footer__about" style="margin-top: var(--sp-4); color: var(--clr-text-muted);">Your rock for remediation. Specialist contractors serving the UK with industry-leading solutions.</p>
          </div>
          <div class="footer-col">
            <h4 class="footer-heading" style="color: var(--clr-text-heading); margin-bottom: var(--sp-4);">Quick Links</h4>
            <ul class="footer__links" style="list-style: none; padding: 0;">
              <li><a href="about.html" style="color: var(--clr-text-muted); text-decoration: none;">About Us</a></li>
              <li><a href="projects.html" style="color: var(--clr-text-muted); text-decoration: none;">Projects</a></li>
              <li><a href="contact.html" style="color: var(--clr-text-muted); text-decoration: none;">Contact Us</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4 class="footer-heading" style="color: var(--clr-text-heading); margin-bottom: var(--sp-4);">Our Services</h4>
            <ul class="footer__links" style="list-style: none; padding: 0;">
              <li><a href="services.html#ground-remediation" style="color: var(--clr-text-muted); text-decoration: none;">Ground Remediation</a></li>
              <li><a href="services.html#gpr" style="color: var(--clr-text-muted); text-decoration: none;">Ground Penetrating Radar</a></li>
              <li><a href="services.html#crack-repair" style="color: var(--clr-text-muted); text-decoration: none;">Crack Repair</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4 class="footer-heading" style="color: var(--clr-text-heading); margin-bottom: var(--sp-4);">Newsletter</h4>
            <p class="footer__newsletter-text" style="color: var(--clr-text-muted); margin-bottom: var(--sp-4);">Subscribe to our newsletter for the latest news and insights.</p>
            <form class="newsletter-form">
              <div class="newsletter-input-group" style="display: flex;">
                <input type="email" placeholder="Your email address" required style="padding: var(--sp-2); border: 1px solid var(--clr-border-subtle); background: var(--clr-glass-bg); color: var(--clr-text-light);">
                <button type="submit" class="btn btn-primary"><i class="fas fa-paper-plane"></i></button>
              </div>
            </form>
          </div>
        </div>
        <div class="footer__bottom" style="padding-top: var(--sp-6); text-align: center; color: var(--clr-text-muted);">
          <p>&copy; 2022-2026 <strong><a href="index.html" style="color: var(--clr-accent-orange);">Restek UK Ltd</a></strong>. All rights reserved.</p>
        </div>
      </div>
    </footer>
    <script src="js/main.js"></script>
</body>
</html>
"""

index_content = """
    <!-- Hero Section -->
    <section class="hero" id="hero-section">
      <div class="hero__bg">
        <img src="images/hero-bg.png" alt="Restek UK ground remediation project" />
      </div>
      <div class="container">
        <div class="hero__content animate-on-scroll">
          <div class="hero__label">
            <span class="dot"></span>
            Your Rock for Remediation
          </div>
          <h1 class="hero__title">
            Specialist Ground <span style="color: var(--clr-accent-orange);">Remediation</span> &<br>Structural Repair
          </h1>
          <p class="hero__description">
            Industry-leading solutions in ground stabilisation, structural strengthening, waterproofing, crack repair, and ground penetrating radar across infrastructure, commercial, and residential sectors.
          </p>
          <div class="hero__actions">
            <a href="services.html" class="btn btn-primary">Our Services <i class="fas fa-arrow-right"></i></a>
            <a href="contact.html" class="btn btn-outline">Get a Quote</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Overview -->
    <section class="section">
        <div class="container">
            <div style="text-align: center; margin-bottom: var(--sp-12);">
                <p style="color: var(--clr-accent-orange); font-weight: var(--fw-bold); text-transform: uppercase; letter-spacing: var(--ls-wider); margin-bottom: var(--sp-2);">What We Do</p>
                <h2 style="font-size: var(--fs-3xl); font-weight: var(--fw-bold); color: var(--clr-text-heading);">Our Solutions & Services</h2>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: var(--sp-8);">
                <div class="service-card" style="background: var(--clr-card-bg); border: 1px solid var(--clr-glass-border); padding: var(--sp-8); border-radius: var(--radius-lg); transition: transform var(--tr-normal);">
                    <i class="fas fa-road" style="font-size: var(--fs-3xl); color: var(--clr-accent-orange); margin-bottom: var(--sp-6);"></i>
                    <h3 style="font-size: var(--fs-xl); color: var(--clr-text-heading); margin-bottom: var(--sp-4);">Infrastructure</h3>
                    <p style="color: var(--clr-text-muted); margin-bottom: var(--sp-6);">Specialist remediation for roads, rail, and utilities.</p>
                    <a href="services.html" style="color: var(--clr-accent-orange); font-weight: var(--fw-bold);">Learn More <i class="fas fa-arrow-right"></i></a>
                </div>
                <div class="service-card" style="background: var(--clr-card-bg); border: 1px solid var(--clr-glass-border); padding: var(--sp-8); border-radius: var(--radius-lg); transition: transform var(--tr-normal);">
                    <i class="fas fa-building" style="font-size: var(--fs-3xl); color: var(--clr-accent-orange); margin-bottom: var(--sp-6);"></i>
                    <h3 style="font-size: var(--fs-xl); color: var(--clr-text-heading); margin-bottom: var(--sp-4);">Commercial</h3>
                    <p style="color: var(--clr-text-muted); margin-bottom: var(--sp-6);">Structural repairs and waterproofing for commercial buildings.</p>
                    <a href="services.html" style="color: var(--clr-accent-orange); font-weight: var(--fw-bold);">Learn More <i class="fas fa-arrow-right"></i></a>
                </div>
                <div class="service-card" style="background: var(--clr-card-bg); border: 1px solid var(--clr-glass-border); padding: var(--sp-8); border-radius: var(--radius-lg); transition: transform var(--tr-normal);">
                    <i class="fas fa-house" style="font-size: var(--fs-3xl); color: var(--clr-accent-orange); margin-bottom: var(--sp-6);"></i>
                    <h3 style="font-size: var(--fs-xl); color: var(--clr-text-heading); margin-bottom: var(--sp-4);">Residential</h3>
                    <p style="color: var(--clr-text-muted); margin-bottom: var(--sp-6);">Subsidence and ground stabilisation for homes.</p>
                    <a href="services.html" style="color: var(--clr-accent-orange); font-weight: var(--fw-bold);">Learn More <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>
        </div>
    </section>

    <!-- Statistics Section -->
    <section class="stats section" id="stats-section" style="background: var(--clr-glass-bg); border-top: 1px solid var(--clr-glass-border); border-bottom: 1px solid var(--clr-glass-border);">
      <div class="container">
        <div class="stats-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: var(--sp-8); text-align: center;">
          <div class="stat-card">
            <p style="color: var(--clr-text-muted); font-weight: var(--fw-bold); text-transform: uppercase;">YEARS EXPERIENCE</p>
            <div class="stat__number" data-count="25" style="font-size: var(--fs-4xl); font-weight: var(--fw-black); color: var(--clr-accent-orange); margin: var(--sp-2) 0;">0</div>
            <p style="color: var(--clr-text-muted); font-weight: var(--fw-bold);">+</p>
          </div>
          <div class="stat-card">
            <p style="color: var(--clr-text-muted); font-weight: var(--fw-bold); text-transform: uppercase;">PROJECTS COMPLETED</p>
            <div class="stat__number" data-count="500" style="font-size: var(--fs-4xl); font-weight: var(--fw-black); color: var(--clr-accent-orange); margin: var(--sp-2) 0;">0</div>
            <p style="color: var(--clr-text-muted); font-weight: var(--fw-bold);">+</p>
          </div>
          <div class="stat-card">
            <p style="color: var(--clr-text-muted); font-weight: var(--fw-bold); text-transform: uppercase;">EXPERT TEAM MEMBERS</p>
            <div class="stat__number" data-count="50" style="font-size: var(--fs-4xl); font-weight: var(--fw-black); color: var(--clr-accent-orange); margin: var(--sp-2) 0;">0</div>
            <p style="color: var(--clr-text-muted); font-weight: var(--fw-bold);">+</p>
          </div>
          <div class="stat-card">
            <p style="color: var(--clr-text-muted); font-weight: var(--fw-bold); text-transform: uppercase;">SECTORS SERVED</p>
            <div class="stat__number" data-count="3" style="font-size: var(--fs-4xl); font-weight: var(--fw-black); color: var(--clr-accent-orange); margin: var(--sp-2) 0;">0</div>
            <p style="color: var(--clr-text-muted); font-weight: var(--fw-bold);">+</p>
          </div>
        </div>
      </div>
    </section>
"""

about_content = """
    <div style="padding: 120px 0 80px; background: var(--clr-glass-bg); text-align: center; border-bottom: 1px solid var(--clr-glass-border);">
        <h1 style="font-size: var(--fs-4xl); font-weight: var(--fw-black); color: var(--clr-text-heading);">About Restek</h1>
        <p style="font-size: var(--fs-lg); color: var(--clr-text-muted);">Your rock for remediation.</p>
    </div>
    
    <div class="container" style="padding: 80px 0;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--sp-12); align-items: center;">
            <div>
                <h2 style="font-size: var(--fs-3xl); font-weight: var(--fw-bold); color: var(--clr-text-heading); margin-bottom: var(--sp-6);">Our Story</h2>
                <p style="font-size: var(--fs-lg); line-height: var(--lh-relaxed); color: var(--clr-text-light); margin-bottom: var(--sp-4);">Restek is a specialist concrete and ground remediation company established in 2013, with the capability to deliver full turn key projects nationally. Restek's focus is on three main sectors; Infrastructure, Commercial & Residential.</p>
                <p style="font-size: var(--fs-lg); line-height: var(--lh-relaxed); color: var(--clr-text-light); margin-bottom: var(--sp-4);">Restek's unique deep depth Ground Penetrating Radar (GPR), identifies the full extent of the problem beneath the ground, ensuring blind spots and guess work are eliminated when identifying the remedial solution needed. We offer remedial solutions that are value engineered for our clients and we can validate our decisions to the client, throughout the project using our LIVE deep depth GPR system.</p>
                <p style="font-size: var(--fs-lg); line-height: var(--lh-relaxed); color: var(--clr-text-light); margin-bottom: var(--sp-4);">Unlike our competitor's, Restek's GPR system offers highways & OnTrack rail specific options, deep depth results and blended data using our bespoke software to ensure precise, accurate and reliable data results. Restek's industry experience and vast portfolio of remedial services sets us apart from the competition and ensures our projects run smoothly and efficiently from start to finish.</p>
                <p style="font-size: var(--fs-lg); line-height: var(--lh-relaxed); color: var(--clr-text-light);">Since 2021, Restek has been an EOT (Employee Ownership Trust). This has ensured that our team benefits from having a stake in the business & everyone has their say on key decisions that drive our success.</p>
            </div>
            <div>
                <img src="images/about-team.png" alt="Restek Team" style="width: 100%; height: auto; border: 1px solid var(--clr-border-subtle); border-radius: var(--radius-lg); box-shadow: var(--shadow-xl);">
            </div>
        </div>
    </div>
"""

services_content = """
    <div style="padding: 120px 0 80px; background: var(--clr-glass-bg); text-align: center; border-bottom: 1px solid var(--clr-glass-border);">
        <h1 style="font-size: var(--fs-4xl); font-weight: var(--fw-black); color: var(--clr-text-heading);">Solutions & Services</h1>
        <p style="font-size: var(--fs-lg); color: var(--clr-text-muted);">Expert remediation tailored to your sector.</p>
    </div>
    <div class="container" style="padding: 80px 0;">
        <div style="text-align: center; max-width: 800px; margin: 0 auto 60px;">
            <p style="font-size: var(--fs-lg); line-height: var(--lh-relaxed); color: var(--clr-text-light);">Restek's specialist concrete & ground remediation team undertake all aspects of concrete repair and ground stabilisation. Listed below by sector are the key remediation services we offer to our clients. Restek has a comprehensive portfolio of remediation services in addition to our key services.</p>
        </div>
        
        <div style="display: grid; grid-template-columns: 1fr; gap: 80px;">
            
            <!-- Service 1 -->
            <div id="gpr" style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--sp-10); align-items: center;">
                <div style="order: 2;">
                    <h3 style="font-size: var(--fs-2xl); font-weight: var(--fw-bold); color: var(--clr-text-heading); margin-bottom: var(--sp-4);">Ground Penetrating Radar (GPR)</h3>
                    <p style="color: var(--clr-text-light); line-height: var(--lh-relaxed); margin-bottom: var(--sp-4);">Restek offer a unique deep depth Ground Penetrating Radar system. We have developed the OnTrack Rail GPR system for deep depth data retrieval.</p>
                    <ul style="color: var(--clr-text-light); line-height: var(--lh-relaxed); margin-left: var(--sp-6);">
                        <li>GPR for Rail – Specialist Rail Surveys</li>
                        <li>GPR for Roads – Specialist Highways Surveys</li>
                        <li>Trackbed Stabilisation</li>
                        <li>Pavement / Carriageway Rehabilitation</li>
                    </ul>
                </div>
                <div style="order: 1;">
                    <img src="images/services-gpr.png" alt="GPR Services" style="width: 100%; height: auto; border: 1px solid var(--clr-border-subtle); border-radius: var(--radius-lg); box-shadow: var(--shadow-xl);">
                </div>
            </div>

            <!-- Service 2 -->
            <div id="crack-repair" style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--sp-10); align-items: center;">
                <div>
                    <h3 style="font-size: var(--fs-2xl); font-weight: var(--fw-bold); color: var(--clr-text-heading); margin-bottom: var(--sp-4);">Crack Repair & Structural Strengthening</h3>
                    <p style="color: var(--clr-text-light); line-height: var(--lh-relaxed); margin-bottom: var(--sp-4);">We offer remedial solutions that are value engineered for our clients. Our crack repair and structural strengthening services are unmatched.</p>
                    <ul style="color: var(--clr-text-light); line-height: var(--lh-relaxed); margin-left: var(--sp-6);">
                        <li>Carbon Fibre Structural Strengthening</li>
                        <li>Crack Repair & Stitching</li>
                        <li>Underpinning Traditional & Resin Injection</li>
                        <li>Slab Jacking / Lifting</li>
                    </ul>
                </div>
                <div>
                    <img src="images/services-repair.png" alt="Crack Repair Services" style="width: 100%; height: auto; border: 1px solid var(--clr-border-subtle); border-radius: var(--radius-lg); box-shadow: var(--shadow-xl);">
                </div>
            </div>

            <!-- Service 3 -->
            <div id="waterproofing" style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--sp-10); align-items: center;">
                <div style="order: 2;">
                    <h3 style="font-size: var(--fs-2xl); font-weight: var(--fw-bold); color: var(--clr-text-heading); margin-bottom: var(--sp-4);">Waterproofing & Surface Coatings</h3>
                    <p style="color: var(--clr-text-light); line-height: var(--lh-relaxed); margin-bottom: var(--sp-4);">Restek's industry experience and vast portfolio of remedial services sets us apart from the competition, including advanced waterproofing.</p>
                    <ul style="color: var(--clr-text-light); line-height: var(--lh-relaxed); margin-left: var(--sp-6);">
                        <li>Structural & Barrier Waterproofing</li>
                        <li>Surface Coatings</li>
                        <li>Joint Sealing</li>
                        <li>Floor Screeds & Levelling</li>
                    </ul>
                </div>
                <div style="order: 1;">
                    <img src="images/services-waterproofing.png" alt="Waterproofing Services" style="width: 100%; height: auto; border: 1px solid var(--clr-border-subtle); border-radius: var(--radius-lg); box-shadow: var(--shadow-xl);">
                </div>
            </div>

        </div>
    </div>
"""

projects_content = """
    <div style="padding: 120px 0 80px; background: var(--clr-glass-bg); text-align: center; border-bottom: 1px solid var(--clr-glass-border);">
        <h1 style="font-size: var(--fs-4xl); font-weight: var(--fw-black); color: var(--clr-text-heading);">Our Projects</h1>
        <p style="font-size: var(--fs-lg); color: var(--clr-text-muted);">See our remediation expertise in action.</p>
    </div>
    <div class="container" style="padding: 80px 0; min-height: 50vh;">
        <p style="font-size: var(--fs-lg); line-height: var(--lh-relaxed); color: var(--clr-text-light); text-align: center; max-width: 800px; margin: 0 auto 60px;">The case study archive below shows some of the projects our Restek team has successfully completed in the Infrastructure, Commercial or Residential sectors. Our key services include Ground Penetrating Radar (GPR) Surveys, Ground & Concrete Remediation By Resin Injection, Underpinning, Crack Stitching, Waterproofing and Surface Coatings to name just a few.</p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: var(--sp-8);">
            
            <div class="service-card" style="background: var(--clr-card-bg); border: 1px solid var(--clr-glass-border); padding: var(--sp-8); border-radius: var(--radius-lg); transition: transform var(--tr-normal);">
                <h3 style="font-size: var(--fs-xl); color: var(--clr-text-heading); margin-bottom: var(--sp-4);">A483 Highway Ground Remediation</h3>
                <p style="color: var(--clr-text-muted); margin-bottom: var(--sp-6);">Restek's Deep Depth GPR & Ground Remediation in North Wales.</p>
                <a href="#" style="color: var(--clr-accent-orange); font-weight: var(--fw-bold);">Read Case Study <i class="fas fa-arrow-right"></i></a>
            </div>

            <div class="service-card" style="background: var(--clr-card-bg); border: 1px solid var(--clr-glass-border); padding: var(--sp-8); border-radius: var(--radius-lg); transition: transform var(--tr-normal);">
                <h3 style="font-size: var(--fs-xl); color: var(--clr-text-heading); margin-bottom: var(--sp-4);">Thurvaston Culvert Case Study</h3>
                <p style="color: var(--clr-text-muted); margin-bottom: var(--sp-6);">Infrastructure remediation and structural strengthening.</p>
                <a href="#" style="color: var(--clr-accent-orange); font-weight: var(--fw-bold);">Read Case Study <i class="fas fa-arrow-right"></i></a>
            </div>

            <div class="service-card" style="background: var(--clr-card-bg); border: 1px solid var(--clr-glass-border); padding: var(--sp-8); border-radius: var(--radius-lg); transition: transform var(--tr-normal);">
                <h3 style="font-size: var(--fs-xl); color: var(--clr-text-heading); margin-bottom: var(--sp-4);">High Trees Residential Case Study</h3>
                <p style="color: var(--clr-text-muted); margin-bottom: var(--sp-6);">Subsidence and ground stabilisation for residential properties.</p>
                <a href="#" style="color: var(--clr-accent-orange); font-weight: var(--fw-bold);">Read Case Study <i class="fas fa-arrow-right"></i></a>
            </div>
            
        </div>
    </div>
"""

contact_content = """
    <div style="padding: 120px 0 80px; background: var(--clr-glass-bg); text-align: center; border-bottom: 1px solid var(--clr-glass-border);">
        <h1 style="font-size: var(--fs-4xl); font-weight: var(--fw-black); color: var(--clr-text-heading);">Contact Us</h1>
        <p style="font-size: var(--fs-lg); color: var(--clr-text-muted);">Get in touch for a quote or consultation.</p>
    </div>
    <div class="container" style="padding: 80px 0; min-height: 50vh;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--sp-12);">
            
            <div>
                <h2 style="font-size: var(--fs-3xl); font-weight: var(--fw-bold); color: var(--clr-text-heading); margin-bottom: var(--sp-6);">Get in Touch</h2>
                <p style="font-size: var(--fs-lg); line-height: var(--lh-relaxed); color: var(--clr-text-light); margin-bottom: var(--sp-8);">Whether you're looking for specialist ground remediation, structural repairs, or GPR surveys, the team at Restek UK Ltd is here to help.</p>
                
                <div style="margin-bottom: var(--sp-6);">
                    <h4 style="font-size: var(--fs-xl); font-weight: var(--fw-bold); color: var(--clr-text-heading); margin-bottom: var(--sp-2);"><i class="fas fa-map-marker-alt" style="color: var(--clr-accent-orange); margin-right: 10px;"></i> Address</h4>
                    <p style="color: var(--clr-text-light);">Restek House, Unit 1<br>Booth Street<br>Ripley<br>Derbyshire<br>DE5 3DN</p>
                </div>

                <div style="margin-bottom: var(--sp-6);">
                    <h4 style="font-size: var(--fs-xl); font-weight: var(--fw-bold); color: var(--clr-text-heading); margin-bottom: var(--sp-2);"><i class="fas fa-phone" style="color: var(--clr-accent-orange); margin-right: 10px;"></i> Phone</h4>
                    <p style="color: var(--clr-text-light);">01773 438905</p>
                </div>

                <div style="margin-bottom: var(--sp-6);">
                    <h4 style="font-size: var(--fs-xl); font-weight: var(--fw-bold); color: var(--clr-text-heading); margin-bottom: var(--sp-2);"><i class="fas fa-envelope" style="color: var(--clr-accent-orange); margin-right: 10px;"></i> Email</h4>
                    <p style="color: var(--clr-text-light);">info@restekltd.com</p>
                </div>
            </div>

            <div style="background: var(--clr-card-bg); border: 1px solid var(--clr-glass-border); padding: var(--sp-8); border-radius: var(--radius-lg); box-shadow: var(--shadow-xl);">
                <form>
                    <div style="margin-bottom: var(--sp-4);">
                        <label style="display: block; color: var(--clr-text-heading); font-weight: var(--fw-bold); margin-bottom: var(--sp-2);">Name</label>
                        <input type="text" style="width: 100%; padding: var(--sp-3); border: 1px solid var(--clr-border-subtle); background: var(--clr-glass-bg); color: var(--clr-text-light); border-radius: var(--radius-md);" required>
                    </div>
                    <div style="margin-bottom: var(--sp-4);">
                        <label style="display: block; color: var(--clr-text-heading); font-weight: var(--fw-bold); margin-bottom: var(--sp-2);">Email</label>
                        <input type="email" style="width: 100%; padding: var(--sp-3); border: 1px solid var(--clr-border-subtle); background: var(--clr-glass-bg); color: var(--clr-text-light); border-radius: var(--radius-md);" required>
                    </div>
                    <div style="margin-bottom: var(--sp-4);">
                        <label style="display: block; color: var(--clr-text-heading); font-weight: var(--fw-bold); margin-bottom: var(--sp-2);">Message</label>
                        <textarea rows="5" style="width: 100%; padding: var(--sp-3); border: 1px solid var(--clr-border-subtle); background: var(--clr-glass-bg); color: var(--clr-text-light); border-radius: var(--radius-md);" required></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary" style="width: 100%;">Send Message</button>
                </form>
            </div>

        </div>
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

print("All HTML files reconstructed successfully with fully scraped content and images!")
