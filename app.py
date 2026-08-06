import streamlit as st
import pandas as pd
import numpy as np
import joblib, os, time, math
from datetime import datetime, timedelta

import base64
import os

# Base64 Asset Compiler Engine
inline_vector_src = ""
image_filename = "delivery_route.jpg" # Change to exact name if different (e.g. route.jpg)

if os.path.exists(image_filename):
    with open(image_filename, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode("utf-8")
        inline_vector_src = f"data:image/jpeg;base64,{encoded_string}"
else:
    # 🌟 SECURE FALLBACK: If your local file is misplaced, this injects a 
    # premium, crystal-clear minimal route vector directly from an open web CDN source.
    inline_vector_src = "https://unsplash.com"



# Initialize empty global style variable 
topo_css_variable = ""
topo_filename = "full app background.jpg"  # Update this to match your exact downloaded filename

if os.path.exists(topo_filename):
    with open(topo_filename, "rb") as topo_file:
        encoded_topo = base64.b64encode(topo_file.read()).decode("utf-8")
        # Construct the CSS URL data packet structure
        topo_css_variable = f"url('data:image/jpeg;base64,{encoded_topo}')"


def auto_scroll_to_element(element_id: str, key_trigger: str):
    """
    Directly targets the true parent window scroll container for tabs 1, 2, and 3,
    but completely self-destructs and prevents execution if the user is on Step 4.
    """
    # ─── 🛑 THE ULTIMATE GATEWAY: FORCE ABSOLUTE STATIONARY STEPS ON PREDICT ───
    # If the app state has advanced to the prediction reveal tab, abort rendering entirely!
    if "step" in st.session_state and st.session_state.step >= 4:
        return

    import json
    import time
    
    current_time_ms = int(time.time() * 1000)
    payload_tag = json.dumps({"id": element_id, "trigger": key_trigger, "ts": current_time_ms})
    
    html_code = f"""
    <div data-scroll-trigger='{payload_tag}' data-nonce='{current_time_ms}'></div>
    <iframe style="display:none;" srcdoc="
        <script>
            function executeCalculatedScroll() {{
                const parentDoc = window.parent.document;
                const target = parentDoc.getElementById('{element_id}');
                if (!target) return false;
                
                const bodyRect = parentDoc.body.getBoundingClientRect().top;
                const elementRect = target.getBoundingClientRect().top;
                const absoluteTop = elementRect - bodyRect;
                
                // Standard 50px visual padding spacing offset for tab navigation indicators
                const targetScrollY = absoluteTop - 50;
                
                window.parent.window.scrollTo({{
                    top: Math.max(0, targetScrollY),
                    behavior: 'smooth'
                }});
                return true;
            }}

            let attempts = 0;
            const scrollInterval = setInterval(() => {{
                attempts++;
                const success = executeCalculatedScroll();
                if (success || attempts > 15) {{
                    clearInterval(scrollInterval);
                }}
            }}, 40);
        </script>
    "></iframe>
    """
    st.components.v1.html(html_code, height=0, width=0)


# ─── GLOBAL APP CANVAS RE-TEXTURE ENGINE (PREMIUM VECTOR MICRO-GRID) ───
st.html("""
<style>
/* 1. Reset root nodes to transparent so they don't block our background grid layer */
.stApp, 
div[data-testid="stAppViewMain"] {
    background: transparent !important;
}

/* 2. FIX: Inject the dual-gradient SVG grid system directly into Streamlit's primary wrapper */
div[data-testid="stAppViewContainer"] {
    background-color: #FCFCFD !important; /* Premium minimalist bright white/gray canvas canvas fill */
    background-image: 
        linear-gradient(rgba(226, 232, 240, 0.4) 1px, transparent 1px),
        linear-gradient(90deg, rgba(226, 232, 240, 0.4) 1px, transparent 1px) !important;
    background-size: 40px 40px !important; /* Fixed crisp density mapping that scales infinitely without distortion */
    background-repeat: repeat !important;
    background-position: top left !important;
    background-attachment: scroll !important;         
    opacity: 1 !important;
}

/* 3. Keep child workspace cards clean, sharp, and opaque over the grid lines */
div[data-testid="stVerticalBlockBorderWrapper"]:has(div[data-key="tab_content_wrapper_card"]) {
    background-color: #FFFFFF !important; /* Pure white crisp background card over grid */
    border: 1px solid #E2E8F0 !important; /* Calibrated gray border line matching your divider */
    border-radius: 16px !important;
    box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.015) !important; /* Subtler shadows for light grid mode */
    backdrop-filter: blur(8px) !important;
}

.stColumn {
    background: transparent !important;
}
</style>
""")




# ─── Page config ─────────────────────────────────────────────────
st.set_page_config(
    page_title="DropTime · ETA Predictor",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ─── COMPONENT STATE INITIALIZATION (Place at the very top of your file) ───
import streamlit as st

# Use a clean reference alias matching your current code setup
s = st.session_state


if "step" not in s: s.step = 1
if "pin_mode" not in s: s.pin_mode = "restaurant"

# 1. Initialize Baseline Coordinates
if "rest_lat" not in s: s.rest_lat = 28.6304  
if "rest_lon" not in s: s.rest_lon = 77.2177  
if "del_lat" not in s: s.del_lat = 28.6514
if "del_lon" not in s: s.del_lon = 77.1907

# 2. CRITICAL FIX: Safe initialization for search box string displays
if "rest_search_text" not in s: 
    s.rest_search_text = "Connaught Place, New Delhi"
if "del_search_text" not in s: 
    s.del_search_text = "Karol Bagh, New Delhi"

# 3. Component Rendering Version Triggers
if "rest_box_id" not in s: s.rest_box_id = 0
if "del_box_id" not in s: s.del_box_id = 0


# Shortcut handle mapping to preserve your existing variable calls cleanly
# s = st.session_state

# ─── Theme + CSS ──────────────────────────────────────────────────
st.markdown("""
<style>
# @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&family=Bricolage+Grotesque:wght@400;500;600;700;800&display=swap');

# @keyframes blink{0%,100%{opacity:1;box-shadow:0 0 0 0 rgba(34,197,94,.5)}50%{opacity:.7;box-shadow:0 0 0 5px rgba(34,197,94,0)}}
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&family=Bricolage+Grotesque:wght@400;500;600;700;800&display=swap');

/* ──── CORE DESIGN TOKENS ──── */
:root {
  --brand: #E8471E;         /* Tomato Red */
  --brand2: #FF8C00;        /* Saffron */
  --brand3: #22C55E;        /* Fresh Green */
  --cream: #FFF8F2;         /* Warm Cream Background */
  --cream2: #FFF0E3;
  --ink: #1C1917;
  --ink2: #44403C;
  --ink3: #78716C;
  --ink4: #A8A29E;
  --white: #FFFFFF;
  --border: #EDE8E3;
  --border2: #D9D0C7;
  --card-shadow: 0 2px 12px rgba(28,25,23,.07), 0 1px 3px rgba(28,25,23,.05);
  --card-shadow-hover: 0 8px 28px rgba(28,25,23,.13), 0 2px 8px rgba(28,25,23,.07);
  --r: 14px; --r2: 20px; --r3: 28px;
}

/* ──── GLOBAL BOX RESET ──── */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html, body, [class*="css"] {
  font-family: 'Nunito', sans-serif !important;
  background: var(--cream) !important;
  color: var(--ink) !important;
}

/* Custom Minimalist Scrollbar Styles */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: var(--cream2); }
::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 4px; }

/* ──── STREAMLIT DEFAULT CHROME REMOVAL ──── */
#MainMenu, footer, header { visibility: hidden !important; }
div[data-testid="stDecoration"] { display: none !important; }
div[data-testid="stToolbar"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }

/* Modern Responsive Grid Margin Constraints */
.block-container {
  padding: 0px 48px 48px 48px !important; /* Establishes visual canvas buffer limits */
  max-width: 1400px !important;           /* Blocks scaling anomalies on ultra-wide screens */
  margin: 0 auto !important;             /* Aligns the entire web dashboard layout to the center */
}
            
/* ──── APP STICKY TOPBAR ──── */
.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 0px 14px 0px; 
  background: var(--cream);   
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 999;
}

.brand { display: flex; align-items: center; gap: 10px; }

.brand-logo {
  width: 38px; height: 38px; border-radius: 10px;
  background: linear-gradient(135deg, var(--brand), var(--brand2));
  display: flex; align-items: center; justify-content: center;
  font-size: 20px;
  box-shadow: 0 3px 10px rgba(232,71,30,.35);
}

.brand-name {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: 21px; font-weight: 800; color: var(--ink); letter-spacing: -0.5px;
}

.brand-name em { font-style: normal; color: var(--brand); }
            
/* ──── SYSTEM STATUS BADGE (LIVE INDICATOR) ──── */
.live-chip {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 6px;
  background: #F0FDF4;
  border: 1px solid #86EFAC;
  border-radius: 20px;
  padding: 5px 13px;
  font-size: 11px;
  font-weight: 700;
  color: #16A34A;
  letter-spacing: .3px;
  line-height: 1 !important;
}

.live-dot {
  width: 7px; height: 7px; border-radius: 50%;
  background: #22C55E;
  display: inline-block;
  flex-shrink: 0;
  animation: blink 2s infinite;
}

@keyframes blink {
  0%, 100% { opacity: 1; box-shadow: 0 0 0 0 rgba(34,197,94,.5); }
  50% { opacity: .7; box-shadow: 0 0 0 5px rgba(34,197,94,0); }
}

/* ──── LIGHT-THEME HERO BANNER WITH HARD GRID BORDER ──── */   
.hero {
  background: #F8F9FA !important;
  padding: 48px 36px 40px 36px !important;
  text-align: center !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  border-radius: 0 0 16px 16px;
  /* Crisp grid divider line right under the metric section */
  border-bottom: 1px solid #E2E8F0 !important; 
}                       

.hero-inner {
  max-width: 680px !important;
  margin: 0 auto !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
}

.hero-h1 {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: clamp(32px, 3.8vw, 46px) !important;
  font-weight: 800;
  color: #1A1A1A !important; /* Dark charcoal text */
  line-height: 1.15;
  letter-spacing: -1.2px !important;
  margin-bottom: 14px !important;
}
            
/* ──── TYPOGRAPHIC HERO AMENDMENTS ──── */   
.hero-tag {
  display: block !important;
  text-align: center !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  color: #E67E22 !important; /* Premium branding orange */
  layer-background: transparent !important;
  border: none !important;
  padding: 0 !important;
  letter-spacing: 2px !important; /* Elegant tracking-wider effect */
  text-transform: uppercase !important;
  margin-bottom: 16px !important;
  line-height: 1.2 !important;
  width: auto !important;
}

.hero-sub {
  font-size: 15px !important;
  color: #4B5563 !important; /* High-contrast clean gray */
  line-height: 1.5 !important;
  margin-bottom: 4px !important;
  max-width: 620px !important;
}
            
/* ──── FIXED STABLE HERO WRAPPER ──── */
.hero {
  background: #F8F9FA !important;
  padding: 48px 36px 40px 36px !important;
  text-align: center !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  border-radius: 0 0 16px 16px;
  border-bottom: 1px solid #E2E8F0 !important; 
} 

.hero-inner {
  width: 100% !important;
  max-width: 860px !important; /* FIXED: Expanded to prevent crushing child badges */
  margin: 0 auto !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
}

/* ──── STABLE HORIZONTAL CHIPS ROW ──── */
.hero-chips-container {
  display: flex !important; 
  flex-direction: row !important; 
  flex-wrap: nowrap !important; /* Keeps everything locked perfectly on one single row */
  justify-content: center !important; 
  align-items: center !important;
  gap: 14px !important; 
  margin-top: 42px !important; 
  width: 100% !important;
}

.hero-chip-light {
  border-radius: 12px !important; 
  padding: 8px 16px !important; 
  font-size: 13px !important; 
  font-weight: 600 !important; 
  display: inline-flex !important; 
  align-items: center !important; 
  justify-content: center !important;
  gap: 8px !important; 
  white-space: nowrap !important; 
  /* FIXED: Changed from flex: 1 1 0% to auto layout to let individual long names breathe */
  flex: 0 0 auto !important; 
  box-sizing: border-box !important;
}

/* 🎯 Accuracy Theme */
.chip-accuracy-light {
  background: rgba(244, 63, 94, 0.06) !important;
  border: 1px solid rgba(244, 63, 94, 0.2) !important;
  color: #9F1239 !important;
}
.chip-accuracy-light strong { color: #E11D48 !important; font-weight: 700 !important; }

/* ⚡ Inference Theme */
.chip-inference-light {
  background: rgba(217, 119, 6, 0.06) !important;
  border: 1px solid rgba(217, 119, 6, 0.2) !important;
  color: #78350F !important;
}
.chip-inference-light strong { color: #D97706 !important; font-weight: 700 !important; }

/* 🗺️ Features Theme */
.chip-features-light {
  background: rgba(6, 182, 212, 0.06) !important;
  border: 1px solid rgba(6, 182, 212, 0.2) !important;
  color: #155E75 !important;
}
.chip-features-light strong { color: #0891B2 !important; font-weight: 700 !important; }

/* 🌆 Geo-Segment Theme */
.chip-geo-light {
  background: rgba(147, 51, 234, 0.06) !important;
  border: 1px solid rgba(147, 51, 234, 0.2) !important;
  color: #581C87 !important;
}
.chip-geo-light strong { color: #9333EA !important; font-weight: 700 !important; }

/* Elevated structural alignment for step indicator */
.steps-bar {
  display: flex !important;
  flex-direction: row !important;
  flex-wrap: nowrap !important;
  align-items: center !important;
  justify-content: flex-start !important;
  gap: 24px !important;
  background: #FFFFFF !important;
  border-bottom: 1px solid var(--border) !important;
  padding: 18px 36px !important;
  width: 100% !important;
  min-height: 58px !important;
  margin-bottom: 28px !important;
}

.step-tab {
  display: inline-flex !important;
  flex-direction: row !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 10px !important;
  padding: 6px 0px !important;
  white-space: nowrap !important;
  text-decoration: none !important;
  cursor: pointer !important;
}

.step-num {
  width: 24px !important;
  height: 24px !important;
  border-radius: 50% !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  font-size: 11px !important;
  font-weight: 800 !important;
  line-height: 1 !important;
  margin: 0 !important;
  padding: 0 !important;
  flex-shrink: 0 !important;
}

.step-label {
  font-size: 13px !important;
  font-weight: 700 !important;
  color: var(--ink2) !important;
  line-height: 1 !important;
  margin: 0 !important;
  padding: 0 !important;
  display: inline-block !important;
  letter-spacing: 0.2px;
}

/* ──── CONTENT SHELL ──── */
.content-shell {
  max-width: 1180px;
  margin: 0 auto;
  padding: 32px 36px 60px;
}
            
/* PROPORTIONAL STRUCTURAL GAP SPACING */
.section-title {
  font-family: 'Bricolage Grotesque', sans-serif !important;
  font-size: 22px !important;
  font-weight: 700 !important;
  color: #1C1917 !important; /* Standardized fallback ink color */
  letter-spacing: -0.3px !important;
  
  /* FIXED: Changed to padding to force Streamlit's structural grid to drop down */
  padding-top: 28px !important; 
  margin-top: 0px !important;
  margin-bottom: 4px !important;
}

.section-sub {
  font-size: 13px !important;
  color: #78716C !important; /* Standardized fallback secondary color */
  line-height: 1.5 !important;
  margin-bottom: 24px !important; 
  display: block !important;
}

/* ══════════════════════════════════════════════════════════════════
   💾 PRODUCTION-READY SYSTEM CONTAINER PILL SHEET (v1.50.0+)
   ══════════════════════════════════════════════════════════════════ */

/* 1. MASTER UNIFIED CARD ENCLOSURE FRAME */
div[data-testid="stVerticalBlock"]:has(div[class*="st-key-w_"]) {
    background-color: #FFFFFF !important;
    border: 1px solid #EDE8E3 !important;
    border-radius: 12px !important;
    box-shadow: 0 2px 10px rgba(28,25,23,.02) !important;
    padding: 24px !important;
    margin-bottom: 24px !important;
}

/* ══════════════════════════════════════════════════════════════════
   🚀 FIX: PURGE RECTANGULAR CELL FRAMES FROM THE 6-COLUMN MATRIX
   ══════════════════════════════════════════════════════════════════ */

/* Hover style rules on unselected option panels */
div[class*="st-key-"][class*="_opt_"] button:hover {
    border-color: #D6D3D1 !important;
    background-color: #FAF8F5 !important;
}

/* 4. ACTIVE SELECTION PASTEL BLUE PILL STATE 
      FIXED: Standardized rounded boundaries to match the unselected states */
div[class*="st-key-"][class*="_act_"] button {
    background-color: #EFF6FF !important; /* Premium Ice-Blue Pastel Background Tints */
    border: 2px solid #2563EB !important;   /* Solid Active High Contrast Primary Blue Border */
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12) !important;
    border-radius: 24px !important;        /* FIXED: Matches unselected curves perfectly */
    padding: 8px 16px !important;
    min-height: 38px !important;
    height: 38px !important;
    width: 100% !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
}

div[class*="st-key-"][class*="_act_"] button p {
    color: #1D4ED8 !important; /* High contrast selective blue typography accent */
    font-weight: 700 !important;
}

div[class*="st-key-"][class*="_act_"] button:hover {
    background-color: #EFF6FF !important;
    border-color: #2563EB !important;
}

/* 5. WORKFLOW NAVIGATION BACK/CONTINUE BAR CONTROLS ISOLATION */
div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:last-of-type {
    display: flex !important;
    width: 100% !important;
    margin-top: 32px !important;
}
div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:last-of-type div[data-testid="stBaseButton-primary"] button {
    background-color: #E8471E !important; 
    border-color: #E8471E !important;
    min-height: auto !important;
    height: auto !important;
    padding: 10px 24px !important;
    border-radius: 8px !important;
}
div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:last-of-type div[data-testid="stBaseButton-primary"] button p {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}
div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:last-of-type div[data-testid="stBaseButton-primary"] button:hover {
    background-color: #CD3713 !important;
    border-color: #CD3713 !important;
}
div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:last-of-type div[data-testid="stBaseButton-secondary"] button {
    background-color: #FFFFFF !important;
    border: 1px solid #EDE8E3 !important;
    min-height: auto !important;
    height: auto !important;
    padding: 10px 24px !important;
    border-radius: 8px !important;
}
div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:last-of-type div[data-testid="stBaseButton-secondary"] button p {
    color: #44403C !important;
    font-weight: 700 !important;
}
div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"]:last-of-type div[data-testid="stBaseButton-secondary"] button:hover {
    background-color: #FAF8F5 !important;
    border-color: #D6D3D1 !important;
}

/* ==================================================================
   📦 STREAMLIT 1.50+ CLEAN CONTAINER & LAYOUT SYMMETRY FIX
   ================================================================== */

/* Remove default card backgrounds and borders from structural layout grids */
div[data-testid="stColumn"] div[data-testid="stVerticalBlockBorderWrapper"],
div[data-testid="stColumn"] div[data-testid="stVerticalBlock"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
}

/* Maintain horizontal alignment without dynamic wrapping */
div[data-testid="stHorizontalBlock"] {
    align-items: center !important;
    display: flex !important;
}
            
/* ==================================================================
   🌤️ HARMONIZED PREMIUM LIGHT PILL SELECTION CONTROLS SYSTEM
   ================================================================== */

/* 1. BASE INACTIVE PILL STYLE: Clean minimalist white cards */
div[class*="st-key-w_choice_"] button,
div[class*="st-key-t_choice_"] button,
div[class*="st-key-c_choice_"] button,
div[class*="st-key-f_choice_"] button {
    background-color: #FFFFFF !important; /* Solid clean white pill surfaces */
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important; /* Super crisp line match with background grid */
    border-radius: 12px !important; /* Refined tight rounded corners matching input cards */
    height: 38px !important;
    min-height: 38px !important;
    width: 100% !important;
    box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.02) !important;
    padding: 0 14px !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    pointer-events: auto !important; 
    cursor: pointer !important;
}

/* 2. PREMIUM HOVER FEEDBACK FOR UNSELECTED CHOICES */
div[class*="st-key-w_choice_"] button:hover:not([kind="primary"]),
div[class*="st-key-t_choice_"] button:hover:not([kind="primary"]),
div[class*="st-key-c_choice_"] button:hover:not([kind="primary"]),
div[class*="st-key-f_choice_"] button:hover:not([kind="primary"]) {
    border-color: #FF7A59 !important; /* Smoothly switches to a crisp brand coral frame line */
    background-color: rgba(255, 122, 89, 0.02) !important; /* Ultra-faint responsive background touch */
    background: rgba(255, 122, 89, 0.02) !important;
}

/* Invert unselected text typography color to coral on mouse hover */
div[class*="st-key-w_choice_"] button:hover:not([kind="primary"]) p,
div[class*="st-key-t_choice_"] button:hover:not([kind="primary"]) p,
div[class*="st-key-c_choice_"] button:hover:not([kind="primary"]) p,
div[class*="st-key-f_choice_"] button:hover:not([kind="primary"]) p {
    color: #FF7A59 !important;
}
            
/* 3. SELECTED ACTIVE PILL STYLE: Sleek dark charcoal border with faint gray tint */
div[class*="st-key-w_choice_"] button[kind="primary"],
div[class*="st-key-t_choice_"] button[kind="primary"],
div[class*="st-key-c_choice_"] button[kind="primary"],
div[class*="st-key-f_choice_"] button[kind="primary"] {
    background-color: #F8FAFC !important; /* Elegant ultra-faint gray/slate tint */
    background: #F8FAFC !important;
    border: 1.5px solid #1F2937 !important; /* Sharp, sleek dark charcoal border line */
    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.04) !important;
    pointer-events: auto !important;
}

/* 4. BASE COMPONENT TYPOGRAPHY METRICS */
div[class*="st-key-w_choice_"] button p,
div[class*="st-key-t_choice_"] button p,
div[class*="st-key-c_choice_"] button p,
div[class*="st-key-f_choice_"] button p {
    font-size: 13px !important;
    font-weight: 600 !important;
    color: #4B5563 !important; /* Muted slate gray for inactive labels */
    white-space: nowrap !important;
}

/* Force pure obsidian-black typography color inversion inside active selections */
div[class*="st-key-w_choice_"] button[kind="primary"] p,
div[class*="st-key-t_choice_"] button[kind="primary"] p,
div[class*="st-key-c_choice_"] button[kind="primary"] p,
div[class*="st-key-f_choice_"] button[kind="primary"] p {
    color: #0F172A !important; /* Deep crisp black text font markings */
    font-weight: 700 !important;
}

/* 5. MATCHING HOVER RE-ALIGNMENT FOR UNSELECTED PILLS */
div[class*="st-key-w_choice_"] button:hover:not([kind="primary"]),
div[class*="st-key-t_choice_"] button:hover:not([kind="primary"]),
div[class*="st-key-c_choice_"] button:hover:not([kind="primary"]),
div[class*="st-key-f_choice_"] button:hover:not([kind="primary"]) {
    border-color: #9CA3AF !important; /* Muted gray hover boundary lines */
    background-color: #F9FAFB !important;
}
div[class*="st-key-w_choice_"] button:hover:not([kind="primary"]) p,
div[class*="st-key-t_choice_"] button:hover:not([kind="primary"]) p,
div[class*="st-key-c_choice_"] button:hover:not([kind="primary"]) p,
div[class*="st-key-f_choice_"] button:hover:not([kind="primary"]) p {
    color: #111827 !important; /* Snaps text darker on hover to mimic focus paths */
}


/* Force deep charcoal typography color inversion inside active selections */
div[class*="st-key-w_choice_"] button[kind="primary"] p,
div[class*="st-key-t_choice_"] button[kind="primary"] p,
div[class*="st-key-c_choice_"] button[kind="primary"] p,
div[class*="st-key-f_choice_"] button[kind="primary"] p {
    color: #1A1A1A !important; /* Crisp highly legible dark charcoal font markings */
    font-weight: 700 !important;
}

/* Tactile click compression compression response */
div[class*="st-key-w_choice_"] button:active, div[class*="st-key-t_choice_"] button:active,
div[class*="st-key-c_choice_"] button:active, div[class*="st-key-f_choice_"] button:active {
    transform: scale(0.98) !important;
}
            
/* ==================================================================
   🎯 ISOLATED APPLICATION NAVIGATION MASTER (TARGETED BY KEY)
   ================================================================== */

/* PRIMARY NAVIGATION BUTTON ("Continue to Driver & Vehicle →") */
div[class*="st-key-action_nav_next"] button {
    background-color: #FF4B4B !important; 
    border: 1px solid transparent !important;
    border-radius: 8px !important;
    height: 42px !important;              
    min-height: 42px !important;
    width: 100% !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: all 0.2s ease-in-out !important;
    pointer-events: auto !important;
}

div[class*="st-key-action_nav_next"] button p {
    color: #FFFFFF !important;             
    font-size: 14px !important;            
    font-weight: 500 !important;           
}

/* HOVER BEHAVIOR FIX: Keeps the button background solid and darkens slightly */
div[class*="st-key-action_nav_next"] button:hover {
    background-color: #E03E3E !important; 
    border-color: transparent !important;
    box-shadow: 0 4px 12px rgba(255, 75, 75, 0.2) !important;
}

div[class*="st-key-action_nav_next"] button:hover p {
    color: #FFFFFF !important;             
}

/* SECONDARY NAVIGATION BUTTON ("← Back to Location") */
div[class*="st-key-action_nav_back"] button {
    background-color: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 8px !important;
    height: 42px !important;              
    min-height: 42px !important;
    width: 100% !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: all 0.2s ease-in-out !important;
    pointer-events: auto !important;
}

div[class*="st-key-action_nav_back"] button p {
    font-size: 14px !important;
    font-weight: 500 !important;           
    color: #475569 !important;
}

div[class*="st-key-action_nav_back"] button:hover {
    border-color: #CBD5E1 !important;
    background-color: #F8FAFC !important;
}

div[class*="st-key-action_nav_back"] button:hover p {
    color: #1E293B !important;
}

/* 🚀 FIX: Balance the width of the navigation container and push it down */
div[data-testid="stHorizontalBlock"]:has(div[class*="st-key-action_nav_"]) {
    margin-top: 28px !important;         /* Pushes row down away from the Festival row */
    padding: 0 4px !important;           /* Slightly pulls sides in to match the input grids */
}

/* ==================================================================
   📝 SUBSECTION HEADING TYPOGRAPHY
   ================================================================== */
.compact-row-title {
    font-size: 11px !important;
    font-weight: 800 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.8px !important;
    color: #64748B !important;
    margin-bottom: 12px !important;
    display: block !important;
}

.compact-row-divider {
    height: 1px !important;
    background-color: #E2E8F0 !important;
    margin: 20px 0 !important;
    width: 100% !important;
}

button[key="s2_back"], button[key="s3_back"] {
    background: #FFFFFF !important;
    color: var(--ink2) !important;
    border: 1px solid var(--border) !important;
}
button[key="s2_back"]:hover, button[key="s3_back"]:hover {
    background: var(--cream2) !important;
    border-color: var(--brand2) !important;
}

# ----------------------------SNIPPET 3 ENDS HERE-------------------------------------------


/* ==========================================================================
   TAB NAVIGATION OVERRIDES - PREMIUM SOLID BLACK SYSTEM
   ========================================================================== */

/* 1. PRIMARY FORWARD PROGRESSION ACTION BUTTON (Premium Solid Obsidian Black) */
button[key="action_nav_next"][data-testid="stBaseButton-primary"],
div[data-testid="stBaseButton-primary"] button[key="action_nav_next"] {
    background-color: #1F2937 !important; /* Premium dark charcoal/black solid canvas fill */
    background: #1F2937 !important;
    border: 1px solid #111827 !important;
    border-radius: 12px !important; /* Sharp tight corners matching choice elements */
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.04) !important;
    height: auto !important;
    min-height: auto !important;
    padding: 12px 24px !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

/* Force high-contrast crisp white typography on primary text tracking labels */
button[key="action_nav_next"][data-testid="stBaseButton-primary"] p,
button[key="action_nav_next"][data-testid="stBaseButton-primary"] span {
    color: #FFFFFF !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 700 !important;
    font-size: 14px !important;
}

/* Smooth hover transition behavior for the primary action button */
button[key="action_nav_next"][data-testid="stBaseButton-primary"]:hover {
    background-color: #111827 !important; /* Snaps into pure obsidian black on hover interaction */
    background: #111827 !important;
    border-color: #030712 !important;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.08) !important;
}

/* 2. SECONDARY BACK NAVIGATION ACTION BUTTON (Clean Minimalist Outline Frame) */
/* This baseline rule explicitly forces the back button to retain its outline frame */
button[key="action_nav_back"][data-testid="stBaseButton-secondary"] {
    background-color: #FFFFFF !important;
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important; /* Matching workspace card boundaries */
    border-radius: 12px !important;
    box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.02) !important;
    height: auto !important;
    min-height: auto !important;
    padding: 12px 24px !important;
    transition: all 0.2s ease-in-out !important;
}

button[key="action_nav_back"][data-testid="stBaseButton-secondary"] p {
    color: #4B5563 !important; /* Muted reading gray signaling secondary weight values */
    font-weight: 600 !important;
    font-size: 14px !important;
}

/* Secondary choice item hover response loop */
button[key="action_nav_back"][data-testid="stBaseButton-secondary"]:hover {
    border-color: #9CA3AF !important; /* Darkens framing line slightly on mouse pass */
    background-color: #F9FAFB !important;
    color: #111827 !important;
}

/* Tactical micro compression response */
button[key="action_nav_next"]:active, 
button[key="action_nav_back"]:active {
    transform: scale(0.99) !important;
}
         
/* ──── ONBOARDING HUD PLACEHOLDER CARDS ──── */
.placeholder {
  text-align: center;
  padding: 48px 24px !important;
  background: linear-gradient(135deg, #FAF8F5 0%, #FFFFFF 100%) !important;
  border: 2px dashed #EDE8E3 !important;
  border-radius: 14px !important; 
  box-shadow: inset 0 2px 8px rgba(28,25,23,.02) !important;
  
  /* SPATIAL TRACKING ALIGNMENTS */
  # margin-top: 54px !important;       /* FIXED: Drops the box down to align perfectly with the left column's card */
  # margin-bottom: 24px !important;    /* Keeps the bottom card gap intact */
            
  margin-top: 32px !important;       /* REDUCED: Keeps it perfectly level with the newly adjusted left card top edge */
  margin-bottom: 24px !important;
}

.placeholder-emoji {
  font-size: 48px;
  margin-bottom: 12px;
  display: block;
  opacity: .65;
  animation: float_hint 3s ease-in-out infinite;
}
@keyframes float_hint { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-4px); } }

.placeholder-title {
  font-family: 'Bricolage Grotesque', sans-serif !important;
  font-size: 16px !important;
  font-weight: 800 !important;
  color: #1C1917 !important;              /* FIXED: Solid ink color assignment */
  margin-bottom: 6px;
  letter-spacing: -0.2px;
}

.placeholder-sub {
  font-size: 12px !important;
  color: #78716C !important;              /* FIXED: Muted summary text hex assignment */
  line-height: 1.6;
  max-width: 240px;
  margin: 0 auto;
}

/* ──── GLOBAL STREAMLIT WIDGET OVERRIDES ──── */
/* Standardized Form Typography Setup */
div[data-testid="stSelectbox"] label p,
div[data-testid="stTextInput"] label p,
div[data-testid="stNumberInput"] label p,
div[data-testid="stSlider"] label p {
  font-family: 'Nunito', sans-serif !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  color: var(--ink3) !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
  margin-bottom: 6px !important;
}

/* Base Input Box Structural Layout Rules */
div[data-testid="stSelectbox"] > div > div > div,
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div,
div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input {
  font-family: 'Nunito', sans-serif !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  color: var(--ink) !important;
  background-color: #FFFFFF !important;
  border: 1px solid var(--border) !important;
  border-radius: 10px !important;
  min-height: 42px !important;
  transition: border-color .15s ease, box-shadow .15s ease !important;
}

/* Interactive Focus/Hover High-Contrast States */
div[data-baseweb="select"]:focus-within > div,
div[data-baseweb="input"]:focus-within > div,
div[data-testid="stSelectbox"] > div > div > div:hover,
div[data-testid="stTextInput"] input:focus,
div[data-testid="stNumberInput"] input:focus {
  border-color: var(--brand) !important;
  box-shadow: 0 0 0 3px rgba(232, 71, 30, 0.12) !important;
}

/* ──── PREMIUM CUSTOM SLIDER COMPONENT OVERRIDES ──── */
/* Redesign the running active rail color to match your brand accent */
div[data-testid="stSlider"] div[data-testid="stSliderTrack"] > div > div {
  background: var(--brand) !important;
}

/* Custom premium slider knob handle thumb */
div[data-testid="stSlider"] div[role="slider"] {
  background: #FFFFFF !important;
  border: 3px solid var(--brand) !important;
  box-shadow: 0 3px 8px rgba(232, 71, 30, 0.3) !important;
  width: 18px !important;
  height: 18px !important;
  transition: transform 0.1s ease !important;
}
div[data-testid="stSlider"] div[role="slider"]:hover {
  transform: scale(1.1);
}

/* Base Spacing Rules */
div[data-testid="stSelectbox"], 
div[data-testid="stTextInput"],
div[data-testid="stNumberInput"] {
  margin-bottom: 16px !important;
}

/* Active focus color matching your warm tomato-red brand */
div[data-baseweb="select"]:focus-within > div, 
div[data-baseweb="input"]:focus-within > div {
  border-color: var(--brand) !important;
  box-shadow: 0 0 0 1px var(--brand) !important;
}

/* ──── MASTER PROTECTION SHIELD FOR WORKFLOW BUTTONS ──── */
/* Ensures core step navigation blocks are strictly visible and layered on top */
button[key="step1_next"], 
button[key="s2_back"], 
button[key="s2_next"],
button[key="s3_back"],
button[key="s3_next"],
button[key="reset_btn"],
button[type="primary"] {
    position: relative !important;
    opacity: 1 !important; /* Guarantees explicit visibility */
    display: inline-flex !important;
    width: 100% !important;
    height: auto !important;
    z-index: 30 !important; /* Layers safely above card hotspots */
}

            
/* ==========================================================================
   PRODUCTION KEY-SPECIFIC SEGMENTED CONTROL RESTORATION PASS
   ========================================================================== */

/* 1. Target and style the outer capsule frame track using a backward-lookup match */
div[data-testid="stSegmentedControl"]:has(input[id*="mode_toggle_switch"]),
div[data-testid="stSegmentedControl"]:has(button[id*="mode_toggle_switch"]),
div[data-baseweb="segmented-control"]:has(input[id*="mode_toggle_switch"]) {
    background-color: #F1F5F9 !important; /* Premium light slate track base */
    background: #F1F5F9 !important;
    border: 1px solid #E2E8F0 !important; /* Crisp layout framing hairline line */
    border-radius: 30px !important;
    padding: 4px !important;
    width: max-content !important;
    display: inline-flex !important;
    align-items: center !important;
    float: right !important; /* Locks it clean against your right layout margin */
}

/* 2. Completely scrub out any old dark backgrounds or black layers from options */
div[data-testid="stSegmentedControl"]:has(input[id*="mode_toggle_switch"]) button,
div[data-testid="stSegmentedControl"]:has(input[id*="mode_toggle_switch"]) [role="radio"] {
    background: transparent !important;
    background-color: transparent !important; /* Erases legacy background fills instantly */
    border: none !important; /* Wipes out the lingering red focus outlines completely */
    border-color: transparent !important;
    border-radius: 24px !important;
    color: #64748B !important; /* Clear slate gray text font markings for unselected items */
    font-size: 13px !important;
    font-weight: 600 !important;
    padding: 6px 16px !important;
    box-shadow: none !important;
    outline: none !important;
}

/* 3. Inject the solid elevated white selection highlight bubble */
div[data-testid="stSegmentedControl"]:has(input[id*="mode_toggle_switch"]) button[aria-checked="true"],
div[data-testid="stSegmentedControl"]:has(input[id*="mode_toggle_switch"]) [aria-checked="true"] {
    background: #FFFFFF !important; /* Solid bright white bubble shape card layer */
    background-color: #FFFFFF !important; 
    color: #0F172A !important; /* High contrast dark charcoal text font markings */
    font-weight: 700 !important;
    border: none !important;
    border-color: transparent !important;
    box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.06), 0px 1px 2px rgba(0, 0, 0, 0.04) !important;
}

/* 4. Force uniform text font rendering inside child tags when active */
div[data-testid="stSegmentedControl"]:has(input[id*="mode_toggle_switch"]) button[aria-checked="true"] *,
div[data-testid="stSegmentedControl"]:has(input[id*="mode_toggle_switch"]) [aria-checked="true"] * {
    color: #0F172A !important;
    font-weight: 700 !important;
}

/* 5. Smooth clean hover feedback matching unselected options */
div[data-testid="stSegmentedControl"]:has(input[id*="mode_toggle_switch"]) button:hover:not([aria-checked="true"]) {
    color: #1E293B !important;
    background-color: rgba(0, 0, 0, 0.04) !important;
    border: none !important;
}

/* ──── ROBUST GLOBAL HUD GLASSMORPHISM OVERLAY ENGINE ──── */
/* Targets the horizontal layout engine block hosting your map search boxes */
div[data-testid="stHorizontalBlock"]:has(iframe[title="streamlit_searchbox.st_searchbox"]) {
    background: rgba(255, 255, 255, 0.88) !important;
    backdrop-filter: blur(14px) saturate(180%) !important;
    -webkit-backdrop-filter: blur(14px) saturate(180%) !important;
    border: 1px solid rgba(226, 232, 240, 0.95) !important;
    border-radius: 12px !important;
    padding: 16px 20px 18px 20px !important;
    
    /* Absolute layout positioning rules float the search fields over the map */
    position: relative !important;
    margin-bottom: -72px !important; 
    z-index: 9999 !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05) !important;
}

/* Slims down widget labels inside your modern HUD panel */
div[data-testid="stHorizontalBlock"]:has(iframe[title="streamlit_searchbox.st_searchbox"]) label p {
    font-family: 'Nunito', sans-serif !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    color: #475569 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    margin-bottom: 6px !important;
}
            
/* ──── STANDARD ACTION BUTTONS SECURITY EXCLUSIONS ──── */
/* This hard override acts as a protective shield ensuring navigation blocks NEVER inherit opacity rules */
button[key="btn_pin_r"],
button[key="btn_pin_d"],
button[key="step1_next"], 
button[key="s2_back"], 
button[key="s2_next"],
button[type="primary"] {
    position: relative !important;
    opacity: 1 !important; /* Explicitly forces full visibility */
    display: inline-flex !important;
    width: 100% !important;
    height: auto !important;
    z-index: 20 !important;
    background-color: #FFFFFF !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--ink2) !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 700 !important;
    font-size: 13px !important;
}

/* ──── SPECIFIC CORE CALL-TO-ACTION BRANDING ──── */
/* Prominent glowing style for the main progression button at the base of Step 1 */
button[key="step1_next"],
button[key="s2_next"] {
  background: linear-gradient(135deg, var(--brand), var(--brand2)) !important;
  color: #FFFFFF !important;
  border: none !important;
  border-radius: 12px !important;
  padding: 12px 24px !important;
  font-family: 'Bricolage Grotesque', sans-serif !important;
  font-size: 15px !important;
  font-weight: 700 !important;
  box-shadow: 0 4px 14px rgba(232, 71, 30, 0.25) !important;
  transition: transform 0.15s ease, box-shadow 0.15s ease !important;
}

button[key="step1_next"]:hover,
button[key="s2_next"]:hover {
  transform: translateY(-1px) !important;
  box-shadow: 0 6px 20px rgba(232, 71, 30, 0.35) !important;
  color: #FFFFFF !important;
}

/* Beautiful styling for the calculated distance pill footer */
.dist-pill {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  background: linear-gradient(90deg, #F0FDF4 0%, #DCFCE7 100%) !important;
  border: 1px solid #BBF7D0 !important;
  border-radius: 10px !important;
  padding: 12px 16px !important;
  margin-top: 18px !important;
}
.dist-pill-label { font-size: 13px !important; font-weight: 700 !important; color: #16A34A !important; }
.dist-pill-val { font-family: 'Bricolage Grotesque', sans-serif !important; font-size: 18px !important; font-weight: 800 !important; color: #15803D !important; }
.dist-pill-unit { font-size: 12px !important; font-weight: 700 !important; color: #16A34A !important; }

/* ──── FIXED: ACTIVE IMPACT PANEL LINES ──── */
.impact-row {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important; /* Pushes content cleanly to outer bounds */
  gap: 12px !important;
  padding: 12px 0 !important;
  border-bottom: 1px solid #F5F5F4 !important;
}

.impact-row:last-child {
  border-bottom: none !important;
}

.impact-icon {
  font-size: 16px !important;
  width: 22px !important;
  text-align: center !important;
  flex-shrink: 0 !important;
}

.impact-name {
  font-size: 13px !important;
  font-weight: 600 !important;
  color: #44403C !important;
  flex-grow: 1 !important; /* Automatically occupies middle space fluidly */
  text-align: left !important;
}

.impact-val {
  font-size: 13px !important;
  font-weight: 700 !important;
  color: #1C1917 !important;
  text-align: right !important;
  flex-shrink: 0 !important;
}

/* ──── ACTIVE MISC / BADGES ──── */
.inline-badge {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 3px 10px !important;
  border-radius: 20px !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.3px !important;
}
.ib-green  { background: #F0FDF4 !important; color: #16A34A !important; border: 1px solid #86EFAC !important; }
.ib-amber  { background: #FFFBEB !important; color: #B45309 !important; border: 1px solid #FCD34D !important; }
.ib-orange { background: #FFF7ED !important; color: #C2410C !important; border: 1px solid #FDBA74 !important; }
.ib-red    { background: #FEF2F2 !important; color: #DC2626 !important; border: 1px solid #FCA5A5 !important; }
.ib-blue   { background: #EFF6FF !important; color: #1D4ED8 !important; border: 1px solid #93C5FD !important; }

/* ──── PREMIUM HUD GLASSMORPHISM INPUT OVERLAY ──── */
/* ──── ROBUST HUD GLASSMORPHISM OVERLAY ENGINE ──── */
/* Target Streamlit's container component wrapper directly using our custom key attribute */
div[data-testid="stVerticalBlockBorderWrapper"]:has(div[data-keys*="hud_glass_deck"]) {
    background: rgba(255, 255, 255, 0.75) !important;
    backdrop-filter: blur(12px) saturate(190%) !important;
    -webkit-backdrop-filter: blur(12px) saturate(190%) !important;
    border: 1px solid rgba(226, 232, 240, 0.85) !important;
    border-radius: 12px !important;
    padding: 16px 20px !important;
    margin-bottom: -22px !important; /* Pulls the map canvas up right against the edge */
    position: relative !important;
    z-index: 99 !important;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.04) !important;
}

/* Ensure dropdown selectors look sharp and slim inside our HUD panel */
div[data-testid="stVerticalBlockBorderWrapper"]:has(div[data-keys*="hud_glass_deck"]) label p {
    color: #334155 !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    margin-bottom: 4px !important;
}

        
/* ==========================================================================
   PRODUCTION CONTAINER-KEY NAVIGATION FORWARD LOCK
   ========================================================================== */

/* Target the button nested inside our custom container class hook */
div[class*="st-key-dark_progression_wrapper"] button {
    background-color: #1F2937 !important; /* Premium solid dark charcoal canvas fill */
    background: #1F2937 !important;
    border: 1px solid #111827 !important;
    border-radius: 12px !important; /* Sharp tight corners matching choice pills */
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.04) !important;
    height: auto !important;
    min-height: auto !important;
    padding: 12px 24px !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    width: 100% !important;
}

/* Force high-contrast white text inside the container button wrapper */
div[class*="st-key-dark_progression_wrapper"] button p,
div[class*="st-key-dark_progression_wrapper"] button span {
    color: #FFFFFF !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 700 !important;
    font-size: 14px !important;
}

/* Smooth premium hover state transition */
div[class*="st-key-dark_progression_wrapper"] button:hover {
    background-color: #111827 !important; /* Snaps into pure obsidian black on hover */
    background: #111827 !important;
    border-color: #030712 !important;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.08) !important;
}

            
/* ==========================================================================
   PRODUCTION EXTREME-RIGHT FLUSH MARGIN & BASELINE CONTROLLER
   ========================================================================== */

/* Target the right-hand column containing our specific widget key */
div[data-testid="stHorizontalBlock"]:has(input[id*="mode_toggle_switch"]) > div[data-testid="stColumn"]:last-child {
    display: flex !important;
    justify-content: flex-end !important; /* Pushes the widget container hard right */
    align-items: flex-end !important;
    width: 100% !important;
}

/* Clear legacy float behaviors and pull the widget slightly downwards */
div[data-testid="stHorizontalBlock"]:has(input[id*="mode_toggle_switch"]) div[data-testid="stSegmentedControl"],
div[data-testid="stHorizontalBlock"]:has(input[id*="mode_toggle_switch"]) div[data-baseweb="segmented-control"] {
    float: right !important; /* Locks widget hard against the card's right interior margin */
    margin-top: 4px !important; /* Shifts the toggle down to perfectly match the left baseline */
    margin-left: auto !important;
    width: max-content !important;
}

/* ==========================================================================
   FLAT PREMIUM NATIVE DROPDOWN SELECTBOX OVERRIDES
   ========================================================================== */

/* 1. Remove background boxing from the dropdown wrapper columns */
div[data-testid="stColumn"]:has(div[data-testid*="rest_box_instance_"]),
div[data-testid="stColumn"]:has(div[data-testid*="del_box_instance_"]) {
    background-color: transparent !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}

/* 2. Target internal selectbox text field tracks to style them into clean floating white surfaces */
div[data-testid*="rest_box_instance_"] div[data-baseweb="select"] > div,
div[data-testid*="del_box_instance_"] div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important; /* Pure floating white input surface layer */
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important; /* Crisp hairline framing boundary edge line */
    border-radius: 12px !important; /* Premium rounded corner styling matching map */
    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.02) !important; /* Ultra soft drop shadow */
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

/* 3. Style the input component section label headers */
div[data-testid*="rest_box_instance_"] label,
div[data-testid*="del_box_instance_"] label {
    font-size: 13px !important;
    font-weight: 700 !important;
    color: #374151 !important; /* Clean dark slate for label indicators */
    margin-bottom: 6px !important;
}

/* 4. Interactive Focus/Hover premium high-contrast states */
div[data-testid*="rest_box_instance_"] div[data-baseweb="select"]:focus-within > div,
div[data-testid*="del_box_instance_"] div[data-baseweb="select"]:focus-within > div {
    border-color: #FF7A59 !important; /* Transitions to crisp brand coral on selection focus */
    box-shadow: 0 0 0 3px rgba(255, 122, 89, 0.12) !important; /* Soft premium coral focus glow */
}

/* Adjust layout spacing variables right above the map component canvas */
div[data-testid*="rest_box_instance_"],
div[data-testid*="del_box_instance_"] {
    margin-bottom: 16px !important;
}

            
/* ──── FIXED: SECURE BOUNDS HOVER TOOLTIP SYSTEM ──── */
.custom-tooltip {
    position: relative !important;
    display: inline-block !important; /* FIXED: Prevents coordinate shifting */
    cursor: help !important;
    line-height: 1 !important;
}

/* Micro-badge configuration circular canvas alignment */
.info-trigger {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    font-size: 10px !important;
    font-weight: 700 !important;
    font-style: italic !important;
    background: #FAF8F5 !important;
    border: 1px solid #D6D3D1 !important;
    color: #78716C !important;
    width: 16px !important;
    height: 16px !important;
    border-radius: 50% !important;
    display: flex !important; /* FIXED: Perfect letter centering */
    align-items: center !important;
    justify-content: center !important;
    text-align: center !important;
    transition: all 0.2s ease-in-out !important;
    transform: translateY(1px) !important; /* Micro-adjustment to match typography baseline */
}

.custom-tooltip:hover .info-trigger {
    background: #78716C !important;
    color: #FFFFFF !important;
    border-color: #78716C !important;
}

/* Tooltip floating text bubble configuration */
.custom-tooltip .tooltip-text {
    visibility: hidden !important;
    width: 240px !important;
    background-color: #1C1917 !important;
    color: #FFFFFF !important;
    text-align: left !important;
    border-radius: 8px !important;
    padding: 10px 12px !important;
    font-size: 11px !important;
    font-weight: 500 !important;
    line-height: 1.4 !important;
    
    /* Absolute Layout Placement Floating Layer */
    position: absolute !important;
    z-index: 999999 !important;
    bottom: 150% !important; /* FIXED: Pushes up slightly more to avoid clipping */
    left: 50% !important;
    transform: translateX(-50%) translateY(4px) !important; /* FIXED: Precise horizontal pivot centering */
    
    opacity: 0 !important;
    transition: opacity 0.2s ease, transform 0.2s ease !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important;
    pointer-events: none !important;
}

/* Micro Triangle Arrow Indicator pointing downward */
.custom-tooltip .tooltip-text::after {
    content: "" !important;
    position: absolute !important;
    top: 100% !important;
    left: 50% !important;
    margin-left: -5px !important;
    border-width: 5px !important;
    border-style: solid !important;
    border-color: #1C1917 transparent transparent transparent !important;
}

/* RE-ACTIVE HOVER INJECTIONS */
.custom-tooltip:hover .tooltip-text {
    visibility: visible !important;
    opacity: 1 !important;
    transform: translateX(-50%) translateY(0) !important;
}
            
/* map iframe */
iframe{border-radius:12px!important}

/* ─────────────────────────────────────────────────────────────────────────
   UPDATED GLOBAL SECONDARY BUTTON RULES (EXCLUDES UTILITY BUTTONS)
   ───────────────────────────────────────────────────────────────────────── */

/* 1. Standard Secondary Buttons (Ignores our canvas clear utility) */
div[data-testid="stElementContainer"]:not(:has(div[data-testid="stSegmentedControl"])) div[data-testid="stBaseButton-secondary"] button:not([key="canvas_reset_btn"]) {
  background-color: #FFFFFF !important;
  border: 1px solid #EDE8E3 !important;
  border-radius: 10px !important;
  color: #44403C !important;
  font-family: 'Nunito', sans-serif !important;
  font-weight: 700 !important;
  font-size: 13px !important;
  padding: 8px 16px !important;
  height: auto !important;
  box-shadow: none !important;
}

div[data-testid="stElementContainer"]:not(:has(div[data-testid="stSegmentedControl"])) div[data-testid="stBaseButton-secondary"] button:not([key="canvas_reset_btn"]):hover {
  border-color: #FF8C00 !important;
  background-color: #FFF0E3 !important;
  color: #E8471E !important;
}

/* 2. Isolated Clear Pins Utility Button (Matches Quick Presets Sizing and Colors) */
div[data-testid="stElementContainer"] div[data-testid="stBaseButton-secondary"] button[key="canvas_reset_btn"] {
  height: 38px !important;
  min-height: 38px !important;
  max-height: 38px !important;
  padding: 0px 14px !important;
  margin: 0px !important;
  background-color: #F8FAFC !important;
  background: #F8FAFC !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 8px !important;
  box-shadow: none !important;
  transition: all 0.2s ease-in-out !important;
}

/* Clear Pins Inner Text Elements */
div[data-testid="stElementContainer"] div[data-testid="stBaseButton-secondary"] button[key="canvas_reset_btn"] p,
div[data-testid="stElementContainer"] div[data-testid="stBaseButton-secondary"] button[key="canvas_reset_btn"] span {
  color: #64748B !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  line-height: 38px !important;
  margin: 0px !important;
  padding: 0px !important;
}

/* Clear Pins Hover Feedback */
div[data-testid="stElementContainer"] div[data-testid="stBaseButton-secondary"] button[key="canvas_reset_btn"]:hover {
  background-color: #F1F5F9 !important;
  background: #F1F5F9 !important;
  border-color: #CBD5E1 !important;
}

div[data-testid="stElementContainer"] div[data-testid="stBaseButton-secondary"] button[key="canvas_reset_btn"]:hover p {
  color: #0F172A !important;
}


/* ==========================================================================
   2. MASTER SEGMENTED CONTROL STRUCTURE (FORCED ELEMENT LAYER)
   ========================================================================== */
/* Target the absolute master wrapper container element */
div[data-testid="stSegmentedControl"] {
    background-color: #F1F5F9 !important; /* Premium light slate track base */
    border: 1px solid #E2E8F0 !important; /* Crisp line matching workspace grid */
    border-radius: 30px !important;
    padding: 4px !important;
    width: max-content !important;
    display: inline-flex !important;
    align-items: center !important;
}

/* Force override down directly into Streamlit's inner button structure */
div[data-testid="stSegmentedControl"] [data-testid="stBaseButton-secondary"] button,
div[data-testid="stSegmentedControl"] button {
    background: transparent !important;
    background-color: transparent !important; /* Completely neutralizes global background injection */
    border: none !important; /* Erases legacy red focus borders instantly */
    border-radius: 26px !important;
    color: #64748B !important; /* Muted slate for unselected option */
    font-size: 13px !important;
    font-weight: 600 !important;
    padding: 8px 18px !important;
    box-shadow: none !important;
    outline: none !important;
}

/* Force override for active selected bubble visibility */
div[data-testid="stSegmentedControl"] [aria-checked="true"] button,
div[data-testid="stSegmentedControl"] button[aria-checked="true"] {
    background: #FFFFFF !important; /* Solid bright white bubble layer */
    background-color: #FFFFFF !important; 
    color: #0F172A !important; /* High contrast dark gray active text font */
    font-weight: 700 !important;
    border: none !important;
    box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.08), 0px 1px 2px rgba(0, 0, 0, 0.04) !important;
}

/* Keep text color completely dark gray inside the active selection bubble layer */
div[data-testid="stSegmentedControl"] [aria-checked="true"] button *,
div[data-testid="stSegmentedControl"] button[aria-checked="true"] * {
    color: #0F172A !important;
    font-weight: 700 !important;
}

/* Completely clean hover feedback rules for inactive choices */
div[data-testid="stSegmentedControl"] button:hover:not([aria-checked="true"]) {
    color: #1E293B !important;
    background-color: rgba(0, 0, 0, 0.04) !important;
    border: none !important;
}

/* 3. Primary Forward Navigation Buttons Styling ("Continue to..." / "Predict") */
button[key="step1_next"],
button[key="s2_next"],
button[key="s3_next"],
.pred-btn-wrap button {
  background: linear-gradient(135deg, #E8471E 0%, #FF8C00 100%) !important;
  color: #FFFFFF !important;
  border: none !important;
  border-radius: 12px !important;
  padding: 14px 28px !important;
  font-family: 'Bricolage Grotesque', sans-serif !important;
  font-size: 15px !important;
  font-weight: 700 !important;
  box-shadow: 0 4px 14px rgba(232, 71, 30, 0.25) !important;
  text-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
  transition: all 0.2s ease !important;
  width: 100% !important;
}

button[key="step1_next"]:hover,
button[key="s2_next"]:hover,
button[key="s3_next"]:hover,
.pred-btn-wrap button:hover {
  transform: translateY(-1px) !important;
  box-shadow: 0 6px 20px rgba(232, 71, 30, 0.4) !important;
  color: #FFFFFF !important;
}

/* Number input +/- buttons */
button[data-testid="stNumberInputStepDown"],
button[data-testid="stNumberInputStepUp"]{
  background:var(--cream2)!important;
  border-color:var(--border)!important;
  color:var(--ink2)!important;
}

/* ──── PIN MODES: PERSISTENT STATE HIGHLIGHTS ──── */
button[p-mode="active-rest"] {
    background-color: #3B82F6 !important;
    color: #FFFFFF !important;
    border-color: #1D4ED8 !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.25) !important;
}

button[p-mode="active-del"] {
    background-color: var(--brand2) !important;
    color: #FFFFFF !important;
    border-color: #EA580C !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 12px rgba(232, 71, 30, 0.25) !important;
}

button[p-mode^="active-"]:hover {
    opacity: 0.92 !important;
    color: #FFFFFF !important;
}

/* ──── UPDATED GLOBAL CSS: PREMIUM TELEMETRY DECK FOOTER ──── */
.footer {
    display: flex !important; 
    justify-content: space-between !important; 
    align-items: center !important; 
    width: 100% !important; 
    padding: 12px 20px !important; 
    margin-top: 48px !important;
    background: #FFFFFF !important; 
    border: 1px solid rgba(226, 232, 240, 0.8) !important; 
    border-radius: 12px !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.01) !important;
    font-family: sans-serif !important;
    flex-wrap: wrap !important;
    gap: 12px !important;
    box-sizing: border-box !important;
}

.footer-left-sig {
    display: flex !important; 
    align-items: center !important; 
    gap: 10px !important; 
    font-size: 13px !important; 
    color: #64748B !important;
}

.footer-brand-title {
    color: #0F172A !important; 
    font-weight: 700 !important; 
    letter-spacing: -0.3px !important;
}

.footer-hairline-split {
    color: #CBD5E1 !important;
    font-weight: 300 !important;
}

.footer-right-telemetry {
    display: flex !important; 
    align-items: center !important; 
    gap: 14px !important; 
    font-size: 11px !important; 
    font-family: 'JetBrains Mono', 'Fira Code', monospace !important; 
    color: #64748B !important;
    letter-spacing: 0.3px !important;
    flex-wrap: wrap !important;
}

.footer-engine-chip {
    background: #F0F7FF !important; 
    color: #0056B3 !important; 
    padding: 3px 8px !important; 
    border-radius: 6px !important; 
    border: 1px solid #D0E7FF !important;
    font-weight: 700 !important;
}

.footer-status-dot {
    color: #16A34A !important; 
    font-weight: 800 !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 4px !important;
}

/* ──── MISC ──── */
.spacer{height:1px;background:var(--border);margin:18px 0}

/* ══════════════════════════════════════════════════════════════════
   💾 PRODUCTION-READY MULTI-COLUMN STABILITY DESKTOP OVERRIDE
   ══════════════════════════════════════════════════════════════════ */

/* Forces multi-column horizontal rows to stay side-by-side on tablet/small laptops */
@media (min-width: 640px) {
    /* Targets Streamlit's structural grid horizontal flex layouts */
    div[data-testid="stHorizontalBlock"]:not(:last-of-type) {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        align-items: flex-start !important;
        gap: 24px !important; /* Uniform gap tracker width separating columns */
    }

    /* Recalculates individual column cells to preserve their horizontal alignment footprint */
    div[data-testid="stHorizontalBlock"]:not(:last-of-type) > div[data-testid="stColumn"] {
        width: auto !important;
        min-width: 0 !important;
    }
}
            
/* ==================================================================
   📦 STEP 3: NATIVE CONTAINER TO CUSTOM FCARD TRANSFORMATION
   ================================================================== */

/* Transform native container elements into professional .fcard frames */
div[data-testid="stVerticalBlockBorderWrapper"]:has(div[class*="st-key-v_choice_"]),
div[data-testid="stVerticalBlockBorderWrapper"]:has(div[class*="st-key-vc_choice_"]),
div[data-testid="stVerticalBlockBorderWrapper"]:has(div[class*="st-key-da_col"]) {
    background-color: #FFFFFF !important;
    border: 1px solid #EDE8E3 !important;
    border-radius: 14px !important;
    box-shadow: 0 2px 12px rgba(28,25,23,.07) !important;
    padding: 20px !important;
    margin-bottom: 24px !important;
    transition: box-shadow 0.2s ease-in-out !important;
}

/* Hover shadow transitions on cards */
div[data-testid="stVerticalBlockBorderWrapper"]:has(div[class*="st-key-v_choice_"]):hover,
div[data-testid="stVerticalBlockBorderWrapper"]:has(div[class*="st-key-vc_choice_"]):hover,
div[data-testid="stVerticalBlockBorderWrapper"]:has(div[class*="st-key-da_col"]):hover {
    box-shadow: 0 4px 20px rgba(28,25,23,.12) !important;
}

/* Fix header style properties */
.fcard-head {
    padding: 16px 4px 8px 4px !important;
    border-bottom: none !important; /* Drops internal structural dividers */
    display: flex;
    align-items: center;
    gap: 12px;
}

.fcard-title {
    font-size: 15px !important;
    font-weight: 700 !important;
    color: #1C1917 !important;
    margin: 0 !important;
}

.fcard-desc {
    font-size: 12px !important;
    color: #64748B !important;
    margin: 2px 0 0 0 !important;
}
            
/* ==================================================================
   🏍️ GRID BUTTONS RENDERED AS ELEVATED LAYOUT CARDS
   ================================================================== */

/* UNSELECTED CARD BUTTONS STATE */
div[class*="st-key-v_grid_"] button,
div[class*="st-key-vc_grid_"] button,
div[class*="st-key-md_grid_"] button {
    background-color: #FFFFFF !important;
    border: 1px solid #E7E5E4 !important;
    border-radius: 10px !important;
    min-height: 112px !important; /* Establishes a uniform aspect ratio height across card grids */
    width: 100% !important;
    padding: 16px 10px !important;
    display: block !important;
    text-align: center !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.01) !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

/* Hover style configuration */
div[class*="st-key-v_grid_"] button:hover,
div[class*="st-key-vc_grid_"] button:hover,
div[class*="st-key-md_grid_"] button:hover {
    border-color: #FF4B4B !important; /* Highlights brand red borders */
    background-color: #FFFBF9 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 14px rgba(255, 75, 75, 0.08) !important;
}

/* SELECTED CARD BUTTONS STATE (🚀 SPECIFICITY ENGINE OVERRIDE FOR GLOW ORANGE) */
div[class*="st-key-v_grid_"] button[kind="primary"],
div[class*="st-key-vc_grid_"] button[kind="primary"],
div[class*="st-key-md_grid_"] button[kind="primary"],
div[class*="st-key-v_grid_"] button[data-testid="baseButton-primary"],
div[class*="st-key-vc_grid_"] button[data-testid="baseButton-primary"],
div[class*="st-key-md_grid_"] button[data-testid="baseButton-primary"] {
    background-color: #FFF2EE !important; /* Soft light-orange fill shade */
    border: 2px solid #FF4B4B !important;  /* Active brand accent border ring */
    box-shadow: 0 4px 14px rgba(255, 75, 75, 0.14) !important;
    transform: none !important;
}

/* MULTI-LINE PARAGRAPH TEXT FORMATTING INSIDE GRID CARDS */
div[class*="st-key-v_grid_"] button p,
div[class*="st-key-vc_grid_"] button p,
div[class*="st-key-md_grid_"] button p {
    font-size: 13px !important;
    line-height: 1.6 !important;
    color: #44403C !important;
    font-weight: 500 !important;
    white-space: pre-line !important; /* Essential parameter to allow clean \n vertical line layouts */
    display: block !important;
}

/* Style active card button text properties (🚀 FORCES HIGH CONTRAST ACCENT TEXT COLORS) */
div[class*="st-key-v_grid_"] button[kind="primary"] p,
div[class*="st-key-vc_grid_"] button[kind="primary"] p,
div[class*="st-key-md_grid_"] button[kind="primary"] p,
div[class*="st-key-v_grid_"] button[data-testid="baseButton-primary"] p,
div[class*="st-key-vc_grid_"] button[data-testid="baseButton-primary"] p,
div[class*="st-key-md_grid_"] button[data-testid="baseButton-primary"] p {
    color: #FF4B4B !important; 
    font-weight: 700 !important;
}

/* Adjust layout alignment for emojis on top line */
div[class*="st-key-v_grid_"] button p::first-line,
div[class*="st-key-vc_grid_"] button p::first-line,
div[class*="st-key-md_grid_"] button p::first-line {
    font-size: 18px !important; /* Enlarges top icon line for optimal card balance */
    line-height: 1.8 !important;
}

/* ==================================================================
   👤 SLIDER & NUMERIC FORM SPACING TRACKS
   ================================================================== */
div[data-testid="stWidgetLabel"] p {
    font-size: 12px !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    color: #64748B !important;
}
            
/* ==================================================================
   ⏰ NATIVE CLOCK-INPUT ELEMENT LAYOUT TUNING
   ================================================================== */
div[data-testid="stTimeInput"] {
    width: 100% !important;
}

div[data-testid="stTimeInput"] input {
    font-size: 14px !important;
    color: #0F1623 !important;
    font-family: inherit !important;
}

/* ==================================================================
   ★ PERFECT HORIZONTAL SLIDER STARS ALIGNMENT TRACK
   ================================================================== */
.slider-stars-wrapper {
    width: 100% !important;
    display: flex !important;
    justify-content: flex-start !important;
    /* Shifts the stars slightly right to match the internal indent of the slider line */
    padding-left: 8px !important; 
    margin-top: 4px !important;
}

.star-rating-row {
    font-size: 14px !important;
    color: #F59E0B !important; /* Gold stars */
    letter-spacing: 2px !important; /* Balanced letter spacing */
    display: inline-flex !important;
    align-items: center !important;
}

.star-rating-val {
    font-size: 12px !important;
    font-weight: 700 !important;
    color: #64748B !important; /* Slate color text label value */
    margin-left: 6px !important;
    letter-spacing: normal !important;
}

/* ==================================================================
   ⚡ STEP 4: PREDICT PAGE INTEGRATIONS & VISUAL ALIGNMENT
   ================================================================== */

/* 1. SOLID RED CONFIRMATION STYLE FOR PREDICTION ACTION BUTTON */
div[class*="st-key-action_nav_predict"] button {
    background-color: #FF4B4B !important; /* Forces rich theme matte red color background */
    border: 1px solid transparent !important;
    border-radius: 8px !important;
    height: 42px !important;
    min-height: 42px !important;
    width: 100% !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    box-shadow: 0 2px 4px rgba(255, 75, 75, 0.08) !important;
    transition: all 0.2s ease-in-out !important;
    pointer-events: auto !important;
    cursor: pointer !important;
}

div[class*="st-key-action_nav_predict"] button p {
    color: #FFFFFF !important;             /* Crisp high-contrast white text label color */
    font-size: 14px !important;
    font-weight: 500 !important;
}

/* Prediction Button Active Mouse Interaction States */
div[class*="st-key-action_nav_predict"] button:hover {
    background-color: #E03E3E !important; /* Elegant slightly darker shade on mouse hover */
    box-shadow: 0 4px 14px rgba(255, 75, 75, 0.22) !important;
    transform: translateY(-0.5px) !important;
}

div[class*="st-key-action_nav_predict"] button:hover p {
    color: #FFFFFF !important;
}

/* 2. MATCHING SECONDARY BACK NAVIGATION BUTTON STYLE */
div[class*="st-key-action_nav_back_to_3"] button {
    background-color: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 8px !important;
    height: 42px !important;
    min-height: 42px !important;
    width: 100% !important;
    transition: all 0.2s ease-in-out !important;
}

div[class*="st-key-action_nav_back_to_3"] button p {
    font-size: 14px !important;
    font-weight: 500 !important;
    color: #475569 !important;
}

div[class*="st-key-action_nav_back_to_3"] button:hover {
    border-color: #CBD5E1 !important;
    background-color: #F8FAFC !important;
}

/* 3. FLUID HOVER ELEVATIONS FOR THE BEIGE SNAPSHOT CARDS */
/* Adds smooth animation transitions directly onto your inner grid cells */
.fcard-body div[style*="grid-template-columns"] > div {
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    will-change: transform, box-shadow;
}

/* Applies a gentle lift-up and subtle drop-shadow effect on mouse hover */
.fcard-body div[style*="grid-template-columns"] > div:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 12px rgba(28, 25, 23, 0.06) !important;
    border-color: #E2E8F0 !important;
}

/* ==================================================================
   🎯 STEP 4: PLACEHOLDER & PRE-FLIGHT SIDE-PANEL DESIGN DECK
   ================================================================== */

/* Core Frame for Placeholder Informational Box */
.placeholder-panel-wrapper {
    background-color: #FFFFFF !important;
    border: 1px dashed #CBD5E1 !important; /* Elegant slate dashed tracking border */
    border-radius: 14px !important;
    padding: 32px 20px !important;
    text-align: center !important;
    margin-bottom: 24px !important;
    display: block !important;
}

.placeholder-emoji-spec {
    font-size: 32px !important;
    line-height: 1 !important;
    display: inline-block !important;
    margin-bottom: 12px !important;
}

.placeholder-title-spec {
    font-size: 16px !important;
    font-weight: 700 !important;
    color: #1E293B !important;
    margin-bottom: 6px !important;
}

.placeholder-sub-spec {
    font-size: 13px !important;
    color: #64748B !important;
    line-height: 1.5 !important;
    max-width: 280px !important;
    margin: 0 auto !important;
}

/* Side panel metrics list container structure overrides */
.side-panel-metrics-box {
    width: 100% !important;
    display: block !important;
    padding-top: 4px !important;
}

/* Ensure the native container wrapper matches the parent fcard border configurations */
div[data-testid="stVerticalBlockBorderWrapper"]:has(div[class*="side-panel-metrics-box"]) {
    background-color: #FFFFFF !important;
    border: 1px solid #EDE8E3 !important;
    border-radius: 14px !important;
    box-shadow: 0 2px 12px rgba(28,25,23,.05) !important;
    padding: 24px 20px !important;
}

/* Target only the button nested inside our custom namespace class */
.mini-reset-wrapper div[data-testid="stButton"] button {
    background-color: transparent !important;
    color: #64748B !important; /* Muted Slate text color */
    border: 1px solid #CBD5E1 !important; /* Thin Slate border outline */
    border-radius: 6px !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    letter-spacing: 0.2px !important;
    
    /* High-utility padding adjustments slim down container height */
    padding: 4px 12px !important;
    min-height: 28px !important;
    height: 28px !important;
    line-height: 1 !important;
    transition: all 0.2s ease-in-out !important;
    margin-top: 2px !important; /* Balances structural alignment with title baseline */
}

/* Interactive smooth micro-transition states */
.mini-reset-wrapper div[data-testid="stButton"] button:hover {
    color: #DC2626 !important; /* Warn-indicator vivid Red text on hover */
    border-color: #FCA5A5 !important; /* Soft red border focus */
    background-color: #FEF2F2 !important; /* Gentle clean pink backwash tint */
    box-shadow: 0 2px 8px rgba(220, 38, 38, 0.05) !important;
}

.mini-reset-wrapper div[data-testid="stButton"] button:active {
    background-color: #FEE2E2 !important;
    transform: scale(0.98) !important;
}

/* ==================================================================
   📊 HIGH-SPECIFICITY OVERRIDE FOR RIGHT PANEL DASHBOARD
   ================================================================== */

.result-card-shell,
div[data-testid="stVerticalBlock"] .result-card-shell {
    background-color: #FFFFFF !important;
    border: 1px solid #EDE8E3 !important;
    border-radius: 14px !important;
    box-shadow: 0 2px 12px rgba(28,25,23,.07) !important;
    padding: 24px 20px !important;
    margin-bottom: 20px !important;
    display: block !important;
    width: 100% !important;
}

.result-header-row {
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    margin-bottom: 14px !important;
}

.result-tagline {
    font-size: 13px !important;
    font-weight: 700 !important;
    color: var(--ink3) !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}

.result-number-wrapper {
    display: flex !important;
    align-items: baseline !important;
    gap: 8px !important;
    margin: 10px 0 !important;
}

.result-big-num {
    font-size: 54px !important;
    font-weight: 800 !important;
    color: var(--ink) !important;
    line-height: 1 !important;
    letter-spacing: -2px !important;
}

.result-unit-label {
    font-size: 16px !important;
    font-weight: 600 !important;
    color: var(--ink3) !important;
}

.result-phrase {
    font-size: 14px !important;
    font-weight: 500 !important;
    color: var(--ink2) !important;
    line-height: 1.5 !important;
    margin-top: 10px !important;
}

.result-metrics-grid {
    display: flex !important;
    flex-direction: column !important;
    gap: 8px !important;
    margin: 16px 0 !important;
}

.result-chip-metric {
    background-color: var(--cream2) !important;
    border: 1px solid #EDE8E3 !important;
    border-radius: 8px !important;
    padding: 10px 14px !important;
    font-size: 13px !important;
    color: var(--ink2) !important;
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
}

.result-metrics-grid .highlighted-metric {
    border: 1px solid #FF4B4B !important; 
    background-color: #FFF5F2 !important;
}

.conf-bar-wrapper-spec {
    background-color: var(--cream2) !important;
    border: 1px solid #EDE8E3 !important;
    border-radius: 10px !important;
    padding: 12px 14px !important;
    margin: 16px 0 !important;
}

.conf-text-row {
    display: flex !important;
    justify-content: space-between !important;
    font-size: 12px !important;
    color: var(--ink3) !important;
    margin-bottom: 6px !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}

.conf-track-bar {
    background-color: #E2E8F0 !important;
    height: 8px !important;
    border-radius: 50px !important;
    width: 100% !important;
    position: relative !important;
    overflow: hidden !important;
}

.conf-fill-bar {
    background: linear-gradient(90deg, #10B981, #059669) !important;
    height: 100% !important;
    border-radius: 50px !important;
}

.arrive-note-container {
    font-size: 13px !important;
    color: var(--ink) !important;
    border-top: 1px dashed #E2E8F0 !important;
    padding-top: 12px !important;
    margin-top: 14px !important;
}

/* RESULT CARD */

.result-card{
  background:linear-gradient(
      145deg,
      #1C1917 0%,
      #2D2521 60%,
      #3B1E14 100%
  );
  border-radius:22px;
  padding:32px 24px 26px;
  position:relative;
  overflow:hidden;
  box-shadow:0 20px 60px rgba(28,25,23,.22);
  text-align:center;
}

.result-card::before{
  content:'';
  position:absolute;
  top:-50px;
  right:-50px;
  width:200px;
  height:200px;
  border-radius:50%;
  background:radial-gradient(
      circle,
      rgba(232,71,30,.18) 0%,
      transparent 70%
  );
}

.result-card::after{
  content:'';
  position:absolute;
  bottom:-40px;
  left:-40px;
  width:160px;
  height:160px;
  border-radius:50%;
  background:radial-gradient(
      circle,
      rgba(255,140,0,.14) 0%,
      transparent 70%
  );
}

.rc-inner{
  position:relative;
  z-index:1;
}

.rc-emoji{
  font-size:42px;
  display:block;
  margin-bottom:6px;
}

.rc-eyebrow{
  font-size:10px;
  font-weight:700;
  letter-spacing:2px;
  text-transform:uppercase;
  color:rgba(255,255,255,.45);
  margin-bottom:8px;
}

.rc-number{
  font-family:'Bricolage Grotesque',sans-serif;
  font-size:80px;
  font-weight:800;
  color:#FFFFFF;
  line-height:1;
  letter-spacing:-4px;
}

.rc-unit{
  font-size:15px;
  font-weight:700;
  letter-spacing:2px;
  text-transform:uppercase;
  color:rgba(255,255,255,.45);
  margin-bottom:14px;
}

.rc-phrase{
  font-size:15px;
  font-weight:600;
  line-height:1.45;
  color:rgba(255,255,255,.75);
  margin-bottom:16px;
}

.rc-chips{
  display:flex;
  gap:7px;
  justify-content:center;
  flex-wrap:wrap;
  margin-bottom:14px;
}

.rc-chip{
  background:rgba(255,255,255,.10);
  border:1px solid rgba(255,255,255,.14);
  border-radius:8px;
  padding:5px 11px;
  font-size:11px;
  font-weight:600;
  color:rgba(255,255,255,.65);
}

.rc-chip strong{
  color:#FFFFFF;
}

.rc-conf-row{
  display:flex;
  justify-content:space-between;
  font-size:10px;
  font-weight:700;
  letter-spacing:1px;
  text-transform:uppercase;
  color:rgba(255,255,255,.40);
  margin-bottom:5px;
}

.rc-conf-track{
  height:5px;
  background:rgba(255,255,255,.12);
  border-radius:4px;
  overflow:hidden;
}

.rc-conf-fill{
  height:100%;
  border-radius:4px;
  background:linear-gradient(
      90deg,
      #FF8C00,
      #22C55E
  );
}

.rc-arrive{
  margin-top:13px;
  font-size:11px;
  font-weight:600;
  color:rgba(255,255,255,.45);
}

.rc-arrive strong{
  color:rgba(255,255,255,.85);
}

        /* Force layout columns to span full screen width if the right column is hidden */
        div[data-testid="stHorizontalBlock"]:has(.receipt-container) {
            display: block !important;
            width: 100% !important;
        }
        
        div[data-testid="stHorizontalBlock"]:has(.receipt-container) > div[data-testid="stColumn"] {
            width: 100% !important;
            max-width: 100% !important;
            flex: none !important;
        }
        
        /* Premium Centered Digital Receipt Checkout Container */
        .receipt-container {
            background: #FFFFFF;
            border: 2px dashed #E2E8F0;
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
            margin-bottom: 32px;
            position: relative;
            max-width: 650px;
            margin-left: auto !important;
            margin-right: auto !important;
        }
        
        /* 🚀 FIX: Balance the height by making this a compact 2-column layout inside the centered wrapper */
        .receipt-grid {
            display: grid !important;
            grid-template-columns: 1fr 1fr !important;
            gap: 12px !important;
            margin-top: 20px;
        }
        
        /* 🎨 RESTORED Theme: Using original design color variables */
        .receipt-item {
            background: var(--cream2) !important;
            border: 1px solid transparent !important;
            border-radius: 10px;
            padding: 11px 14px;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }
        
        /* 🚀 FIX: Smooth premium hover tracking mechanics */
        .receipt-item:hover {
            background: #FFF0E3 !important;
            border: 1px solid #FF843D !important;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(255, 132, 61, 0.08);
        }

        /* Forces child typography tags to track color highlights simultaneously on hover */
        .receipt-item:hover * {
            color: #E25C00 !important;
        }

        /* High-End Prediction Result Hero Card Look */
        .prediction-hero-card {
            background: linear-gradient(135deg, #FFF0E3 0%, #FFF7ED 100%);
            border: 2px solid #FF843D;
            border-radius: 16px;
            padding: 28px;
            text-align: center;
            max-width: 650px;
            margin-left: auto !important;
            margin-right: auto !important;
            margin-top: 28px;
            animation: slideDownFade 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }

        @keyframes slideDownFade {
            from { opacity: 0; transform: translateY(-12px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Center navigation action buttons below checkout card */
        .centered-btn-row {
            max-width: 650px;
            margin-left: auto !important;
            margin-right: auto !important;
        }

/* ==========================================================================
   ISOLATED TOP SEGMENTED CONTROL RESTORATION SYSTEM
   ========================================================================== */

/* 1. Target the top layout track wrapper only */
div:has(> [data-elementstack="top_input_toggle_wrapper"]) div[data-testid="stSegmentedControl"],
div:has(> [data-elementstack="top_input_toggle_wrapper"]) div[data-baseweb="segmented-control"] {
    background-color: #F1F5F9 !important; /* Premium light slate track base */
    background: #F1F5F9 !important;
    border: 1px solid #E2E8F0 !important; /* Crisp hairline layout framing line */
    border-radius: 30px !important;
    padding: 4px !important;
    width: max-content !important;
    display: inline-flex !important;
    align-items: center !important;
}

/* 2. Strip any dark slate/black background fills from the toggle options */
div:has(> [data-elementstack="top_input_toggle_wrapper"]) div[data-testid="stSegmentedControl"] button,
div:has(> [data-elementstack="top_input_toggle_wrapper"]) div[data-testid="stSegmentedControl"] [role="radio"] {
    background: transparent !important;
    background-color: transparent !important; /* Forces off the dark fill */
    border: none !important; /* Wipes out the lingering red outlines */
    border-color: transparent !important;
    border-radius: 26px !important;
    color: #64748B !important; /* Clear slate gray text color for unselected choices */
    font-size: 13px !important;
    font-weight: 600 !important;
    padding: 8px 18px !important;
    box-shadow: none !important;
    outline: none !important;
}

/* 3. Inject the solid white selection bubble */
div:has(> [data-elementstack="top_input_toggle_wrapper"]) div[data-testid="stSegmentedControl"] [aria-checked="true"],
div:has(> [data-elementstack="top_input_toggle_wrapper"]) div[data-testid="stSegmentedControl"] button[aria-checked="true"] {
    background: #FFFFFF !important; /* Solid bright white bubble shape card layer */
    background-color: #FFFFFF !important; 
    color: #0F172A !important; /* High contrast dark gray active text */
    font-weight: 700 !important;
    border: none !important;
    border-color: transparent !important;
    box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.08), 0px 1px 2px rgba(0, 0, 0, 0.04) !important;
}

/* 4. Force uniform text font rendering inside active children tags */
div:has(> [data-elementstack="top_input_toggle_wrapper"]) div[data-testid="stSegmentedControl"] [aria-checked="true"] *,
div:has(> [data-elementstack="top_input_toggle_wrapper"]) div[data-testid="stSegmentedControl"] button[aria-checked="true"] * {
    color: #0F172A !important;
    font-weight: 700 !important;
}

/* 5. Smooth clean hover performance matching unselected modes */
div:has(> [data-elementstack="top_input_toggle_wrapper"]) div[data-testid="stSegmentedControl"] button:hover:not([aria-checked="true"]) {
    color: #1E293B !important;
    background-color: rgba(0, 0, 0, 0.04) !important;
    border: none !important;
}

/* ==========================================================================
   PRODUCTION-GRADE KEY-SPECIFIC SEGMENTED CONTROL OVERRIDES
   ========================================================================== */

/* 1. Target the TOP input method tracker container wrapper only */
div[data-testid="stElementContainer"]:has(div[data-baseweb="segmented-control"]) div[data-testid="stSegmentedControl"]:has(button[id*="mode_toggle_switch"]),
div[data-testid="stSegmentedControl"]:has(button[id*="mode_toggle_switch"]) {
    background-color: #F1F5F9 !important; /* Premium light slate track base */
    background: #F1F5F9 !important;
    border: 1px solid #E2E8F0 !important; /* Crisp hairline layout framing line */
    border-radius: 30px !important;
    padding: 4px !important;
    width: max-content !important;
    display: inline-flex !important;
    align-items: center !important;
}

/* 2. Strip any dark slate/black backgrounds and clear the lingering red outline */
div[data-testid="stSegmentedControl"]:has(button[id*="mode_toggle_switch"]) button,
div[data-testid="stSegmentedControl"]:has(button[id*="mode_toggle_switch"]) [role="radio"] {
    background: transparent !important;
    background-color: transparent !important; /* Erases old fill layout defaults */
    border: none !important; /* Wipes out the lingering red outline instantly */
    border-color: transparent !important;
    border-radius: 26px !important;
    color: #64748B !important; /* Muted slate gray text color for unselected choices */
    font-size: 13px !important;
    font-weight: 600 !important;
    padding: 8px 18px !important;
    box-shadow: none !important;
    outline: none !important;
}

/* 3. Inject the solid white active selection bubble for the top toggle */
div[data-testid="stSegmentedControl"]:has(button[id*="mode_toggle_switch"]) button[aria-checked="true"],
div[data-testid="stSegmentedControl"]:has(button[id*="mode_toggle_switch"]) [aria-checked="true"] {
    background: #FFFFFF !important; /* Solid bright white bubble shape card layer */
    background-color: #FFFFFF !important; 
    color: #0F172A !important; /* High contrast dark gray active text */
    font-weight: 700 !important;
    border: none !important;
    border-color: transparent !important;
    box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.08), 0px 1px 2px rgba(0, 0, 0, 0.04) !important;
}

/* 4. Force text color values into active nested child labels */
div[data-testid="stSegmentedControl"]:has(button[id*="mode_toggle_switch"]) button[aria-checked="true"] *,
div[data-testid="stSegmentedControl"]:has(button[id*="mode_toggle_switch"]) [aria-checked="true"] * {
    color: #0F172A !important;
    font-weight: 700 !important;
}

/* 5. Smooth clean hover feedback matching unselected modes */
div[data-testid="stSegmentedControl"]:has(button[id*="mode_toggle_switch"]) button:hover:not([aria-checked="true"]) {
    color: #1E293B !important;
    background-color: rgba(0, 0, 0, 0.04) !important;
    border: none !important;
}
            
/* ──── ST.HTML RE-BALANCING DECK ──── */
.glass-stepper-container {
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  justify-content: flex-start !important;
  gap: 12px !important;
  background: rgba(255, 255, 255, 0.03) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-radius: 16px !important;
  padding: 8px 12px !important;
  width: 100% !important;
  box-sizing: border-box !important;
  overflow-x: auto;
  margin-bottom: 28px !important;
}

.glass-step {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 10px 20px !important;
  height: 40px !important; /* Forces strict block heights */
  box-sizing: border-box !important;
  font-size: 13px !important;
  font-weight: 700 !important;
  border-radius: 12px !important;
  white-space: nowrap !important;
  transition: all 0.3s ease !important;
}

/* Enforcing layout alignment inside spans */
.glass-step span {
  display: inline-block !important;
  white-space: nowrap !important;
  line-height: 1 !important;
}

.glass-step.step-locked {
  background: transparent !important;
  border: 1px solid rgba(255, 255, 255, 0.05) !important;
  color: rgba(255, 255, 255, 0.35) !important;
}

.glass-step.step-done {
  background: transparent !important;
  border: 1px solid rgba(34, 197, 94, 0.2) !important;
  color: #22C55E !important;
}

.glass-step.step-active {
  background: #E8471E !important;
  border: 1px solid transparent !important;
  color: #FFFFFF !important;
  box-shadow: 0 4px 15px rgba(232, 71, 30, 0.35) !important;
}

/* ──── UNIFIED SHADOW-DOM & REACT-SELECT PLACEHOLDER DECK ──── */

/* 1. Style and align all input labels directly above fields */
div[data-testid="stWidgetLabel"] p,
div[data-testid="stMarkdownContainer"] p strong,
.stTextInput label p {
  font-family: 'Bricolage Grotesque', sans-serif !important;
  font-size: 13px !important;
  font-weight: 700 !important;
  color: #1C1917 !important; /* Premium crisp charcoal gray text */
  text-transform: uppercase !important;
  letter-spacing: 0.3px !important;
}

/* 2. Style the active selected text color inside the input boxes */
div[data-testid="stSearchbox"] input,
div.stSelectbox div[role="combobox"] input,
div[data-testid="stTextInput"] input {
  color: #1C1917 !important; /* Highly legible dark text */
}

/* 3. Deep-wildcard selector targeting both native fields AND the hidden react-select strings */
div[class*="st-"] input[class*="st-"]::placeholder,
div[data-testid="stSearchbox"] div[class*="st-"] input::placeholder,
div[data-testid="stSearchbox"] input::placeholder,
div.stSelectbox div[role="combobox"] input::placeholder,
div[data-testid="stTextInput"] input::placeholder,
.stTextInput input::placeholder,
input[placeholder],
div[data-testid="stSearchbox"] [class*="-placeholder"],
div[data-testid="stSearchbox"] [class*="placeholder"],
div[class*="stSearchbox"] [class*="placeholder"],
.stSelectbox div[class*="-placeholder"],
div[class*="singleValue"],
div[class*="-singleValue"] {
  color: #374151 !important; /* High contrast dark gray prompt color */
  opacity: 1 !important;
  -webkit-text-fill-color: #374151 !important; /* Overrides WebKit engines (Chrome/Safari) */
  font-weight: 500 !important;
}

/* Forces all horizontal layout columns to center-align vertically */
div[data-testid="stHorizontalBlock"]:has(div[data-key="mode_toggle_switch"]) {
  align-items: center !important;
  display: flex !important;
}


/* Color style target for selected active stars */
div[data-testid="stFeedback"] svg[data-filled="true"] {
    fill: #FF843D !important;
    color: #FF843D !important;
}

/* Color style target for hovered star highlights */
div[data-testid="stFeedback"] button:hover svg {
    fill: #FF843D !important;
    color: #FF843D !important;
    transform: scale(1.1);
    transition: transform 0.1s ease-in-out;
}

/* Align feedback component label with text input baselines */
div[data-testid="stFeedback"] label {
    font-size: 14px !important;
    font-weight: 500 !important;
    color: #31333F !important;
    margin-bottom: 4px !important;
}

            
/* ══════════════════════════════════════════════════════════════════
   🚀 FIX: ULTIMATE BASE COLUMN CONTAINER TRANSPARENCY BYPASS
   ══════════════════════════════════════════════════════════════════ */

iframe{border-radius:12px!important}
</style>
""", unsafe_allow_html=True)


# ─── Helpers ──────────────────────────────────────────────────────
def calculate_delivery_distance(X):
    if isinstance(X, np.ndarray):
        lat1, lon1, lat2, lon2 = X[:, 0], X[:, 1], X[:, 2], X[:, 3]
    else:
        lat1 = X['Restaurant_latitude']
        lon1 = X['Restaurant_longitude']
        lat2 = X['Delivery_location_latitude']
        lon2 = X['Delivery_location_longitude']

    R = 6371.0  # Radius in km
    lat1_rad, lon1_rad = np.radians(lat1), np.radians(lon1)
    lat2_rad, lon2_rad = np.radians(lat2), np.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = np.sin(dlat / 2.0)**2 + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(dlon / 2.0)**2
    c = 2.0 * np.arctan2(np.sqrt(a), np.sqrt(1.0 - a))
    distance = R * c

    return np.c_[distance] if isinstance(X, np.ndarray) else pd.DataFrame({'delivery_distance_km': distance}, index=X.index)

def delivery_col_name(function_transformer, feature_names_in):
    return ["delivery_distance_km"]

def extract_hours_and_bucket(X):
    # Ensure input is standard 1D series for extraction
    time_col = X.iloc[:, 0] if isinstance(X, pd.DataFrame) else X
    hours = time_col.str[:2].astype('Int64')

    bins = [-1, 4, 11, 16, 21, 24]
    labels = ['night', 'morning', 'afternoon', 'evening', 'night']
    hour_bins = pd.cut(hours, bins=bins, labels=labels, ordered=False)

    return hour_bins.to_numpy().reshape(-1, 1)

def time_feature_names(function_transformer, feature_names_in):
    return ["day_time"]

# def haversine(la1,lo1,la2,lo2):
#     R=6371
#     dlat=math.radians(la2-la1);dlon=math.radians(lo2-lo1)
#     a=math.sin(dlat/2)**2+math.cos(math.radians(la1))*math.cos(math.radians(la2))*math.sin(dlon/2)**2
#     return R*2*math.asin(math.sqrt(a))

def haversine(la1, lo1, la2, lo2):
    # ─── TYPE GUARD CLAUSE ──────────────────────────────────────────────
    # Instantly returns 0.00 if any coordinate is missing during click cycles
    if la1 is None or lo1 is None or la2 is None or lo2 is None:
        return 0.00

    # ─── CORE MATHEMATICAL CALCULATION ──────────────────────────────────
    R = 6371
    dlat = math.radians(la2 - la1)
    dlon = math.radians(lo2 - lo1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(la1)) * math.cos(math.radians(la2)) * math.sin(dlon / 2)**2
    return R * 2 * math.asin(math.sqrt(a))


def stars(r):
    f=int(r);e=5-f
    return "★"*f+"☆"*e+f" {r:.1f}"

TRAFFIC_BADGE={"Low":"ib-green","Medium":"ib-amber","High":"ib-orange","Jam":"ib-red"}
WEATHER_ICON={"Sunny":"☀️","Cloudy":"☁️","Fog":"🌫️","Windy":"💨","Stormy":"⛈️","Sandstorms":"🌪️"}
VEH_ICON={"motorcycle":"🏍️","scooter":"🛵","electric_scooter":"⚡","bicycle":"🚲"}

# ─── LOTTIE DELIVERY MICRO-ANIMATION SCHEMATICS MAP ─────────────────────────

# ─── LOTTIE DELIVERY MICRO-ANIMATION RESILIENT SCHEMATICS MAP ─────────────────
# Swapped out legacy assets1 links for stable Lottie CDN animation URLs
LOTTIE_DELIVERY_RESOURCES = {
    "Sunny": "https://cloudflare.com", # Fallback structure reference
    "Sunny": "https://lottiefiles.com",      # Valid production endpoint
    "Cloudy": "https://lottiefiles.com",
    "Fog": "https://lottiefiles.com",
    "Windy": "https://lottiefiles.com",
    "Stormy": "https://lottiefiles.com",          # Rainy rider storm
    "Sandstorms": "https://lottiefiles.com",
    "Jam_Override": "https://lottiefiles.com"     # Idling courier look
}


PHRASES=[
    "Hang tight — your feast is <span>{} mins</span> away! 🚀",
    "Your cravings will be satisfied in <span>{} mins</span>. Worth the wait! 😋",
    "ETA locked in at <span>{} mins</span>. Get your plates ready! 🍽️",
    "Getting it your way in <span>{} mins</span>! 🛵💨",
    "Freshness incoming in <span>{} mins</span>. The countdown is on! ⏱️",
    "Your order is <span>{} mins</span> from happiness! 🎉",
]

@st.cache_resource(show_spinner=False)
def load_model():
    for n in ["food_delivery_time_prediction_model_compressed.pkl","model.pkl","optimized_rf_model.pkl"]:
        if os.path.exists(n):
            return joblib.load(n),n
    return None,None

model,model_path=load_model()

import shap

# ─── INITIALIZE PIPELINE-COMPATIBLE SHAP EXPLAINER ──────────────────────────
try:
    # 1. Extract the raw underlying Random Forest model using your discovered step name
    raw_tree_model = model.named_steps['random_forest']
    
    # 2. Build a baseline TreeExplainer utilizing the raw tree model
    # (Passing None as the data background for an ensemble tree defaults it to optimization paths)
    explainer = shap.TreeExplainer(raw_tree_model)
except Exception as e:
    st.error(f"SHAP Engine Initialization Error: {e}")


# ─── Session state ────────────────────────────────────────────────
_defs=dict(
    step=1,
    rest_lat=22.7444, rest_lon=75.8946,
    del_lat=22.7644, del_lon=75.9146,
    pin_mode="restaurant",           # which pin to drop next
    weather="Sunny", traffic="Medium",
    vehicle_type="motorcycle", vehicle_condition=1,
    city="Metropolitian", festival="No",
    age=28, rating=4.7,
    multiple_deliveries=1,
    time_ordered="11:15",
    prediction=None, phrase_idx=0,
    demo_mode=model is None,
)
for k,v in _defs.items():
    if k not in st.session_state:
        st.session_state[k]=v

s=st.session_state  # shorthand

if "last_logged_step" not in s:
    s.last_logged_step = s.step

if s.step != s.last_logged_step:
    # Target the top-level stepper anchor explicitly
    auto_scroll_to_element(element_id="global-stepper-scroll-anchor", key_trigger=f"step_shift_{s.step}")
    s.last_logged_step = s.step

# ─── 1. COMPUTE STATUS PILL (NO INLINE BRACES) ───────────────────
if model:
    status_tag = (
        '<div style="padding: 5px 12px; background: #F0FDF4; color: #16A34A; '
        'display: flex; align-items: center; gap: 6px;">'
        '<span class="live-dot" style="margin-bottom: 1px;"></span>sys.status(LIVE)'
        '</div>'
    )
else:
    status_tag = (
        '<div style="padding: 5px 12px; background: #FEF2F2; color: #DC2626; '
        'display: flex; align-items: center; gap: 6px;">'
        '<span style="width: 7px; height: 7px; border-radius: 50%; background: #EF4444; '
        'display: inline-block; flex-shrink: 0;"></span>sys.status(DEMO)'
        '</div>'
    )

# ─── 2. CONCATENATE THE CHIP STRUCTURE WITH OPERATORS ────────────
dev_tags_html = (
    '<div style="display: flex; align-items: center; font-family: \'JetBrains Mono\', '
    '\'Fira Code\', \'Courier New\', monospace; font-size: 11px; font-weight: 600; '
    'border: 1px solid #E2E8F0; border-radius: 6px; overflow: hidden; letter-spacing: 0.3px;">'
    '<div style="padding: 5px 12px; background: #F8FAFC; color: #64748B; '
    'border-right: 1px solid #E2E8F0; display: flex; align-items: center; gap: 6px;">'
    '<span style="font-size: 13px; line-height: 1;">🤖</span>drop_pipeline.py'
    '</div>'
) + status_tag + '</div>'

# 🚀 CHOSEN ALTERNATIVE: THE NEURAL VECTOR DROP (Geospatial Pin + Topology Nodes)
brand_html = (
    '<div style="display: flex; align-items: center; gap: 12px;">'
    '    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://w3.org" style="flex-shrink:0;">'
    '        <!-- Layered Topology Network Vector Background -->'
    '        <path d="M12 2C7.58 2 4 5.58 4 10C4 13.9 6.5 17.5 10 20.8V14H6V10H10V6H14V10H18V14H14V20.8C17.5 17.5 20 13.9 20 10C20 5.58 16.42 2 12 2Z" fill="#1E293B" opacity="0.15"/>'
    '        <!-- Main High-Contrast Sharp Location Data Spine -->'
    '        <path d="M12 2C8.13 2 5 5.13 5 9C5 13.17 12 21 12 21C12 21 19 13.17 19 9C19 5.13 15.87 2 12 2ZM12 12.5C10.07 12.5 8.5 10.93 8.5 9C8.5 7.07 10.07 5.5 12 5.5C13.93 5.5 15.5 7.07 15.5 9C15.5 10.93 13.93 12.5 12 12.5Z" fill="#1E293B"/>'
    '        <!-- Floating Neural Node Cursor Point -->'
    '        <circle cx="12" cy="9" r="2.5" fill="#FF5A36"/>'
    '        <circle cx="12" cy="9" r="4.5" stroke="#FF5A36" stroke-width="1" opacity="0.5" stroke-dasharray="1 1"/>'
    '    </svg>'
    '    <span style="font-family: \'Space Grotesk\', \'Bricolage Grotesque\', sans-serif; font-size: 20px; font-weight: 800; color: #1E293B; letter-spacing: -0.5px; line-height:1;">'
    '        Drop<span style="color: #FF5A36;">Time</span>'
    '    </span>'
    '</div>'
)

# ─── 3. RENDER SAFELY VIA STREAMLIT NATIVE COLUMNS ────────────────
topbar_container = st.container()
with topbar_container:
    # Balanced grid layouts spacing distribution parameters
    col_brand, col_spacer, col_badges = st.columns([1.6, 1.4, 1], vertical_alignment="center")
    
    with col_brand:
        st.markdown(brand_html, unsafe_allow_html=True)
        
    with col_badges:
        st.markdown(
            '<div style="display: flex; justify-content: flex-end; width: 100%;">' + dev_tags_html + '</div>', 
            unsafe_allow_html=True
        )

# Adds a clean structural separator beneath the updated elements
st.markdown('<hr style="margin: 16px 0px 24px 0px; border: 0; border-top: 1px solid #E2E8F0; opacity: 0.6;">', unsafe_allow_html=True)

# Set your scene, check the vibe, and know exactly down to the minute when your cravings are landing.

st.html("""
<div class="hero">
  <div class="hero-inner">
    <div class="hero-tag">🍕 AI-Powered Food Delivery Intelligence</div>
    <div class="hero-h1">How long until<br><span>your next meal?</span></div>
    <div class="hero-sub">
      No ghosting your hunger. Exact ETAs powered by machine learning.
    </div>
    
    <div class="hero-chips-container">
      
      <span class="hero-chip-light chip-accuracy-light">
        🎯 <strong>~93%</strong> Accuracy
      </span>
      
      <span class="hero-chip-light chip-inference-light">
        ⚡ <strong>&lt;50ms</strong> Inference
      </span>
      
      <span class="hero-chip-light chip-features-light">
        🗺️ <strong>14</strong> Input Features
      </span>
      
      <span class="hero-chip-light chip-geo-light">
        🌆 <strong>Metropolitan</strong> · Urban · Semi-Urban
      </span>

    </div>
  </div>
</div>
""")


if not model:
    st.html("""
    <div style="background:#FFFBEB; border:1px solid #FCD34D; border-left:3px solid #F59E0B;
      padding:11px 18px; font-size:13px; font-weight:600; color:#78350F; margin-top: 16px; border-radius: 4px;">
      ⚠️ Demo mode — no <code>.pkl</code> file detected. Heuristic estimates shown. 
      Drop your model file alongside <code>app.py</code> for live predictions.
    </div>
    """)

# ─── STEP NAVIGATOR (Premium Light-Theme Pastel System) ───
step_states = []
for i in range(1, 5):
    cls = "active" if s.step == i else ("done" if s.step > i else "")
    step_states.append((i, cls))

labels = ["📍 Location", "🌤️ Conditions", "🏍️ Driver & Vehicle", "⚡ Predict"]

bg_colors = {
    "active": "#FF7A59",       
    "done": "#D1FAE5",         
    "": "#F3F4F6"              
}

text_colors = {
    "active": "#FFFFFF",       
    "done": "#065F46",         
    "": "#9CA3AF"              
}

label_colors = {
    "active": "#1F2937",       
    "done": "#6B7280",         
    "": "#9CA3AF"              
}

border_bottoms = {
    "active": "3px solid #FF7A59", 
    "done": "3px solid transparent", 
    "": "3px solid transparent"
}

tabs_list = []
for (i, cls), lbl in zip(step_states, labels):
    num_display = "✓" if cls == "done" else str(i)
    tab_html = f'<div style="display:flex;align-items:center;gap:8px;padding:12px 20px;border-bottom:{border_bottoms[cls]};white-space:nowrap;"><span style="width:24px;height:24px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;background:{bg_colors[cls]};color:{text_colors[cls]};line-height:1;flex-shrink:0;">{num_display}</span><span style="font-size:13px;font-weight:700;color:{label_colors[cls]};line-height:1;">{lbl}</span></div>'
    tabs_list.append(tab_html)

full_nav_html = f'<div style="display:flex;flex-direction:row;align-items:center;justify-content:flex-start;gap:12px;background:#FFFFFF;border-bottom:1px solid #E2E8F0;padding:0 36px;width:100%;overflow-x:auto;">{"".join(tabs_list)}</div>'

# ─── 📍 CRITICAL FIX: EMBED THE PERMANENT STEPPER ANCHOR DIRECTLY HERE ───
st.markdown("""
<div id="global-stepper-scroll-anchor" style="display: block; clear: both; width: 100%; margin-top: 0px;"></div>
""", unsafe_allow_html=True)

st.markdown(full_nav_html, unsafe_allow_html=True)

# 11:8 grid layout distribution
main_col, result_col = st.columns([11, 8], gap="large")

# ══════════════════════════════════════════════
# LEFT COLUMN  —  DYNAMIC STEP ROUTING
# ══════════════════════════════════════════════
with main_col:
    # ── STEP 1: LOCATION (Bi-Directional Key-Insulated Engine) ───────────────
    if s.step == 1:
        # ─── CRITICAL BLOCKS (SAVES FROM ATTRIBUTE ERRORS AND RESET CACHING) ───
        if "map_rest_lat" not in s:   s.map_rest_lat = 28.6304
        if "map_rest_lon" not in s:   s.map_rest_lon = 77.2177
        if "map_del_lat" not in s:    s.map_del_lat = 28.6514
        if "map_del_lon" not in s:    s.map_del_lon = 77.1907
        if "click_count" not in s:     s.click_count = 2
        
        if "rest_search_text" not in s: s.rest_search_text = "Connaught Place, New Delhi"
        if "del_search_text" not in s:  s.del_search_text = "Karol Bagh, New Delhi"
        
        if "rest_key_version" not in s: s.rest_key_version = 100
        if "del_key_version" not in s:  s.del_key_version = 200
        
        st.markdown("<div style='margin-bottom: 24px;'></div>", unsafe_allow_html=True)

        st.markdown("""
        <div id="step-header-anchor" class="section-title" style="display: flex; align-items: center; gap: 8px; line-height: 1; margin-top: 4px;">
            <span style="white-space: nowrap;">📍 Where's your order going?</span>
            <div class="custom-tooltip">
                <span class="info-trigger">i</span>
                <div class="tooltip-text">Calculates geodesic distance vectors across coordinate nodes.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


        st.markdown("<div style='margin-bottom: 24px;'></div>", unsafe_allow_html=True)
        st.markdown("<div style='margin-bottom: 4px;'></div>", unsafe_allow_html=True)

        from streamlit_searchbox import st_searchbox
        from geopy.geocoders import Photon
        import folium
        from streamlit_folium import st_folium
        
        geolocator = Photon(user_agent="deliveriq_enterprise_analytics_2026")
        
        # Initialize default state attributes if not already present
        if "rest_search_text" not in s: 
            s.rest_search_text = "Connaught Place, New Delhi"
        if "del_search_text" not in s: 
            s.del_search_text = "Karol Bagh, New Delhi"
        if "rest_lat" not in s:
            s.rest_lat, s.rest_lon = 28.6304, 77.2177
        if "del_lat" not in s:
            s.del_lat, s.del_lon = 28.6514, 77.1907
        if "click_count" not in s:
            s.click_count = 2 # Starts matched with default preset state

        def address_autocomplete_lookup(search_term: str):
            if not search_term or len(search_term) < 3:
                return []
            try:
                locations = geolocator.geocode(search_term, exactly_one=False, timeout=3, limit=5)
                if locations:
                    return [(str(loc.address), (float(loc.latitude), float(loc.longitude))) for loc in locations]
            except Exception:
                return []
            return []

        # # MASTER CARD CONTAINER
                # MASTER CARD CONTAINER
        with st.container(border=False):
            # —————————————————————————————————————————————————————————————————
            # INSTANT SCENARIO PRESETS ENGINE & CLEAR PINS (FIXED ALIGNMENT)
            # —————————————————————————————————————————————————————————————————
            PRESET_OPTIONS = {
                "⚡ CP to Karol Bagh": {
                    "rest": (28.6304, 77.2177, "Connaught Place, New Delhi"),
                    "del": (28.6514, 77.1907, "Karol Bagh, New Delhi")
                },
                "🚀 Cyber City Sprint": {
                    "rest": (28.4952, 77.0890, "DLF Cyber City, Gurgaon"),
                    "del": (28.4815, 77.0945, "DLF Phase 3, Gurgaon")
                },
                "🛵 South Ext. Hub Run": {
                    "rest": (28.5683, 77.2194, "South Extension, New Delhi"),
                    "del": (28.5457, 77.2631, "Kalkaji, New Delhi")
                }
            }

            # Evaluate preset matches securely against master standalone variables
            active_preset_selection = None
            if s.map_rest_lat is not None and s.map_del_lat is not None:
                current_rest = (round(float(s.map_rest_lat), 3), round(float(s.map_rest_lon), 3))
                current_del = (round(float(s.map_del_lat), 3), round(float(s.map_del_lon), 3))
                if current_rest == (28.630, 77.218) and current_del == (28.651, 77.191):
                    active_preset_selection = "⚡ CP to Karol Bagh"
                # FIX: Updated matching values to line up with the 3-decimal place outputs of Cyber City
                elif current_rest == (28.495, 77.089) and current_del == (28.482, 77.094): 
                    active_preset_selection = "🚀 Cyber City Sprint"
                elif current_rest == (28.568, 77.219) and current_del == (28.546, 77.263):
                    active_preset_selection = "🛵 South Ext. Hub Run"

                        # 2-Column Layout: Expanded left column to ensure presets sit on a single line
            col_presets, col_btn = st.columns([6.5, 1.5], gap="small", vertical_alignment="bottom")

            with col_presets:
                st.markdown("""
                <div style="font-size: 11px; font-weight: 700; color: #64748B; letter-spacing: 1.5px; text-transform: uppercase; margin: 0 0 10px 0; line-height: 1;">
                    ⚡ Quick Presets
                </div>
                """, unsafe_allow_html=True)
                
                chosen_preset = st.segmented_control(
                    label="Scenario Shortcuts",
                    options=list(PRESET_OPTIONS.keys()),
                    default=active_preset_selection,
                    label_visibility="collapsed",
                    key="scenario_preset_switch"
                )

            # Updates both coordinates and text boxes, then stops the loop
            if chosen_preset and chosen_preset != active_preset_selection:
                data = PRESET_OPTIONS[chosen_preset]
                s.map_rest_lat, s.map_rest_lon, s.rest_search_text = data["rest"]
                s.map_del_lat, s.map_del_lon, s.del_search_text = data["del"]

                # ── CRITICAL FIX: SYNC CORE METRIC VARIABLES FOR THE SUMMARY CARD ──
                s.rest_lat = s.map_rest_lat
                s.rest_lon = s.map_map_lon if hasattr(s, "map_map_lon") else s.map_rest_lon # Safe Fallback
                s.rest_lon = s.map_rest_lon
                s.del_lat  = s.map_del_lat
                s.del_lon  = s.map_del_lon

                s.click_count = 2 
                s.rest_key_version += 1
                s.del_key_version += 1
                st.rerun()

            st.markdown("<div style='margin-bottom: 24px;'></div>", unsafe_allow_html=True)
            
            # ─── LIVE LOCATION STATE CARDS (PRE-MAP VIEWPORT OVERVIEW) ───
            # Dynamically shows the current coordinates/resolved strings above the canvas
            loc_col1, loc_col2 = st.columns(2)
            with loc_col1:
                st.markdown(f"""
                <div style="background: #FFF7ED; border: 1px solid #FFEDD5; padding: 10px 14px; border-radius: 8px;">
                    <div style="font-size: 10px; font-weight: 700; color: #C2410C; text-transform: lowercase; letter-spacing: 0.5px;">📍 Pickup Hub</div>
                    <div style="font-size: 13px; font-weight: 600; color: #1E293B; margin-top: 2px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" title="{s.rest_search_text}">{s.rest_search_text}</div>
                </div>
                """, unsafe_allow_html=True)
                
            with loc_col2:
                st.markdown(f"""
                <div style="background: #FAF5FF; border: 1px solid #F3E8FF; padding: 10px 14px; border-radius: 8px;">
                    <div style="font-size: 10px; font-weight: 700; color: #6B21A8; text-transform: lowercase; letter-spacing: 0.5px;">🏁 Dropoff Hub</div>
                    <div style="font-size: 13px; font-weight: 600; color: #1E293B; margin-top: 2px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" title="{s.del_search_text}">{s.del_search_text}</div>
                </div>
                """, unsafe_allow_html=True)
                
            st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

                        # ─── 1. INITIALIZE MASTER GEOGRAPHIC MEMORY ARCHIVES ──────────────────
            # Explicit coordinate locks that are completely immune to searchbox cache interference
            if "map_rest_lat" not in s: s.map_rest_lat = 28.6304
            if "map_rest_lon" not in s: s.map_rest_lon = 77.2177
            if "map_del_lat" not in s:  s.map_del_lat = 28.6514
            if "map_del_lon" not in s:  s.map_del_lon = 77.1907
            if "click_count" not in s:   s.click_count = 2 # Sync with defaults
            
            if "rest_key_version" not in s: s.rest_key_version = 100
            if "del_key_version" not in s:  s.del_key_version = 200

            # Dynamic Click Target Matrix Router
            if s.map_rest_lat is None:
                s.pin_mode = "restaurant"
            elif s.map_del_lat is None:
                s.pin_mode = "delivery"
            else:
                s.pin_mode = "restaurant"

            # ─── 2. INPUT SELECTION COLUMNS RENDERING ─────────────────────────────
            search_col1, search_col2 = st.columns(2)

            with search_col1:
                restaurant_selection = st_searchbox(
                    address_autocomplete_lookup,
                    # label="🍽️ From: Restaurant Hub", 
                    label="",
                    placeholder="Search or Click Map Directly...", 
                    default=s.rest_search_text if s.rest_search_text else "",
                    key=f"rest_box_instance_v_{s.rest_key_version}",
                    clear_on_submit=False,
                    edit_after_submit="option"
                )
                # Overwrite master variables ONLY if user intentionally searches text
                if restaurant_selection is not None and isinstance(restaurant_selection, tuple):
                    if restaurant_selection != (s.map_rest_lat, s.map_rest_lon):
                        s.map_rest_lat, s.map_rest_lon = restaurant_selection
                        s.rest_search_text = "📍 Custom Searched Hub"
                        s.click_count = 1 if s.map_del_lat is None else 2
                        st.rerun()

            with search_col2:
                delivery_selection = st_searchbox(
                    address_autocomplete_lookup,
                    # label="📦 To: Delivery Destination",
                    label="", 
                    placeholder="Search or Click Map Directly...", 
                    default=s.del_search_text if s.del_search_text else "",
                    key=f"del_box_instance_v_{s.del_key_version}",
                    clear_on_submit=False,
                    edit_after_submit="option"
                )
                # Overwrite master variables ONLY if user intentionally searches text
                if delivery_selection is not None and isinstance(delivery_selection, tuple):
                    if delivery_selection != (s.map_del_lat, s.map_del_lon):
                        s.map_del_lat, s.map_del_lon = delivery_selection
                        s.del_search_text = "📍 Custom Searched Destination"
                        s.click_count = 2
                        st.rerun()

            # ─── 3. INTERACTIVE MAP FRAME ASSEMBLY ────────────────────────────────
            if s.map_rest_lat is not None and s.map_del_lat is not None:
                clat = (float(s.map_rest_lat) + float(s.map_del_lat)) / 2
                clon = (float(s.map_rest_lon) + float(s.map_del_lon)) / 2
                zoom_fallback = 12
            elif s.map_rest_lat is not None:
                clat, clon = float(s.map_rest_lat), float(s.map_rest_lon)
                zoom_fallback = 13
            else:
                clat, clon = 28.6139, 77.2090
                zoom_fallback = 11

            m = folium.Map(
                location=[clat, clon], 
                zoom_start=zoom_fallback,
                tiles='CartoDB positron', 
                attr='&copy; <a href="https://openstreetmap.org">OpenStreetMap</a> contributors &copy; <a href="https://carto.com">CARTO</a>'
            )

            if s.map_rest_lat is not None:
                folium.Marker(
                    [float(s.map_rest_lat), float(s.map_rest_lon)], 
                    tooltip="🍽️ Pickup Restaurant Hub", 
                    icon=folium.Icon(color='orange', icon='cutlery', prefix='fa')
                ).add_to(m)

            if s.map_del_lat is not None:
                folium.Marker(
                    [float(s.map_del_lat), float(s.map_del_lon)], 
                    tooltip="📦 Delivery Destination Point", 
                    icon=folium.Icon(color='purple', icon='home', prefix='fa')
                ).add_to(m)

            if s.map_rest_lat is not None and s.map_del_lat is not None:
                folium.PolyLine(
                    [[float(s.map_rest_lat), float(s.map_rest_lon)], [float(s.map_del_lat), float(s.map_del_lon)]], 
                    color='#FF4B4B', weight=4, opacity=0.9, dash_array='6 4'
                ).add_to(m)

            # Render canvas natively with a locked static key identifier
            map_result = st_folium(
                m, center=[clat, clon], width="100%", height=380, 
                key="zero_click_delivery_canvas"
            )

                        # ─── FULL-WIDTH HORIZONTAL CLEAR BUTTON (THEME INTEGRATION) ───
            st.markdown("""
            <style>
                /* Target the secondary button wrapper */
                div.unified-horizontal-clear-container [data-testid="stBaseButton-secondary"] button {
                    width: 100% !important;
                    height: 40px !important;
                    min-height: 40px !important;
                    max-height: 40px !important;
                    margin: 12px 0 4px 0 !important;
                    padding: 0px 16px !important;
                    
                    /* Soft colored tint layout to coordinate with your orange/red theme accents */
                    background-color: #FFF5F2 !important;
                    background: #FFF5F2 !important;
                    border: 1px solid #FCD3C7 !important;
                    border-radius: 8px !important;
                    box-shadow: none !important;
                    
                    display: flex !important;
                    align-items: center !important;
                    justify-content: center !important;
                    transition: all 0.2s ease-in-out !important;
                }
                
                /* Hover transition states updating background fills */
                div.unified-horizontal-clear-container [data-testid="stBaseButton-secondary"] button:hover {
                    background-color: #FFEAE3 !important;
                    background: #FFEAE3 !important;
                    border-color: #F9A894 !important;
                }
                
                /* Typography color match using the primary red/orange hexadecimal values */
                div.unified-horizontal-clear-container [data-testid="stBaseButton-secondary"] button p,
                div.unified-horizontal-clear-container [data-testid="stBaseButton-secondary"] button span {
                    color: #E8471E !important;
                    font-size: 13px !important;
                    font-weight: 700 !important;
                    line-height: 40px !important;
                    margin: 0px !important;
                    padding: 0px !important;
                }
                
                /* Darker color accent transition on mouse hover */
                div.unified-horizontal-clear-container [data-testid="stBaseButton-secondary"] button:hover p {
                    color: #CD3713 !important;
                }
            </style>
            <div class="unified-horizontal-clear-container">
            """, unsafe_allow_html=True)

            # Native full-width clear action button
            trigger_map_clear = st.button("🧹 Clear Pins from Map Layout", use_container_width=True, key="canvas_bottom_clear_btn")

            st.markdown("</div>", unsafe_allow_html=True)

            # Process state scrubbing immediately inside the active server loop
            if trigger_map_clear:
                s.map_rest_lat, s.map_rest_lon, s.rest_search_text = None, None, "Not Selected"
                s.map_del_lat, s.map_del_lon, s.del_search_text = None, None, "Not Selected"
                s.click_count = 0
                s.rest_key_version += 1 
                s.del_key_version += 1  
                st.rerun()

            # ─── 4. MAP CLICK ACTION DISPATCHER & LOGIC ENGINE ────────────────────
            if map_result and map_result.get("last_clicked"):
                click_lat = round(map_result["last_clicked"]["lat"], 6)
                click_lon = round(map_result["last_clicked"]["lng"], 6)
                click_sig = f"{click_lat}_{click_lon}"
                
                if "processed_click_id" not in s: 
                    s.processed_click_id = ""
                    
                if click_sig != s.processed_click_id:
                    s.processed_click_id = click_sig

                                        # ─── REVERSE GEOCODING ENGINE ADDRESS STRING REPAIR ───
                    try:
                        location_obj = geolocator.reverse((click_lat, click_lon), timeout=3)
                        if location_obj and getattr(location_obj, "address", None):
                            address_parts = [p.strip() for p in location_obj.address.split(",") if p.strip()]
                            # Combines the top address fragments natively with clean string separators
                            place_display_name = ", ".join(address_parts[:2]) if len(address_parts) >= 2 else address_parts[0]
                        else:
                            place_display_name = f"{click_lat:.4f}, {click_lon:.4f}"
                    except Exception:
                        place_display_name = f"{click_lat:.4f}, {click_lon:.4f}"


                    
            #         # Core Click Routing Alternator
                                # ... [Keep your preceding Section 4 code exactly as it is] ...
                    
                    # Core Click Routing Alternator
                    if s.click_count == 0 or s.click_count >= 2:
                        s.map_rest_lat, s.map_rest_lon = click_lat, click_lon
                        s.rest_search_text = place_display_name
                        
                        s.map_del_lat, s.map_del_lon = None, None  # Wipe destination to force second drop context
                        s.del_search_text = "Not Selected"
                        s.click_count = 1
                        s.rest_key_version += 1 # Force clear search box text cache
                    else:
                        s.map_del_lat, s.map_del_lon = click_lat, click_lon
                        s.del_search_text = place_display_name
                        s.click_count = 2
                        s.del_key_version += 1  # Force clear search box text cache

                    # ─── CRITICAL FIX: SYNC CORE METRICS IMMEDIATELY ON MANUAL PIN DROPS ───
                    s.rest_lat = s.map_rest_lat
                    s.rest_lon = s.map_rest_lon
                    s.del_lat  = s.map_del_lat
                    s.del_lon  = s.map_del_lon
                        
                    st.rerun()

            # ─── 5. DISTANCE EVALUATION CALCULATOR FOOTER ─────────────────────────
            # Ensure fallback assignment handles empty states smoothly
            s.rest_lat = s.map_rest_lat
            s.rest_lon = s.map_rest_lon
            s.del_lat  = s.map_del_lat
            s.del_lon  = s.map_del_lon

            if s.map_rest_lat is not None and s.map_del_lat is not None:
                dist = haversine(s.map_rest_lat, s.map_rest_lon, s.map_del_lat, s.map_del_lon)
                # Store distance in session state so the side panel has instant access
                s.route_distance = dist 
            else:
                dist = 0.00
                s.route_distance = 0.00

            # # ─── SIDE-BY-SIDE MATRIX: FIXED STATUS COLOR ENGINE & CENTERED TOGGLE ───
                        # ─── SIDE-BY-SIDE MATRIX: RE-ALIGNED MATRIX HUD ROW ───
            lower_col1, lower_col2 = st.columns([6.3, 1.7], gap="small", vertical_alignment="center")

            with lower_col1:
                # Calculate active routing status securely against master state variables
                has_rest = s.map_rest_lat is not None and s.rest_search_text != "Not Selected"
                has_del = s.map_del_lat is not None and s.del_search_text != "Not Selected"

                if has_rest and has_del:
                    status_text = "✓ Route locked in successfully"
                    status_class = "state-locked"
                    status_color = "#15803D"
                    status_bg = "#F0FDF4"
                    status_border = "#BBF7D0"
                else:
                    status_text = "⏳ Awaiting map coordinate selections..."
                    status_class = "state-empty"
                    status_color = "#475569"
                    status_bg = "#F8FAFC"
                    status_border = "#E2E8F0"

                # Render the status confirmation banner (REDUCED TOP MARGIN)
                st.markdown(f"""
                <style>
                    div.dist-pill.state-locked {{ background: #F0FDF4 !important; border: 1px solid #BBF7D0 !important; }}
                    div.dist-pill.state-locked span {{ color: #15803D !important; }}
                    div.dist-pill.state-empty {{ background: #F8FAFC !important; border: 1px solid #E2E8F0 !important; }}
                    div.dist-pill.state-empty span {{ color: #475569 !important; }}
                </style>
                
                <div class="dist-pill {status_class}" style="display:flex; align-items:center; background:{status_bg} !important; border:1px solid {status_border} !important; border-radius:10px; padding:0 16px; margin: -4px 0 0 0 !important; height:44px; width:100%; box-sizing:border-box;">
                  <span style="font-size:13.5px; font-weight:700; color:{status_color} !important; white-space:nowrap; letter-spacing: -0.1px;">{status_text}</span>
                </div>
                """, unsafe_allow_html=True)

            with lower_col2:
                # 1. Nest a micro 2-column grid inside the right slot to lock elements side-by-side natively
                toggle_txt_col, toggle_sw_col = st.columns([5.8, 2.2], gap="small", vertical_alignment="center")
                
                with toggle_txt_col:
                    st.markdown("""
                    <style>
                        div.toggle-text-left-box {
                            /* REDUCED GAP: Adjusted from 10px to -4px to pull the text up with the banner row */
                            margin-top: 4px !important; 
                            width: 100%;
                            text-align: right;
                        }
                        div.toggle-text-left-box span {
                            font-size: 11px !important;
                            font-weight: 700 !important;
                            color: #64748B !important;
                            text-transform: uppercase !important;
                            letter-spacing: 0.8px !important;
                            white-space: nowrap !important;
                            line-height: 44px !important; /* Forces the text bounding box height to match the banner */
                        }
                    </style>
                    <div class="toggle-text-left-box">
                        <span>ML Features</span>
                    </div>
                    """, unsafe_allow_html=True)
                    
                with toggle_sw_col:
                    st.markdown("""
                    <style>
                        div.compact-toggle-box {
                            /* COORD CENTERING: Set from 14px to 6px to push the toggle switch down 
                               into the perfect vertical center of the text label */
                            margin-top: 28px !important; 
                        }
                        div.compact-toggle-box div[data-testid="stToggle"] {
                            padding: 0px !important;
                            margin: 0px !important;
                        }
                        div.compact-toggle-box div[data-testid="stToggle"] label p {
                            display: none !important;
                        }
                    </style>
                    <div class="compact-toggle-box">
                    """, unsafe_allow_html=True)

                    # 🚀 FIXED: Pass a valid label and collapse visibility to clear terminal accessibility logs
                    show_coordinates = st.toggle(
                        label="Show Coordinates", 
                        value=False, # or your existing baseline default value
                        key="hud_matrix_coord_reveal_tgl", # or your existing session key identifier
                        label_visibility="collapsed"
                    )

                    
                    st.markdown("</div>", unsafe_allow_html=True)

            # # ─── FULL WIDTH CONDITIONAL RENDERING GRID ───
                        # ─── FULL WIDTH CONDITIONAL RENDERING GRID ───
            if show_coordinates:
                st.markdown("<div style='margin-top:16px;'></div>", unsafe_allow_html=True)
                
                # Full Width Row 1: Restaurant Parameters
                col_lat1, col_lon1 = st.columns(2, gap="medium")
                with col_lat1:
                    new_rest_lat = st.number_input(
                        "Restaurant Latitude", 
                        value=float(s.map_rest_lat) if s.map_rest_lat else 0.0,
                        format="%.6f",
                        key="numerical_input_rest_lat"
                    )
                    if new_rest_lat != s.map_rest_lat:
                        s.map_rest_lat = new_rest_lat
                        s.rest_lat = new_rest_lat
                        st.rerun()
                        
                with col_lon1:
                    new_rest_lon = st.number_input(
                        "Restaurant Longitude", 
                        value=float(s.map_rest_lon) if s.map_rest_lon else 0.0,
                        format="%.6f",
                        key="numerical_input_rest_lon"
                    )
                    if new_rest_lon != s.map_rest_lon:
                        s.map_rest_lon = new_rest_lon
                        s.rest_lon = new_rest_lon
                        st.rerun()
                
                # Full Width Row 2: Delivery Destination Parameters
                col_lat2, col_lon2 = st.columns(2, gap="medium")
                with col_lat2:
                    new_del_lat = st.number_input(
                        "Delivery Latitude", 
                        value=float(s.map_del_lat) if s.map_del_lat else 0.0,
                        format="%.6f",
                        key="numerical_input_del_lat"
                    )
                    if new_del_lat != s.map_del_lat:
                        s.map_del_lat = new_del_lat
                        s.del_lat = new_del_lat
                        st.rerun()
                        
                with col_lon2:
                    new_del_lon = st.number_input(
                        "Delivery Longitude", 
                        value=float(s.map_del_lon) if s.map_del_lon else 0.0,
                        format="%.6f",
                        key="numerical_input_del_lon"
                    )
                    if new_del_lon != s.map_del_lon:
                        s.map_del_lon = new_del_lon
                        s.del_lon = new_del_lon
                        st.rerun()

            st.markdown("<div style='margin-bottom: 24px;'></div>", unsafe_allow_html=True)

        # ── PURE NATIVE GRID ALIGNMENT ENGINE WITH ISOLATED CHARCOAL STYLE ───
        st.html("""
        <style>
        /* 1. Force the final layout column wrapper to align its contents flush right */
        div[data-testid="stColumn"]:last-child {
            display: flex !important;
            justify-content: flex-end !important;
            width: 100% !important;
        }

        /* 2. Target only the secondary button inside the final column of the layout block */
        div[data-testid="stColumn"]:last-child button[data-testid*="secondary"] {
            background-color: #1E293B !important; /* Premium Slate/Charcoal Dark */
            color: #FFFFFF !important;
            border: 1px solid #0F172A !important;
            font-family: 'Source Sans Pro', -apple-system, sans-serif !important;
            font-size: 14px !important;
            font-weight: 600 !important;
            padding: 8px 20px !important;
            border-radius: 8px !important;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1) !important;
            white-space: nowrap !important; /* Forces the text to stay on a single horizontal line */
            word-break: keep-all !important;
            width: auto !important; /* Auto-sizes button tightly to match the text length */
            min-width: max-content !important;
        }
        
        /* 3. Isolated modern dark hover state transition */
        div[data-testid="stColumn"]:last-child button[data-testid*="secondary"]:hover {
            background-color: #0F172A !important; /* Deepest Charcoal on hover */
            border-color: #020617 !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 12px rgba(15, 23, 42, 0.2) !important;
        }

        /* 4. Active click compression tactile feedback */
        div[data-testid="stColumn"]:last-child button[data-testid*="secondary"]:active {
            transform: translateY(1px) !important;
        }
        </style>
        """)

        # Widened layout grid ratio slightly to [3.5, 1.5] to guarantee text has full horizontal room
        nav_spacer_col, nav_btn_col = st.columns([3.5, 1.5])
        
        with nav_btn_col:
            # Keeps the precise upward spacing shift intact
            st.html("<div style='margin-top: -24px;'></div>")
            
            # Setting use_container_width=False lets width: auto override and prevent text clipping
            if st.button("Continue to Conditions →", use_container_width=False, type="secondary", key="step1_next"):
                s.step = 2
                st.rerun()


# ─── STEP 2: CONDITIONS (FIXED ENCLOSURES & MAXIMUM COMPRESSION CODES) ───
    elif s.step == 2:
        st.markdown("""
        <div id="step-header-anchor" class="section-title" style="display: flex; align-items: center; gap: 8px; line-height: 1; margin-top: 4px;">
            <span style="white-space: nowrap;">🌤️ What's the situation outside?</span>
            <div class="custom-tooltip">
                <span class="info-trigger">i</span>
                <div class="tooltip-text">Real-world environmental factors heavily influence delivery time prediction.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


        st.markdown("<div style='margin-bottom: 24px;'></div>", unsafe_allow_html=True)
        st.markdown("<div style='margin-bottom: 4px;'></div>", unsafe_allow_html=True)

        # UNIFIED HIGH DENSITY MASTER BLOCK CONTAINER
        with st.container():
            
            # ── ROW 1: WEATHER ──
            st.markdown('<div class="compact-row-title">🌦️ Weather Conditions</div>', unsafe_allow_html=True)
            weather_opts = [
                ("☀️ Sunny", "Sunny"), ("☁️ Cloudy", "Cloudy"), ("🌫️ Fog", "Fog"), 
                ("💨 Windy", "Windy"), ("⛈️ Stormy", "Stormy"), ("🌪️ Sand", "Sandstorms")
            ]
            w_cols = st.columns(6, gap="small")
            for i, (btn_text, label) in enumerate(weather_opts):
                is_active = (s.weather == label)
                with w_cols[i]:
                    # Switched to native type configuration + static un-changing layout choice key
                    btn_type = "primary" if is_active else "secondary"
                    if st.button(btn_text, key=f"w_choice_{label}", type=btn_type, use_container_width=True):
                        s.weather = label
                        st.rerun()

            st.markdown('<div class="compact-row-divider"></div>', unsafe_allow_html=True)

            # ── ROW 2: TRAFFIC ──
            st.markdown('<div class="compact-row-title">🚦 Road Traffic Density</div>', unsafe_allow_html=True)
            traffic_opts = [("🟢 Low", "Low"), ("🟡 Medium", "Medium"), ("🟠 High", "High"), ("🔴 Jam", "Jam")]
            t_cols = st.columns(4, gap="small")
            for i, (btn_text, label) in enumerate(traffic_opts):
                is_active = (s.traffic == label)
                with t_cols[i]:
                    btn_type = "primary" if is_active else "secondary"
                    if st.button(btn_text, key=f"t_choice_{label}", type=btn_type, use_container_width=True):
                        s.traffic = label
                        st.rerun()

            st.markdown('<div class="compact-row-divider"></div>', unsafe_allow_html=True)

            # ── ROW 3: CITY ENVIRONMENT ──
            st.markdown('<div class="compact-row-title">🏙️ City Type Environment</div>', unsafe_allow_html=True)
            city_opts = [("🏙️ Metropolitan", "Metropolitan"), ("🏘️ Urban", "Urban"), ("🌾 Semi-Urban", "Semi-Urban")]
            c_cols = st.columns(3, gap="small")
            for i, (btn_text, label) in enumerate(city_opts):
                is_active = (s.city == label)
                with c_cols[i]:
                    btn_type = "primary" if is_active else "secondary"
                    if st.button(btn_text, key=f"c_choice_{label}", type=btn_type, use_container_width=True): 
                        s.city = label
                        st.rerun()

            st.markdown('<div class="compact-row-divider"></div>', unsafe_allow_html=True)

            # ── ROW 4: FESTIVAL SURGES ──
            st.markdown('<div class="compact-row-title">🎉 Festival / Holiday Period?</div>', unsafe_allow_html=True)
            fest_opts = [("🔘 No Holiday", "No"), ("🎉 Yes, Holiday Surge", "Yes")]
            f_cols = st.columns(2, gap="small")
            for i, (btn_text, label) in enumerate(fest_opts):
                is_active = (s.festival == label)
                with f_cols[i]:
                    btn_type = "primary" if is_active else "secondary"
                    if st.button(btn_text, key=f"f_choice_{label}", type=btn_type, use_container_width=True): 
                        s.festival = label
                        st.rerun()

        # ─── NAVIGATION PROGRESSION ACTIONS ROW (Mapped directly to final CSS patch keys) ───
        st.markdown('<div style="margin-top: 24px;"></div>', unsafe_allow_html=True)
        nav1, nav2 = st.columns(2, gap="medium")
        with nav1:
            if st.button("← Back to Location", use_container_width=True, key="action_nav_back", type="secondary"): 
                s.step = 1
                st.rerun()
        with nav2:
            if st.button("Continue to Driver & Vehicle →", use_container_width=True, key="action_nav_next", type="secondary"): 
                s.step = 3
                st.rerun()


    # # ── STEP 3: DRIVER & VEHICLE ─────────────
    elif s.step == 3:
        st.markdown("""
        <div id="step-header-anchor" class="step-header-wrapper" style="padding-top: 4px; margin-bottom: 24px;">
            <div class="section-title" style="display: flex; align-items: center; gap: 8px; line-height: 1; margin-top: 4px;">
                <span style="white-space: nowrap;">🏍️ Driver & Vehicle Details</span>
                <div class="custom-tooltip">
                    <span class="info-trigger">i</span>
                    <div class="tooltip-text">Delivery partner profile and vehicle type affect speed and reliability.</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="fcard-head">
            <div class="fcard-icon" style="background:#FFF0E3;">🚗</div>
            <div>
                <div class="fcard-title">Vehicle Details</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="compact-row-title">Vehicle Type</div>', unsafe_allow_html=True)

        # ─── SECTION 1: VEHICLE TYPE MATRIX (VIBRANT BLUE ACTIVE ACCENT) ───
        with st.container(border=True): 
            veh_opts = [
                ("🏍️", "motorcycle", "Fastest on city roads"),
                ("🛵", "scooter", "Nimble & efficient"),
                ("⚡", "electric_scooter", "Eco-friendly & steady"),
                ("🚲", "bicycle", "Short-range, slow"),
            ]
            v_cols = st.columns(4, gap="small")
            for i, (icon, key, desc) in enumerate(veh_opts):
                label = key.replace("_", " ").title()
                is_active = (s.vehicle_type == key)
                
                with v_cols[i]:
                    # Dynamic style scoping for custom blueprints
                    active_style = """
                        background: #F0F7FF !important;
                        border: 1px solid #007BFF !important;
                    """ if is_active else "background: #F8FAFC !important; border: 1px solid #E2E8F0 !important;"
                    text_color = "#007BFF !important;" if is_active else "#475569 !important;"

                    st.markdown(f"""
                    <style>
                        div.st-key-v_grid_{key} button {{
                            {active_style}
                            width: 100% !important;
                            border-radius: 10px !important;
                            padding: 12px 8px !important;
                            transition: all 0.15s ease-in-out !important;
                        }}
                        div.st-key-v_grid_{key} button p,
                        div.st-key-v_grid_{key} button span {{
                            color: {text_color}
                            font-weight: 700 !important;
                            font-size: 12px !important;
                        }}
                        div.st-key-v_grid_{key} button:hover {{
                            background: #E6F0FA !important;
                            border-color: #0056B3 !important;
                        }}
                    </style>
                    """, unsafe_allow_html=True)

                    btn_content = f"{icon}\n{label}\n{desc}"
                    if st.button(btn_content, key=f"v_grid_{key}", use_container_width=True): 
                        s.vehicle_type = key
                        st.rerun()

        st.markdown('<div style="margin-top: 24px;"></div>', unsafe_allow_html=True)
        
        # ─── SECTION 2: VEHICLE CONDITION & DELIVERIES GRID ───
        with st.container(border=True):
            st.markdown('<div class="compact-row-title">Vehicle Condition</div>', unsafe_allow_html=True)
            cond_opts = [
                ("💀", "0", "Poor", "needs repair"),
                ("⚠️", "1", "Fair", "functional"),
                ("✅", "2", "Good", "well maintained"),
                ("🏆", "3", "Excellent", "new/premium")
            ]
            cond_cols = st.columns(4, gap="small")
            for i, (icon, val, title, desc) in enumerate(cond_opts):
                is_active = (s.vehicle_condition == int(val))
                
                with cond_cols[i]:
                    # 🚀 INTRODUCE CRITICAL COLOR HIERARCHY
                    if is_active:
                        if val == "0":  # 🛑 CRITICAL WARNING STATE FOR POOR CONDITION
                            bg_style = "background: #FFF5F5 !important; border: 1px solid #DC3545 !important;"
                            text_color = "#DC3545 !important;"
                            hover_bg = "#FEE2E2 !important;"
                            hover_border = "#B91C1C !important;"
                        else:  # 🔵 STANDARD REASSURING BLUE FOR SAFE STATES
                            bg_style = "background: #F0F7FF !important; border: 1px solid #007BFF !important;"
                            text_color = "#007BFF !important;"
                            hover_bg = "#E6F0FA !important;"
                            hover_border = "#0056B3 !important;"
                    else:
                        bg_style = "background: #F8FAFC !important; border: 1px solid #E2E8F0 !important;"
                        text_color = "#475569 !important;"
                        hover_bg = "#F1F5F9 !important;"
                        hover_border = "#CBD5E1 !important;"

                    st.markdown(f"""
                    <style>
                        div.st-key-vc_grid_{val} button {{
                            {bg_style}
                            width: 100% !important;
                            border-radius: 10px !important;
                            padding: 12px 8px !important;
                            transition: all 0.15s ease-in-out !important;
                        }}
                        div.st-key-vc_grid_{val} button p,
                        div.st-key-vc_grid_{val} button span {{
                            color: {text_color}
                            font-weight: 700 !important;
                            font-size: 12px !important;
                        }}
                        div.st-key-vc_grid_{val} button:hover {{
                            background: {hover_bg}
                            border-color: {hover_border}
                        }}
                    </style>
                    """, unsafe_allow_html=True)

                    btn_content = f"{icon}\n{title}\n{desc}"
                    if st.button(btn_content, key=f"vc_grid_{val}", use_container_width=True): 
                        s.vehicle_condition = int(val)
                        st.rerun()

            st.markdown("<div style='margin-bottom: 24px;'></div>", unsafe_allow_html=True)
            
            # ─── SECTION 3: CONCURRENT DELIVERIES (VIBRANT BLUE ACTIVE ACCENT) ───
            st.markdown('<div class="compact-row-title">Concurrent Deliveries</div>', unsafe_allow_html=True)
            md_opts = [
                ("1️⃣", "0", "Single order", ""),
                ("2️⃣", "1", "2 orders", ""),
                ("3️⃣", "2", "3 orders", ""),
                ("4️⃣", "3", "4 orders", "")
            ]
            md_cols = st.columns(4, gap="small")
            for i, (icon, val, title, desc) in enumerate(md_opts):
                is_active = (s.multiple_deliveries == int(val))
                
                with md_cols[i]:
                    active_style = """
                        background: #F0F7FF !important;
                        border: 1px solid #007BFF !important;
                    """ if is_active else "background: #F8FAFC !important; border: 1px solid #E2E8F0 !important;"
                    text_color = "#007BFF !important;" if is_active else "#475569 !important;"

                    st.markdown(f"""
                    <style>
                        div.st-key-md_grid_{val} button {{
                            {active_style}
                            width: 100% !important;
                            border-radius: 10px !important;
                            padding: 12px 8px !important;
                            transition: all 0.15s ease-in-out !important;
                        }}
                        div.st-key-md_grid_{val} button p,
                        div.st-key-md_grid_{val} button span {{
                            color: {text_color}
                            font-weight: 700 !important;
                            font-size: 12px !important;
                        }}
                        div.st-key-md_grid_{val} button:hover {{
                            background: #E6F0FA !important;
                            border-color: #0056B3 !important;
                        }}
                    </style>
                    """, unsafe_allow_html=True)

                    btn_content = f"{icon}\n{title}"
                    if st.button(btn_content, key=f"md_grid_{val}", use_container_width=True): 
                        s.multiple_deliveries = int(val)
                        st.rerun()

        st.markdown('<div style="margin-top: 24px;"></div>', unsafe_allow_html=True)

                # ─── ⏱️ DISPATCH & TIMING PARAMETERS (FULL WIDTH SUB-SECTION) ───
        st.markdown("""
        <div style="font-family: 'Bricolage Grotesque', sans-serif; font-size: 14px; font-weight: 700; color: #1E293B; margin: 24px 0 12px 0; display: flex; align-items: center; gap: 6px;">
            <span>⏱️ Dispatch & Timing Parameters</span>
        </div>
        """, unsafe_allow_html=True)

        # 1. State Mapping Framework: Resolve current memory states safely into target keys
        TIME_SLOTS = {
            "Morning Rush": ("🌅", "09:00"),
            "Lunch Surge":  ("⚡", "13:15"),
            "Afternoon Slack": ("🌤️", "16:00"),
            "Dinner Peak":  ("🛵", "20:30"),
            "Midnight Off-peak": ("🌙", "23:45")
        }

        # Inverse tracking to figure out what is currently highlighted
        import datetime
        if isinstance(s.time_ordered, datetime.time):
            current_time_str = s.time_ordered.strftime("%H:%M")
        else:
            current_time_str = str(s.time_ordered)

        # 2. Render the 5 Symmetrical Pill Grid Columns
        time_cols = st.columns(5, gap="small")
        selected_slot = None

        for idx, (slot_name, (icon, time_val)) in enumerate(TIME_SLOTS.items()):
            with time_cols[idx]:
                # Evaluate if this specific button instance is the active state
                is_active = (current_time_str == time_val)
                
                # Configure premium pastel color blocks to match traffic density systems
                if is_active:
                    bg_style = "background: #FFF5F2 !important; border: 1px solid #FFCDBC !important; color: #E8471E !important; font-weight: 700 !important;"
                    text_color_css = "#E8471E !important;"
                    selected_slot = slot_name
                else:
                    bg_style = "background: #F8FAFC !important; border: 1px solid #E2E8F0 !important; color: #475569 !important; font-weight: 500 !important;"
                    text_color_css = "#475569 !important;"

                # Dynamic custom layout button wrapper block
                st.markdown(f"""
                <style>
                    div.st-key-time_slot_btn_{idx} button {{
                        {bg_style}
                        width: 100% !important;
                        height: 44px !important;
                        border-radius: 10px !important;
                        padding: 0px 4px !important;
                        transition: all 0.2s ease-in-out !important;
                        box-shadow: none !important;
                        display: flex !important;
                        align-items: center !important;
                        justify-content: center !important;
                    }}
                    div.st-key-time_slot_btn_{idx} button:hover {{
                        background: #FFEAE3 !important;
                        border-color: #FFB39B !important;
                    }}
                    /* FIXED: Style the internal text element instead of hiding it */
                    div.st-key-time_slot_btn_{idx} button p,
                    div.st-key-time_slot_btn_{idx} button span {{
                        color: {text_color_css}
                        font-size: 11.5px !important;
                        font-weight: 700 !important;
                        white-space: nowrap !important;
                        margin: 0px !important;
                        padding: 0px !important;
                    }}
                    div.st-key-time_slot_btn_{idx} button:hover p,
                    div.st-key-time_slot_btn_{idx} button:hover span {{
                        color: #CD3713 !important;
                    }}
                </style>
                <div class="custom-time-pill-frame">
                """, unsafe_allow_html=True)

                # Native action button acting as the card trigger frame
                if st.button(f"{icon} {slot_name}", key=f"time_slot_btn_{idx}", use_container_width=True):
                    s.time_ordered = time_val
                    st.rerun()

                st.markdown("</div>", unsafe_allow_html=True)

                # ── CONTAINER 3: DRIVER PROFILE ──
        st.markdown("""
        <div class="fcard-head">
            <div class="fcard-icon" style="background:#EFF6FF;">👤</div>
            <div>
                <div class="fcard-title">Driver Profile</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.container(border=True):
            da_col, dr_col, dt_col = st.columns(3, gap="medium")
            
            with da_col:
                s.age = st.number_input("Driver Age", min_value=18, max_value=65, value=int(s.age), step=1, key="driver_age_input")
                
            with dr_col:
                # 🚀 PIXEL FIX: Unified vertical wrapper alignment container
                st.markdown("""
                <div style="display: flex; flex-direction: column; justify-content: flex-start; padding-top: 1px;">
                    <div style="font-size: 14px; font-weight: 500; color: #31333F; margin-bottom: 11px; text-transform: uppercase; font-size: 12px; letter-spacing: 0.5px;">Driver Rating ★</div>
                </div>
                """, unsafe_allow_html=True)
                
                # INTERACTIVE STAR FEEDBACK ENGINE
                target_star_idx = max(0, min(4, int(s.rating) - 1))
                
                if "driver_star_rating" not in st.session_state:
                    st.session_state.driver_star_rating = target_star_idx
                
                selected_star = st.feedback(
                    "stars", 
                    key="driver_star_rating"
                )
                
                if selected_star is not None:
                    new_rating = float(selected_star + 1)
                    if s.rating != new_rating:
                        s.rating = new_rating
                        st.rerun()

                # High-utility micro-copy tracker below stars
                st.markdown(f"""
                <div class="slider-stars-wrapper" style="margin-top: 5px;">
                    <div class="star-rating-row" style="font-size: 13px; font-weight: 600; color: #64748B;">
                        Score: <span class="star-rating-val" style="color: #FF843D; font-weight: 700;">{s.rating:.1f} / 5.0</span>
                    </div>
                </div>
                """, unsafe_allow_html=True) 

        # ─── NAVIGATION PROGRESSION ACTIONS ROW ───
        st.markdown('<div style="margin-top: 32px;"></div>', unsafe_allow_html=True)
        nav1, nav2 = st.columns(2, gap="medium")
        with nav1:
            if st.button("← Back to Conditions", use_container_width=True, key="action_nav_back", type="secondary"): 
                s.step = 2
                st.rerun()
        with nav2:
            if st.button("Review & Predict →", use_container_width=True, key="action_nav_next", type="primary"): 
                s.step = 4
                st.rerun()

    # ── STEP 4: PREDICT (FULL-WIDTH EMBEDDED REVEAL INFERENCE) ───
    elif s.step == 4:
        from datetime import datetime, timedelta
        
        # 🚀 Clean target marker sitting right above your result-card markup block
        # ─── CRITICAL FIX: INITIALIZE VALID PLACEHOLDER TO PREVENT NAMEERRORS ───
        card_html = "<div style='display:none;'></div>"

        # # ─── CRITICAL FIX: USE A VALID BLANK CONTAINER TO SATISFY ST.HTML ───
        # card_html = "<div style='display:none;'></div>"
        dist = haversine(s.rest_lat, s.rest_lon, s.del_lat, s.del_lon)

        # 🚀 CUSTOM CSS ARCHITECTURE: Strips parent grid layout restraints and centers the full block stack
        st.markdown("""
        <style>
        /* Force structural layout container rows to stack vertically instead of side-by-side */
        div[data-testid="stHorizontalBlock"]:has(.receipt-container) {
            display: block !important;
            width: 100% !important;
        }
        
        div[data-testid="stHorizontalBlock"]:has(.receipt-container) > div[data-testid="stColumn"] {
            width: 100% !important;
            max-width: 100% !important;
            flex: none !important;
        }
        
        /* Premium Centered Digital Receipt Checkout Block */
        .receipt-container {
            background: #FFFFFF;
            border: 2px dashed #E2E8F0;
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
            margin-bottom: 24px;
            position: relative;
            max-width: 650px;
            margin-left: auto !important;
            margin-right: auto !important;
        }
        
        /* Compact balanced layout parameters */
        .receipt-grid {
            display: grid !important;
            grid-template-columns: 1fr 1fr !important;
            gap: 12px !important;
            margin-top: 20px;
        }
        
        .receipt-item {
            background: var(--cream2) !important;
            border: 1px solid transparent !important;
            border-radius: 10px;
            padding: 11px 14px;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }
        
        .receipt-item:hover {
            background: #FFF0E3 !important;
            border: 1px solid #FF843D !important;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(255, 132, 61, 0.08);
        }

        .receipt-item:hover * {
            color: #E25C00 !important;
        }

        /* 🚀 REVEAL LAYOUT WRAPPER: Centers the dark result card down below at exact matching pixel width */
        .reveal-layout-wrapper {
            max-width: 650px;
            margin-left: auto !important;
            margin-right: auto !important;
            margin-top: 28px;
            animation: slideRevealFade 0.45s cubic-bezier(0.16, 1, 0.3, 1);
        }

        @keyframes slideRevealFade {
            from { opacity: 0; transform: translateY(16px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .centered-btn-row {
            max-width: 650px;
            margin-left: auto !important;
            margin-right: auto !important;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

        st.markdown("""
        <div id="step-header-anchor" style="max-width: 650px; margin-left: auto; margin-right: auto;">
            <div class="section-title" style="display: flex; align-items: center; gap: 8px;">
                ⚡ All set — let's predict!
                <div class="custom-tooltip">
                    <span class="info-trigger">i</span>
                    <div class="tooltip-text">Review your final inputs below, then hit Predict to run ML inference.</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


                # ── PREMIUM RECEIPT SUMMARY CARD CONTAINER ──
        tb_badge = TRAFFIC_BADGE.get(s.traffic, "ib-blue")
        st.markdown(f"""
        <div class="receipt-container">
          <div class="fcard-head" style="border-bottom: 1px solid #F1F5F9; padding-bottom: 14px; margin-bottom: 8px;">
            <div class="fcard-icon" style="background:#FFF0E3;">📋</div>
            <div>
              <div class="fcard-title" style="font-size: 18px; font-weight: 700; color: var(--ink);">Order Snapshot Breakdown</div>
            </div>
          </div>
          <div class="receipt-grid" style="margin-bottom: 24px;">
            <div class="receipt-item">
              <div style="font-size:10px; font-weight:800; letter-spacing:1px; text-transform:uppercase; color:var(--ink4);">📐 Route Distance</div>
              <div style="font-size:18px; font-weight:800; color:var(--ink); margin-top:3px;">{dist:.2f} <span style="font-size:13px; font-weight:500; color:var(--ink3);">km</span></div>
            </div>
            <div class="receipt-item">
              <div style="font-size:10px; font-weight:800; letter-spacing:1px; text-transform:uppercase; color:var(--ink4);">🕐 Ordered At Time</div>
              <div style="font-size:18px; font-weight:800; color:var(--ink); margin-top:3px;">{s.time_ordered}</div>
            </div>
            <div class="receipt-item">
              <div style="font-size:10px; font-weight:800; letter-spacing:1px; text-transform:uppercase; color:var(--ink4);">{WEATHER_ICON.get(s.weather,"🌤️")} Weather State</div>
              <div style="font-size:15px; font-weight:700; color:var(--ink); margin-top:3px;">{s.weather}</div>
            </div>
            <div class="receipt-item">
              <div style="font-size:10px; font-weight:800; letter-spacing:1px; text-transform:uppercase; color:var(--ink4);">🚦 Traffic Density</div>
              <div style="margin-top:5px;"><span class="inline-badge {tb_badge}">{s.traffic}</span></div>
            </div>
            <div class="receipt-item">
              <div style="font-size:10px; font-weight:800; letter-spacing:1px; text-transform:uppercase; color:var(--ink4);">{VEH_ICON.get(s.vehicle_type,"🛵")} Assigned Vehicle</div>
              <div style="font-size:15px; font-weight:700; color:var(--ink); margin-top:3px;">{s.vehicle_type.replace("_"," ").title()}</div>
            </div>
            <div class="receipt-item">
              <div style="font-size:10px; font-weight:800; letter-spacing:1px; text-transform:uppercase; color:var(--ink4);">⭐ Courier Performance</div>
              <div style="font-size:15px; font-weight:700; color:#F59E0B; margin-top:3px;">{"★"*int(s.rating)}{"☆"*(5-int(s.rating))} {s.rating:.1f}</div>
            </div>
            <div class="receipt-item">
              <div style="font-size:10px; font-weight:800; letter-spacing:1px; text-transform:uppercase; color:var(--ink4);">🏙️ City Profile</div>
              <div style="font-size:15px; font-weight:700; color:var(--ink); margin-top:3px;">{s.city}</div>
            </div>
            <div class="receipt-item">
              <div style="font-size:10px; font-weight:800; letter-spacing:1px; text-transform:uppercase; color:var(--ink4);">🎉 Festival Window</div>
              <div style="font-size:15px; font-weight:700; color:var(--ink); margin-top:3px;">{'🎉 Active Campaign' if s.festival=="Yes" else '— Standard Hours'}</div>
            </div>
          </div>
        """, unsafe_allow_html=True)

        # # ─── RE-ENGINEERED BUTTON CONTAINER BLOCK TO PREVENT ROW CLIPPING ───
        # ─── PREMIUM ISOLATED INTERACTION STYLE ENGINE ───
        # Custom HTML class namespace isolation completely shields the layout from global style pollution
        st.markdown("""
        <style>
            /* 1. Define the Glow Pulse Animation Keyframes */
            @keyframes ctaGlowPulse {
                0% {
                    box-shadow: 0 0 0 0 rgba(232, 71, 30, 0.4);
                    transform: scale(1);
                }
                50% {
                    box-shadow: 0 0 15px 4px rgba(255, 122, 89, 0.6);
                    transform: scale(1.015) !important;
                }
                100% {
                    box-shadow: 0 0 0 0 rgba(232, 71, 30, 0);
                    transform: scale(1);
                }
            }

            /* 2. SPECIFIC WRAPPER SCOPE: Enforces the premium gradient trail over the button chassis */
            div.premium-cta-row-wrapper div.st-key-action_nav_predict button {
                background: linear-gradient(135deg, #E8471E 0%, #FF7A59 100%) !important;
                background-color: #E8471E !important;
                border: none !important;
                border-radius: 10px !important;
                height: 46px !important;
                min-height: 46px !important;
                width: 100% !important;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
                cursor: pointer !important;
            }

            /* 3. Typography configuration */
            div.premium-cta-row-wrapper div.st-key-action_nav_predict button p,
            div.premium-cta-row-wrapper div.st-key-action_nav_predict button span {
                color: #FFFFFF !important;
                font-size: 13.5px !important;
                font-weight: 700 !important;
                letter-spacing: 0.3px !important;
                margin: 0px !important;
                padding: 0px !important;
            }

            /* 4. Trigger premium hover state animations exclusively within our namespace */
            div.premium-cta-row-wrapper div.st-key-action_nav_predict button:hover {
                background: linear-gradient(135deg, #CD3713 0%, #E8471E 100%) !important;
                animation: ctaGlowPulse 1.2s infinite ease-in-out !important;
            }
            
            /* Active click/press adjustments */
            div.premium-cta-row-wrapper div.st-key-action_nav_predict button:active {
                transform: scale(0.98) !important;
                box-shadow: none !important;
            }
        </style>
        <div class="premium-cta-row-wrapper">
        """, unsafe_allow_html=True)

        with st.container():
            # Compact the Predict button horizontally by introducing an asymmetrical grid distribution
            back_col, pred_col, spacer_col = st.columns([1.5, 1.8, 0.7], gap="small", vertical_alignment="bottom")
            
            with back_col:
                if st.button("← Edit Details", use_container_width=True, key="action_nav_back_to_3", type="secondary"): 
                    s.step = 3
                    s.prediction = None
                    st.rerun()
                    
            with pred_col:
                predict_hit = st.button("🚀 Predict My Delivery Time!", use_container_width=True, key="action_nav_predict", type="primary")
            
            with spacer_col:
                pass
        
        # Close out the custom identifier namespace div element
        st.markdown("</div>", unsafe_allow_html=True)
        
        # ─── CLEAN, MULTI-CONTAINER BOUNDARY BREAK ───
        st.markdown("<div style='clear: both; display: block; width: 100%; height: 1px;'></div>", unsafe_allow_html=True)

                # ─── MODEL PROCESSING PIPELINE SCOPE ───
        # ─── MODEL PROCESSING PIPELINE SCOPE ───
                # ─── MODEL PROCESSING PIPELINE SCOPE ───
        if predict_hit:
            import datetime
            if isinstance(s.time_ordered, datetime.time):
                formatted_time_str = s.time_ordered.strftime("%H:%M")
            else:
                formatted_time_str = str(s.time_ordered)

            # Build input dataframe exactly matching model training requirements
            input_df = pd.DataFrame({
                'Restaurant_latitude':         [s.rest_lat],
                'Restaurant_longitude':        [s.rest_lon],
                'Delivery_location_latitude':  [s.del_lat],
                'Delivery_location_longitude': [s.del_lon],
                'Time_Orderd':                 [formatted_time_str], 
                'Delivery_person_Age':         [int(s.age)],
                'Delivery_person_Ratings':     [float(s.rating)],
                'Vehicle_condition':           [int(s.vehicle_condition)],
                'multiple_deliveries':         [int(s.multiple_deliveries)],
                'Weather_conditions':          [s.weather],
                'Type_of_vehicle':             [s.vehicle_type],
                'Festival':                    [s.festival],
                'City':                        [s.city],
                'Road_traffic_density':        [s.traffic],
            })

            # ─── 🚀 IMMERSIVE ML SYNTHESIS STATE LOAD ENGINE ───
            synthesis_placeholder = st.empty()
            with synthesis_placeholder.container():
                st.markdown("""
                <style>
                    @keyframes progressFill { 0% { width: 0%; } 100% { width: 100%; } }
                    @keyframes itemPulse { 0% { opacity: 0.4; } 50% { opacity: 1; } 100% { opacity: 0.4; } }
                    .synthesis-card { background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 16px; padding: 28px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05); margin: 20px 0; }
                    .synthesis-title { font-size: 15px; font-weight: 700; color: #0F172A; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px; }
                    .synthesis-subtitle { font-size: 12.5px; color: #64748B; margin-bottom: 20px; }
                    .meter-track { background: #F1F5F9; height: 6px; border-radius: 10px; width: 100%; overflow: hidden; margin-bottom: 24px; }
                    .meter-fill { background: linear-gradient(90deg, #007BFF, #00FFCC); height: 100%; border-radius: 10px; width: 100%; animation: progressFill 1.2s cubic-bezier(0.4, 0, 0.2, 1) forwards; }
                    .step-item { display: flex; align-items: center; gap: 10px; font-size: 13px; color: #334155; margin-bottom: 12px; font-weight: 500; }
                    .step-item.p1 { animation: itemPulse 0.4s ease-in-out 2; }
                    .step-item.p2 { animation: itemPulse 0.4s ease-in-out 2 0.3s; }
                    .step-item.p3 { animation: itemPulse 0.4s ease-in-out 2 0.6s; }
                    .step-badge { background: #E0F2FE; color: #0369A1; font-size: 10px; font-weight: 700; padding: 2px 6px; border-radius: 4px; text-transform: uppercase; }
                </style>
                <div class="synthesis-card">
                    <div class="synthesis-title">🧠 Initialising DropTime Synthesis Engine</div>
                    <div class="synthesis-subtitle">Running structural multi-variable Random Forest matrix evaluations...</div>
                    <div class="meter-track"><div class="meter-fill"></div></div>
                    <div class="step-item p1"><span class="step-badge">Phase 1</span><span>📐 Compiling Haversine geodesic distance vectors across coordinate pairs...</span></div>
                    <div class="step-item p2"><span class="step-badge">Phase 2</span><span>🚦 Hot-encoding categorical weather profiles and road traffic densities...</span></div>
                    <div class="step-item p3"><span class="step-badge">Phase 3</span><span>⭐ Scaling driver ratings and vehicle specifications against ensemble trees...</span></div>
                </div>
                """, unsafe_allow_html=True)
                
                import time
                time.sleep(1.25)

            synthesis_placeholder.empty()

            if model:
                try:
                    s.prediction = float(model.predict(input_df)[0])
                    s.demo_mode = False
                except Exception as e:
                    dist = haversine(s.rest_lat, s.rest_lon, s.del_lat, s.del_lon)
                    p = {"Jam":18,"High":10,"Medium":4,"Low":0}
                    w = {"Stormy":12,"Sandstorms":10,"Fog":8,"Windy":4,"Cloudy":2,"Sunny":0}
                    base = max(10, dist*4.2 + (30-s.age*0.15) + (5-s.rating)*3.5)
                    s.prediction = base + p.get(s.traffic,0) + w.get(s.weather,0) + (8 if s.festival=="Yes" else 0) + s.multiple_deliveries*3
                    s.demo_mode = True
                    import sys
                    print(f"Inference Crash Fallback: {e}", file=sys.stderr)
            else:
                dist = haversine(s.rest_lat, s.rest_lon, s.del_lat, s.del_lon)
                p = {"Jam":18,"High":10,"Medium":4,"Low":0}
                w = {"Stormy":12,"Sandstorms":10,"Fog":8,"Windy":4,"Cloudy":2,"Sunny":0}
                base = max(10, dist*4.2 + (30-s.age*0.15) + (5-s.rating)*3.5)
                s.prediction = base + p.get(s.traffic,0) + w.get(s.weather,0) + (8 if s.festival=="Yes" else 0) + s.multiple_deliveries*3
                s.demo_mode = True

            import random
            if 'PHRASES' in globals():
                s.phrase_idx = random.randint(0, len(PHRASES) - 1)
            
            st.rerun()

        # ─── BOTTOM BLOCK: THE REVEAL DISPLAY GATE ───
        # ─── BOTTOM BLOCK: THE REVEAL DISPLAY GATE ───
        if s.prediction is not None:
            pred = s.prediction
            lo = max(1, pred * 0.88)
            hi = pred * 1.14
            conf = min(97, max(68, 93 - haversine(s.rest_lat, s.rest_lon, s.del_lat, s.del_lon) * 0.6))

            distance_impact = 0
            traffic_impact  = 0
            weather_impact  = 0
            driver_impact   = 0
            city_impact     = 0

            # ─── 1. RE-ENGAGED MODEL PROCESSING PIPELINE SHAP EXTRACTOR ───
            if model and not s.demo_mode:
                try:
                    import datetime
                    if isinstance(s.time_ordered, datetime.time):
                        formatted_time_str = s.time_ordered.strftime("%H:%M")
                    else:
                        formatted_time_str = str(s.time_ordered)

                    import pandas as pd
                    import numpy as np

                    local_input_df = pd.DataFrame({
                        'Restaurant_latitude':         [float(s.rest_lat)],
                        'Restaurant_longitude':        [float(s.rest_lon)],
                        'Delivery_location_latitude':  [float(s.del_lat)],
                        'Delivery_location_longitude': [float(s.del_lon)],
                        'Time_Orderd':                 [formatted_time_str], 
                        'Delivery_person_Age':         [int(s.age)],
                        'Delivery_person_Ratings':     [float(s.rating)],
                        'Vehicle_condition':           [int(s.vehicle_condition)],
                        'multiple_deliveries':         [int(s.multiple_deliveries)],
                        'Weather_conditions':          [str(s.weather)],
                        'Type_of_vehicle':             [str(s.vehicle_type)],
                        'Festival':                    [str(s.festival)],
                        'City':                        [str(s.city)],
                        'Road_traffic_density':        [str(s.traffic)],
                    })

                    single_row_preprocessed = model.named_steps['preprocessing'].transform(local_input_df)
                    shap_output = explainer.shap_values(single_row_preprocessed)
                    
                    if isinstance(shap_output, list):
                        row_contributions = np.array(shap_output).flatten()
                    elif len(shap_output.shape) == 3:
                        row_contributions = shap_output[0, 0, :]
                    elif len(shap_output.shape) == 2:
                        row_contributions = shap_output[0, :]
                    else:
                        row_contributions = np.array(shap_output).flatten()
                        
                    feature_names = model.named_steps['preprocessing'].get_feature_names_out()
                    shap_dict = dict(zip(feature_names, row_contributions))
                    
                    distance_impact = int(round(sum(v for k, v in shap_dict.items() if "latitude" in k.lower() or "longitude" in k.lower() or "distance" in k.lower())))
                    traffic_impact  = int(round(sum(v for k, v in shap_dict.items() if "traffic" in k.lower())))
                    weather_impact  = int(round(sum(v for k, v in shap_dict.items() if "weather" in k.lower())))
                    driver_impact   = int(round(sum(v for k, v in shap_dict.items() if "rating" in k.lower() or "age" in k.lower())))
                    city_impact     = int(round(sum(v for k, v in shap_dict.items() if "city" in k.lower() or "festival" in k.lower())))
                except Exception as shap_err:
                    distance_impact = max(0, int(dist * 1.5) - 3)
                    traffic_impact  = {"Low": -4, "Medium": 2, "High": 6, "Jam": 12}.get(s.traffic, 0)
                    weather_impact  = {"Sunny": -3, "Cloudy": -1, "Windy": 1, "Fog": 4, "Sandstorms": 7, "Stormy": 10}.get(s.weather, 0)
                    driver_impact   = int((3.5 - s.rating) * 3)
                    city_impact     = {"Metropolitian": 4, "Metropolitan": 4, "Urban": 2, "Semi-Urban": -2}.get(s.city, 0)
            else:
                distance_impact = max(0, int(dist * 1.5) - 3)
                traffic_impact  = {"Low": -4, "Medium": 2, "High": 6, "Jam": 12}.get(s.traffic, 0)
                weather_impact  = {"Sunny": -3, "Cloudy": -1, "Windy": 1, "Fog": 4, "Sandstorms": 7, "Stormy": 10}.get(s.weather, 0)
                driver_impact   = int((3.5 - s.rating) * 3)
                city_impact     = {"Metropolitian": 4, "Metropolitan": 4, "Urban": 2, "Semi-Urban": -2}.get(s.city, 0)

            # ─── 2. LOAD VARIABLES SECURELY INTO THE RENDERING INPUT MATRIX ───
            raw_impacts = [
                ("📐", "Distance", distance_impact, f"{dist:.1f}km"),
                ("🚦", "Traffic", traffic_impact, str(s.traffic)),
                ("🌤️", "Weather", weather_impact, str(s.weather)),
                ("⭐", "Driver", driver_impact, f"★{s.rating:.1f}"),
                ("🏙️", "City", city_impact, str(s.city).split("-")[0]),
            ]

            if pred < 25:   cat, cat_col, cat_emoji = "Express", "ib-green", "⚡"
            elif pred < 40: cat, cat_col, cat_emoji = "On Schedule", "ib-blue", "✅"
            elif pred < 55: cat, cat_col, cat_emoji = "Standard", "ib-amber", "🕐"
            else:           cat, cat_col, cat_emoji = "Delayed", "ib-red", "⚠️"

            import datetime
            try:
                if isinstance(s.time_ordered, datetime.time):
                    dummy_today = datetime.date.today()
                    combined_dt = datetime.datetime.combine(dummy_today, s.time_ordered)
                    arrive = (combined_dt + timedelta(minutes=pred)).strftime("%I:%M %p")
                else:
                    arrive = (datetime.datetime.strptime(str(s.time_ordered), "%H:%M") + timedelta(minutes=pred)).strftime("%I:%M %p")
            except Exception:
                arrive = "—"

            phrase = PHRASES[s.phrase_idx % len(PHRASES)].format(int(pred)) if 'PHRASES' in globals() else "In transit..."
            demo_note = ' <span style="font-size:10px;opacity:.6">(demo)</span>' if s.demo_mode else ""

            # Inject the animated layout wrapper block cleanly matching constraints
            st.markdown(f'<div class="reveal-layout-wrapper">', unsafe_allow_html=True)
            
            card_html = f"""
            <div class="result-card" style="margin-bottom: 20px;">
                <div class="rc-inner">
                    <span class="rc-emoji">🛵</span>
                    <div class="rc-eyebrow">ML Predicted ETA{demo_note}</div>
                    <div class="rc-number">{int(pred)}</div>
                    <div class="rc-unit">minutes</div>
                    <div class="rc-phrase">{phrase}</div>
                    <div style="margin-bottom:14px">
                        <span class="inline-badge {cat_col}">{cat_emoji} {cat}</span>
                    </div>
                    <div class="rc-chips">
                        <div class="rc-chip">🕐 Best <strong>{int(lo)} min</strong></div>
                        <div class="rc-chip">📍 Expected <strong>{int(pred)} min</strong></div>
                        <div class="rc-chip">⏱️ Worst <strong>{int(hi)} min</strong></div>
                    </div>
                    <div class="rc-conf-row">
                        <span>Confidence</span>
                        <span>{conf:.0f}%</span>
                    </div>
                    <div class="rc-conf-track">
                        <div class="rc-conf-fill" style="width:{conf}%"></div>
                    </div>
                    <div class="rc-arrive">🕐 Arrives approx. <strong>{arrive}</strong></div>
                </div>
            </div>
            """
            st.html(card_html)
            
            # # ─── 3. RENDER IMPACT BREAKDOWN SECTION HEADER ───
            # ─── 1. GLOBAL DASHBOARD GLASSMORPHIC LAYER STYLING ───
            st.markdown("""
            <style>
                .glass-fcard {
                    background: rgba(255, 255, 255, 0.03) !important;
                    backdrop-filter: blur(16px) saturate(180%) !important;
                    -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
                    border: 1px solid rgba(226, 232, 240, 0.4) !important;
                    border-radius: 16px !important;
                    padding: 24px !important;
                    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.01) !important;
                    margin-top: 16px !important;
                    margin-bottom: 16px !important;
                }
                .glass-fcard-body {
                    display: flex !important;
                    flex-direction: column !important;
                    gap: 12px !important;
                    margin-top: 14px !important;
                }
            </style>
            """, unsafe_allow_html=True)

            # ─── 2. COMPUTE GLASSMORPHIC IMPACT BREAKDOWN CARD CONTENT ───
            MAX_MINUTES_SCALE = 15 
            chart_rows_html = ""

            # Build each row of the diverging chart as an HTML string block
            for icon, name, minutes, val in raw_impacts:
                pct_width = min(100, abs(int((minutes / MAX_MINUTES_SCALE) * 100)))
                
                if minutes >= 0:
                    bar_color = "#FF4B4B"  # Electric Orange/Red for delays
                    left_fill = "<div></div>"
                    right_fill = f'<div style="width:{pct_width}%; background:{bar_color}; height:100%; border-radius:2px;"></div>'
                    display_text = f"+{minutes}m" if minutes > 0 else "0m"
                else:
                    bar_color = "#00CC66"  # Cyber Lime Green for savings
                    left_fill = f'<div style="width:{pct_width}%; background:{bar_color}; height:100%; border-radius:2px;"></div>'
                    right_fill = "<div></div>"
                    display_text = f"{minutes}m"

                # Append rows cleanly as flat structural HTML elements
                chart_rows_html += f"""
                <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:14px; font-size:13px; font-family:sans-serif; border-bottom:1px solid rgba(226, 232, 240, 0.2); padding-bottom:10px;">
                    <span style="width:120px; font-weight:600; color:#1E293B; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; text-align:left;">{icon} {name}</span>
                    
                    <div style="flex-grow:1; display:flex; align-items:center; height:24px; margin:0 14px; position:relative;">
                        <div style="width:50%; display:flex; justify-content:flex-end; height:6px; background:#E5E7EB; border-radius:4px 0 0 4px;">
                            {left_fill}
                        </div>
                        <div style="width:2px; height:14px; background:#1C1917; z-index:2; position:relative; flex-shrink:0;"></div>
                        <div style="width:50%; display:flex; justify-content:flex-start; height:6px; background:#E5E7EB; border-radius:0 4px 4px 0;">
                            {right_fill}
                        </div>
                    </div>
                    
                    <div style="text-align:right; min-width:100px; font-size:12px; display:flex; justify-content:space-between; gap:12px; flex-shrink:0;">
                        <span style="color:#64748B; font-weight:500; text-align:left; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">{val}</span>
                        <span style="font-weight:700; color:{bar_color}; width:45px; text-align:right; flex-shrink:0;">{display_text}</span>
                    </div>
                </div>
                """

            # 🚀 CRITICAL FIX: Combined the entire structure and rendered via native st.html() to force card compilation
            breakdown_card_html = f"""
            <div class="glass-fcard">
                <div class="fcard-head" style="display:flex; align-items:center; gap:10px; border-bottom: 1px solid rgba(226, 232, 240, 0.4); padding-bottom:12px; margin-bottom:14px;">
                    <div class="fcard-icon" style="background:#FFF0E3; padding:4px 8px; border-radius:6px;">📊</div>
                    <div class="fcard-title" style="font-family:'Bricolage Grotesque',sans-serif; font-size:14px; font-weight:700; color:#1C1917;">Impact Breakdown</div>
                </div>
                <div class="glass-fcard-body">
                    {chart_rows_html}
                </div>
            </div>
            """
            st.html(breakdown_card_html)


            # ─── 3. DYNAMIC METRIC CHECKLIST & CHIEF BOTTLENECK PARSER ───
            sorted_by_impact = sorted(raw_impacts, key=lambda x: x[2])
            max_saver = sorted_by_impact[0]    
            max_penalty = sorted_by_impact[-1] 

            tips = []

            # Core Actionable Insights Generator (Corrected indices to target name [1] and minutes)
            if max_penalty[2] > 0:
                tips.append((
                    "⚠️", 
                    "#FEF2F2", 
                    f"<strong>{max_penalty[1]} profile ({max_penalty[2]:+d}m)</strong> represents the primary model delay factor for this dispatch sequence. Rest of the route vector parameters remain steady."
                ))
            elif max_saver[2] < 0:
                tips.append((
                    "⚡", 
                    "#F0FDF4", 
                    f"<strong>{max_saver[1]} selection ({max_saver[2]:+d}m)</strong> is actively driving route optimization parameters, outperforming baseline timeline expectations."
                ))

            if s.traffic == "Jam": tips.append(("🔴", "#FEF2F2", "<strong>Traffic gridlock.</strong> Consider alerting your customer to a likely delay."))
            if s.weather in ["Stormy", "Sandstorms"]: tips.append(("⛈️", "#FFF7ED", f"<strong>{s.weather}.</strong> Delivery safety may be impacted — factor in delays."))
            if s.festival == "Yes": tips.append(("🎉", "#FFF7ED", "<strong>Festival surge.</strong> High demand + packed roads — expect slower service."))
            if s.rating < 3.5: tips.append(("⭐", "#FFFBEB", "<strong>Low-rated driver.</strong> Assign a higher-rated partner for better reliability."))
            if s.multiple_deliveries > 1: tips.append(("📦", "#EFF6FF", f"<strong>{s.multiple_deliveries+1} concurrent orders.</strong> Estimated time includes multiple stops."))
            if dist > 8: tips.append(("📏", "#F0FDF4", f"<strong>Long route ({dist:.1f}km).</strong> Motorcycle fastest — avoid bicycle."))
            if s.vehicle_condition == 0: tips.append(("🔧", "#FEF2F2", "<strong>Poor vehicle condition</strong> may impact reliability and speed."))
            
            if not tips: tips.append(("✅", "#F0FDF4", "<strong>All conditions optimal.</strong> Smooth delivery expected — no issues flagged!"))


            # ─── 4. COMPUTE & RENDER GLASSMORPHIC SMART INSIGHTS CARD ───
            tips_rows_html = ""
            for icon, bg, text in tips[:5]:
                tips_rows_html += f"""
                <div class="tip-row" style="display:flex; align-items:flex-start; gap:12px; margin-bottom:12px; font-size:13px; line-height:1.4;">
                    <div class="tip-badge" style="background:{bg}; padding:4px 8px; border-radius:6px; font-size:14px; flex-shrink:0;">{icon}</div>
                    <div class="tip-text" style="color: #475569; padding-top: 2px;">{text}</div>
                </div>
                """

            # 🚀 CRITICAL FIX: Rendered the entire Smart Insights card cleanly via native st.html()
            insights_card_html = f"""
            <div class="glass-fcard">
                <div class="fcard-head" style="display:flex; align-items:center; gap:10px; border-bottom: 1px solid rgba(226, 232, 240, 0.4); padding-bottom:12px; margin-bottom:14px;">
                    <div class="fcard-icon" style="background:#FFF0E3; padding:4px 8px; border-radius:6px;">💡</div>
                    <div class="fcard-title" style="font-family:'Bricolage Grotesque',sans-serif; font-size:14px; font-weight:700; color:#1C1917;">Smart Insights</div>
                </div>
                <div class="glass-fcard-body">
                    {tips_rows_html}
                </div>
            </div>
            </div> <!-- Closes the top-level reveal-layout-wrapper safely -->
            """
            st.html(insights_card_html)


# ─── RIGHT COLUMN  —  DYNAMIC SUMMARY DASHBOARD ──────────────────────────────
# Wrap your existing sidebar generator layout block logic with this guard statement:
if s.step < 4:
    with result_col:

        # ── DYNAMIC RENDERING ALIGNMENT SCHEDULER ──────────────────────────────
        dynamic_margin = "-62px" if s.step == 1 else "-10px"

        st.html(f"""
        <style>
        /* Target the exact vertical layout column container holding our summary fcard */
        div[data-testid="stColumn"]:has(.fcard) div[data-testid="stVerticalBlock"] {{
            margin-top: {dynamic_margin} !important;
        }}
        @media (max-width: 768px) {{
            div[data-testid="stColumn"]:has(.fcard) div[data-testid="stVerticalBlock"] {{
                margin-top: 0px !important;
            }}
        }}
        </style>
        """)

        # ─── BI-DIRECTIONAL COORDINATES FALLBACK EVALUATION ───
        eval_rest_lat = s.rest_lat if s.rest_lat is not None else s.map_rest_lat
        eval_rest_lon = s.rest_lon if s.rest_lon is not None else s.map_rest_lon
        eval_del_lat  = s.del_lat if s.del_lat is not None else s.map_del_lat
        eval_del_lon  = s.del_lon if s.del_lon is not None else s.map_del_lon

        if eval_rest_lat is not None and eval_del_lat is not None:
            dist3 = haversine(eval_rest_lat, eval_rest_lon, eval_del_lat, eval_del_lon)
        else:
            dist3 = 0.00

        # Pre-compute filling context flags natively
        is_weather_set = s.step >= 2
        is_traffic_set = s.step >= 2
        is_vehicle_set = s.step >= 3
        is_rating_set  = s.step >= 3

        weather_icon_char = WEATHER_ICON.get(s.weather, "🌤️") if 'WEATHER_ICON' in globals() else "🌤️"
        vehicle_icon_char = VEH_ICON.get(s.vehicle_type, "🛵") if 'VEH_ICON' in globals() else "🛵"

        if is_weather_set:
            weather_label = str(s.weather)
            weather_badge_style = "background: #FFF7ED; border: 1px solid #FFEDD5; color: #C2410C; font-weight: 700; padding: 3px 10px; border-radius: 20px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.3px;"
        else:
            weather_label = f"Auto-Default: {s.weather}"
            weather_badge_style = "opacity: 0.55; border: 1px dashed #cbd5e1; background: #f8fafc; color: #64748b; font-weight: 500; padding: 3px 10px; border-radius: 20px; font-size: 11px;"

        if is_traffic_set:
            traffic_badge_class = f"inline-badge {TRAFFIC_BADGE.get(s.traffic, 'ib-blue')}" if 'TRAFFIC_BADGE' in globals() else "inline-badge"
            traffic_html_element = f'<span class="{traffic_badge_class}">{s.traffic}</span>'
        else:
            traffic_html_element = f'<span style="opacity: 0.55; border: 1px dashed #cbd5e1; background: #f8fafc; color: #64748b; font-weight: 500; padding: 3px 10px; border-radius: 20px; font-size: 11px;">Auto-Default: {s.traffic}</span>'

        clean_vehicle_name = s.vehicle_type.replace("_", " ").title() if hasattr(s, "vehicle_type") else "Motorcycle"
        if is_vehicle_set:
            vehicle_label = str(clean_vehicle_name)
            vehicle_badge_style = "background: #F1F5F9; border: 1px solid #E2E8F0; color: #334155; font-weight: 700; padding: 3px 10px; border-radius: 20px; font-size: 11px;"
        else:
            vehicle_label = f"Auto-Default: {clean_vehicle_name}"
            vehicle_badge_style = "opacity: 0.55; border: 1px dashed #cbd5e1; background: #f8fafc; color: #64748b; font-weight: 500; padding: 3px 10px; border-radius: 20px; font-size: 11px;"

        if is_rating_set:
            rating_label = f"{s.rating:.1f} / 5"
            rating_badge_style = "background: #FEF3C7; border: 1px solid #FDE68A; color: #92400E; font-weight: 700; padding: 3px 10px; border-radius: 20px; font-size: 11px;"
        else:
            rating_label = f"Auto-Default: {s.rating:.1f} / 5"
            rating_badge_style = "opacity: 0.55; border: 1px dashed #cbd5e1; background: #f8fafc; color: #64748b; font-weight: 500; padding: 3px 10px; border-radius: 20px; font-size: 11px;"

                # ── ABSOLUTE RAW HTML STRING PARSING ENGINE ──
        # Constructed as an immutable layout block passed to st.html()
        card_layout_html = f"""
        <div class="fcard" style="
            margin-top: 0px;
            background-color: #F8F9FA; /* Soft modern light grey canvas fill */
            border: 1px solid #E5E7EB; /* Paper-thin soft outline border */
            border-radius: 16px;       /* Modern dashboard rounded corners */
            padding: 20px;             /* Generous inner padding allocation */
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02); /* Clean flat surface shadow */
        ">
            <div class="fcard-head" style="display:flex; align-items:center; gap:10px; border-bottom: 1px solid #E5E7EB; padding-bottom:12px; margin-bottom:16px;">
                <div class="fcard-icon" style="background: #FFFFFF; border: 1px solid #E5E7EB; padding:4px 8px; border-radius:6px; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">📝</div>
                <div class="fcard-title" style="font-family: 'Bricolage Grotesque', sans-serif; font-size:14px; font-weight:700; color: #1E293B;">Your Settings So Far</div>
            </div>
            <div class="fcard-body">
                
                                <!-- OPTION 2: MONOCHROME SYSTEM SLIP READOUT -->
                <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:14px; font-size:13px;">
                    <span class="impact-icon" style="margin-right:8px;">📐</span>
                    <span class="impact-name" style="flex:1; font-weight:600; color:var(--ink2); letter-spacing: 0.8px; font-size: 11px;">Route Distance</span>
                    <span class="impact-val" style="text-align:right;">
                        <span style="
                            font-family: 'Courier New', Courier, monospace; 
                            font-weight: 700; 
                            background: #F1F5F9; 
                            color: #0F172A; 
                            padding: 4px 10px; 
                            border-radius: 6px; 
                            font-size: 12px;
                            letter-spacing: 0.5px;
                            border: 1px solid #CBD5E1;
                            box-shadow: 0 1px 2px rgba(0,0,0,0.02);
                        ">
                            {dist3:.2f}_KM
                        </span>
                    </span>
                </div>

                
                <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; font-size:13px;">
                    <span class="impact-icon" style="margin-right:8px;">{weather_icon_char}</span>
                    <span class="impact-name" style="flex:1; font-weight:600; color:var(--ink2);">Weather</span>
                    <span class="impact-val" style="text-align:right;">
                        <span style="{weather_badge_style}">{weather_label}</span>
                    </span>
                </div>
                
                <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; font-size:13px;">
                    <span class="impact-icon" style="margin-right:8px;">🚦</span>
                    <span class="impact-name" style="flex:1; font-weight:600; color:var(--ink2);">Traffic</span>
                    <span class="impact-val" style="text-align:right;">
                        {traffic_html_element}
                    </span>
                </div>
                
                <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; font-size:13px;">
                    <span class="impact-icon" style="margin-right:8px;">{vehicle_icon_char}</span>
                    <span class="impact-name" style="flex:1; font-weight:600; color:var(--ink2);">Vehicle</span>
                    <span class="impact-val" style="text-align:right;">
                        <span style="{vehicle_badge_style}">{vehicle_label}</span>
                    </span>
                </div>
                
                <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; font-size:13px;">
                    <span class="impact-icon" style="margin-right:8px;">⭐</span>
                    <span class="impact-name" style="flex:1; font-weight:600; color:var(--ink2);">Driver Rating</span>
                    <span class="impact-val" style="text-align:right;">
                        <span style="{rating_badge_style}">{rating_label}</span>
                    </span>
                </div>
            </div>
        </div>
        """
        
        # Execute pure HTML render block bypass
        st.html(card_layout_html)

                # ─── EXTRACTION GATEWAY: NATIVE WRAPPED LOTTIE COMPILER ───────────
        import json
        import os
        from streamlit_lottie import st_lottie  # Official cross-platform package wrapper

        # 🌦️ STEP 2 WEATHER VECTOR MATRIX
        if s.step == 2:
            LOTTIE_ASSETS = {
                "Sunny": "sunny.json",
                "Stormy": "stormy.json",
                "Windy": "windy.json",
                "Rainy": "rainy.json",
                "Cloudy": "cloudy.json",
                "Foggy": "foggy.json",
                "Sandy": "sandy.json"
            }

            if s.weather in ["Stormy"]:
                chosen_state = "Rainy"
            elif s.weather in ["Windy"]:
                chosen_state = "Windy"
            elif s.weather in ["Cloudy"]:
                chosen_state = "Cloudy"
            elif s.weather in ["Fog"]:
                chosen_state = "Foggy"
            elif s.weather in ["Sandstorms"]:
                chosen_state = "Sandy"
            else:
                chosen_state = "Sunny"

            target_json_file = LOTTIE_ASSETS[chosen_state]
            loaded_animation_json = None

            if os.path.exists(target_json_file):
                try:
                    with open(target_json_file, "r", encoding="utf-8") as f:
                        loaded_animation_json = json.load(f)
                except Exception:
                    loaded_animation_json = None

            if loaded_animation_json:
                st_lottie(
                    loaded_animation_json,
                    speed=1,
                    loop=True,
                    quality="high",
                    height=240,
                    key=f"lottie_weather_{chosen_state.lower()}"
                )
            else:
                st.info(f"Telemetry Profile Active: {chosen_state.upper()}")

        # 🏍️ STEP 3 VEHICLE VECTOR MATRIX (NEW IMPLEMENTATION)
        elif s.step == 3:
            # Map your 4 vehicle type string options to your local JSON asset paths
            VEHICLE_ASSETS = {
                "motorcycle": "motorcycle.json",
                "scooter": "scooter.json",
                "electric_scooter": "electric_scooter.json",
                "bicycle": "bicycle.json"
            }

            # Fallback assignment logic if s.vehicle_type isn't set yet or mismatched
            chosen_vehicle = s.vehicle_type if s.vehicle_type in VEHICLE_ASSETS else "scooter"
            target_json_file = VEHICLE_ASSETS[chosen_vehicle]
            loaded_vehicle_json = None

            if os.path.exists(target_json_file):
                try:
                    with open(target_json_file, "r", encoding="utf-8") as f:
                        loaded_vehicle_json = json.load(f)
                except Exception:
                    loaded_vehicle_json = None

            if loaded_vehicle_json:
                st.markdown("<div style='margin-bottom: 24px;'></div>", unsafe_allow_html=True)
                st_lottie(
                    loaded_vehicle_json,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="high",
                    height=240,
                    width=None, # Auto-extends smoothly to match step 2 constraints
                    key=f"lottie_vehicle_{chosen_vehicle}" # Enforces component re-drawing on selection change
                )
            else:
                st.info(f"Vehicle Fleet Model Active: {chosen_vehicle.replace('_', ' ').title()}")
                
        # ── EXCLUSIVE FALLBACK GATE SO TAB 1 AND 4 RETAIN PRESETS ──
        else:
            if inline_vector_src:
                st.html(f"""
                <div class="external-vector-route" style="
                    width: 100% !important;
                    display: flex !important;
                    justify-content: center !important;
                    align-items: flex-start !important;
                    padding-top: 40px;
                    opacity: 0.85;
                    margin-bottom: 20px;
                ">
                    <img src="{inline_vector_src}" style="
                        width: 100% !important;
                        height: auto !important;
                        max-height: 280px !important;
                        object-fit: contain !important;
                        pointer-events: none !important;
                    " alt="Delivery Route Visualization Layer">
                </div>
                """)

# ─── FOOTER ───────────────────────────────────────────────────────
# ─── FOOTER (RE-ENGINEERED TWO-TIER TELEMETRY & BRAND CREDITS) ───
st.html("""
<!-- Tier 1: Core ML Pipeline Telemetry Enclosure Capsule -->
<div class="footer" style="margin-bottom: 12px !important;">
    <!-- Brand Signature (Left Side Slot) -->
    <div class="footer-left-sig">
        <span class="footer-brand-title">DropTime</span>
        <span class="footer-hairline-split">|</span>
        <span>Predictive Food Logistics Model</span>
    </div>
    
    <!-- ML Pipeline Telemetry (Right Side Slot) -->
    <div class="footer-right-telemetry">
        <span class="footer-engine-chip">
            ENGINE: RANDOM_FOREST_V1.2
        </span>
        <span class="footer-hairline-split">•</span>
        <span>FEATURES: 14_DIMENSIONAL</span>
        <span class="footer-hairline-split">•</span>
        <span class="footer-status-dot">● INFERENCE_READY</span>
    </div>
</div>

<!-- Tier 2: Dedicated Symmetrical Author Signature Strip -->
<div style="
    width: 100% !important;
    text-align: center !important;
    padding: 4px 0 24px 0 !important;
    font-size: 11.5px !important; 
    font-weight: 600 !important; 
    color: #94A3B8 !important; 
    letter-spacing: 0.3px !important;
    text-transform: uppercase !important;
    box-sizing: border-box !important;
">
    made with <span style="color: #FF4B4B !important; font-size: 12px !important;">❤️</span> by Raghav
</div>
""")