#!/usr/bin/env python3
"""Build script: assembles CFT website pages from a shared shell."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
WA = "250788750184"
PHONE = "+250 788 750 184 and +250 792 757 653"
EMAIL = "cftrading26@gmail.com"
ADDRESS_LINE1 = "35a KG 37 Avenue"
ADDRESS_LINE2 = "Kimironko, Gasabo District, Kigali, Rwanda"
AIRBNB1 = "https://www.airbnb.com/rooms/1710869845463366565"
AIRBNB2 = "https://www.airbnb.com/rooms/14240039"
AIRBNB3 = "https://www.airbnb.com/rooms/1341268755139378216"
MAP = ("https://maps.google.com/maps?q=-1.945522,30.1362201&t=&z=16&ie=UTF8&iwloc=&output=embed")
FORMSPREE = "https://formspree.io/f/xlgyqwdg"

WA_SVG = '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3C9.4 3 4 8.4 4 15c0 2.6.8 5 2.3 7L4 29l7.2-2.3c1.9 1 4 1.6 6.3 1.6 6.6 0 12-5.4 12-12S22.6 3 16 3zm0 21.8c-2 0-3.9-.6-5.5-1.5l-.4-.2-4.3 1.4 1.4-4.1-.3-.4A9.7 9.7 0 0 1 6.2 15c0-5.4 4.4-9.8 9.8-9.8s9.8 4.4 9.8 9.8-4.4 9.8-9.8 9.8zm5.4-7.3c-.3-.2-1.8-.9-2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7 0a8 8 0 0 1-2.4-1.5 9 9 0 0 1-1.6-2c-.2-.3 0-.5.1-.7l.5-.5.3-.5c.1-.2 0-.4 0-.6l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5 0-.8.4-.3.3-1 1-1 2.5s1 2.9 1.2 3.1c.2.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.3-.7.3-1.3.2-1.4l-.6-.3z"/></svg>'

def header(active):
    def cur(name):
        return ' aria-current="page"' if name == active else ''
    return f'''<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="CFT Apartments and Shops home">
      <span class="brand-mark">CFT</span>
      <span class="brand-name">Apartments &amp; Shops<small>Cyabukombe Family Trading</small></span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-label="Open menu">☰</button>
    <nav class="main-nav" aria-label="Main navigation">
      <ul>
        <li><a href="index.html"{cur('home')}>Home</a></li>
        <li><a href="apartments.html"{cur('apartments')}>Apartments</a></li>
        <li><a href="shops.html"{cur('shops')}>Commercial Shops</a></li>
        <li><a href="about.html"{cur('about')}>About Us</a></li>
        <li><a href="gallery.html"{cur('gallery')}>Gallery</a></li>
        <li><a href="contact.html"{cur('contact')}>Contact</a></li>
        <li><a class="nav-cta" href="booking.html">Book Now</a></li>
      </ul>
    </nav>
  </div>
</header>'''

FOOTER = f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand" href="index.html" style="margin-bottom:1rem">
          <span class="brand-mark">CFT</span>
          <span class="brand-name">Apartments &amp; Shops<small>Cyabukombe Family Trading</small></span>
        </a>
        <p style="font-size:.94rem;max-width:32ch;margin-top:1rem">Luxury furnished apartments and quality commercial spaces in Kimironko, Kigali, Rwanda.</p>
      </div>
      <div>
        <h4>Quick Links</h4>
        <ul>
          <li><a href="apartments.html">Apartments</a></li>
          <li><a href="shops.html">Commercial Shops</a></li>
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="about.html">About Us</a></li>
          <li><a href="booking.html">Book Now</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li>{PHONE}</li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp Us</a></li>
        </ul>
      </div>
      <div>
        <h4>Location</h4>
        <p style="font-size:.94rem">Kimironko, Gasabo District<br>Kigali, Rwanda</p>
        <div class="socials">
          <a href="#" aria-label="Instagram">IG</a>
          <a href="#" aria-label="Facebook">FB</a>
          <a href="#" aria-label="X / Twitter">X</a>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year></span> Cyabukombe Family Trading. All rights reserved.</span>
      <span><a href="#">Privacy Policy</a><a href="#">Terms of Service</a></span>
    </div>
  </div>
</footer>
<a class="wa-float" href="https://wa.me/{WA}?text=Hello%20CFT%20Apartments%20%26%20Shops%2C%20I%27d%20like%20to%20make%20an%20inquiry."
   target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">{WA_SVG}</a>
<div class="lightbox" role="dialog" aria-modal="true" aria-label="Image viewer">
  <button class="lb-close" aria-label="Close image viewer">✕</button>
  <img src="" alt="">
  <span class="lb-caption"></span>
</div>
<script src="js/main.js"></script>'''

def shell(title, desc, active, body):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="images/cft-building-night.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="css/styles.css">
</head>
<body>
{header(active)}
{body}
{FOOTER}
</body>
</html>'''

def write(name, html):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name)

# ---------------------------------------------------------------- HOME
home_body = f'''
<main>
<section class="hero" style="padding:0">
  <img class="hero-bg" src="images/cft-building-night.jpg" alt="CFT Offices, Shops & Apartments building at night" fetchpriority="high">
  <div class="wrap hero-inner">
    <div class="frame">
      <span class="eyebrow on-dark">Murakaza Neza · Welcome</span>
      <h1>Welcome to CFT Apartments &amp; Shops</h1>
      <p>Luxury furnished apartments and quality commercial spaces in the heart of Kimironko, Kigali.</p>
      <div class="hero-actions">
        <a class="btn btn-gold" href="apartments.html">View Apartments</a>
        <a class="btn btn-outline" href="shops.html">Commercial Shops</a>
        <a class="btn btn-outline" href="booking.html">Book Now</a>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow center">Why Choose CFT</span>
      <h2>Everything a comfortable stay should be</h2>
      <p class="lead" style="margin:1rem auto 0">A family-owned property, cared for like a home and run like a fine hotel.</p>
    </div>
    <div class="feature-grid">
      <div class="feature reveal"><div class="f-icon">📍</div><h3>Prime Location</h3><p>Minutes from Kimironko Market, banks, restaurants and Kigali's business districts.</p></div>
      <div class="feature reveal"><div class="f-icon">🛡</div><h3>24/7 Security</h3><p>Gated community with round-the-clock guards and exterior security cameras.</p></div>
      <div class="feature reveal"><div class="f-icon">🛋</div><h3>Fully Furnished</h3><p>Move-in ready apartments with quality furniture, linens and equipped kitchens.</p></div>
      <div class="feature reveal"><div class="f-icon">📶</div><h3>High-Speed Wi-Fi</h3><p>Reliable fibre internet included, ready for streaming and remote work.</p></div>
      <div class="feature reveal"><div class="f-icon">🚗</div><h3>Free Parking</h3><p>Secure on-premises parking for residents, guests and shop customers.</p></div>
      <div class="feature reveal"><div class="f-icon">👨‍👩‍👧</div><h3>Family Friendly</h3><p>Quiet, green surroundings with space for children to feel at home.</p></div>
      <div class="feature reveal"><div class="f-icon">💼</div><h3>Business Friendly</h3><p>Self check-in, housekeeping options and workspaces for corporate travellers.</p></div>
      <div class="feature reveal"><div class="f-icon">🗓</div><h3>Flexible Stays</h3><p>Nightly, monthly and long-term arrangements to suit your plans.</p></div>
    </div>
  </div>
</section>

<section class="bg-sand">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Featured Residences</span>
      <h2>Stay with us in Kigali</h2>
    </div>
    <div class="prop-grid">
      <article class="prop-card reveal">
        <div class="prop-media"><span class="badge">Kimironko</span>
          <img src="images/kimironko-building.avif" alt="Exterior of the Kimironko Garden Residence building" loading="lazy"></div>
        <div class="prop-body">
          <h3>Kimironko Garden Residence</h3>
          <div class="prop-stats"><span class="stat">2 guests</span><span class="stat">1 bedroom</span><span class="stat">1 bed</span><span class="stat">1 bath</span></div>
          <p>A warm, quiet one-bedroom apartment steps from Kimironko's markets and cafés — comfortable furnishings, equipped kitchen and balcony.</p>
          <div class="prop-actions">
            <a class="btn btn-green" href="apartment-kimironko.html">View Apartment</a>
            <a class="btn btn-ghost" href="{AIRBNB2}" target="_blank" rel="noopener">View on Airbnb</a>
          </div>
        </div>
      </article>
      <article class="prop-card reveal">
        <div class="prop-media"><span class="badge">Kimironko</span>
          <img src="images/ap16livingroom.avif" alt="Living room of Inganji Apartment 16" loading="lazy"></div>
        <div class="prop-body">
          <h3>Inganji Apartment 16</h3>
          <div class="prop-stats"><span class="stat">2 guests</span><span class="stat">1 bedroom</span><span class="stat">1 bed</span><span class="stat">1 bath</span></div>
          <p>A cosy, fully furnished one-bedroom apartment in Kimironko — living room, equipped kitchen and private balcony.</p>
          <div class="prop-actions">
            <a class="btn btn-green" href="apartment-inganji.html">View Apartment</a>
            <a class="btn btn-ghost" href="{AIRBNB3}" target="_blank" rel="noopener">View on Airbnb</a>
          </div>
        </div>
      </article>
      <article class="prop-card reveal">
        <div class="prop-media"><span class="badge">Vision City</span>
          <img src="images/Vision/living-room-2.jpg" alt="Living room of the Luxury 3BR apartment in Vision City" loading="lazy"></div>
        <div class="prop-body">
          <h3>Luxury 3BR in Vision City</h3>
          <div class="prop-stats"><span class="stat">6 guests</span><span class="stat">3 bedrooms</span><span class="stat">3 beds</span><span class="stat">2.5 baths</span></div>
          <p>A fully furnished three-bedroom apartment in Kigali's premier gated community — Wi-Fi, washer &amp; dryer, private balconies and free parking.</p>
          <div class="prop-actions">
            <a class="btn btn-green" href="apartment-vision-city.html">View Apartment</a>
            <a class="btn btn-ghost" href="{AIRBNB1}" target="_blank" rel="noopener">View on Airbnb</a>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="img-frame reveal"><img src="images/Vision/vision-city-aerial.jpg" alt="Aerial view of the Vision City estate in Kigali" loading="lazy"></div>
    <div class="reveal">
      <span class="eyebrow">Commercial Spaces</span>
      <h2>Grow your business at CFT</h2>
      <p class="lead" style="margin:1rem 0 1.6rem">Ground-floor commercial shops in a busy, secure neighbourhood — ideal for boutiques, offices, pharmacies and cafés.</p>
      <a class="btn btn-green" href="shops.html">Explore Commercial Shops</a>
    </div>
  </div>
</section>

<section class="bg-green">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow on-dark center">Guest Words</span>
      <h2>What our guests say</h2>
    </div>
    <div class="testi-grid">
      <blockquote class="testi reveal"><div class="stars">★★★★★</div><q>The apartment felt like home from the first evening. Spotless, quiet and the self check-in was effortless.</q><footer>Guest placeholder — replace with a real review</footer></blockquote>
      <blockquote class="testi reveal"><div class="stars">★★★★★</div><q>Perfect base for a work trip to Kigali. Fast Wi-Fi, secure parking and everything within reach.</q><footer>Guest placeholder — replace with a real review</footer></blockquote>
      <blockquote class="testi reveal"><div class="stars">★★★★★</div><q>Our family of five was completely comfortable. The hosts were responsive and genuinely kind.</q><footer>Guest placeholder — replace with a real review</footer></blockquote>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="cta-band reveal">
      <span class="eyebrow on-dark center">Ready when you are</span>
      <h2>Book your stay, or your storefront</h2>
      <p>Reach us directly — no agents, no middlemen. We respond quickly on WhatsApp and email.</p>
      <div class="hero-actions" style="justify-content:center">
        <a class="btn btn-gold" href="booking.html">Book Now</a>
        <a class="btn btn-outline" href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp Us</a>
      </div>
    </div>
  </div>
</section>
</main>'''
write("index.html", shell(
  "CFT Apartments & Shops | Furnished Apartments & Commercial Spaces in Kimironko, Kigali",
  "Luxury furnished apartments and quality commercial shops for rent in Kimironko, Kigali, Rwanda. Book directly with Cyabukombe Family Trading.",
  "home", home_body))

# ---------------------------------------------------------------- APARTMENTS
apts_body = f'''
<main>
<section class="hero compact" style="padding:0">
  <img class="hero-bg" src="images/kimironko-building.avif" alt="Exterior of the Kimironko Garden Residence building">
  <div class="wrap hero-inner">
    <div class="frame">
      <span class="eyebrow on-dark">Our Residences</span>
      <h1 class="page-hero-title">Apartments</h1>
      <p class="page-hero-sub">Fully furnished homes for short and long stays — book directly or through Airbnb.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="prop-grid">
      <article class="prop-card reveal">
        <div class="prop-media"><span class="badge">Kimironko</span>
          <img src="images/kimironko-building.avif" alt="Exterior of the Kimironko Garden Residence building" loading="lazy"></div>
        <div class="prop-body">
          <h3>Kimironko Garden Residence</h3>
          <div class="prop-stats"><span class="stat">2 guests</span><span class="stat">1 bedroom</span><span class="stat">1 bed</span><span class="stat">1 bath</span></div>
          <p>A calm, comfortable one-bedroom apartment in the heart of Kimironko — quality furnishings, an equipped kitchen, living room and balcony, minutes from the famous Kimironko Market.</p>
          <div class="prop-actions">
            <a class="btn btn-green" href="apartment-kimironko.html">Availability &amp; Details</a>
            <a class="btn btn-gold" href="booking.html">Book Now</a>
            <a class="btn btn-ghost" href="{AIRBNB2}" target="_blank" rel="noopener">View on Airbnb</a>
          </div>
        </div>
      </article>

      <article class="prop-card reveal">
        <div class="prop-media"><span class="badge">Kimironko</span>
          <img src="images/ap16livingroom.avif" alt="Living room of Inganji Apartment 16" loading="lazy"></div>
        <div class="prop-body">
          <h3>Inganji Apartment 16</h3>
          <div class="prop-stats"><span class="stat">2 guests</span><span class="stat">1 bedroom</span><span class="stat">1 bed</span><span class="stat">1 bath</span></div>
          <p>A cosy, fully furnished one-bedroom apartment in Kimironko — living room, equipped kitchen and private balcony.</p>
          <div class="prop-actions">
            <a class="btn btn-green" href="apartment-inganji.html">Availability &amp; Details</a>
            <a class="btn btn-gold" href="booking.html">Book Now</a>
            <a class="btn btn-ghost" href="{AIRBNB3}" target="_blank" rel="noopener">View on Airbnb</a>
          </div>
        </div>
      </article>

      <article class="prop-card reveal">
        <div class="prop-media"><span class="badge">Vision City · New</span>
          <img src="images/Vision/living-room-2.jpg" alt="Living room of Luxury 3BR in Vision City" loading="lazy"></div>
        <div class="prop-body">
          <h3>Luxury 3BR in Vision City</h3>
          <div class="prop-stats"><span class="stat">6 guests</span><span class="stat">3 bedrooms</span><span class="stat">3 beds</span><span class="stat">2.5 baths</span></div>
          <p>Comfort and style in Kigali's premier gated community. High-speed Wi-Fi, fully equipped kitchen, private balconies, washer &amp; dryer, smart-lock self check-in and free parking.</p>
          <ul class="amenity-grid" style="grid-template-columns:1fr 1fr;font-size:.92rem">
            <li>Kitchen</li><li>Wi-Fi</li><li>Free parking</li><li>Smart TV</li><li>Washer &amp; dryer</li><li>Balcony</li><li>24/7 security</li><li>Housekeeping (optional)</li>
          </ul>
          <div class="prop-actions">
            <a class="btn btn-green" href="apartment-vision-city.html">Availability &amp; Details</a>
            <a class="btn btn-gold" href="booking.html">Book Now</a>
            <a class="btn btn-ghost" href="{AIRBNB1}" target="_blank" rel="noopener">View on Airbnb</a>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="bg-sand tight">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">A Closer Look</span><h2>Inside the apartments</h2></div>
    <div class="gallery-grid">
      <figure class="g-item reveal" data-lightbox data-caption="Living room"><img src="images/Vision/living-room-1.jpg" alt="Living room with balcony view" loading="lazy"><figcaption>Living room</figcaption></figure>
      <figure class="g-item reveal" data-lightbox data-caption="Master bedroom"><img src="images/Vision/bedroom-main.jpg" alt="Master bedroom with king bed" loading="lazy"><figcaption>Master bedroom</figcaption></figure>
      <figure class="g-item reveal" data-lightbox data-caption="Private balcony"><img src="images/Vision/balcony.jpg" alt="Private balcony with garden view" loading="lazy"><figcaption>Private balcony</figcaption></figure>
    </div>
  </div>
</section>
</main>'''
write("apartments.html", shell(
  "Apartments | CFT Apartments & Shops, Kigali",
  "Browse fully furnished apartments for rent in Vision City and Kimironko, Kigali — short-term and long-term stays with CFT.",
  "apartments", apts_body))

# ---------------------------------------------------------------- APARTMENT DETAIL: VISION CITY
vc_body = f'''
<main>
<section class="hero compact" style="padding:0">
  <img class="hero-bg" src="images/Vision/living-room-2.jpg" alt="Luxury 3BR apartment in Vision City, Kigali">
  <div class="wrap hero-inner">
    <div class="frame">
      <span class="eyebrow on-dark">Vision City · Kigali</span>
      <h1 class="page-hero-title">Luxury 3BR in Vision City</h1>
      <p class="page-hero-sub">Wi-Fi · Washer &amp; Dryer · Free Parking · Self Check-in</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap detail-grid">
    <div>
      <div class="reveal">
        <span class="eyebrow">Overview</span>
        <h2>Comfort and style in Kigali's premier gated community</h2>
        <p class="lead" style="margin-top:1rem">Stay in comfort and style in this fully furnished 3-bedroom apartment in Vision City. Enjoy high-speed Wi-Fi, a fully equipped kitchen, private balconies, free parking, a washer and dryer, and optional housekeeping. With 24/7 security and easy access to Kigali's business districts, restaurants, shopping and attractions, it offers everything you need for a comfortable, safe, stress-free stay.</p>
      </div>

      <div class="gallery-grid" style="margin-top:2.4rem">
        <figure class="g-item reveal" data-lightbox data-caption="Living room"><img src="images/Vision/living-room-1.jpg" alt="Living room seating area" loading="lazy"><figcaption>Living room</figcaption></figure>
        <figure class="g-item reveal" data-lightbox data-caption="Living room and TV wall"><img src="images/Vision/living-room-2.jpg" alt="Living room with television unit" loading="lazy"><figcaption>TV lounge</figcaption></figure>
        <figure class="g-item reveal" data-lightbox data-caption="Bedroom 1 — king bed"><img src="images/Vision/bedroom-main.jpg" alt="Bedroom with king bed" loading="lazy"><figcaption>Bedroom 1 · King</figcaption></figure>
        <figure class="g-item reveal" data-lightbox data-caption="Wardrobes and vanity"><img src="images/Vision/bedroom-wardrobe.jpg" alt="Bedroom wardrobes and dressing table" loading="lazy"><figcaption>Wardrobes</figcaption></figure>
        <figure class="g-item reveal" data-lightbox data-caption="Private balcony"><img src="images/Vision/balcony.jpg" alt="Private balcony" loading="lazy"><figcaption>Balcony</figcaption></figure>
        <figure class="g-item reveal" data-lightbox data-caption="Washer and dryer"><img src="images/Vision/washer-dryer.jpg" alt="Washer and dryer" loading="lazy"><figcaption>Washer &amp; dryer</figcaption></figure>
      </div>

      <div class="reveal" style="margin-top:3rem">
        <span class="eyebrow">Amenities</span>
        <h2 style="font-size:1.7rem;margin-bottom:1.4rem">What this place offers</h2>
        <ul class="amenity-grid">
          <li>Fully equipped kitchen</li><li>High-speed Wi-Fi</li><li>Free parking on premises</li>
          <li>Smart TV</li><li>Washer &amp; dryer</li><li>Private balconies</li>
          <li>Self check-in (smart lock)</li><li>24/7 gated security</li><li>Exterior security cameras</li>
          <li>Smoke alarm</li><li>Optional housekeeping</li><li>Family friendly</li>
        </ul>
      </div>

      <div class="reveal" style="margin-top:3rem">
        <span class="eyebrow">House Rules</span>
        <h2 style="font-size:1.7rem;margin-bottom:1rem">Things to know</h2>
        <ul class="rule-list">
          <li>Check-in after 3:00 PM — self check-in with smart lock</li>
          <li>Maximum 6 guests</li>
          <li>No pets</li>
          <li>Please treat the home with the care of family</li>
        </ul>
      </div>

      <div class="reveal" style="margin-top:3rem">
        <span class="eyebrow">Location</span>
        <h2 style="font-size:1.7rem;margin-bottom:1.4rem">Where you'll be</h2>
        <div class="map-embed"><iframe src="{MAP}" title="Map of Kimironko, Kigali" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
        <ul class="rule-list" style="margin-top:1.4rem">
          <li>Kimironko Market — Kigali's largest and liveliest market</li>
          <li>Kigali Convention Centre &amp; business district — short drive</li>
          <li>Restaurants, banks, pharmacies and supermarkets nearby</li>
          <li>Easy access to Kigali International Airport</li>
        </ul>
      </div>
    </div>

    <aside class="info-card reveal">
      <h3>At a glance</h3>
      <ul class="info-list">
        <li><span>Guests</span><span>Up to 6</span></li>
        <li><span>Bedrooms</span><span>3</span></li>
        <li><span>Beds</span><span>2 King · 1 Queen</span></li>
        <li><span>Bathrooms</span><span>2.5</span></li>
        <li><span>Check-in</span><span>After 3:00 PM</span></li>
        <li><span>Parking</span><span>Free on premises</span></li>
      </ul>
      <div style="display:flex;flex-direction:column;gap:.7rem;margin-top:1.4rem">
        <a class="btn btn-gold" href="booking.html" style="justify-content:center">Book Now</a>
        <a class="btn btn-ghost" href="{AIRBNB1}" target="_blank" rel="noopener" style="justify-content:center">View on Airbnb</a>
        <a class="btn btn-whatsapp" href="https://wa.me/{WA}?text=Hello%2C%20I%27m%20interested%20in%20the%20Luxury%203BR%20in%20Vision%20City." target="_blank" rel="noopener" style="justify-content:center">WhatsApp Inquiry</a>
      </div>
    </aside>
  </div>
</section>

<section class="bg-sand">
  <div class="wrap" style="max-width:820px">
    <div class="section-head center reveal"><span class="eyebrow center">Inquiry</span><h2>Ask about this apartment</h2></div>
    <div class="form-card reveal">
      <form data-inquiry novalidate action="{FORMSPREE}" method="POST">
        <input type="hidden" name="_subject" value="CFT website inquiry — Vision City apartment">
        <div class="form-grid">
          <div class="field"><label for="v-name">Full Name</label><input id="v-name" name="name" type="text" required autocomplete="name"></div>
          <div class="field"><label for="v-phone">Phone / WhatsApp</label><input id="v-phone" name="phone" type="tel" required autocomplete="tel"></div>
          <div class="field"><label for="v-email">Email</label><input id="v-email" name="email" type="email" required autocomplete="email"></div>
          <div class="field"><label for="v-guests">Guests</label><select id="v-guests" name="guests"><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option></select></div>
          <div class="field"><label for="v-in">Check-in</label><input id="v-in" name="checkin" type="date" required></div>
          <div class="field"><label for="v-out">Check-out</label><input id="v-out" name="checkout" type="date" required></div>
          <div class="field full"><label for="v-msg">Message</label><textarea id="v-msg" name="message" rows="4" placeholder="Tell us about your stay…"></textarea></div>
        </div>
        <button class="btn btn-green" type="submit" style="margin-top:1.4rem">Send Inquiry</button>
      </form>
      <div class="form-success" role="status">Thank you for contacting CFT Apartments &amp; Shops. Your inquiry has been received. Our team will contact you shortly.</div>
      <div class="form-error" role="alert">Sorry, something went wrong sending your message. Please try again, or reach us directly on WhatsApp.</div>
    </div>
  </div>
</section>
</main>'''
write("apartment-vision-city.html", shell(
  "Luxury 3BR in Vision City | CFT Apartments & Shops",
  "Fully furnished 3-bedroom apartment in Vision City, Kigali — Wi-Fi, washer & dryer, free parking, self check-in, 24/7 security. Sleeps 6.",
  "apartments", vc_body))

# ---------------------------------------------------------------- APARTMENT DETAIL: KIMIRONKO (placeholder)
km_body = f'''
<main>
<section class="hero compact" style="padding:0">
  <img class="hero-bg" src="images/kimironko-building.avif" alt="Exterior of the Kimironko Garden Residence building">
  <div class="wrap hero-inner">
    <div class="frame">
      <span class="eyebrow on-dark">Kimironko · Kigali</span>
      <h1 class="page-hero-title">Kimironko Garden Residence</h1>
      <p class="page-hero-sub">A calm, fully furnished home in the heart of Kimironko.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap detail-grid">
    <div>
      <div class="reveal">
        <span class="eyebrow">Overview</span>
        <h2>Quiet comfort, steps from Kimironko's best</h2>
        <p class="lead" style="margin-top:1rem">A warm one-bedroom apartment with quality furnishings, a living room, fully equipped kitchen and balcony — ideal for couples and long-stay professionals who want to live in one of Kigali's most convenient neighbourhoods.</p>
      </div>

      <div class="gallery-grid" style="margin-top:2.4rem">
        <figure class="g-item reveal" data-lightbox data-caption="Building exterior"><img src="images/kimironko-building.avif" alt="Exterior of the Kimironko Garden Residence building" loading="lazy"><figcaption>Building exterior</figcaption></figure>
        <figure class="g-item reveal" data-lightbox data-caption="Bedroom"><img src="images/kimironko-bedroom.avif" alt="Bedroom with single bed" loading="lazy"><figcaption>Bedroom</figcaption></figure>
        <figure class="g-item reveal" data-lightbox data-caption="Kitchen and living area"><img src="images/kimironko-kitchen-living-1.jpg" alt="Kitchen and living area" loading="lazy"><figcaption>Kitchen &amp; living room</figcaption></figure>
        <figure class="g-item reveal" data-lightbox data-caption="Kitchen and living area"><img src="images/kimironko-kitchen-living-2.jpg" alt="Kitchen and living area, alternate view" loading="lazy"><figcaption>Kitchen &amp; living room</figcaption></figure>
        <figure class="g-item reveal" data-lightbox data-caption="Hallway and wardrobes"><img src="images/kimironko-hallway-wardrobe.avif" alt="Hallway with fitted wardrobes" loading="lazy"><figcaption>Hallway &amp; wardrobes</figcaption></figure>
        <figure class="g-item reveal" data-lightbox data-caption="Bathroom"><img src="images/kimironko-bathroom.avif" alt="Bathroom with shower" loading="lazy"><figcaption>Bathroom</figcaption></figure>
      </div>

      <div class="reveal" style="margin-top:3rem">
        <span class="eyebrow">Amenities</span>
        <h2 style="font-size:1.7rem;margin-bottom:1.4rem">What this place offers</h2>
        <ul class="amenity-grid">
          <li>Equipped kitchen</li><li>High-speed Wi-Fi</li><li>Free parking</li>
          <li>Smart TV</li><li>Washer</li><li>Balcony</li>
          <li>24/7 security</li><li>Fitted wardrobes</li><li>Housekeeping (optional)</li>
        </ul>
      </div>

      <div class="reveal" style="margin-top:3rem">
        <span class="eyebrow">House Rules</span>
        <h2 style="font-size:1.7rem;margin-bottom:1rem">Things to know</h2>
        <ul class="rule-list">
          <li>Check-in after 3:00 PM</li>
          <li>No pets</li>
          <li>Quiet hours after 10:00 PM</li>
        </ul>
      </div>

      <div class="reveal" style="margin-top:3rem">
        <span class="eyebrow">Location</span>
        <h2 style="font-size:1.7rem;margin-bottom:1.4rem">Where you'll be</h2>
        <div class="map-embed"><iframe src="{MAP}" title="Map of Kimironko, Kigali" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
        <ul class="rule-list" style="margin-top:1.4rem">
          <li>Kimironko Market — a five-minute walk</li>
          <li>Local cafés, banks and supermarkets nearby</li>
          <li>Direct routes to the city centre and airport</li>
        </ul>
      </div>
    </div>

    <aside class="info-card reveal">
      <h3>At a glance</h3>
      <ul class="info-list">
        <li><span>Guests</span><span>Up to 2</span></li>
        <li><span>Bedrooms</span><span>1</span></li>
        <li><span>Beds</span><span>1</span></li>
        <li><span>Bathrooms</span><span>1</span></li>
        <li><span>Check-in</span><span>After 3:00 PM</span></li>
        <li><span>Parking</span><span>Free on premises</span></li>
      </ul>
      <div style="display:flex;flex-direction:column;gap:.7rem;margin-top:1.4rem">
        <a class="btn btn-gold" href="booking.html" style="justify-content:center">Book Now</a>
        <a class="btn btn-ghost" href="{AIRBNB2}" target="_blank" rel="noopener" style="justify-content:center">View on Airbnb</a>
        <a class="btn btn-whatsapp" href="https://wa.me/{WA}?text=Hello%2C%20I%27m%20interested%20in%20the%20Kimironko%20Garden%20Residence." target="_blank" rel="noopener" style="justify-content:center">WhatsApp Inquiry</a>
      </div>
    </aside>
  </div>
</section>

<section class="bg-sand">
  <div class="wrap" style="max-width:820px">
    <div class="section-head center reveal"><span class="eyebrow center">Inquiry</span><h2>Ask about this apartment</h2></div>
    <div class="form-card reveal">
      <form data-inquiry novalidate action="{FORMSPREE}" method="POST">
        <input type="hidden" name="_subject" value="CFT website inquiry — Kimironko Garden Residence">
        <div class="form-grid">
          <div class="field"><label for="k-name">Full Name</label><input id="k-name" name="name" type="text" required autocomplete="name"></div>
          <div class="field"><label for="k-phone">Phone / WhatsApp</label><input id="k-phone" name="phone" type="tel" required autocomplete="tel"></div>
          <div class="field"><label for="k-email">Email</label><input id="k-email" name="email" type="email" required autocomplete="email"></div>
          <div class="field"><label for="k-guests">Guests</label><select id="k-guests" name="guests"><option>1</option><option>2</option><option>3</option><option>4</option></select></div>
          <div class="field"><label for="k-in">Check-in</label><input id="k-in" name="checkin" type="date" required></div>
          <div class="field"><label for="k-out">Check-out</label><input id="k-out" name="checkout" type="date" required></div>
          <div class="field full"><label for="k-msg">Message</label><textarea id="k-msg" name="message" rows="4" placeholder="Tell us about your stay…"></textarea></div>
        </div>
        <button class="btn btn-green" type="submit" style="margin-top:1.4rem">Send Inquiry</button>
      </form>
      <div class="form-success" role="status">Thank you for contacting CFT Apartments &amp; Shops. Your inquiry has been received. Our team will contact you shortly.</div>
      <div class="form-error" role="alert">Sorry, something went wrong sending your message. Please try again, or reach us directly on WhatsApp.</div>
    </div>
  </div>
</section>
</main>'''
write("apartment-kimironko.html", shell(
  "Kimironko Garden Residence | CFT Apartments & Shops",
  "Furnished one-bedroom apartment in Kimironko, Kigali — quiet, secure and minutes from Kimironko Market. Book directly with CFT.",
  "apartments", km_body))

# ---------------------------------------------------------------- APARTMENT DETAIL: INGANJI
ig_body = f'''
<main>
<section class="hero compact" style="padding:0">
  <img class="hero-bg" src="images/inganji-building.jpg" alt="Exterior of the Inganji Apartment 16 building">
  <div class="wrap hero-inner">
    <div class="frame">
      <span class="eyebrow on-dark">Kimironko · Kigali</span>
      <h1 class="page-hero-title">Inganji Apartment 16</h1>
      <p class="page-hero-sub">A cosy, fully furnished one-bedroom home in Kimironko.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap detail-grid">
    <div>
      <div class="reveal">
        <span class="eyebrow">Overview</span>
        <h2>Simple, comfortable and well located</h2>
        <p class="lead" style="margin-top:1rem">A furnished one-bedroom apartment with its own living room, equipped kitchen and private balcony — a practical, comfortable base for a couple or solo traveller staying in Kimironko.</p>
      </div>

      <div class="gallery-grid" style="margin-top:2.4rem">
        <figure class="g-item reveal" data-lightbox data-caption="Building exterior"><img src="images/inganji-building.jpg" alt="Exterior of the Inganji Apartment 16 building" loading="lazy"><figcaption>Building exterior</figcaption></figure>
        <figure class="g-item reveal" data-lightbox data-caption="Living room and kitchen"><img src="images/inganji-living-kitchen.jpg" alt="Furnished living room with open kitchen" loading="lazy"><figcaption>Living room &amp; kitchen</figcaption></figure>
        <figure class="g-item reveal" data-lightbox data-caption="Bedroom"><img src="images/inganji-bedroom.avif" alt="Bedroom with double bed" loading="lazy"><figcaption>Bedroom</figcaption></figure>
        <figure class="g-item reveal" data-lightbox data-caption="Kitchen"><img src="images/inganji-kitchen.jpg" alt="Kitchen with stove and cabinets" loading="lazy"><figcaption>Kitchen</figcaption></figure>
        <figure class="g-item reveal" data-lightbox data-caption="Bathroom"><img src="images/inganji-bathroom.avif" alt="Bathroom with shower and tub" loading="lazy"><figcaption>Bathroom</figcaption></figure>
        <figure class="g-item reveal" data-lightbox data-caption="Wardrobe and dining nook"><img src="images/inganji-dining-nook.jpg" alt="Wardrobe and small dining nook" loading="lazy"><figcaption>Wardrobe &amp; dining nook</figcaption></figure>
      </div>

      <div class="reveal" style="margin-top:3rem">
        <span class="eyebrow">Amenities</span>
        <h2 style="font-size:1.7rem;margin-bottom:1.4rem">What this place offers</h2>
        <ul class="amenity-grid">
          <li>Equipped kitchen</li><li>Smart TV</li><li>Balcony</li>
          <li>Fitted wardrobe</li><li>Furnished living room</li><li>Housekeeping (optional)</li>
        </ul>
      </div>

      <div class="reveal" style="margin-top:3rem">
        <span class="eyebrow">House Rules</span>
        <h2 style="font-size:1.7rem;margin-bottom:1rem">Things to know</h2>
        <ul class="rule-list">
          <li>Check-in after 3:00 PM</li>
          <li>No pets</li>
          <li>Quiet hours after 10:00 PM</li>
        </ul>
      </div>

      <div class="reveal" style="margin-top:3rem">
        <span class="eyebrow">Location</span>
        <h2 style="font-size:1.7rem;margin-bottom:1.4rem">Where you'll be</h2>
        <div class="map-embed"><iframe src="{MAP}" title="Map of Kimironko, Kigali" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
        <ul class="rule-list" style="margin-top:1.4rem">
          <li>Kimironko Market — a five-minute walk</li>
          <li>Local cafés, banks and supermarkets nearby</li>
          <li>Direct routes to the city centre and airport</li>
        </ul>
      </div>
    </div>

    <aside class="info-card reveal">
      <h3>At a glance</h3>
      <ul class="info-list">
        <li><span>Guests</span><span>Up to 2</span></li>
        <li><span>Bedrooms</span><span>1</span></li>
        <li><span>Beds</span><span>1</span></li>
        <li><span>Bathrooms</span><span>1</span></li>
        <li><span>Check-in</span><span>After 3:00 PM</span></li>
      </ul>
      <div style="display:flex;flex-direction:column;gap:.7rem;margin-top:1.4rem">
        <a class="btn btn-gold" href="booking.html" style="justify-content:center">Book Now</a>
        <a class="btn btn-ghost" href="{AIRBNB3}" target="_blank" rel="noopener" style="justify-content:center">View on Airbnb</a>
        <a class="btn btn-whatsapp" href="https://wa.me/{WA}?text=Hello%2C%20I%27m%20interested%20in%20the%20Inganji%20Apartment%2016." target="_blank" rel="noopener" style="justify-content:center">WhatsApp Inquiry</a>
      </div>
    </aside>
  </div>
</section>

<section class="bg-sand">
  <div class="wrap" style="max-width:820px">
    <div class="section-head center reveal"><span class="eyebrow center">Inquiry</span><h2>Ask about this apartment</h2></div>
    <div class="form-card reveal">
      <form data-inquiry novalidate action="{FORMSPREE}" method="POST">
        <input type="hidden" name="_subject" value="CFT website inquiry — Inganji Apartment 16">
        <div class="form-grid">
          <div class="field"><label for="ig-name">Full Name</label><input id="ig-name" name="name" type="text" required autocomplete="name"></div>
          <div class="field"><label for="ig-phone">Phone / WhatsApp</label><input id="ig-phone" name="phone" type="tel" required autocomplete="tel"></div>
          <div class="field"><label for="ig-email">Email</label><input id="ig-email" name="email" type="email" required autocomplete="email"></div>
          <div class="field"><label for="ig-guests">Guests</label><select id="ig-guests" name="guests"><option>1</option><option>2</option></select></div>
          <div class="field"><label for="ig-in">Check-in</label><input id="ig-in" name="checkin" type="date" required></div>
          <div class="field"><label for="ig-out">Check-out</label><input id="ig-out" name="checkout" type="date" required></div>
          <div class="field full"><label for="ig-msg">Message</label><textarea id="ig-msg" name="message" rows="4" placeholder="Tell us about your stay…"></textarea></div>
        </div>
        <button class="btn btn-green" type="submit" style="margin-top:1.4rem">Send Inquiry</button>
      </form>
      <div class="form-success" role="status">Thank you for contacting CFT Apartments &amp; Shops. Your inquiry has been received. Our team will contact you shortly.</div>
      <div class="form-error" role="alert">Sorry, something went wrong sending your message. Please try again, or reach us directly on WhatsApp.</div>
    </div>
  </div>
</section>
</main>'''
write("apartment-inganji.html", shell(
  "Inganji Apartment 16 | CFT Apartments & Shops",
  "Furnished one-bedroom apartment in Kimironko, Kigali — living room, equipped kitchen and balcony. Book directly with CFT.",
  "apartments", ig_body))

# ---------------------------------------------------------------- SHOPS
shops_body = f'''
<main>
<section class="hero compact" style="padding:0">
  <img class="hero-bg" src="images/Vision/building-exterior.jpg" alt="CFT mixed-use building with commercial spaces">
  <div class="wrap hero-inner">
    <div class="frame">
      <span class="eyebrow on-dark">Commercial Property</span>
      <h1 class="page-hero-title">Commercial Shops</h1>
      <p class="page-hero-sub">Quality retail and office spaces in a secure, high-visibility location in Kimironko.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="reveal">
      <span class="eyebrow">The Opportunity</span>
      <h2>A storefront where Kigali does business</h2>
      <p class="lead" style="margin:1rem 0 1.4rem">Our ground-floor commercial units sit within a well-maintained, gated mixed-use property with free customer parking, 24/7 security and steady foot traffic from residents and the surrounding Kimironko neighbourhood.</p>
      <h3 style="margin-bottom:.6rem">Ideal for</h3>
      <ul class="amenity-grid" style="grid-template-columns:1fr 1fr">
        <li>Boutiques &amp; retail</li><li>Pharmacies &amp; clinics</li>
        <li>Cafés &amp; restaurants</li><li>Professional offices</li>
        <li>Salons &amp; wellness</li><li>Financial services</li>
      </ul>
    </div>
    <div class="img-frame reveal"><img src="images/Vision/building-exterior.jpg" alt="Building exterior with commercial frontage" loading="lazy"></div>
  </div>
</section>

<section class="bg-sand">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Available Spaces</span><h2>Current listings</h2></div>
    <div class="prop-grid">
      <article class="prop-card reveal">
        <div class="prop-media"><span class="badge">Available</span>
          <img src="images/Vision/building-exterior.jpg" alt="Commercial shop unit A" loading="lazy"></div>
        <div class="prop-body">
          <h3>Shop Unit A — Ground Floor</h3>
          <div class="prop-stats"><span class="stat">± 45 m²</span><span class="stat">Street facing</span><span class="stat">Parking</span></div>
          <p>Bright corner unit with excellent visibility. Water, electricity and security included. <em>Placeholder — update floor area, rent and photos.</em></p>
          <div class="prop-actions">
            <a class="btn btn-green" href="contact.html">Inquire About This Space</a>
            <a class="btn btn-whatsapp" href="https://wa.me/{WA}?text=Hello%2C%20I%27m%20interested%20in%20Shop%20Unit%20A." target="_blank" rel="noopener">WhatsApp</a>
          </div>
        </div>
      </article>
      <article class="prop-card reveal">
        <div class="prop-media"><span class="badge">Coming Soon</span>
          <img src="images/Vision/vision-city-aerial.jpg" alt="Commercial shop unit B" loading="lazy"></div>
        <div class="prop-body">
          <h3>Shop Unit B — Ground Floor</h3>
          <div class="prop-stats"><span class="stat">± 30 m²</span><span class="stat">Interior unit</span><span class="stat">Parking</span></div>
          <p>Versatile space suited to offices or service businesses. <em>Placeholder — this card is ready for your next available unit.</em></p>
          <div class="prop-actions">
            <a class="btn btn-ghost" href="contact.html">Join the Waiting List</a>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="cta-band reveal">
      <span class="eyebrow on-dark center">Direct from the owner</span>
      <h2>Let's talk about your business</h2>
      <p>Tell us what you need — size, timing, fit-out — and we'll respond with availability and terms, no agents involved.</p>
      <div class="hero-actions" style="justify-content:center">
        <a class="btn btn-gold" href="contact.html">Send an Inquiry</a>
        <a class="btn btn-outline" href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp Us</a>
      </div>
    </div>
  </div>
</section>
</main>'''
write("shops.html", shell(
  "Commercial Shops for Rent | CFT Apartments & Shops, Kimironko Kigali",
  "Commercial shop spaces for rent in Kimironko, Kigali — secure, high-visibility units ideal for retail, offices, pharmacies and cafés.",
  "shops", shops_body))

# ---------------------------------------------------------------- GALLERY
gal_body = '''
<main>
<section class="hero compact" style="padding:0">
  <img class="hero-bg" src="images/Vision/balcony.jpg" alt="Balcony view at CFT Apartments">
  <div class="wrap hero-inner">
    <div class="frame">
      <span class="eyebrow on-dark">A Look Inside</span>
      <h1 class="page-hero-title">Gallery</h1>
      <p class="page-hero-sub">Explore the apartments, the building and the neighbourhood.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="gallery-filters" role="tablist" aria-label="Gallery categories">
      <button class="active" data-filter="all">All</button>
      <button data-filter="living">Living Room</button>
      <button data-filter="bedroom">Bedroom</button>
      <button data-filter="laundry">Laundry</button>
      <button data-filter="balcony">Balcony</button>
      <button data-filter="exterior">Building Exterior</button>
      <button data-filter="commercial">Commercial Area</button>
    </div>
    <div class="gallery-grid">
      <figure class="g-item reveal" data-cat="living" data-lightbox data-caption="Living room with balcony access"><img src="images/Vision/living-room-1.jpg" alt="Living room with balcony access" loading="lazy"><figcaption>Living room</figcaption></figure>
      <figure class="g-item reveal" data-cat="living" data-lightbox data-caption="Living room and entertainment wall"><img src="images/Vision/living-room-2.jpg" alt="Living room with entertainment unit" loading="lazy"><figcaption>Living room</figcaption></figure>
      <figure class="g-item reveal" data-cat="bedroom" data-lightbox data-caption="Master bedroom"><img src="images/Vision/bedroom-main.jpg" alt="Master bedroom" loading="lazy"><figcaption>Bedroom</figcaption></figure>
      <figure class="g-item reveal" data-cat="bedroom" data-lightbox data-caption="Fitted wardrobes and vanity"><img src="images/Vision/bedroom-wardrobe.jpg" alt="Fitted wardrobes and vanity" loading="lazy"><figcaption>Wardrobes</figcaption></figure>
      <figure class="g-item reveal" data-cat="laundry" data-lightbox data-caption="Washer and dryer"><img src="images/Vision/washer-dryer.jpg" alt="Washer and dryer" loading="lazy"><figcaption>Washer &amp; dryer</figcaption></figure>
      <figure class="g-item reveal" data-cat="balcony" data-lightbox data-caption="Private balcony"><img src="images/Vision/balcony.jpg" alt="Private balcony" loading="lazy"><figcaption>Balcony</figcaption></figure>
      <figure class="g-item reveal" data-cat="exterior" data-lightbox data-caption="Building exterior"><img src="images/Vision/building-exterior.jpg" alt="Building exterior" loading="lazy"><figcaption>Building exterior</figcaption></figure>
      <figure class="g-item reveal" data-cat="exterior" data-lightbox data-caption="The Vision City estate"><img src="images/Vision/vision-city-aerial.jpg" alt="Aerial view of Vision City" loading="lazy"><figcaption>The estate</figcaption></figure>
      <figure class="g-item reveal" data-cat="commercial" data-lightbox data-caption="Commercial frontage — placeholder"><img src="images/Vision/building-exterior.jpg" alt="Commercial area placeholder" loading="lazy"><figcaption>Commercial area · placeholder</figcaption></figure>
    </div>
    <p class="placeholder-note" style="margin-top:2rem">Add kitchen, bathroom and commercial-area photos here as they become available — each image slots into a category above.</p>
  </div>
</section>
</main>'''
write("gallery.html", shell(
  "Gallery | CFT Apartments & Shops, Kigali",
  "Photo gallery of CFT Apartments & Shops — living rooms, bedrooms, balconies, the building and commercial spaces in Kimironko, Kigali.",
  "gallery", gal_body))

# ---------------------------------------------------------------- ABOUT
about_body = '''
<main>
<section class="hero compact" style="padding:0">
  <img class="hero-bg" src="images/Vision/vision-city-aerial.jpg" alt="Vision City estate, Kigali">
  <div class="wrap hero-inner">
    <div class="frame">
      <span class="eyebrow on-dark">Our Story</span>
      <h1 class="page-hero-title">About Us</h1>
      <p class="page-hero-sub">A family business, built on trust.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="reveal">
      <span class="eyebrow">Cyabukombe Family Trading</span>
      <h2>What CFT stands for</h2>
      <p class="lead" style="margin:1rem 0 1.2rem">CFT is <strong>Cyabukombe Family Trading</strong> — a family-owned company providing quality furnished apartments and commercial rental spaces in Kigali, Rwanda.</p>
      <p style="color:var(--ink-60)">Our mixed-use property in Kimironko brings together comfortable homes for guests and residents with practical, secure spaces for businesses. We manage everything ourselves, which means when you stay or rent with CFT, you deal directly with the family that owns and cares for the property — no agents, no run-around, just honest hospitality.</p>
    </div>
    <div class="img-frame reveal"><img src="images/Vision/building-exterior.jpg" alt="The CFT building in Kimironko" loading="lazy"></div>
  </div>
</section>

<section class="bg-sand">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">What Guides Us</span><h2>Our values</h2></div>
    <div class="values-grid">
      <div class="value reveal"><h3>Quality</h3><p>Well-built spaces, quality furnishings and careful upkeep in every unit.</p></div>
      <div class="value reveal"><h3>Comfort</h3><p>Homes that feel like homes — quiet, warm and fully equipped from day one.</p></div>
      <div class="value reveal"><h3>Professionalism</h3><p>Clear terms, quick responses and reliable service, every time.</p></div>
      <div class="value reveal"><h3>Security</h3><p>Gated premises, 24/7 guards and cameras — peace of mind included.</p></div>
      <div class="value reveal"><h3>Customer Satisfaction</h3><p>We measure success by returning guests and thriving tenant businesses.</p></div>
      <div class="value reveal"><h3>Community</h3><p>Proudly part of Kimironko — supporting the neighbourhood we call home.</p></div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <div class="cta-band reveal">
      <span class="eyebrow on-dark center">Karibu · You're welcome here</span>
      <h2>Come see for yourself</h2>
      <p>Book a stay, arrange a viewing or simply say hello — we'd love to hear from you.</p>
      <div class="hero-actions" style="justify-content:center">
        <a class="btn btn-gold" href="booking.html">Book Now</a>
        <a class="btn btn-outline" href="contact.html">Contact Us</a>
      </div>
    </div>
  </div>
</section>
</main>'''
write("about.html", shell(
  "About Us | Cyabukombe Family Trading (CFT), Kigali",
  "CFT — Cyabukombe Family Trading — provides quality furnished apartments and commercial rental spaces in Kimironko, Kigali, Rwanda.",
  "about", about_body))

# ---------------------------------------------------------------- BOOKING
booking_body = f'''
<main>
<section class="hero compact" style="padding:0">
  <img class="hero-bg" src="images/Vision/bedroom-main.jpg" alt="Comfortable bedroom at CFT Apartments">
  <div class="wrap hero-inner">
    <div class="frame">
      <span class="eyebrow on-dark">Direct Booking</span>
      <h1 class="page-hero-title">Book Now</h1>
      <p class="page-hero-sub">Send your dates and we'll confirm availability within hours — usually much sooner.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap" style="max-width:860px">
    <div class="form-card reveal">
      <form data-inquiry novalidate action="{FORMSPREE}" method="POST">
        <input type="hidden" name="_subject" value="CFT website inquiry — Booking">
        <div class="form-grid">
          <div class="field"><label for="b-name">Full Name</label><input id="b-name" name="name" type="text" required autocomplete="name"></div>
          <div class="field"><label for="b-phone">Phone Number</label><input id="b-phone" name="phone" type="tel" required autocomplete="tel"></div>
          <div class="field"><label for="b-wa">WhatsApp</label><input id="b-wa" name="whatsapp" type="tel" placeholder="If different from phone" autocomplete="tel"></div>
          <div class="field"><label for="b-email">Email</label><input id="b-email" name="email" type="email" required autocomplete="email"></div>
          <div class="field full"><label for="b-prop">Property</label>
            <select id="b-prop" name="property" required>
              <option value="">Choose a property…</option>
              <option>Luxury 3BR in Vision City</option>
              <option>Kimironko Garden Residence</option>
              <option>Inganji Apartment 16</option>
              <option>Commercial Shop Space</option>
              <option>Not sure yet — advise me</option>
            </select></div>
          <div class="field"><label for="b-in">Check-in Date</label><input id="b-in" name="checkin" type="date" required></div>
          <div class="field"><label for="b-out">Check-out Date</label><input id="b-out" name="checkout" type="date" required></div>
          <div class="field"><label for="b-guests">Number of Guests</label>
            <select id="b-guests" name="guests"><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option></select></div>
          <div class="field full"><label for="b-msg">Message</label><textarea id="b-msg" name="message" rows="5" placeholder="Anything we should know — arrival time, long-stay interest, special requests…"></textarea></div>
        </div>
        <button class="btn btn-gold" type="submit" style="margin-top:1.5rem">Send Booking Inquiry</button>
      </form>
      <div class="form-success" role="status">Thank you for contacting CFT Apartments &amp; Shops. Your inquiry has been received. Our team will contact you shortly.</div>
      <div class="form-error" role="alert">Sorry, something went wrong sending your message. Please try again, or reach us directly on WhatsApp.</div>
    </div>
  </div>
</section>

<section class="bg-sand tight">
  <div class="wrap">
    <div class="section-head center reveal"><span class="eyebrow center">Good to Know</span><h2>Frequently asked questions</h2></div>
    <div class="faq reveal">
      <details><summary>Can I book directly instead of through Airbnb?</summary><p>Yes — direct bookings are welcome and often more flexible. Send the form above or message us on WhatsApp and we'll confirm availability and payment options.</p></details>
      <details><summary>Do you offer monthly or long-term rates?</summary><p>We do. Both apartments are available for extended stays with discounted monthly rates. Mention your intended duration in the message field.</p></details>
      <details><summary>What time is check-in and check-out?</summary><p>Check-in is after 3:00 PM with smart-lock self check-in at the Vision City apartment. Check-out times are flexible where scheduling allows — just ask.</p></details>
      <details><summary>Is parking really free?</summary><p>Yes — secure parking on the premises is included for apartment guests and shop customers.</p></details>
      <details><summary>Are pets allowed?</summary><p>Unfortunately not — our apartments are pet-free to keep them fresh for every guest.</p></details>
      <details><summary>How do I rent a commercial shop?</summary><p>Select "Commercial Shop Space" in the form above or visit our <a href="shops.html" style="text-decoration:underline">Commercial Shops</a> page, and we'll get back to you with availability, floor plans and terms.</p></details>
    </div>
  </div>
</section>
</main>'''
write("booking.html", shell(
  "Book Now | CFT Apartments & Shops, Kigali",
  "Book a furnished apartment or inquire about commercial space in Kimironko, Kigali. Direct booking with Cyabukombe Family Trading.",
  "booking", booking_body))

# ---------------------------------------------------------------- CONTACT
contact_body = f'''
<main>
<section class="hero compact" style="padding:0">
  <img class="hero-bg" src="images/cft-brand-collage.jpg" alt="CFT Offices, Shops & Apartments — comfort, quality, convenience">
  <div class="wrap hero-inner">
    <div class="frame">
      <span class="eyebrow on-dark">Get in Touch</span>
      <h1 class="page-hero-title">Contact</h1>
      <p class="page-hero-sub">Direct to the family — no agents, no waiting rooms.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap contact-grid">
    <div class="reveal">
      <span class="eyebrow">Reach Us</span>
      <h2 style="margin-bottom:1rem">We reply quickly</h2>
      <ul class="contact-list">
        <li><span class="c-icon">☎</span><div><h3>Phone</h3><p><a href="tel:{PHONE.replace(' ','')}">{PHONE}</a></p></div></li>
        <li><span class="c-icon">✆</span><div><h3>WhatsApp</h3><p><a href="https://wa.me/{WA}" target="_blank" rel="noopener">Message us on WhatsApp</a></p></div></li>
        <li><span class="c-icon">✉</span><div><h3>Email</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div></li>
        <li><span class="c-icon">◆</span><div><h3>Address</h3><p>{ADDRESS_LINE1}<br>{ADDRESS_LINE2}</p></div></li>
        <li><span class="c-icon">🕘</span><div><h3>Business Hours</h3><p>Monday – Saturday: 8:00 AM – 7:00 PM<br>Sunday: 10:00 AM – 5:00 PM<br>Guest support: 24/7 on WhatsApp</p></div></li>
      </ul>
      <div class="socials">
        <a href="#" aria-label="Instagram">IG</a>
        <a href="#" aria-label="Facebook">FB</a>
        <a href="#" aria-label="X / Twitter">X</a>
      </div>
    </div>

    <div class="reveal">
      <div class="form-card">
        <h3 style="margin-bottom:1.2rem">Send an inquiry</h3>
        <form data-inquiry novalidate action="{FORMSPREE}" method="POST">
          <input type="hidden" name="_subject" value="CFT website inquiry — Contact page">
          <div class="form-grid">
            <div class="field"><label for="c-name">Full Name</label><input id="c-name" name="name" type="text" required autocomplete="name"></div>
            <div class="field"><label for="c-phone">Phone / WhatsApp</label><input id="c-phone" name="phone" type="tel" required autocomplete="tel"></div>
            <div class="field full"><label for="c-email">Email</label><input id="c-email" name="email" type="email" required autocomplete="email"></div>
            <div class="field full"><label for="c-topic">I'm interested in</label>
              <select id="c-topic" name="topic"><option>Apartment stay</option><option>Long-term apartment rental</option><option>Commercial shop rental</option><option>Something else</option></select></div>
            <div class="field full"><label for="c-msg">Message</label><textarea id="c-msg" name="message" rows="5" required></textarea></div>
          </div>
          <button class="btn btn-green" type="submit" style="margin-top:1.4rem">Send Message</button>
        </form>
        <div class="form-success" role="status">Thank you for contacting CFT Apartments &amp; Shops. Your inquiry has been received. Our team will contact you shortly.</div>
        <div class="form-error" role="alert">Sorry, something went wrong sending your message. Please try again, or reach us directly on WhatsApp.</div>
      </div>
    </div>
  </div>
</section>

<section class="tight" style="padding-top:0">
  <div class="wrap">
    <div class="map-embed reveal"><iframe src="{MAP}" title="Map of CFT Apartments & Shops, Kimironko, Kigali" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
  </div>
</section>
</main>'''
write("contact.html", shell(
  "Contact | CFT Apartments & Shops, Kimironko Kigali",
  "Contact CFT Apartments & Shops in Kimironko, Kigali — phone, WhatsApp, email and inquiry form. We respond quickly.",
  "contact", contact_body))

print("Build complete.")
