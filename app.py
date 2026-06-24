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

# ─── GLOBAL APP CANVAS RE-TEXTURE ENGINE ────────────────────────
# if topo_css_variable:
#     st.html(f"""
#     <style>
#     /* Target Streamlit's absolute root viewport node layer */
#     .stApp, 
#     div[data-testid="stAppViewContainer"],
#     div[data-testid="stAppViewMain"] {{
#         background-color: #FDFBF7 !important; /* Premium minimalist light warm cream canvas fill */
#         background-image: {topo_css_variable} !important;
#         background-size: 1100px auto !important; /* Controls density; adjust pixel size to make contours dense or wide */
#         background-repeat: repeat !important;    /* Seamless continuous tiling across high-res screens */
#         background-position: top left !important;
#         background-attachment: fixed !important;  /* Keeps pattern locked stable while user scrolls content */
#     }}

#     /* Apply a global, ultra-subtle transparent wash to ALL backgrounds inside child modules */
#     /* This makes sure the topographic lines faintly peek through layout borders without reducing legibility */
#     div[data-testid="stVerticalBlockBorderWrapper"] {{
#         background-color: rgba(255, 255, 255, 0.85) !important; /* Gives cards a premium translucent milky feel */
#         backdrop-filter: blur(8px) !important;                  /* Adds depth over the topography lines */
#     }}
    
#     /* Ensure native column segments drop solid dark backgrounds to remain clean */
#     .stColumn {{
#         background: transparent !important;
#     }}
#     </style>
#     """)

# # ─── GLOBAL APP CANVAS RE-TEXTURE ENGINE (FIXED OPACITY BLENDING) ────────────────────────
# if topo_css_variable:
#     st.html(f"""
#     <style>
#     /* Target Streamlit's absolute root viewport node layers */
#     .stApp, 
#     div[data-testid="stAppViewContainer"],
#     div[data-testid="stAppViewMain"] {{
#         background-color: #FDFBF7 !important; /* Premium minimalist light warm cream canvas fill */
        
#         /* FIX: Layering a solid cream gradient wash on top of the image to force it to bleed out and look fainted */
#         background-image: 
#             linear-gradient(rgba(253, 251, 247, 0.96), rgba(253, 251, 247, 0.96)), 
#             {topo_css_variable} !important;
            
#         background-size: auto, 1200px auto !important; /* Controls pattern size scale */
#         background-repeat: no-repeat, repeat !important;
#         background-position: center, top left !important;
#         background-attachment: fixed !important;  /* Locks everything down cleanly when scrolling */
#     }}

#     /* Enhance child cards with a sharp milky backdrop to isolate workspace containers */
#     div[data-testid="stVerticalBlockBorderWrapper"]:has(div[data-key="tab_content_wrapper_card"]) {{
#         background-color: #FFFFFF !important;
#         border: 1px solid #E5E7EB !important;
#         border-radius: 16px !important;
#         box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.02) !important;
#     }}
    
#     .stColumn {{
#         background: transparent !important;
#     }}
#     </style>
#     """)

# # ─── GLOBAL APP CANVAS RE-TEXTURE ENGINE (MULTIPLY BLENDING SYSTEM) ───
# if topo_css_variable:
#     st.html(f"""
#     <style>
#     /* 1. Reset root nodes to transparent so they don't block the background layer */
#     .stApp, 
#     div[data-testid="stAppViewMain"] {{
#         background: transparent !important;
#     }}

#     /* 2. FIX: Bind the texture and color directly to Streamlit's primary layout block container */
#     div[data-testid="stAppViewContainer"] {{
#         background-color: #FDFBF7 !important; /* Premium minimalist light warm cream canvas fill */
#         background-image: {topo_css_variable} !important;
#         background-size: 1100px auto !important; /* Crisp high-density layout mapping */
#         background-repeat: repeat !important;
#         background-position: top left !important;

#         background-attachment: scroll !important;         
#         /* FIX: Blends the image line drawing natively into the cream canvas color.
#            This ensures the lines are fully visible without looking harsh or clashing with elements */
#         background-blend-mode: multiply !important;
#         opacity: 1 !important;
#     }}

#     /* 3. Keep child workspace cards clean, sharp, and opaque over the lines */
#     div[data-testid="stVerticalBlockBorderWrapper"]:has(div[data-key="tab_content_wrapper_card"]) {{
#         background-color: rgba(255, 255, 255, 0.96) !important;
#         border: 1px solid #E5E7EB !important;
#         border-radius: 16px !important;
#         box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.02) !important;
#         backdrop-filter: blur(8px) !important;
#     }}
    
#     .stColumn {{
#         background: transparent !important;
#     }}
#     </style>
#     """)

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
    page_title="DeliverIQ · ETA Predictor",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# # ─── COMPONENT STATE INITIALIZATION (Place at the top of your file) ───
# import streamlit as st

# # Using an abbreviation for session state variable context matching your architecture
# if "step" not in st.session_state: st.session_state.step = 1
# if "pin_mode" not in st.session_state: st.session_state.pin_mode = "restaurant"

# if "rest_lat" not in st.session_state: st.session_state.rest_lat = 28.6304  # Set to your preferred initial lat
# if "rest_lon" not in st.session_state: st.session_state.rest_lon = 77.2177  # Set to your preferred initial lon
# if "del_lat" not in st.session_state: st.session_state.del_lat = 28.6514
# if "del_lon" not in st.session_state: st.session_state.del_lon = 77.1907  

# # ─── ADD THIS TO YOUR TOP COMPONENT INITIALIZATION BLOCK ───
# if "rest_box_id" not in st.session_state: st.session_state.rest_box_id = 0
# if "del_box_id" not in st.session_state: st.session_state.del_box_id = 0

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

# /* ──── Variables ──── */
# :root{
#   --brand:#E8471E;         /* tomato-red */
#   --brand2:#FF8C00;        /* saffron */
#   --brand3:#22C55E;        /* fresh-green */
#   --cream:#FFF8F2;         /* warm cream bg */
#   --cream2:#FFF0E3;
#   --ink:#1C1917;
#   --ink2:#44403C;
#   --ink3:#78716C;
#   --ink4:#A8A29E;
#   --white:#FFFFFF;
#   --border:#EDE8E3;
#   --border2:#D9D0C7;
#   --card-shadow:0 2px 12px rgba(28,25,23,.07),0 1px 3px rgba(28,25,23,.05);
#   --card-shadow-hover:0 8px 28px rgba(28,25,23,.13),0 2px 8px rgba(28,25,23,.07);
#   --r:14px; --r2:20px; --r3:28px;
# }

# /* ──── Reset ──── */
# *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
# html,body,[class*="css"]{
#   font-family:'Nunito',sans-serif!important;
#   background:var(--cream)!important;
#   color:var(--ink)!important;
# }
# ::-webkit-scrollbar{width:5px}
# ::-webkit-scrollbar-track{background:var(--cream2)}
# ::-webkit-scrollbar-thumb{background:var(--border2);border-radius:4px}

# /* ──── Hide chrome ──── */
# # #MainMenu,footer,header{visibility:hidden!important}
# # .block-container{padding:0!important;max-width:100%!important}
# # section[data-testid="stSidebar"]{display:none!important}
# # div[data-testid="stDecoration"]{display:none!important}
# # div[data-testid="stToolbar"]{display:none!important}

# /* ──── FIX: EXCLUSIVE TARGETED CARDS ──── */
# /* Custom wrapper class that targets ONLY explicit structural components */
# .fcard-container-wrapper {
#     background: #FFFFFF !important;
#     border: 1px solid #EDE8E3 !important;
#     border-radius: 14px !important;
#     box-shadow: 0 2px 12px rgba(28,25,23,.07) !important;
#     padding: 24px 20px 20px 20px !important;
#     margin-bottom: 20px !important;
# }

# /* Form element structural labels styling */
# .fcard-container-wrapper label {
#     font-size: 11px !important;
#     font-weight: 700 !important;
#     color: var(--ink3) !important;
#     text-transform: uppercase !important;
#     letter-spacing: 0.5px !important;
# }

# /* Inline headers styling inside white cards */
# .fcard-inline-header {
#     display: flex;
#     align-items: center;
#     gap: 12px;
#     border-bottom: 1px solid #EDE8E3;
#     padding-bottom: 14px;
#     margin-bottom: 16px;
# }
            
# /* ──── FIX: SCREEN EDGE PADDING BUFFER ──── */
# #MainMenu, footer, header { visibility: hidden !important; }
# div[data-testid="stDecoration"] { display: none !important; }
# div[data-testid="stToolbar"] { display: none !important; }
# section[data-testid="stSidebar"] { display: none !important; }

# /* Restores a modern layout margin grid to stop elements from touching screen edges */
# .block-container {
#   padding: 0px 48px 48px 48px !important; /* Builds 48px protective breathing room on all sides */
#   max-width: 1400px !important;           /* Restricts ultra-wide monitors from stretching fields too far */
#   margin: 0 auto !important;             /* Perfectly centers the entire block layout */
# }

# /* ──── TOPBAR ──── */
# # .topbar{
# #   display:flex;align-items:center;justify-content:space-between;
# #   padding:14px 36px;
# #   background:var(--white);
# #   border-bottom:1px solid var(--border);
# #   position:sticky;top:0;z-index:999;
# # }
            
# .topbar {
#   display: flex;
#   align-items: center;
#   justify-content: space-between;
#   padding: 20px 0px 14px 0px; /* Aligns its padding exactly with the new container edges */
#   background: var(--cream);   /* Changes color to match the body for a unified look */
#   border-bottom: 1px solid var(--border);
#   position: sticky;
#   top: 0;
#   z-index: 999;
# }

# .brand{display:flex;align-items:center;gap:10px}
# .brand-logo{
#   width:38px;height:38px;border-radius:10px;
#   background:linear-gradient(135deg,var(--brand),var(--brand2));
#   display:flex;align-items:center;justify-content:center;
#   font-size:20px;
#   box-shadow:0 3px 10px rgba(232,71,30,.35);
# }
# .brand-name{
#   font-family:'Bricolage Grotesque',sans-serif;
#   font-size:21px;font-weight:800;color:var(--ink);letter-spacing:-0.5px;
# }
# .brand-name em{font-style:normal;color:var(--brand)}
# # .live-chip{
# #   display:inline-flex;align-items:center;gap:6px;
# #   background:#F0FDF4;border:1px solid #86EFAC;
# #   border-radius:20px;padding:5px 13px;
# #   font-size:11px;font-weight:700;color:#16A34A;letter-spacing:.3px;
# # }
# # .live-dot{width:7px;height:7px;border-radius:50%;background:#22C55E;animation:blink 2s infinite}
            
# /* ──── FIX: LIVE CHIP ALIGNMENT ──── */
# .live-chip {
#   display: inline-flex !important;
#   align-items: center !important;
#   justify-content: center !important;
#   gap: 6px;
#   background: #F0FDF4;
#   border: 1px solid #86EFAC;
#   border-radius: 20px;
#   padding: 5px 13px;
#   font-size: 11px;
#   font-weight: 700;
#   color: #16A34A;
#   letter-spacing: .3px;
#   line-height: 1 !important;
# }
# .live-dot {
#   width: 7px;
#   height: 7px;
#   border-radius: 50%;
#   background: #22C55E;
#   display: inline-block;
#   transform: translateY(0px); /* Adjusts micro-alignment if needed */
#   flex-shrink: 0;
#   animation: blink 2s infinite;
# }

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

# /* ──── EXCLUSIVE STRUCTURAL CONTAINER CARDS ──── */
# .fcard-container-wrapper {
#     background: #FFFFFF !important;
#     border: 1px solid #EDE8E3 !important;
#     border-radius: 14px !important;
#     box-shadow: var(--card-shadow) !important;
#     padding: 24px 20px !important;
#     margin-bottom: 20px !important;
# }

# .fcard-container-wrapper label {
#     font-size: 11px !important;
#     font-weight: 700 !important;
#     color: var(--ink3) !important;
#     text-transform: uppercase !important;
#     letter-spacing: 0.5px !important;
# }

# .fcard-inline-header {
#     display: flex;
#     align-items: center;
#     gap: 12px;
#     border-bottom: 1px solid #EDE8E3;
#     padding-bottom: 14px;
#     margin-bottom: 16px;
# }
            
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

# /* ──── HERO BANNER ──── */
            
# /* ──── FIX: PILL SIZE & ACCENT COLOR ──── */
# .hero-tag {
#   display: inline-flex !important;
#   align-items: center !important;
#   gap: 7px !important;
#   background: rgba(255, 140, 0, 0.12) !important; 
#   border: 1px solid rgba(255, 140, 0, 0.35) !important;
#   border-radius: 20px !important;
#   padding: 6px 14px !important;
#   font-size: 11px !important;
#   font-weight: 700 !important;
#   color: #FF9800 !important; 
#   letter-spacing: 1.2px !important;
#   text-transform: uppercase !important;
#   margin-bottom: 18px !important;
#   line-height: 1 !important;
#   width: max-content !important; /* CRITICAL: Stops the pill from stretching full-width */
# }
            
# /* ──── FIX: HERO BANNER PROPORTIONS ──── */
            
# .hero {
#   background: linear-gradient(135deg, #1C1917 0%, #292524 55%, #3B1E14 100%);
#   padding: 56px 36px;
#   text-align: center !important; /* Centers all content */
#   display: flex !important;
#   flex-direction: column !important;
#   align-items: center !important;
#   justify-content: center !important;
# }
            
# .hero-inner {
#   max-width: 780px !important; /* Widens text span */
#   margin: 0 auto !important;
#   display: flex !important;
#   flex-direction: column !important;
#   align-items: center !important;
# }

# .hero-h1 {
#   font-family: 'Bricolage Grotesque', sans-serif;
#   font-size: clamp(28px, 3.2vw, 42px); /* Slightly optimized size */
#   font-weight: 800;
#   color: #fff;
#   line-height: 1.15;
#   letter-spacing: -1px;
#   margin-bottom: 10px;
# }
# .hero-sub {
#   font-size: 14px;
#   color: rgba(255, 255, 255, 0.6);
#   line-height: 1.5;
#   margin-bottom: 20px; /* Reduced bottom gap */
# }
            
# /* ──── FIXED ACCENT CHIPS FOR DARK BG ──── */
            
# /* ──── FIX FOR CENTERED CHIPS ──── */
# .hero-chips {
#   display: flex !important;
#   flex-direction: row !important; /* Changes from vertical stack to a clean horizontal line */
#   flex-wrap: wrap !important;
#   justify-content: center !important; /* Centers them perfectly under the description */
#   gap: 12px !important;
#   margin-top: 24px !important;
# }

# .hero-chip {
#   background: rgba(255, 255, 255, 0.07) !important;
#   border: 1px solid rgba(255, 255, 255, 0.15) !important;
#   border-radius: 20px !important; /* Rounded pills look sleeker horizontally */
#   padding: 6px 16px !important;
#   font-size: 12px !important;
#   font-weight: 600 !important;
#   color: #FFFFFF !important;
#   display: inline-flex !important;
#   align-items: center !important;
#   gap: 6px !important;
#   width: auto !important;
# }

# .hero-chip strong {
#   color: #FF8C00 !important; /* Keeps metrics highlighted in high-contrast orange */
# }

# # /* ──── STEP WIZARD ──── */
            
# /* ──── ULTIMATE RE-ALIGNMENT FIX FOR STEP WIZARD ──── */
# .steps-bar {
#   display: flex !important;
#   flex-direction: row !important;
#   flex-wrap: nowrap !important;
#   align-items: center !important;
#   justify-content: flex-start !important;
#   gap: 16px !important;
#   background: #FFFFFF !important;
#   border-bottom: 1px solid var(--border) !important;
#   padding: 14px 36px !important;
#   width: 100% !important;
#   min-height: 54px !important;
# }

# .step-tab {
#   display: inline-flex !important;
#   flex-direction: row !important;
#   align-items: center !important;
#   justify-content: center !important;
#   gap: 8px !important;
#   padding: 4px 8px !important;
#   white-space: nowrap !important;
#   text-decoration: none !important;
#   cursor: pointer !important;
# }

# .step-num {
#   width: 24px !important;
#   height: 24px !important;
#   border-radius: 50% !important;
#   display: inline-flex !important;
#   align-items: center !important;
#   justify-content: center !important;
#   font-size: 11px !important;
#   font-weight: 800 !important;
#   line-height: 1 !important;
#   margin: 0 !important;
#   padding: 0 !important;
#   flex-shrink: 0 !important;
# }

# .step-label {
#   font-size: 13px !important;
#   font-weight: 700 !important;
#   color: var(--ink2) !important;
#   line-height: 1 !important;
#   margin: 0 !important;
#   padding: 0 !important;
#   display: inline-block !important;
# }
            
# /* ──── HERO BANNER ──── */   
# /* FIX: Precise text tracking & dynamic widths */
# .hero-tag {
#   display: inline-flex !important;
#   align-items: center !important;
#   gap: 7px !important;
#   background: rgba(255, 140, 0, 0.12) !important; 
#   border: 1px solid rgba(255, 140, 0, 0.35) !important;
#   border-radius: 20px !important;
#   padding: 6px 14px !important;
#   font-size: 11px !important;
#   font-weight: 700 !important;
#   color: #FF9800 !important; 
#   letter-spacing: 1.2px !important;
#   text-transform: uppercase !important;
#   margin-bottom: 20px !important;
#   line-height: 1 !important;
#   width: max-content !important;
# }

# .hero {
#   background: linear-gradient(135deg, #1C1917 0%, #292524 55%, #3B1E14 100%);
#   padding: 64px 36px 56px 36px !important;
#   text-align: center !important;
#   display: flex !important;
#   flex-direction: column !important;
#   align-items: center !important;
#   justify-content: center !important;
#   border-radius: 0 0 16px 16px; /* Softens bottom canvas junction */
# }            

# .hero-inner {
#   max-width: 680px !important; /* Optimizes readability to ~65 chars per line */
#   margin: 0 auto !important;
#   display: flex !important;
#   flex-direction: column !important;
#   align-items: center !important;
# }

# .hero-h1 {
#   font-family: 'Bricolage Grotesque', sans-serif;
#   font-size: clamp(32px, 3.8vw, 46px) !important; /* Prompts cleaner hero scaling */
#   font-weight: 800;
#   color: #FFFFFF;
#   line-height: 1.15;
#   letter-spacing: -1.2px !important;
#   margin-bottom: 14px !important;
# }

# .hero-sub {
#   font-size: 14px !important;
#   color: rgba(255, 255, 255, 0.7) !important; /* Increases copy readability over dark bg */
#   line-height: 1.6 !important;
#   margin-bottom: 8px !important;
# }
            
# /* FIX: Glassmorphic high-contrast dashboard metric chips */
# .hero-chips {
#   display: flex !important;
#   flex-direction: row !important;
#   flex-wrap: wrap !important;
#   justify-content: center !important;
#   gap: 12px !important;
#   margin-top: 24px !important;
# }

# .hero-chip {
#   background: rgba(255, 255, 255, 0.06) !important;
#   border: 1px solid rgba(255, 255, 255, 0.14) !important;
#   border-radius: 100px !important; 
#   padding: 8px 16px !important;
#   font-size: 12px !important;
#   font-weight: 600 !important;
#   color: rgba(255, 255, 255, 0.95) !important;
#   display: inline-flex !important;
#   align-items: center !important;
#   gap: 6px !important;
#   width: auto !important;
#   backdrop-filter: blur(8px);
#   box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
# }

# .hero-chip strong {
#   color: #FF8C00 !important; /* Forces precise orange highlight matching token */
#   font-weight: 700 !important;
# }

# /* FIX: Elevated structural alignment for step indicator */
# .steps-bar {
#   display: flex !important;
#   flex-direction: row !important;
#   flex-wrap: nowrap !important;
#   align-items: center !important;
#   justify-content: flex-start !important;
#   gap: 24px !important;
#   background: #FFFFFF !important;
#   border-bottom: 1px solid var(--border) !important;
#   padding: 18px 36px !important;
#   width: 100% !important;
#   min-height: 58px !important;
#   margin-bottom: 28px !important; /* Creates clean spatial breathing room before form sections */
# }

# .step-tab {
#   display: inline-flex !important;
#   flex-direction: row !important;
#   align-items: center !important;
#   justify-content: center !important;
#   gap: 10px !important;
#   padding: 6px 0px !important;
#   white-space: nowrap !important;
#   text-decoration: none !important;
#   cursor: pointer !important;
# }

# .step-num {
#   width: 24px !important;
#   height: 24px !important;
#   border-radius: 50% !important;
#   display: inline-flex !important;
#   align-items: center !important;
#   justify-content: center !important;
#   font-size: 11px !important;
#   font-weight: 800 !important;
#   line-height: 1 !important;
#   margin: 0 !important;
#   padding: 0 !important;
#   flex-shrink: 0 !important;
# }

# .step-label {
#   font-size: 13px !important;
#   font-weight: 700 !important;
#   color: var(--ink2) !important;
#   line-height: 1 !important;
#   margin: 0 !important;
#   padding: 0 !important;
#   display: inline-block !important;
#   letter-spacing: 0.2px;
# }


# /* ──── CONTENT SHELL ──── */
# .content-shell{
#   max-width:1180px;margin:0 auto;
#   padding:32px 36px 60px;
# }

# /* ──── SECTION TITLE ──── */
# # .section-title{
# #   font-family:'Bricolage Grotesque',sans-serif;
# #   font-size:22px;font-weight:700;color:var(--ink);
# #   letter-spacing:-0.3px;margin-bottom:4px;
# # }
# # .section-sub{font-size:13px;color:var(--ink3);margin-bottom:24px;line-height:1.5}
            
# /* ──── FIX: PROPORTIONAL STRUCTURAL GAP SPACING ──── */
# .section-title {
#   font-family: 'Bricolage Grotesque', sans-serif !important;
#   font-size: 22px !important;
#   font-weight: 700 !important;
#   color: var(--ink) !important;
#   letter-spacing: -0.3px !important;
  
#   /* CRITICAL: Creates a perfect gap pushing the title down from the wizard row */
#   margin-top: 24px !important; 
#   margin-bottom: 4px !important;
# }

# .section-sub {
#   font-size: 13px !important;
#   color: var(--ink3) !important;
#   line-height: 1.5 !important;
  
#   /* CRITICAL: Forces a comfortable spatial buffer pushing the white cards down */
#   margin-bottom: 24px !important; 
#   display: block !important;
# }

# /* ──── CARDS ──── */
# .fcard{
#   background:var(--white);border:1px solid var(--border);
#   border-radius:var(--r2);box-shadow:var(--card-shadow);
#   overflow:hidden;margin-bottom:16px;
#   transition:box-shadow .2s;
# }
# .fcard:hover{box-shadow:var(--card-shadow-hover)}
# .fcard-head{
#   padding:16px 20px;border-bottom:1px solid var(--border);
#   display:flex;align-items:center;gap:10px;
# }
# .fcard-icon{
#   width:34px;height:34px;border-radius:10px;
#   display:flex;align-items:center;justify-content:center;font-size:16px;
# }
# .fcard-title{font-size:14px;font-weight:700;color:var(--ink)}
# .fcard-desc{font-size:11px;color:var(--ink4);margin-top:1px}
# .fcard-body{padding:18px 20px 22px}

# /* ──── HERO BANNER ──── */   
# /* Precise text tracking & dynamic widths */
# .hero-tag {
#   display: inline-flex !important;
#   align-items: center !important;
#   gap: 7px !important;
#   background: rgba(255, 140, 0, 0.12) !important; 
#   border: 1px solid rgba(255, 140, 0, 0.35) !important;
#   border-radius: 20px !important;
#   padding: 6px 14px !important;
#   font-size: 11px !important;
#   font-weight: 700 !important;
#   color: #FF9800 !important; 
#   letter-spacing: 1.2px !important;
#   text-transform: uppercase !important;
#   margin-bottom: 20px !important;
#   line-height: 1 !important;
#   width: max-content !important;
# }

# .hero {
#   background: linear-gradient(135deg, #1C1917 0%, #292524 55%, #3B1E14 100%);
#   padding: 64px 36px 56px 36px !important;
#   text-align: center !important;
#   display: flex !important;
#   flex-direction: column !important;
#   align-items: center !important;
#   justify-content: center !important;
#   border-radius: 0 0 16px 16px;
# }            

# .hero-inner {
#   max-width: 680px !important;
#   margin: 0 auto !important;
#   display: flex !important;
#   flex-direction: column !important;
#   align-items: center !important;
# }

# .hero-h1 {
#   font-family: 'Bricolage Grotesque', sans-serif;
#   font-size: clamp(32px, 3.8vw, 46px) !important;
#   font-weight: 800;
#   color: #FFFFFF;
#   line-height: 1.15;
#   letter-spacing: -1.2px !important;
#   margin-bottom: 14px !important;
# }

# .hero-sub {
#   font-size: 14px !important;
#   color: rgba(255, 255, 255, 0.7) !important;
#   line-height: 1.6 !important;
#   margin-bottom: 8px !important;
# }
            
/* ──── LIGHT-THEME HERO BANNER ──── */   
# .hero-tag {
#   display: inline-flex !important;
#   align-items: center !important;
#   gap: 7px !important;
#   background: rgba(255, 140, 0, 0.1) !important; 
#   border: 1px solid rgba(255, 140, 0, 0.25) !important;
#   border-radius: 20px !important;
#   padding: 6px 14px !important;
#   font-size: 11px !important;
#   font-weight: 700 !important;
#   color: #E67E22 !important; 
#   letter-spacing: 1.2px !important;
#   text-transform: uppercase !important;
#   margin-bottom: 20px !important;
#   line-height: 1 !important;
#   width: max-content !important;
# }

# .hero {
#   background: #F8F9FA !important; /* Ultra-light background */
#   padding: 48px 36px 40px 36px !important;
#   text-align: center !important;
#   display: flex !important;
#   flex-direction: column !important;
#   align-items: center !important;
#   justify-content: center !important;
#   border-radius: 0 0 16px 16px;
# } 


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

# .hero-sub {
#   font-size: 14px !important;
#   color: #555555 !important; /* Muted slate gray for secondary reading */
#   line-height: 1.6 !important;
#   margin-bottom: 8px !important;
# }
            
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

/* ──── CLEAN LIGHT-THEME METRICS CHIPS ──── */
# .hero-chips-container {
#   display: flex !important; 
#   flex-direction: row !important; 
#   flex-wrap: wrap !important; 
#   justify-content: center !important; 
#   gap: 12px !important; 
#   margin-top: 24px !important; 
#   width: 100% !important;
# }

# .hero-chip-light {
#   background: #FFFFFF !important; /* Standout white cards */
#   border: 1px solid #E5E7EB !important; /* Subtle gray borders */
#   border-radius: 12px !important; 
#   padding: 8px 18px !important; 
#   font-size: 13px !important; 
#   font-weight: 600 !important; 
#   color: #374151 !important; 
#   display: inline-flex !important; 
#   align-items: center !important; 
#   gap: 8px !important; 
#   white-space: nowrap !important; 
#   width: auto !important;
#   box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
# }

# .hero-chip-light strong {
#   color: #E67E22 !important; /* Bold primary orange accent */
#   font-weight: 700 !important;
# }
            
/* ──── CLEAN LIGHT-THEME METRICS CHIPS ──── */
# .hero-chips-container {
#   display: flex !important; 
#   flex-direction: row !important; 
#   flex-wrap: wrap !important; 
#   justify-content: center !important; 
#   gap: 12px !important; 
#   margin-top: 24px !important; 
#   width: 100% !important;
# }

# .hero-chip-light {
#   border-radius: 12px !important; 
#   padding: 8px 18px !important; 
#   font-size: 13px !important; 
#   font-weight: 600 !important; 
#   display: inline-flex !important; 
#   align-items: center !important; 
#   gap: 8px !important; 
#   white-space: nowrap !important; 
#   width: auto !important;
# }

# /* 🎯 Accuracy: Pastel Pink/Rose Theme */
# .chip-accuracy-light {
#   background: rgba(244, 63, 94, 0.06) !important;
#   border: 1px solid rgba(244, 63, 94, 0.2) !important;
#   color: #9F1239 !important;
# }
# .chip-accuracy-light strong {
#   color: #E11D48 !important;
#   font-weight: 700 !important;
# }

# /* ⚡ Inference: Pastel Orange/Amber Theme */
# .chip-inference-light {
#   background: rgba(217, 119, 6, 0.06) !important;
#   border: 1px solid rgba(217, 119, 6, 0.2) !important;
#   color: #78350F !important;
# }
# .chip-inference-light strong {
#   color: #D97706 !important;
#   font-weight: 700 !important;
# }

# /* 🗺️ Features: Pastel Blue/Cyan Theme */
# .chip-features-light {
#   background: rgba(6, 182, 212, 0.06) !important;
#   border: 1px solid rgba(6, 182, 212, 0.2) !important;
#   color: #155E75 !important;
# }
# .chip-features-light strong {
#   color: #0891B2 !important;
#   font-weight: 700 !important;
# }

# /* 🌆 Geo-Segment: Pastel Purple Theme */
# .chip-geo-light {
#   background: rgba(147, 51, 234, 0.06) !important;
#   border: 1px solid rgba(147, 51, 234, 0.2) !important;
#   color: #581C87 !important;
# }
# .chip-geo-light strong {
#   color: #9333EA !important;
#   font-weight: 700 !important;
# }
            
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

            
/* Glassmorphic high-contrast dashboard metric chips */
# .hero-chips {
#   display: flex !important;
#   flex-direction: row !important;
#   flex-wrap: wrap !important;
#   justify-content: center !important;
#   gap: 12px !important;
#   margin-top: 24px !important;
# }

# .hero-chip {
#   background: rgba(255, 255, 255, 0.06) !important;
#   border: 1px solid rgba(255, 255, 255, 0.14) !important;
#   border-radius: 100px !important; 
#   padding: 8px 16px !important;
#   font-size: 12px !important;
#   font-weight: 600 !important;
#   color: rgba(255, 255, 255, 0.95) !important;
#   display: inline-flex !important;
#   align-items: center !important;
#   gap: 6px !important;
#   width: auto !important;
#   backdrop-filter: blur(8px);
#   box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
# }
            
/* ──── BENTO GLOWING METRIC CHIPS ──── */
# .hero-chips {
#   display: flex !important;
#   flex-direction: row !important;
#   flex-wrap: wrap !important;
#   justify-content: center !important;
#   gap: 14px !important;
#   margin-top: 32px !important;
# }

# .hero-chip {
#   position: relative !important;
#   background: rgba(20, 18, 17, 0.6) !important;
#   border-radius: 12px !important; /* Bento box styling instead of pill shape */
#   padding: 10px 18px !important;
#   font-size: 13px !important;
#   font-weight: 600 !important;
#   display: inline-flex !important;
#   align-items: center !important;
#   gap: 8px !important;
#   width: auto !important;
#   backdrop-filter: blur(12px);
#   transition: transform 0.2s ease, box-shadow 0.2s ease !important;
# }
            
# /* ──── SOFT MINIMALIST LIGHT-THEME METRICS ──── */
# /* ──── DARK-HERO OPTIMIZED LIGHT METRICS ──── */
# .hero-chips {
#   display: flex !important;
#   flex-direction: row !important;
#   flex-wrap: wrap !important;
#   justify-content: center !important;
#   gap: 12px !important;
#   margin-top: 28px !important;
# }

# .hero-chip {
#   /* Using a soft, light semi-transparent background to isolate against the dark gradient */
#   background: rgba(255, 255, 255, 0.05) !important;
#   /* A clean, subtle border that anchors the bento container without blooming or glowing */
#   border: 1px solid rgba(255, 255, 255, 0.15) !important;
#   border-radius: 12px !important; 
#   padding: 8px 18px !important;
#   font-size: 13px !important;
#   font-weight: 600 !important;
#   /* Crisp light gray text ensures immediate readability on the dark background */
#   color: rgba(255, 255, 255, 0.9) !important;
#   display: inline-flex !important;
#   align-items: center !important;
#   gap: 8px !important;
#   width: auto !important;
#   backdrop-filter: blur(4px) !important;
# }

# /* Single warm accent brand color specifically targeting the bold metrics */
# .hero-chip strong {
#   color: #FFA043 !important; /* A bright, premium warm orange that easily pops against dark tones */
#   font-weight: 700 !important;
# }


# /* Individual Neon Theming & Glow Effects */
# .chip-accuracy {
#   border: 1px solid rgba(255, 46, 126, 0.4) !important;
#   color: #FF7EB3 !important;
#   box-shadow: 0 4px 20px rgba(255, 46, 126, 0.15), inset 0 0 8px rgba(255, 46, 126, 0.1) !important;
# }
# .chip-accuracy strong { color: #FF2E7E !important; font-weight: 800 !important; }

# .chip-inference {
#   border: 1px solid rgba(57, 255, 20, 0.4) !important;
#   color: #B3FFB3 !important;
#   box-shadow: 0 4px 20px rgba(57, 255, 20, 0.15), inset 0 0 8px rgba(57, 255, 20, 0.1) !important;
# }
# .chip-inference strong { color: #39FF14 !important; font-weight: 800 !important; }

# .chip-features {
#   border: 1px solid rgba(0, 240, 255, 0.4) !important;
#   color: #B3FAFF !important;
#   box-shadow: 0 4px 20px rgba(0, 240, 255, 0.15), inset 0 0 8px rgba(0, 240, 255, 0.1) !important;
# }
# .chip-features strong { color: #00F0FF !important; font-weight: 800 !important; }

# .chip-geo {
#   border: 1px solid rgba(255, 140, 0, 0.35) !important;
#   color: #FFE0B3 !important;
#   box-shadow: 0 4px 16px rgba(255, 140, 0, 0.1), inset 0 0 8px rgba(255, 140, 0, 0.05) !important;
# }

# .hero-chip strong {
#   color: #FF8C00 !important;
#   font-weight: 700 !important;
# }


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
            
# /* PROPORTIONAL STRUCTURAL GAP SPACING */
# .section-title {
#   font-family: 'Bricolage Grotesque', sans-serif !important;
#   font-size: 22px !important;
#   font-weight: 700 !important;
#   color: var(--ink) !important;
#   letter-spacing: -0.3px !important;
#   margin-top: 24px !important; 
#   margin-bottom: 4px !important;
# }

# .section-sub {
#   font-size: 13px !important;
#   color: var(--ink3) !important;
#   line-height: 1.5 !important;
#   margin-bottom: 24px !important; 
#   display: block !important;
# }
            
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

# /* ──── CONTAINER DECK COMPONENT CARDS ──── */
# .fcard {
#   background: var(--white);
#   border: 1px solid var(--border);
#   border-radius: var(--r2);
#   box-shadow: var(--card-shadow);
#   overflow: hidden;
#   margin-bottom: 20px !important; /* Standardized spatial buffer tracking */
#   transition: box-shadow .2s;
# }

# .fcard:hover {
#   box-shadow: var(--card-shadow-hover);
# }

# .fcard-head {
#   padding: 16px 20px;
#   border-bottom: 1px solid var(--border);
#   display: flex;
#   align-items: center;
#   gap: 10px;
# }

# .fcard-icon {
#   width: 34px;
#   height: 34px;
#   border-radius: 10px;
#   display: flex;
#   align-items: center;
#   justify-content: center;
#   font-size: 16px;
# }

# .fcard-title {
#   font-size: 14px;
#   font-weight: 700;
#   color: var(--ink);
# }

# .fcard-desc {
#   font-size: 11px;
#   color: var(--ink4);
#   margin-top: 1px;
# }

# .fcard-body {
#   padding: 18px 20px 22px;
# }

# /* ──── OPTION CARDS (clickable) ──── */
# .opt-grid{display:grid;gap:10px}
# .opt-grid-2{grid-template-columns:1fr 1fr}
# .opt-grid-3{grid-template-columns:1fr 1fr 1fr}
# .opt-grid-4{grid-template-columns:1fr 1fr 1fr 1fr}
# .opt-card{
#   border:2px solid var(--border);border-radius:var(--r);
#   padding:14px 12px;text-align:center;cursor:pointer;
#   background:var(--white);transition:all .18s;
#   display:flex;flex-direction:column;align-items:center;gap:5px;
# }
# .opt-card:hover{border-color:var(--brand2);background:var(--cream2)}
# .opt-card.selected{border-color:var(--brand);background:#FFF5F2}
# .opt-card-icon{font-size:24px;line-height:1}
# .opt-card-label{font-size:12px;font-weight:700;color:var(--ink2)}
# .opt-card.selected .opt-card-label{color:var(--brand)}
# .opt-card-sub{font-size:10px;color:var(--ink4)}

# /* ──── TOGGLE ROW ──── */
# .toggle-row{display:flex;gap:8px;flex-wrap:wrap}
# .toggle-btn{
#   padding:8px 16px;border-radius:20px;cursor:pointer;
#   border:1.5px solid var(--border);background:var(--white);
#   font-size:13px;font-weight:600;color:var(--ink3);
#   transition:all .15s;
# }
# .toggle-btn:hover{border-color:var(--brand2);color:var(--ink)}
# .toggle-btn.selected{border-color:var(--brand);background:#FFF5F2;color:var(--brand)}

# /* ──── SLIDER CUSTOM ──── */
# .slider-wrap{margin:4px 0 12px}
# .slider-labels{display:flex;justify-content:space-between;font-size:11px;color:var(--ink4);margin-top:4px}

# /* ──── MAP SECTION ──── */
# .map-search-row{display:flex;gap:8px;margin-bottom:10px;align-items:center}
# .search-type-btn{
#   padding:8px 16px;border-radius:10px;cursor:pointer;
#   border:1.5px solid var(--border);background:var(--white);
#   font-size:12px;font-weight:700;color:var(--ink3);white-space:nowrap;
#   transition:all .15s;
# }
# .search-type-btn.active{
#   border-color:var(--brand);background:var(--brand);color:var(--white);
# }
# .coord-display{
#   display:flex;gap:8px;margin-top:10px;
# }
# .coord-box{
#   flex:1;background:var(--cream2);border:1px solid var(--border);
#   border-radius:10px;padding:10px 14px;
# }
# .coord-box-head{font-size:10px;font-weight:700;text-transform:uppercase;
#   letter-spacing:1.2px;color:var(--ink4);margin-bottom:3px;
#   display:flex;align-items:center;gap:5px;
# }
# .coord-box-val{font-size:13px;font-weight:700;color:var(--brand);
#   font-variant-numeric:tabular-nums;
# }
# .dist-pill{
#   background:linear-gradient(90deg,#FFF5F2,#FFF0E3);
#   border:1px solid #FDBA74;border-radius:10px;
#   padding:11px 16px;margin-top:10px;
#   display:flex;justify-content:space-between;align-items:center;
# }
# .dist-pill-label{font-size:11px;font-weight:700;text-transform:uppercase;
#   letter-spacing:1px;color:var(--brand);}
# .dist-pill-val{font-family:'Bricolage Grotesque',sans-serif;
#   font-size:22px;font-weight:800;color:var(--ink);}
# .dist-pill-unit{font-size:13px;font-weight:500;color:var(--ink3)}

# /* ──── PREDICT BTN ──── */
# .pred-btn-wrap > div > button{
#   background:linear-gradient(135deg,#E8471E 0%,#C73D19 100%)!important;
#   color:white!important;border:none!important;
#   border-radius:14px!important;padding:17px 0!important;
#   font-family:'Bricolage Grotesque',sans-serif!important;
#   font-size:16px!important;font-weight:800!important;
#   letter-spacing:.2px!important;
#   box-shadow:0 6px 20px rgba(232,71,30,.4)!important;
#   transition:all .2s!important;width:100%!important;
# }
# .pred-btn-wrap > div > button:hover{
#   background:linear-gradient(135deg,#D43E18 0%,#B5341A 100%)!important;
#   box-shadow:0 8px 28px rgba(232,71,30,.5)!important;
#   transform:translateY(-2px)!important;
# }
# div[data-testid="stButton"] > button{
#   width:100%!important;
# }

# /* ──── RESULT CARD ──── */
# .result-outer{
#   background:linear-gradient(145deg,#1C1917 0%,#292524 100%);
#   border-radius:var(--r3);padding:36px 28px 30px;
#   position:relative;overflow:hidden;
#   box-shadow:0 20px 60px rgba(28,25,23,.25);
# }
# .result-outer::before{
#   content:'';position:absolute;
#   top:-60px;right:-60px;width:220px;height:220px;border-radius:50%;
#   background:radial-gradient(circle,rgba(232,71,30,.2) 0%,transparent 70%);
# }
# .result-outer::after{
#   content:'';position:absolute;
#   bottom:-40px;left:-40px;width:160px;height:160px;border-radius:50%;
#   background:radial-gradient(circle,rgba(255,140,0,.15) 0%,transparent 70%);
# }
# .result-inner{position:relative;z-index:1;text-align:center}
# .result-emoji{font-size:44px;margin-bottom:6px;display:block;
#   animation:bobble 2s ease-in-out infinite}
# @keyframes bobble{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
# .result-tagline{
#   font-size:13px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;
#   color:rgba(255,255,255,.45);margin-bottom:10px;
# }
# .result-big{
#   font-family:'Bricolage Grotesque',sans-serif;
#   font-size:88px;font-weight:800;color:#fff;line-height:1;
#   letter-spacing:-4px;
# }
# .result-unit{
#   font-size:18px;font-weight:700;
#   color:rgba(255,255,255,.45);text-transform:uppercase;
#   letter-spacing:2px;margin-top:4px;margin-bottom:16px;
# }
# .result-phrase{
#   font-size:16px;font-weight:600;
#   color:rgba(255,255,255,.75);
#   line-height:1.4;margin-bottom:18px;min-height:48px;
# }
# .result-phrase span{color:var(--brand2);font-weight:800}
# .result-row{
#   display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-bottom:14px;
# }
# .result-chip{
#   background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.14);
#   border-radius:8px;padding:6px 13px;
#   font-size:12px;font-weight:600;color:rgba(255,255,255,.7);
# }
# .result-chip strong{color:#fff}
# .conf-bar-wrap{margin-top:4px}
# .conf-row{display:flex;justify-content:space-between;
#   font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;
#   color:rgba(255,255,255,.35);margin-bottom:5px}
# .conf-track{height:5px;background:rgba(255,255,255,.12);border-radius:4px;overflow:hidden}
# .conf-fill{height:100%;border-radius:4px;
#   background:linear-gradient(90deg,#FF8C00,#22C55E)}
# .arrive-note{
#   margin-top:14px;font-size:12px;font-weight:600;
#   color:rgba(255,255,255,.4);letter-spacing:.2px;
# }
# .arrive-note strong{color:rgba(255,255,255,.8)}

# /* ──── IMPACT PANEL ──── */
# .impact-row{
#   display:flex;align-items:center;gap:10px;
#   padding:9px 0;border-bottom:1px solid var(--border);
# }
# .impact-row:last-child{border-bottom:none}
# .impact-icon{font-size:16px;width:22px;text-align:center;flex-shrink:0}
# .impact-name{font-size:12px;font-weight:600;color:var(--ink3);width:80px;flex-shrink:0}
# .impact-track{flex:1;height:5px;background:var(--border);border-radius:3px;overflow:hidden}
# .impact-bar{height:100%;border-radius:3px}
# .impact-val{font-size:12px;font-weight:700;color:var(--ink2);
#   width:60px;text-align:right;flex-shrink:0}

# /* ──── TIPS ──── */
# .tip-row{
#   display:flex;gap:11px;align-items:flex-start;
#   padding:10px 0;border-bottom:1px solid var(--border);
# }
# .tip-row:last-child{border-bottom:none}
# .tip-badge{
#   width:28px;height:28px;border-radius:8px;flex-shrink:0;
#   display:flex;align-items:center;justify-content:center;font-size:13px;
# }
# .tip-text{font-size:12px;color:var(--ink2);line-height:1.55;font-weight:500}
# .tip-text strong{color:var(--ink);font-weight:700}
            
# /* ──── INVISIBLE LAYER ENGINE: HIDES DUPLICATE LABELS ──── */
# /* Targets Streamlit button row wrappers exclusively within choice grids */
# div[data-testid="stColumn"]:has(button[key^="w_"]) div.stButton,
# div[data-testid="stColumn"]:has(button[key^="t_"]) div.stButton,
# div[data-testid="stColumn"]:has(button[key^="c_"]) div.stButton,
# div[data-testid="stColumn"]:has(button[key^="f_"]) div.stButton {
#   position: absolute !important;
#   top: 0 !important;
#   left: 0 !important;
#   width: 100% !important;
#   height: 100% !important;
#   margin: 0 !important;
#   padding: 0 !important;
#   z-index: 10 !important;
# }

# /* Transforms raw gray buttons to completely flat, transparent interactive sheets */
# div[data-testid="stColumn"] button[key^="w_"],
# div[data-testid="stColumn"] button[key^="t_"],
# div[data-testid="stColumn"] button[key^="c_"],
# div[data-testid="stColumn"] button[key^="f_"] {
#   position: absolute !important;
#   top: 0 !important;
#   left: 0 !important;
#   width: 100% !important;
#   height: 100% !important;
#   opacity: 0 !important; /* Hides the native text string block */
#   background: transparent !important;
#   border: none !important;
#   cursor: pointer !important;
#   margin: 0 !important;
#   padding: 0 !important;
# }

# /* Ensures layout containment boxes remain stable within card grids */
# div[data-testid="stColumn"]:has(button[key^="w_"]),
# div[data-testid="stColumn"]:has(button[key^="t_"]),
# div[data-testid="stColumn"]:has(button[key^="c_"]),
# div[data-testid="stColumn"]:has(button[key^="f_"]) {
#   position: relative !important;
#   min-height: 92px !important;
#   display: flex !important;
#   flex-direction: column !important;
# }

/* ──── FIXED: ULTIMATE DEEP STYLING HOOK FOR STREAMLIT BUTTONS ──── */

# /* 1. Base Target for All Options & Secondary Buttons inside Columns */
# div[data-testid="stButton"] button {
#   background-color: #FFFFFF !important;
#   border: 1px solid #EDE8E3 !important;
#   border-radius: 10px !important;
#   color: #44403C !important;
#   font-family: 'Nunito', sans-serif !important;
#   font-weight: 700 !important;
#   font-size: 13px !important;
#   padding: 10px 14px !important;
#   min-height: 64px !important; /* Ensures vertical alignment for multi-line text */
#   transition: all 0.2s ease-in-out !important;
#   box-shadow: none !important;
# }

# /* Base button text wrap fix for subtext properties (\n split lines) */
# div[data-testid="stButton"] button p {
#   font-size: 13px !important;
#   font-weight: 600 !important;
#   color: #44403C !important;
#   line-height: 1.3 !important;
#   white-space: pre-line !important; /* Crucial: parses python \n string breaks correctly */
# }

# /* Neutral Hover State for Unselected Options */
# div[data-testid="stButton"] button:hover {
#   border-color: #D6D3D1 !important;
#   background-color: #FAF8F5 !important;
#   color: #1C1917 !important;
# }

# /* 2. HIGH ENGAGEMENT HIGHLIGHT: Active selection targeting keys containing '_act_' */
# div[data-testid="stButton"] button[id*="_act_"] {
#   background-color: #EFF6FF !important; /* Sophisticated Brand Pastel Tint Accent */
#   border: 2px solid #2563EB !important;   /* Solid Active High Contrast Primary Blue Border */
#   box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15) !important;
# }

# /* Text updates inside active selection button wrappers */
# div[data-testid="stButton"] button[id*="_act_"] p {
#   color: #1D4ED8 !important; /* Shifts text ink color blue to emphasize selection clarity */
#   font-weight: 700 !important;
# }

# /* 3. PROTECTIVE EXCLUSIONS: Clean, high-contrast style rules for page navigation workflow controls */
# div[data-testid="stButton"] button[id*="s2_"],
# div[data-testid="stButton"] button[id*="s3_"],
# div[data-testid="stButton"] button[id*="step1_"] {
#   min-height: auto !important; /* Overrides the option button height footprint */
#   padding: 10px 24px !important;
# }

# /* Target primary navigation actions explicitly */
# div[data-testid="stButton"] button[id*="_next"] {
#   background-color: #2563EB !important;
#   border-color: #2563EB !important;
# }
# div[data-testid="stButton"] button[id*="_next"] p {
#   color: #FFFFFF !important;
# }
# div[data-testid="stButton"] button[id*="_next"]:hover {
#   background-color: #1D4ED8 !important;
#   border-color: #1D4ED8 !important;
# }

# /* Target secondary back actions explicitly */
# div[data-testid="stButton"] button[id*="_back"] {
#   background-color: #FFFFFF !important;
#   border: 1px solid #EDE8E3 !important;
# }
# div[data-testid="stButton"] button[id*="_back"] p {
#   color: #44403C !important;
# }
# div[data-testid="stButton"] button[id*="_back"]:hover {
#   background-color: #FAF8F5 !important;
#   border-color: #D6D3D1 !important;
# }

# /* Inner Badge Section Subtext Labels Alignment */
# .section-badge-label {
#   font-size: 11px !important;
#   font-weight: 700 !important;
#   color: #78716C !important;
#   text-transform: uppercase !important;
#   letter-spacing: 0.6px !important;
#   margin-bottom: 12px !important;
#   margin-top: 4px !important;
#   display: block !important;
# }

            
# /* ══════════════════════════════════════════════════════════════════
#    💾 FIXED: ISOLATED SPECIFIC CARD BUTTON SELECTION SHEET (v1.50.0+)
#    ══════════════════════════════════════════════════════════════════ */

# /* 1. UN-SELECTED BASE OPTIONS (Weather, Traffic, City, Festival Options Only)
#       Targets buttons whose unique session IDs contain '_opt_' or '_act_' */
# div[data-testid="stButton"] button[id*="_opt_"],
# div[data-testid="stButton"] button[id*="_act_"] {
#     background-color: #FFFFFF !important;
#     border: 1px solid #EDE8E3 !important;
#     border-radius: 10px !important;
#     padding: 12px 14px !important;
#     min-height: 72px !important; /* Uniform height tracking for step options */
#     width: 100% !important;
#     display: flex !important;
#     align-items: center !important;
#     justify-content: center !important;
#     transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
# }

# /* Paragraph spacing exclusively inside Situation Option buttons */
# div[data-testid="stButton"] button[id*="_opt_"] p,
# div[data-testid="stButton"] button[id*="_act_"] p {
#     font-size: 13px !important;
#     font-weight: 600 !important;
#     color: #44403C !important;
#     line-height: 1.4 !important;
#     text-align: center !important;
#     white-space: pre-line !important; /* Parses \n line-breaks perfectly */
# }

# /* Hover behaviors for unselected cards */
# div[data-testid="stButton"] button[id*="_opt_"]:hover {
#     border-color: #D6D3D1 !important;
#     background-color: #FAF8F5 !important;
# }

# /* 2. DYNAMIC BLUE SELECTION HIGHLIGHT 
#       Triggers ONLY when the button key transitions to an active status string */
# div[data-testid="stButton"] button[id*="_act_"] {
#     background-color: #EFF6FF !important; /* Sophisticated Brand Pastel Tint Accent */
#     border: 2px solid #2563EB !important;   /* Solid Active Contrast Primary Blue Border */
#     box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15) !important;
# }
# div[data-testid="stButton"] button[id*="_act_"] p {
#     color: #1D4ED8 !important; /* Shifts text ink color blue to emphasize selection clarity */
#     font-weight: 700 !important;
# }

# /* 3. STEP 1: RESTAURANT & DELIVERY MODE TOGGLES FIX 
#       Targeting the clear map pin keys to restore their classic dimensions */
# div[data-testid="stButton"] button[id*="clear_rest_"],
# div[data-testid="stButton"] button[id*="clear_del_"] {
#     min-height: auto !important;
#     padding: 8px 16px !important;
#     border-radius: 8px !important;
# }

# /* 4. MAIN FLOW BACK/CONTINUE NAVIGATION CONTROLS FIX 
#       Restores proper layout dimensions for all flow mechanics */
# div[data-testid="stButton"] button[id*="s1_"],
# div[data-testid="stButton"] button[id*="s2_"],
# div[data-testid="stButton"] button[id*="s3_"],
# div[data-testid="stButton"] button[id*="step1_"] {
#     min-height: auto !important;
#     padding: 10px 24px !important;
#     border-radius: 8px !important;
# }

# /* Primary Progression action style rule mapping */
# div[data-testid="stButton"] button[id*="_next"] {
#     background-color: #E8471E !important; /* Restored original brand red/orange background tint */
#     border-color: #E8471E !important;
# }
# div[data-testid="stButton"] button[id*="_next"] p {
#     color: #FFFFFF !important;
#     font-weight: 700 !important;
# }
# div[data-testid="stButton"] button[id*="_next"]:hover {
#     background-color: #CD3713 !important; /* Slightly darker shade for interactive hover hover */
#     border-color: #CD3713 !important;
# }

# /* Secondary Regression action style rule mapping */
# div[data-testid="stButton"] button[id*="_back"] {
#     background-color: #FFFFFF !important;
#     border: 1px solid #EDE8E3 !important;
# }
# div[data-testid="stButton"] button[id*="_back"] p {
#     color: #44403C !important;
# }
# div[data-testid="stButton"] button[id*="_back"]:hover {
#     background-color: #FAF8F5 !important;
#     border-color: #D6D3D1 !important;
# }

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

# /* Forces the outer grid wrapper containers around your weather keys to be completely transparent */
# div[data-testid="stVerticalBlock"]:has(div[class*="st-key-w_"]) div[data-testid="stColumn"] div[data-testid="stButton"] {
#     background-color: transparent !important;
#     border: none !important;
#     box-shadow: none !important;
#     padding: 0 !important;
#     margin: 0 !important;
# }

# /* Forces the inner structural wrapper of the weather buttons to match your clean pill curves */
# div[class*="st-key-w_"] button {
#     border-radius: 24px !important; /* Locks weather choices to the exact same pill shape as traffic */
# }

# /* 2. DENSE SUBSECTION ROWS DESIGN TRACKING */
# .compact-row-title {
#     font-size: 11px !important;
#     font-weight: 800 !important;
#     text-transform: uppercase !important;
#     letter-spacing: 0.6px !important;
#     color: #78716C !important;
#     margin-bottom: 12px !important;
#     display: block !important;
# }

# .compact-row-divider {
#     height: 1px !important;
#     background-color: #EDE8E3 !important;
#     margin: 20px 0 !important;
#     width: 100% !important;
# }

# /* 3. COHESIVE PILL TOGGLE BUTTONS (UN-SELECTED STATE)
#       FIXED: Raised border-radius to 24px and forced transparent column container background styles */
# div[class*="st-key-"][class*="_opt_"] button {
#     background-color: #FFFFFF !important;
#     border: 1px solid #E7E5E4 !important;
#     border-radius: 24px !important; /* FIXED: Perfect circular boundary matching across all rows */
#     padding: 8px 16px !important;   /* Comfortable, clear button spacing */
#     min-height: 38px !important;
#     height: 38px !important;         /* Fixed height across all options ensures symmetry */
#     width: 100% !important;
#     display: inline-flex !important;
#     align-items: center !important;
#     justify-content: center !important;
#     transition: all 0.15s ease-in-out !important;
#     box-shadow: none !important;
# }

# /* Align text lines inside layout frames */
# div[class*="st-key-"][class*="_opt_"] button p,
# div[class*="st-key-"][class*="_act_"] button p {
#     font-size: 13px !important;
#     font-weight: 600 !important;
#     color: #44403C !important;
#     line-height: 1 !important;
#     margin: 0 !important;
#     padding: 0 !important;
#     white-space: nowrap !important; /* Keeps text on one line */
# }

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
   🚀 UNIFIED PILL TOGGLE SYSTEM (STREAMLIT 1.50 COMPATIBLE)
   ================================================================== */

# /* 1. Force the outer structural columns to drop any forced borders, cards, or backgrounds */
# div[data-testid="stColumn"] div[data-testid="stVerticalBlockBorderWrapper"],
# div[data-testid="stColumn"] div[data-testid="stVerticalBlock"] {
#     background-color: transparent !important;
#     border: none !important;
#     box-shadow: none !important;
#     padding: 0 !important;
#     margin: 0 !important;
# }

# /* 2. Target the button containers matching your action keys */
# div[class*="st-key-w_"], 
# div[class*="st-key-t_"], 
# div[class*="st-key-c_"], 
# div[class*="st-key-f_"] {
#     background: transparent !important;
#     border: none !important;
#     padding: 0 !important;
# }

# /* 3. Base style for ALL state selector buttons (Secondary / Unselected) */
# div[class*="st-key-w_"] button[data-testid="baseButton-secondary"],
# div[class*="st-key-t_"] button[data-testid="baseButton-secondary"],
# div[class*="st-key-c_"] button[data-testid="baseButton-secondary"],
# div[class*="st-key-f_"] button[data-testid="baseButton-secondary"] {
#     background-color: #FFFFFF !important;
#     border: 1px solid #E7E5E4 !important;
#     border-radius: 50px !important; /* Forces flawless circular pill edge */
#     height: 40px !important;
#     min-height: 40px !important;
#     width: 100% !important;
#     padding: 0 12px !important;
#     box-shadow: none !important;
#     transition: all 0.2s ease-in-out !important;
# }

# /* Hover style for unselected choices */
# div[class*="st-key-"] button[data-testid="baseButton-secondary"]:hover {
#     border-color: #2563EB !important;
#     background-color: #F8FAFC !important;
# }

# /* 4. Active Selection style (Primary State) */
# div[class*="st-key-w_"] button[data-testid="baseButton-primary"],
# div[class*="st-key-t_"] button[data-testid="baseButton-primary"],
# div[class*="st-key-c_"] button[data-testid="baseButton-primary"],
# div[class*="st-key-f_"] button[data-testid="baseButton-primary"] {
#     background-color: #EFF6FF !important; /* Light blue tint matching screenshot design */
#     border: 2px solid #2563EB !important;  /* Sharp primary blue focus ring */
#     border-radius: 50px !important;
#     height: 40px !important;
#     min-height: 40px !important;
#     width: 100% !important;
#     padding: 0 12px !important;
#     box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15) !important;
# }

# /* 5. Force text rules inside buttons to remain single-line and vertically centered */
# div[class*="st-key-"] button p {
#     font-size: 13px !important;
#     font-weight: 600 !important;
#     color: #1E293B !important;
#     white-space: nowrap !important;
#     overflow: hidden !important;
#     text-overflow: ellipsis !important;
# }

# /* Ensure active button text maintains a clear color matching the theme */
# div[class*="st-key-"] button[data-testid="baseButton-primary"] p {
#     color: #2563EB !important;
#     font-weight: 700 !important;
# }

# /* Typography styles for Subsection Headings */
# .compact-row-title {
#     font-size: 11px !important;
#     font-weight: 800 !important;
#     text-transform: uppercase !important;
#     letter-spacing: 0.8px !important;
#     color: #64748B !important;
#     margin-bottom: 12px !important;
#     display: block !important;
# }

# .compact-row-divider {
#     height: 1px !important;
#     background-color: #E2E8F0 !important;
#     margin: 20px 0 !important;
#     width: 100% !important;
# }
            
# /* ==================================================================
#    🚀 INDIRECT ACTIVE PILL SELECTOR SYSTEM (BYPASSES CONFIG.TOML)
#    ================================================================== */

# /* 1. Strip structural block column layouts */
# div[data-testid="stColumn"] div[data-testid="stVerticalBlockBorderWrapper"],
# div[data-testid="stColumn"] div[data-testid="stVerticalBlock"] {
#     background-color: transparent !important;
#     border: none !important;
#     box-shadow: none !important;
#     padding: 0 !important;
#     margin: 0 !important;
# }

# /* 2. BASE IDLE STATE: Applied to all selection buttons using secondary formatting */
# div[class*="st-key-w_btn_"] button,
# div[class*="st-key-t_btn_"] button,
# div[class*="st-key-c_btn_"] button,
# div[class*="st-key-f_btn_"] button {
#     background-color: #FFFFFF !important;
#     border: 1px solid #E2E8F0 !important;
#     border-radius: 50px !important;
#     height: 38px !important;
#     min-height: 38px !important;
#     width: 100% !important;
#     box-shadow: none !important;
#     padding: 0 14px !important;
#     transition: all 0.2s ease-in-out !important;
# }

# /* Hover style rules for selection controls */
# div[class*="st-key-"] button:hover {
#     border-color: #2563EB !important;
#     background-color: #F8FAFC !important;
# }

# /* 3. DYNAMIC ACTIVE STATE: Overrides secondary styling for active buttons */
# div[class*="_active"] button {
#     background-color: #EFF6FF !important; /* Premium clean soft blue background tint */
#     border: 2px solid #2563EB !important;  /* Vibrant primary blue border highlight */
#     box-shadow: 0 2px 4px rgba(37, 99, 235, 0.08) !important;
# }

# /* 4. BASE TYPOGRAPHY RULES */
# div[class*="st-key-w_btn_"] button p,
# div[class*="st-key-t_btn_"] button p,
# div[class*="st-key-c_btn_"] button p,
# div[class*="st-key-f_btn_"] button p {
#     font-size: 14px !important;     /* Uniform comfortable typography settings */
#     font-weight: 600 !important;
#     color: #475569 !important;      /* Slate visual color palette */
#     white-space: nowrap !important;
# }

# /* 5. ACTIVE TYPOGRAPHY RULES */
# div[class*="_active"] button p {
#     color: #2563EB !important;     /* High contrast matching primary blue text accent */
#     font-weight: 700 !important;
# }

# /* ==================================================================
#    🎯 GLOBAL NAVIGATION & PRIMARY BUTTON RESTORATION
#    ================================================================== */

# /* Keeps bottom navigation elements isolated and clean */
# button[data-testid="baseButton-primary"] {
#     border-radius: 8px !important;
#     height: 46px !important;
#     font-weight: 700 !important;
# }

# button[data-testid="baseButton-primary"] p {
#     color: #FFFFFF !important;     /* Enforces crisp white typography over red theme */
# }

# button[data-testid="baseButton-secondary"]:not([id*="_btn_"]) {
#     border-radius: 8px !important;
#     height: 46px !important;
# }

# /* Headings typography layout classes */
# .compact-row-title {
#     font-size: 11px !important;
#     font-weight: 800 !important;
#     text-transform: uppercase !important;
#     letter-spacing: 0.8px !important;
#     color: #64748B !important;
#     margin-bottom: 12px !important;
#     display: block !important;
# }

# .compact-row-divider {
#     height: 1px !important;
#     background-color: #E2E8F0 !important;
#     margin: 20px 0 !important;
#     width: 100% !important;
# }


# /* ==================================================================
#    🎯 GLOBAL NAVIGATION & PRIMARY BUTTON RESTORATION
#    ================================================================== */

# /* Keeps bottom navigation elements completely isolated and untouched */
# button[data-testid="baseButton-primary"] {
#     border-radius: 8px !important;
#     height: 46px !important;
#     font-weight: 700 !important;
# }

# button[data-testid="baseButton-primary"] p {
#     color: #FFFFFF !important;     /* Keeps navigation text pristine white */
# }

# button[data-testid="baseButton-secondary"] {
#     border-radius: 8px !important;
#     height: 46px !important;
# }

# /* Section Headings Styling Rules */
# .compact-row-title {
#     font-size: 11px !important;
#     font-weight: 800 !important;
#     text-transform: uppercase !important;
#     letter-spacing: 0.8px !important;
#     color: #64748B !important;
#     margin-bottom: 12px !important;
#     display: block !important;
# }

# .compact-row-divider {
#     height: 1px !important;
#     background-color: #E2E8F0 !important;
#     margin: 20px 0 !important;
#     width: 100% !important;
# }

# /* ==================================================================
#    🎯 GLOBAL NAVIGATION & PRIMARY BUTTON RESTORATION
#    ================================================================== */

# /* Keeps bottom navigation elements isolated and clean */
# button[data-testid="baseButton-primary"] {
#     border-radius: 8px !important;
#     height: 46px !important;
#     font-weight: 700 !important;
# }

# button[data-testid="baseButton-primary"] p {
#     color: #FFFFFF !important; /* Enforces crisp white typography over red theme */
# }

# button[data-testid="baseButton-secondary"] {
#     border-radius: 8px !important;
#     height: 46px !important;
# }

# /* Typography styles for Subsection Headings */
# .compact-row-title {
#     font-size: 11px !important;
#     font-weight: 800 !important;
#     text-transform: uppercase !important;
#     letter-spacing: 0.8px !important;
#     color: #64748B !important;
#     margin-bottom: 12px !important;
#     display: block !important;
# }

# .compact-row-divider {
#     height: 1px !important;
#     background-color: #E2E8F0 !important;
#     margin: 20px 0 !important;
#     width: 100% !important;
# }
            
# /* ==================================================================
#    🎯 GLOBAL NAVIGATION & GENERAL APPLICATION BUTTON MASTER
#    ================================================================== */

# /* 1. Base configuration for main primary button state (e.g., "Continue") */
# button[data-testid="baseButton-primary"]:not([id*="_btn_"]) {
#     background-color: #2563EB !important; /* Explicitly forces your theme blue/red color */
#     border: 1px solid transparent !important;
#     border-radius: 8px !important;
#     height: 46px !important;
#     font-weight: 700 !important;
#     transition: all 0.2s ease-in-out !important;
# }

# /* Base configuration for primary button label typography */
# button[data-testid="baseButton-primary"]:not([id*="_btn_"]) p {
#     color: #FFFFFF !important;             /* Enforces crisp white typography */
# }

# /* 🚀 FIX: Prevent the button from turning white or fading out on user hover */
# button[data-testid="baseButton-primary"]:not([id*="_btn_"]):hover {
#     background-color: #1D4ED8 !important; /* Renders a slightly darker blue/shade on hover */
#     border-color: transparent !important;
#     box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2) !important;
# }

# button[data-testid="baseButton-primary"]:not([id*="_btn_"]):hover p {
#     color: #FFFFFF !important;             /* Locks the text label color to solid white */
# }

# /* Active clicked down state configuration */
# button[data-testid="baseButton-primary"]:not([id*="_btn_"]):active {
#     background-color: #1E40AF !important;
#     transform: scale(0.98) !important;
# }

# /* 2. Secondary Navigation Buttons ("← Back to Location") */
# button[data-testid="baseButton-secondary"]:not([id*="_btn_"]) {
#     background-color: #FFFFFF !important;
#     border: 1px solid #E2E8F0 !important;
#     border-radius: 8px !important;
#     height: 46px !important;
#     transition: all 0.2s ease-in-out !important;
# }

# button[data-testid="baseButton-secondary"]:not([id*="_btn_"]):hover {
#     border-color: #2563EB !important;
#     background-color: #F8FAFC !important;
# }

# button[data-testid="baseButton-secondary"]:not([id*="_btn_"]):hover p {
#     color: #2563EB !important;
# }

# /* 3. Typography styles for Subsection Headings */
# .compact-row-title {
#     font-size: 11px !important;
#     font-weight: 800 !important;
#     text-transform: uppercase !important;
#     letter-spacing: 0.8px !important;
#     color: #64748B !important;
#     margin-bottom: 12px !important;
#     display: block !important;
# }

# .compact-row-divider {
#     height: 1px !important;
#     background-color: #E2E8F0 !important;
#     margin: 20px 0 !important;
#     width: 100% !important;
# }

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

# /* ==================================================================
#    🌤️ COHESIVE PILL SELECTION CONTROLS SYSTEM
#    ================================================================== */

# /* BASE COHESIVE PILL STYLE: Targets all choice keys */
# div[class*="st-key-w_choice_"] button,
# div[class*="st-key-t_choice_"] button,
# div[class*="st-key-c_choice_"] button,
# div[class*="st-key-f_choice_"] button {
#     background-color: #FFFFFF !important;
#     border: 1px solid #E2E8F0 !important;
#     border-radius: 50px !important;
#     height: 38px !important;
#     min-height: 38px !important;
#     width: 100% !important;
#     box-shadow: none !important;
#     padding: 0 14px !important;
#     transition: all 0.2s ease-in-out !important;
#     pointer-events: auto !important; /* 🚀 CRITICAL FIX: Restores complete mouse click accessibility */
#     cursor: pointer !important;
# }

# /* Hover styling rules for unselected controls */
# div[class*="st-key-"][class*="_choice_"] button:hover {
#     border-color: #2563EB !important;
#     background-color: #F8FAFC !important;
# }

# /* SELECTED ACTIVE PILL STYLE: Forces the clean soft-blue background */
# div[class*="st-key-w_choice_"] button[kind="primary"],
# div[class*="st-key-t_choice_"] button[kind="primary"],
# div[class*="st-key-c_choice_"] button[kind="primary"],
# div[class*="st-key-f_choice_"] button[kind="primary"] {
#     background-color: #EFF6FF !important; /* Premium soft-blue background */
#     border: 2px solid #2563EB !important;  /* High-contrast blue focus ring */
#     box-shadow: 0 2px 4px rgba(37, 99, 235, 0.08) !important;
#     pointer-events: auto !important;
# }

# /* INPUT MATRIX TYPOGRAPHY METRICS */
# div[class*="st-key-"][class*="_choice_"] button p {
#     font-size: 14px !important;
#     font-weight: 600 !important;
#     color: #475569 !important;
#     white-space: nowrap !important;
# }

# div[class*="st-key-"][class*="_choice_"] button[kind="primary"] p {
#     color: #2563EB !important; /* Vivid blue text color override matching design */
#     font-weight: 700 !important;
# }
            
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

# /* 3. SELECTED ACTIVE PILL STYLE: Faint signature tint with glowing highlight border */
# div[class*="st-key-w_choice_"] button[kind="primary"],
# div[class*="st-key-t_choice_"] button[kind="primary"],
# div[class*="st-key-c_choice_"] button[kind="primary"],
# div[class*="st-key-f_choice_"] button[kind="primary"] {
#     background-color: rgba(255, 122, 89, 0.08) !important; /* Faint signature tint matching macro presets */
#     background: rgba(255, 122, 89, 0.08) !important;
#     border: 1px solid rgba(255, 122, 89, 0.4) !important; /* Premium thin glowing border highlight */
#     box-shadow: none !important;
#     pointer-events: auto !important;
# }

# /* 4. BASE COMPONENT TYPOGRAPHY METRICS */
# div[class*="st-key-w_choice_"] button p,
# div[class*="st-key-t_choice_"] button p,
# div[class*="st-key-c_choice_"] button p,
# div[class*="st-key-f_choice_"] button p {
#     font-size: 13px !important; /* Calibrated micro density typography size scaling */
#     font-weight: 600 !important;
#     color: #4B5563 !important; /* Muted slate gray text color for unselected item labels */
#     white-space: nowrap !important;
# }
            
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
            

# /* ==================================================================
#    🎯 ISOLATED APPLICATION NAVIGATION MASTER (TARGETED BY KEY)
#    ================================================================== */

# /* PRIMARY NAVIGATION BUTTON ("Continue to Driver & Vehicle →") */
# div[class*="st-key-action_nav_next"] button {
#     background-color: #FF4B4B !important; /* Core brand red styling */
#     border: 1px solid transparent !important;
#     border-radius: 8px !important;
#     height: 42px !important;              /* 🚀 REDUCED HEIGHT: Compacted from 46px to initial standards */
#     min-height: 42px !important;
#     width: 100% !important;
#     display: inline-flex !important;
#     align-items: center !important;
#     justify-content: center !important;
#     transition: all 0.2s ease-in-out !important;
#     pointer-events: auto !important;
# }

# div[class*="st-key-action_nav_next"] button p {
#     color: #FFFFFF !important;             /* Enforces crisp white typography */
#     font-size: 14px !important;            /* Clean design text sizing alignment */
#     font-weight: 700 !important;           /* Bold text configuration */
# }

# /* HOVER BEHAVIOR FIX: Keeps the button background solid and darkens slightly */
# div[class*="st-key-action_nav_next"] button:hover {
#     background-color: #E03E3E !important; /* Rich darker red shade on mouse hover */
#     border-color: transparent !important;
#     box-shadow: 0 4px 12px rgba(255, 75, 75, 0.2) !important;
# }

# div[class*="st-key-action_nav_next"] button:hover p {
#     color: #FFFFFF !important;             /* Locks label text color to white */
# }

# /* SECONDARY NAVIGATION BUTTON ("← Back to Location") */
# div[class*="st-key-action_nav_back"] button {
#     background-color: #FFFFFF !important;
#     border: 1px solid #E2E8F0 !important;
#     border-radius: 8px !important;
#     height: 42px !important;              /* 🚀 REDUCED HEIGHT: Balanced symmetry with next item */
#     min-height: 42px !important;
#     width: 100% !important;
#     display: inline-flex !important;
#     align-items: center !important;
#     justify-content: center !important;
#     transition: all 0.2s ease-in-out !important;
#     pointer-events: auto !important;
# }

# div[class*="st-key-action_nav_back"] button p {
#     font-size: 14px !important;
#     font-weight: 700 !important;           /* 🚀 FIXED: Set to bold text to perfectly match the next button style */
#     color: #475569 !important;
# }

# div[class*="st-key-action_nav_back"] button:hover {
#     border-color: #CBD5E1 !important;
#     background-color: #F8FAFC !important;
# }

# div[class*="st-key-action_nav_back"] button:hover p {
#     color: #1E293B !important;
# }
            
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


/* ══════════════════════════════════════════════════════════════════
   🚀 FIX: COMPREHENSIVE RECTANGULAR CELL FRAMES PURGE 
   ══════════════════════════════════════════════════════════════════ */

# /* 1. Strips away the rigid light-grey outline box forced around the columns layout */
# div[data-testid="stVerticalBlock"]:has(div[class*="st-key-w_"]) div[data-testid="stColumn"] div[data-testid="stVerticalBlockBorderWrapper"] {
#     background-color: transparent !important;
#     border: none !important;
#     box-shadow: none !important;
#     padding: 0 !important;
#     margin: 0 !important;
# }

# /* 2. Forces the outer interaction layer around your weather keys to be transparent */
# div[data-testid="stVerticalBlock"]:has(div[class*="st-key-w_"]) div[data-testid="stColumn"] div[data-testid="stButton"] {
#     background-color: transparent !important;
#     border: none !important;
#     box-shadow: none !important;
#     padding: 0 !important;
#     margin: 0 !important;
# }

# /* 3. Re-establishes pristine pill shapes directly on your weather buttons */
# div[class*="st-key-w_"] button {
#     border-radius: 24px !important;
#     background-color: #FFFFFF !important;
#     border: 1px solid #E7E5E4 !important;
#     height: 38px !important;
#     min-height: 38px !important;
# }

# /* 4. Active selection state blue pill transformation for weather choices */
# div[class*="st-key-w_act_"] button {
#     background-color: #EFF6FF !important;
#     border: 2px solid #2563EB !important;
#     box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12) !important;
# }

# /* ──── OPTION CARDS STYLING ──── */
# .opt-grid{display:grid;gap:10px}
# .opt-grid-2{grid-template-columns:1fr 1fr}
# .opt-grid-3{grid-template-columns:1fr 1fr 1fr}
# .opt-grid-4{grid-template-columns:1fr 1fr 1fr 1fr}
# .opt-card{
#   border:2px solid var(--border) !important;
#   border-radius:var(--r) !important;
#   padding:14px 12px !important;
#   text-align:center !important;
#   cursor:pointer !important;
#   background:var(--white) !important;
#   transition:all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
#   display:flex !important;
#   flex-direction:column !important;
#   align-items:center !important;
#   gap:5px !important;
#   width:100% !important;
#   position:relative !important;
#   z-index:1 !important;
# }
# .opt-card:hover{
#   border-color:var(--brand2) !important;
#   background:var(--cream2) !important;
#   transform: translateY(-1px) !important;
# }
# .opt-card.selected{
#   border-color:var(--brand) !important;
#   background:#FFF5F2 !important;
#   box-shadow: 0 4px 12px rgba(232, 71, 30, 0.08) !important;
# }
# .opt-card-icon{font-size:24px !important;line-height:1 !important;}
# .opt-card-label{
#   font-size:13px !important;
#   font-weight:700 !important;
#   color:var(--ink2) !important;
#   white-space: nowrap !important;
#   overflow: hidden !important;
#   text-overflow: ellipsis !important; /* Elegant cutoff protection for 'Sandstorms' */
# }
# .opt-card.selected .opt-card-label{color:var(--brand) !important;}
# .opt-card-sub{font-size:10px !important;color:var(--ink4) !important;}

# /* ──── SECURITY GUARD FOR OPERATIONAL FOOTER BUTTONS ──── */
# button[key="s2_back"], 
# button[key="s2_next"],
# button[key="step1_next"] {
#   position: relative !important;
#   opacity: 1 !important; /* Shields navigation options from taking opacity:0 rules */
#   display: inline-flex !important;
#   z-index: 30 !important;
# }

# /* ──── TOGGLE ROW ──── */
# .toggle-row{display:flex;gap:8px;flex-wrap:wrap}
# .toggle-btn{
#   padding:8px 16px;border-radius:20px;cursor:pointer;
#   border:1.5px solid var(--border);background:var(--white);
#   font-size:13px;font-weight:600;color:var(--ink3);
#   transition:all .15s;
# }
# .toggle-btn:hover{border-color:var(--brand2);color:var(--ink)}
# .toggle-btn.selected{border-color:var(--brand);background:#FFF5F2;color:var(--brand)}

# /* ──── SLIDER CUSTOM ──── */
# .slider-wrap{margin:4px 0 12px}
# .slider-labels{display:flex;justify-content:space-between;font-size:11px;color:var(--ink4);margin-top:4px}

# /* ──── MAP SECTION ──── */
# .map-search-row{display:flex;gap:8px;margin-bottom:10px;align-items:center}
# .search-type-btn{
#   padding:8px 16px;border-radius:10px;cursor:pointer;
#   border:1.5px solid var(--border);background:var(--white);
#   font-size:12px;font-weight:700;color:var(--ink3);white-space:nowrap;
#   transition:all .15s;
# }
# .search-type-btn.active{
#   border-color:var(--brand);background:var(--brand);color:var(--white);
# }
# .coord-display{display:flex;gap:8px;margin-top:10px;}
# .coord-box{flex:1;background:var(--cream2);border:1px solid var(--border);border-radius:10px;padding:10px 14px;}
# .coord-box-head{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:1.2px;color:var(--ink4);margin-bottom:3px;display:flex;align-items:center;gap:5px;}
# .coord-box-val{font-size:13px;font-weight:700;color:var(--brand);font-variant-numeric:tabular-nums;}

# .dist-pill{
#   background:linear-gradient(90deg,#FFF5F2,#FFF0E3);
#   border:1px solid #FDBA74;border-radius:10px;
#   padding:11px 16px;margin-top:10px;
#   display:flex;justify-content:space-between;align-items:center;
# }
# .dist-pill-label{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--brand);}
# .dist-pill-val{font-family:'Bricolage Grotesque',sans-serif;font-size:22px;font-weight:800;color:var(--ink);}
# .dist-pill-unit{font-size:13px;font-weight:500;color:var(--ink3)}

# /* ──── PREDICT MASTER BRAND CTA ──── */
# .pred-btn-wrap > div > button{
#   background:linear-gradient(135deg,#E8471E 0%,#C73D19 100%)!important;
#   color:white!important;border:none!important;
#   border-radius:14px!important;padding:17px 0!important;
#   font-family:'Bricolage Grotesque',sans-serif!important;
#   font-size:16px!important;font-weight:800!important;
#   letter-spacing:.2px!important;
#   box-shadow:0 6px 20px rgba(232,71,30,.4)!important;
#   transition:all .2s!important;width:100%!important;
# }
# .pred-btn-wrap > div > button:hover{
#   background:linear-gradient(135deg,#D43E18 0%,#B5341A 100%)!important;
#   box-shadow:0 8px 28px rgba(232,71,30,.5)!important;
#   transform:translateY(-2px)!important;
# }
# div[data-testid="stButton"] > button{width:100%!important;}

# /* ──── RESULT HUD VISUAL DISPLAY CARD ──── */
# .result-outer{
#   background:linear-gradient(145deg,#1C1917 0%,#292524 100%);
#   border-radius:var(--r3);padding:36px 28px 30px;
#   position:relative;overflow:hidden;
#   box-shadow:0 20px 60px rgba(28,25,23,.25);
# }
# .result-outer::before{
#   content:'';position:absolute;
#   top:-60px;right:-60px;width:220px;height:220px;border-radius:50%;
#   background:radial-gradient(circle,rgba(232,71,30,.2) 0%,transparent 70%);
# }
# .result-outer::after{
#   content:'';position:absolute;
#   bottom:-40px;left:-40px;width:160px;height:160px;border-radius:50%;
#   background:radial-gradient(circle,rgba(255,140,0,.15) 0%,transparent 70%);
# }
# .result-inner{position:relative;z-index:1;text-align:center}
# .result-emoji{font-size:44px;margin-bottom:6px;display:block;animation:bobble 2s ease-in-out infinite}
# @keyframes bobble{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
# .result-tagline{font-size:13px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:rgba(255,255,255,.45);margin-bottom:10px;}
# .result-big{font-family:'Bricolage Grotesque',sans-serif;font-size:88px;font-weight:800;color:#fff;line-height:1;letter-spacing:-4px;}
# .result-unit{font-size:18px;font-weight:700;color:rgba(255,255,255,.45);text-transform:uppercase;letter-spacing:2px;margin-top:4px;margin-bottom:16px;}
# .result-phrase{font-size:16px;font-weight:600;color:rgba(255,255,255,.75);line-height:1.4;margin-bottom:18px;min-height:48px;}
# .result-phrase span{color:var(--brand2);font-weight:800}
# .result-row{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-bottom:14px;}
# .result-chip{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.14);border-radius:8px;padding:6px 13px;font-size:12px;font-weight:600;color:rgba(255,255,255,.7);}
# .result-chip strong{color:#fff}
# .conf-bar-wrap{margin-top:4px}
# .conf-row{display:flex;justify-content:space-between;font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:rgba(255,255,255,.35);margin-bottom:5px}
# .conf-track{height:5px;background:rgba(255,255,255,.12);border-radius:4px;overflow:hidden}
# .conf-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,#FF8C00,#22C55E)}
# .arrive-note{margin-top:14px;font-size:12px;font-weight:600;color:rgba(255,255,255,.4);letter-spacing:.2px;}
# .arrive-note strong{color:rgba(255,255,255,.8)}

# /* ──── FEATURES SHIFT IMPACT PANEL ──── */
# .impact-row{display:flex;align-items:center;gap:10px;padding:9px 0;border-bottom:1px solid var(--border);}
# .impact-row:last-child{border-bottom:none}
# .impact-icon{font-size:16px;width:22px;text-align:center;flex-shrink:0}
# .impact-name{font-size:12px;font-weight:600;color:var(--ink3);width:80px;flex-shrink:0}
# .impact-track{flex:1;height:5px;background:var(--border);border-radius:3px;overflow:hidden}
# .impact-bar{height:100%;border-radius:3px}
# .impact-val{font-size:12px;font-weight:700;color:var(--ink2);width:60px;text-align:right;flex-shrink:0}

# /* ──── SYSTEM ADVISORY INSIGHTS TRIPS ──── */
# .tip-row{display:flex;gap:11px;align-items:flex-start;padding:10px 0;border-bottom:1px solid var(--border);}
# .tip-row:last-child{border-bottom:none}
# .tip-badge{width:28px;height:28px;border-radius:8px;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:13px;}
# .tip-text{font-size:12px;color:var(--ink2);line-height:1.55;font-weight:500}
# .tip-text strong{color:var(--ink);font-weight:700}

/* ════════════════════════════════════════════════════════════════ */
/* SNIPPET 3: PREMIUM EXCLUSION WRAPPERS & BRAND SELECTION HOOKS    */
/* ════════════════════════════════════════════════════════════════ */

# /* Perfect layout padding alignment rules targeting elements inside card shells */
# .fcard-body div[data-testid="stHorizontalBlock"] {
#     padding: 0px 4px !important;
#     gap: 12px !important;
# }

# /* Base custom card parameters for standard option buttons */
# button[key^="w_opt_"], button[key^="w_act_"],
# button[key^="t_opt_"], button[key^="t_act_"],
# button[key^="c_opt_"], button[key^="c_act_"],
# button[key^="f_opt_"], button[key^="f_act_"] {
#     background-color: var(--white) !important;
#     border: 2px solid var(--border) !important;
#     border-radius: var(--r) !important;
#     padding: 18px 12px !important;
#     min-height: 110px !important; /* Establishes total visual height box symmetry */
#     width: 100% !important;
#     display: block !important;
#     white-space: pre-wrap !important; /* Enables native multi-line text layouts */
#     font-family: 'Nunito', sans-serif !important;
#     line-height: 1.6 !important;
#     font-size: 13px !important;
#     font-weight: 700 !important;
#     color: var(--ink) !important;
#     box-shadow: 0 1px 3px rgba(28,25,23,0.02) !important;
#     transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
#     opacity: 1 !important;
# }

# /* Hover configurations for choice cards */
# button[key*="_opt_"]:hover {
#     border-color: var(--brand2) !important;
#     background-color: var(--cream2) !important;
#     transform: translateY(-2px) !important;
#     box-shadow: 0 6px 14px rgba(255, 140, 0, 0.1) !important;
# }

# /* HIGH-CONTRAST BRAND OVERRIDE: Active items instantly get a rich orange border glow */
# button[key*="_act_"] {
#     border: 2px solid var(--brand) !important;
#     background-color: #FFF5F2 !important;
#     box-shadow: 0 4px 14px rgba(232, 71, 30, 0.12) !important;
#     color: var(--brand) !important;
#     transform: none !important;
# }

# /* Typography styles inside white cards */
# .section-badge-label {
#   font-size: 11px !important; 
#   font-weight: 800 !important; 
#   text-transform: uppercase !important; 
#   letter-spacing: 1.2px !important; 
#   color: var(--ink4) !important; 
#   margin-bottom: 12px !important;
# }

/* ──── PROTECTION GUARANTEE FOR MAIN PROGRESSION FOOTERS ──── */
# button[key="step1_next"], 
# button[key="s2_back"], 
# button[key="s2_next"],
# button[key="s3_back"],
# button[key="s3_next"],
# button[key="reset_btn"] {
#     background: linear-gradient(135deg, #E8471E 0%, #FF8C00 100%) !important;
#     color: #FFFFFF !important;
#     border: none !important;
#     border-radius: 12px !important;
#     padding: 14px 28px !important;
#     font-family: 'Bricolage Grotesque', sans-serif !important;
#     font-size: 15px !important;
#     font-weight: 700 !important;
#     box-shadow: 0 4px 14px rgba(232, 71, 30, 0.25) !important;
#     height: auto !important;
#     opacity: 1 !important;
#     white-space: nowrap !important;
# }

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

# /* ──── PLACEHOLDER ──── */
# .placeholder{
#   text-align:center;padding:48px 24px;
#   background:linear-gradient(135deg,var(--cream2),var(--white));
#   border:1.5px dashed var(--border2);border-radius:var(--r2);
# }
# .placeholder-emoji{font-size:48px;margin-bottom:14px;display:block;opacity:.5}
# .placeholder-title{
#   font-family:'Bricolage Grotesque',sans-serif;
#   font-size:17px;font-weight:700;color:var(--ink3);margin-bottom:6px;
# }
# .placeholder-sub{font-size:13px;color:var(--ink4);line-height:1.6;max-width:220px;margin:0 auto}

# /* ──── STREAMLIT WIDGET OVERRIDES ──── */
# div[data-testid="stSelectbox"] label p,
# div[data-testid="stTextInput"] label p,
# div[data-testid="stNumberInput"] label p,
# div[data-testid="stSlider"] label p{
#   font-family:'Nunito',sans-serif!important;
#   font-size:11px!important;font-weight:800!important;
#   letter-spacing:1.5px!important;text-transform:uppercase!important;
#   color:var(--ink3)!important;margin-bottom:4px!important;
# }
# div[data-testid="stSelectbox"] > div > div > div,
# div[data-testid="stTextInput"] > div > div > input,
# div[data-testid="stNumberInput"] > div > div > input{
#   font-family:'Nunito',sans-serif!important;font-size:14px!important;
#   font-weight:600!important;color:var(--ink)!important;
#   background:var(--white)!important;
#   border:1.5px solid var(--border2)!important;border-radius:10px!important;
#   transition:border-color .15s,box-shadow .15s!important;
# }
# div[data-testid="stSelectbox"] > div > div > div:hover,
# div[data-testid="stTextInput"] > div > div > input:focus,
# div[data-testid="stNumberInput"] > div > div > input:focus{
#   border-color:var(--brand)!important;
#   box-shadow:0 0 0 3px rgba(232,71,30,.12)!important;
# }
# /* Slider thumb */
# div[data-testid="stSlider"] > div > div > div > div[role="slider"]{
#   background:var(--white)!important;
#   border:3px solid var(--brand)!important;
#   box-shadow:0 2px 8px rgba(232,71,30,.3)!important;
# }

# /* ──── FIX: NATIVE INPUT OVERRIDES FOR PRECISE DESIGN ──── */
# div[data-testid="stSelectbox"], div[data-testid="stTextInput"] {
#   margin-bottom: 14px !important;
# }

# /* Form element structural labels */
# div[data-testid="stSelectbox"] label, div[data-testid="stTextInput"] label {
#   font-size: 11px !important;
#   font-weight: 700 !important;
#   color: var(--ink3) !important;
#   text-transform: uppercase !important;
#   letter-spacing: 0.5px !important;
# }

# /* Dropdown/Text Input Box borders and field backgrounds */
# div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
#   border-color: var(--border) !important;
#   border-radius: 10px !important;
#   background-color: #FFFFFF !important;
# }

# /* ──── ONBOARDING HUD PLACEHOLDER CARDS ──── */
# .placeholder {
#   text-align: center;
#   padding: 48px 24px !important;
#   background: linear-gradient(135deg, var(--cream2) 0%, var(--white) 100%) !important;
#   border: 2px dashed var(--border2) !important;
#   border-radius: var(--r2) !important;
#   box-shadow: inset 0 2px 8px rgba(28,25,23,.02) !important;
# }

# .placeholder-emoji {
#   font-size: 48px;
#   margin-bottom: 12px;
#   display: block;
#   opacity: .65;
#   animation: float_hint 3s ease-in-out infinite;
# }
# @keyframes float_hint { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-4px); } }

# .placeholder-title {
#   font-family: 'Bricolage Grotesque', sans-serif !important;
#   font-size: 16px !important;
#   font-weight: 800 !important;
#   color: var(--ink) !important;
#   margin-bottom: 6px;
#   letter-spacing: -0.2px;
# }

# .placeholder-sub {
#   font-size: 12px !important;
#   color: var(--ink3) !important;
#   line-height: 1.6;
#   max-width: 240px;
#   margin: 0 auto;
# }

/* ──── ONBOARDING HUD PLACEHOLDER CARDS ──── */
# .placeholder {
#   text-align: center;
#   padding: 48px 24px !important;
#   background: linear-gradient(135deg, #FAF8F5 0%, #FFFFFF 100%) !important;
#   border: 2px dashed #EDE8E3 !important; /* FIXED: Explicit clean fallback hex color */
#   border-radius: 14px !important;         /* FIXED: Standardized to 14px to match your .fcard */
#   box-shadow: inset 0 2px 8px rgba(28,25,23,.02) !important;
#   margin-bottom: 24px !important;        /* FIXED: Added explicit vertical separation margin */
# }


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
            
# /* Active focus color matching your warm tomato-red brand */
# div[data-baseweb="select"]:focus-within > div, 
# div[data-baseweb="input"]:focus-within > div {
#   border-color: var(--brand) !important;
#   box-shadow: 0 0 0 1px var(--brand) !important;
# }

# /* ──── CARD OVERLAYS: TURN BASE OPTION BUTTONS TRANSPARENT ──── */
# /* Use an isolated selector to ensure ONLY card-grid choice selectors are layered invisible */
# div[data-testid="stColumn"] button[key^="w_"],
# div[data-testid="stColumn"] button[key^="t_"],
# div[data-testid="stColumn"] button[key^="c_"],
# div[data-testid="stColumn"] button[key^="f_"] {
#     position: absolute !important;
#     top: 0 !important;
#     left: 0 !important;
#     width: 100% !important;
#     height: 100% !important;
#     opacity: 0 !important; /* Invisible overlay capturing clicks */
#     z-index: 10 !important;
#     cursor: pointer !important;
#     margin: 0 !important;
#     padding: 0 !important;
#     border: none !important;
# }

# /* ──── OPTION CARDS STYLING ──── */
# .opt-card {
#     transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
#     cursor: pointer;
#     position: relative;
#     z-index: 1;
# }

# .opt-card.selected {
#     border: 2px solid var(--brand) !important;
#     box-shadow: 0 4px 14px rgba(232, 71, 30, 0.15) !important;
#     background: #FFFBF9 !important;
# }

# /* Hover events on interactive selection cards */
# div[data-testid="stColumn"]:has(button[key^="w_"]):hover .opt-card,
# div[data-testid="stColumn"]:has(button[key^="t_"]):hover .opt-card,
# div[data-testid="stColumn"]:has(button[key^="c_"]):hover .opt-card,
# div[data-testid="stColumn"]:has(button[key^="f_"]):hover .opt-card {
#     border-color: var(--brand2) !important;
#     transform: translateY(-1px);
# }

# /* Fix text truncation layout glitches for long words */
# .opt-card-label {
#     font-size: 13px !important;
#     font-weight: 700 !important;
#     white-space: nowrap !important;
#     overflow: hidden !important;
#     text-overflow: ellipsis !important;
# }

# /* ──── STANDARD ACTION BUTTONS SECURITY EXCLUSIONS ──── */
# /* This hard override acts as a protective shield ensuring navigation blocks NEVER inherit opacity rules */
# button[key="btn_pin_r"],
# button[key="btn_pin_d"],
# button[key="step1_next"], 
# button[key="s2_back"], 
# button[key="s2_next"],
# button[type="primary"] {
#     position: relative !important;
#     opacity: 1 !important; /* Explicitly forces full visibility */
#     display: inline-flex !important;
#     width: 100% !important;
#     height: auto !important;
#     z-index: 20 !important;
#     background-color: #FFFFFF !important;
#     border: 1px solid var(--border) !important;
#     border-radius: 10px !important;
#     color: var(--ink2) !important;
#     font-family: 'Nunito', sans-serif !important;
#     font-weight: 700 !important;
#     font-size: 13px !important;
# }

# /* ──── SPECIFIC CORE CALL-TO-ACTION BRANDING ──── */
# /* Prominent glowing style for the main progression button at the base of Step 1 */
# button[key="step1_next"],
# button[key="s2_next"] {
#   background: linear-gradient(135deg, var(--brand), var(--brand2)) !important;
#   color: #FFFFFF !important;
#   border: none !important;
#   border-radius: 12px !important;
#   padding: 12px 24px !important;
#   font-family: 'Bricolage Grotesque', sans-serif !important;
#   font-size: 15px !important;
#   font-weight: 700 !important;
#   box-shadow: 0 4px 14px rgba(232, 71, 30, 0.25) !important;
#   transition: transform 0.15s ease, box-shadow 0.15s ease !important;
# }

# button[key="step1_next"]:hover,
# button[key="s2_next"]:hover {
#   transform: translateY(-1px) !important;
#   box-shadow: 0 6px 20px rgba(232, 71, 30, 0.35) !important;
#   color: #FFFFFF !important;
# }

# /* Beautiful styling for the calculated distance pill footer */
# .dist-pill {
#   display: flex !important;
#   align-items: center !important;
#   justify-content: space-between !important;
#   background: linear-gradient(90deg, #F0FDF4 0%, #DCFCE7 100%) !important;
#   border: 1px solid #BBF7D0 !important;
#   border-radius: 10px !important;
#   padding: 12px 16px !important;
#   margin-top: 18px !important;
# }
# .dist-pill-label {
#   font-size: 13px !important;
#   font-weight: 700 !important;
#   color: #16A34A !important;
# }
# .dist-pill-val {
#   font-family: 'Bricolage Grotesque', sans-serif !important;
#   font-size: 18px !important;
#   font-weight: 800 !important;
#   color: #15803D !important;
# }
# .dist-pill-unit {
#   font-size: 12px !important;
#   font-weight: 700 !important;
#   color: #16A34A !important;
# }


# /* ──── FIX: MODERN EMBEDDED CONTAINER STYLE SHEET ──── */

# /* Selects only the major user-input block cards */
# div[data-testid="stVerticalBlockBorderWrapper"] {
#     background-color: #FFFFFF !important;
#     border: 1px solid #EDE8E3 !important;
#     border-radius: 14px !important;
#     box-shadow: 0 2px 12px rgba(28,25,23,.07) !important;
#     padding: 24px 20px 20px 20px !important;
#     margin-bottom: 24px !important;
# }

# /* Stops nested grid structures (like columns) from drawing a white card inside a card */
# div[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stVerticalBlockBorderWrapper"] {
#     background-color: transparent !important;
#     border: none !important;
#     box-shadow: none !important;
#     padding: 0 !important;
#     margin-bottom: 0 !important;
# }

# /* Clear, modern typography layout rules for field labels */
# div[data-testid="stVerticalBlockBorderWrapper"] label {
#     font-size: 11px !important;
#     font-weight: 700 !important;
#     color: var(--ink3) !important;
#     text-transform: uppercase !important;
#     letter-spacing: 0.5px !important;
# }

# /* Elegant header layout rule used inside native container frames */
# .fcard-inline-header {
#     display: flex;
#     align-items: center;
#     gap: 12px;
#     border-bottom: 1px solid #EDE8E3;
#     padding-bottom: 14px;
#     margin-bottom: 16px;
#     width: 100%;
# }

/* Active focus color matching your warm tomato-red brand */
div[data-baseweb="select"]:focus-within > div, 
div[data-baseweb="input"]:focus-within > div {
  border-color: var(--brand) !important;
  box-shadow: 0 0 0 1px var(--brand) !important;
}

/* ──── CARD OVERLAYS: TURN BASE OPTION BUTTONS TRANSPARENT ──── */
# /* Use an isolated selector to ensure ONLY card-grid choice selectors are layered invisible */
# div[data-testid="stColumn"] button[key^="w_"],
# div[data-testid="stColumn"] button[key^="t_"],
# div[data-testid="stColumn"] button[key^="c_"],
# div[data-testid="stColumn"] button[key^="f_"] {
#     position: absolute !important;
#     top: 0 !important;
#     left: 0 !important;
#     width: 100% !important;
#     height: 100% !important;
#     opacity: 0 !important; /* Invisible overlay capturing clicks */
#     z-index: 10 !important;
#     cursor: pointer !important;
#     margin: 0 !important;
#     padding: 0 !important;
#     border: none !important;
#     background: transparent !important;
# }
            
/* ──── CARD OVERLAYS: TARGET ALL GRID SELECTION COLUMNS ──── */
/* Targets choice columns directly by blocking their internal native button wrappers */
# div[data-testid="stFormSubmitButton"] div.stButton,
# div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:has(.opt-card) div.stButton {
#     position: absolute !important;
#     top: 0 !important;
#     left: 0 !important;
#     width: 100% !important;
#     height: 100% !important;
#     margin: 0 !important;
#     padding: 0 !important;
#     z-index: 10 !important;
# }

# div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:has(.opt-card) button {
#     position: absolute !important;
#     top: 0 !important;
#     left: 0 !important;
#     width: 100% !important;
#     height: 100% !important;
#     opacity: 0 !important; /* Forces the duplicate text labels to completely vanish */
#     background: transparent !important;
#     border: none !important;
#     cursor: pointer !important;
#     margin: 0 !important;
#     padding: 0 !important;
#     box-shadow: none !important;
# }

# /* Maintain container block heights so custom cards stretch uniformly */
# div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:has(.opt-card) {
#     position: relative !important;
#     min-height: 96px !important;
#     display: flex !important;
#     flex-direction: column !important;
# }

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

            
# /* ──── OPTION CARDS STYLING ──── */
# .opt-card {
#     transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
#     cursor: pointer;
#     position: relative;
#     z-index: 1;
# }

# .opt-card.selected {
#     border: 2px solid var(--brand) !important;
#     box-shadow: 0 4px 14px rgba(232, 71, 30, 0.15) !important;
#     background: #FFFBF9 !important;
# }

# /* Hover events on interactive selection cards */
# div[data-testid="stColumn"]:has(button[key^="w_"]):hover .opt-card,
# div[data-testid="stColumn"]:has(button[key^="t_"]):hover .opt-card,
# div[data-testid="stColumn"]:has(button[key^="c_"]):hover .opt-card,
# div[data-testid="stColumn"]:has(button[key^="f_"]):hover .opt-card {
#     border-color: var(--brand2) !important;
#     transform: translateY(-1px);
# }

# /* Fix text truncation layout glitches for long words */
# .opt-card-label {
#     font-size: 13px !important;
#     font-weight: 700 !important;
#     white-space: nowrap !important;
#     overflow: hidden !important;
#     text-overflow: ellipsis !important;
# }

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


# /* ──── FIX: MODERN EMBEDDED CONTAINER STYLE SHEET ──── */
# /* TARGET FIX: Apply backgrounds ONLY to explicit layout cards containing forms, preventing grid leakage */
# .fcard, .fcard-container-wrapper {
#     background-color: #FFFFFF !important;
#     border: 1px solid #EDE8E3 !important;
#     border-radius: 14px !important;
#     box-shadow: 0 2px 12px rgba(28,25,23,.07) !important;
#     padding: 24px 20px 20px 20px !important;
#     margin-bottom: 24px !important;
# }

# /* Clear, modern typography layout rules for field labels */
# .fcard-container-wrapper label, .fcard label {
#     font-size: 11px !important;
#     font-weight: 700 !important;
#     color: var(--ink3) !important;
#     text-transform: uppercase !important;
#     letter-spacing: 0.5px !important;
# }

# /* Elegant header layout rule used inside native container frames */
# .fcard-inline-header {
#     display: flex;
#     align-items: center;
#     gap: 12px;
#     border-bottom: 1px solid #EDE8E3;
#     padding-bottom: 14px;
#     margin-bottom: 16px;
#     width: 100%;
# }
   

# /* ──── FIXED: CONTAINER DECK COMPONENT CARDS ──── */
# .fcard {
#   background-color: #FFFFFF !important;
#   border: 1px solid #EDE8E3 !important;
#   border-radius: 14px !important;
#   box-shadow: 0 2px 12px rgba(28,25,23,.07) !important;
#   overflow: hidden;
#   margin-bottom: 24px !important;
#   transition: box-shadow .2s;
#   padding: 0px !important; /* FIXED: Prevent master-card container padding conflicts */
# }

# .fcard:hover {
#   box-shadow: 0 4px 20px rgba(28,25,23,.12) !important;
# }

# .fcard-head {
#   padding: 16px 20px;
#   border-bottom: 1px solid #EDE8E3;
#   display: flex;
#   align-items: center;
#   gap: 10px;
#   background: #FFFFFF;
# }

# .fcard-icon {
#   width: 34px;
#   height: 34px;
#   border-radius: 10px;
#   display: flex;
#   align-items: center;
#   justify-content: center;
#   font-size: 16px;
# }

# .fcard-title {
#   font-size: 14px;
#   font-weight: 700;
#   color: #1C1917;
# }

# .fcard-body {
#   padding: 4px 20px 20px 20px !important;
#   background: #FFFFFF;
# }

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

# /* ──── ULTIMATE DEEP STYLING HOOK FOR STREAMLIT BUTTONS ──── */

# /* 1. Targets the Pin Picker Toggle Buttons on Step 1 */
# div[data-testid="stBaseButton-secondary"] button {
#   background-color: #FFFFFF !important;
#   border: 1px solid #EDE8E3 !important;
#   border-radius: 10px !important;
#   color: #44403C !important;
#   font-family: 'Nunito', sans-serif !important;
#   font-weight: 700 !important;
#   font-size: 13px !important;
#   padding: 8px 16px !important;
#   height: auto !important;
#   transition: all 0.2s ease-in-out !important;
# }

# div[data-testid="stBaseButton-secondary"] button:hover {
#   border-color: #FF8C00 !important;
#   background-color: #FFF0E3 !important;
#   color: #E8471E !important;
# }

# /* 2. Primary Navigation Button ("Continue to Conditions →") */
# div[data-testid="element-container"] blockquote + div div[data-testid="stBaseButton-secondary"] button,
# div[data-testid="stVerticalBlockBorderWrapper"] > div > div:last-child div[data-testid="stBaseButton-secondary"] button {
#   /* This targets the lone action button sitting outside cards at the very bottom */
# }

# /* Let's make an explicit override rule targeting the absolute last button container on screen */
# .stApp [data-testid="stBaseButton-secondary"]:last-of-type button {
#   background: linear-gradient(135deg, #E8471E 0%, #FF8C00 100%) !important;
#   color: #FFFFFF !important;
#   border: none !important;
#   border-radius: 12px !important;
#   padding: 14px 28px !important;
#   font-family: 'Bricolage Grotesque', sans-serif !important;
#   font-size: 15px !important;
#   font-weight: 700 !important;
#   box-shadow: 0 4px 14px rgba(232, 71, 30, 0.25) !important;
#   text-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
#   transition: all 0.2s ease !important;
#   width: 100% !important;
# }

# .stApp [data-testid="stBaseButton-secondary"]:last-of-type button:hover {
#   transform: translateY(-1px) !important;
#   box-shadow: 0 6px 20px rgba(232, 71, 30, 0.4) !important;
#   color: #FFFFFF !important;
# }

# /* Number input +/- buttons */
# button[data-testid="stNumberInputStepDown"],
# button[data-testid="stNumberInputStepUp"]{
#   background:var(--cream2)!important;border-color:var(--border)!important;
#   color:var(--ink2)!important;
# }

# /* ──── PIN MODES: PERSISTENT STATE HIGHLIGHTS ──── */
# /* Primary target state style tracking */
# button[p-mode="active-rest"] {
#     background-color: #3B82F6 !important; /* Premium Blue Accent text color matching pins */
#     color: #FFFFFF !important;
#     border-color: #1D4ED8 !important;
#     font-weight: 700 !important;
#     box-shadow: 0 4px 12px rgba(59, 130, 246, 0.25) !important;
# }

# button[p-mode="active-del"] {
#     background-color: var(--brand2) !important; /* Saffron/Orange Accent token matching delivery indicators */
#     color: #FFFFFF !important;
#     border-color: #EA580C !important;
#     font-weight: 700 !important;
#     box-shadow: 0 4px 12px rgba(232, 71, 30, 0.25) !important;
# }

# /* Ensure secondary focus highlights clear text visibility */
# button[p-mode^="active-"]:hover {
#     opacity: 0.92 !important;
#     color: #FFFFFF !important;
# }

# /* ──── OVERRIDE: PERFECTLY HIDE CARD UTILITY ROW BUTTONS ──── */
# /* Target the inner Streamlit button layout wrappers directly */
# div[data-testid="stColumn"]:has(button[key^="w_"]) div.stButton,
# div[data-testid="stColumn"]:has(button[key^="t_"]) div.stButton,
# div[data-testid="stColumn"]:has(button[key^="c_"]) div.stButton,
# div[data-testid="stColumn"]:has(button[key^="f_"]) div.stButton {
#     position: absolute !important;
#     top: 0 !important;
#     left: 0 !important;
#     width: 100% !important;
#     height: 100% !important;
#     margin: 0 !important;
#     padding: 0 !important;
# }

# /* Force the actual native interactive buttons to stretch completely flat and turn transparent */
# div[data-testid="stColumn"] button[key^="w_"],
# div[data-testid="stColumn"] button[key^="t_"],
# div[data-testid="stColumn"] button[key^="c_"],
# div[data-testid="stColumn"] button[key^="f_"] {
#     position: absolute !important;
#     top: 0 !important;
#     left: 0 !important;
#     width: 100% !important;
#     height: 100% !important;
#     opacity: 0 !important; /* Turns the gray button invisible */
#     z-index: 10 !important; /* Positions it over your custom HTML layer */
#     cursor: pointer !important;
#     margin: 0 !important;
#     padding: 0 !important;
#     border: none !important;
#     background: transparent !important;
# }

# /* Fix vertical layout height shrinkage issues inside Streamlit grids */
# div[data-testid="stColumn"]:has(button[key^="w_"]),
# div[data-testid="stColumn"]:has(button[key^="t_"]),
# div[data-testid="stColumn"]:has(button[key^="c_"]),
# div[data-testid="stColumn"]:has(button[key^="f_"]) {
#     min-height: 105px !important;
#     display: flex !important;
#     flex-direction: column !important;
#     justify-content: flex-start !important;
# }
            
# /* ──── INTERACTIVE FLOATING HOVER TOOLTIP SYSTEM ──── */
# .custom-tooltip {
#     position: relative;
#     display: inline-flex;
#     align-items: center;
#     cursor: help;
# }

# /* Micro trigger info design styling */
# .info-trigger {
#     font-size: 11px !important;
#     background: #F5F5F4 !important;
#     border: 1px solid #E7E5E4 !important;
#     color: #78716C !important;
#     width: 16px !important;
#     height: 16px !important;
#     border-radius: 50% !important;
#     display: flex !important;
#     align-items: center !important;
#     justify-content: center !important;
#     font-weight: bold !important;
#     transition: all 0.2s ease-in-out;
# }

# .custom-tooltip:hover .info-trigger {
#     background: #E7E5E4 !important;
#     color: #1C1917 !important;
# }

# /* The actual floating text bubble (Hidden by default) */
# .custom-tooltip .tooltip-text {
#     visibility: hidden;
#     width: 240px;
#     background-color: #1C1917 !important; /* Elegant dark slate background */
#     color: #FFFFFF !important;
#     text-align: left;
#     border-radius: 8px !important;
#     padding: 10px 12px !important;
#     font-size: 11px !important;
#     font-weight: 500 !important;
#     line-height: 1.4 !important;
    
#     /* Absolute Floating Placement */
#     position: absolute;
#     z-index: 99999 !important; /* Ensure it floats completely over map structures */
#     bottom: 140%; /* Spits out above the ℹ️ badge */
#     left: 50%;
#     transform: translateX(-50%) translateY(4px);
    
#     /* Smooth Transitions */
#     opacity: 0;
#     transition: opacity 0.2s ease, transform 0.2s ease;
#     box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important;
#     pointer-events: none; /* Prevents cursor stuttering */
# }

# /* Micro Triangle Arrow Indicator pointing downward */
# .custom-tooltip .tooltip-text::after {
#     content: "";
#     position: absolute;
#     top: 100%;
#     left: 50%;
#     margin-left: -5px;
#     border-width: 5px;
#     border-style: solid;
#     border-color: #1C1917 transparent transparent transparent;
# }

# /* RE-ACTIVE HOVER INJECTIONS */
# .custom-tooltip:hover .tooltip-text {
#     visibility: visible;
#     opacity: 1;
#     transform: translateX(-50%) translateY(0);
# }
            
# /* ──── FIXED: INTERACTIVE FLOATING HOVER TOOLTIP SYSTEM ──── */
# .custom-tooltip {
#     position: relative !important;
#     display: inline-flex !important;
#     align-items: center !important;
#     cursor: help !important;
# }

# /* Fixed circular badge using clear letter string characters */
# .info-trigger {
#     font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
#     font-size: 10px !important;
#     font-weight: 700 !important;
#     font-style: italic !important;
#     background: #F5F5F4 !important;
#     border: 1px solid #D6D3D1 !important;
#     color: #78716C !important;
#     width: 15px !important;
#     height: 15px !important;
#     border-radius: 50% !important;
#     display: inline-flex !important;
#     align-items: center !important;
#     justify-content: center !important;
#     text-align: center !important;
#     line-height: 1 !important;
#     transition: all 0.2s ease-in-out !important;
# }

# .custom-tooltip:hover .info-trigger {
#     background: #78716C !important;
#     color: #FFFFFF !important;
#     border-color: #78716C !important;
# }

# /* Tooltip floating text container bubble configuration */
# .custom-tooltip .tooltip-text {
#     visibility: hidden !important;
#     width: 240px !important;
#     background-color: #1C1917 !important;
#     color: #FFFFFF !important;
#     text-align: left !important;
#     border-radius: 8px !important;
#     padding: 10px 12px !important;
#     font-size: 11px !important;
#     font-weight: 500 !important;
#     line-height: 1.4 !important;
    
#     /* Absolute Layout Placement Floating Layer */
#     position: absolute !important;
#     z-index: 999999 !important; /* Forces it over search dropdown wrappers */
#     bottom: 140% !important; 
#     left: 50% !important;
#     transform: translateX(-50%) translateY(4px) !important;
    
#     opacity: 0 !important;
#     transition: opacity 0.2s ease, transform 0.2s ease !important;
#     box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important;
#     pointer-events: none !important;
# }

# .custom-tooltip .tooltip-text::after {
#     content: "" !important;
#     position: absolute !important;
#     top: 100% !important;
#     left: 50% !important;
#     margin-left: -5px !important;
#     border-width: 5px !important;
#     border-style: solid !important;
#     border-color: #1C1917 transparent transparent transparent !important;
# }

# .custom-tooltip:hover .tooltip-text {
#     visibility: visible !important;
#     opacity: 1 !important;
#     transform: translateX(-50%) translateY(0) !important;
# }

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

# /* ──── FOOTER ──── */
# .footer{
#   margin:0;padding:18px 36px;
#   background:var(--white);border-top:1px solid var(--border);
#   display:flex;justify-content:space-between;align-items:center;
#   flex-wrap:wrap;gap:8px;
# }
# .footer-l{font-size:13px;font-weight:700;color:var(--ink3)}
# .footer-r{font-size:11px;color:var(--ink4);letter-spacing:.3px}

# /* ──── RESPONSIVE ──── */
# @media(max-width:860px){
#   .opt-grid-4{grid-template-columns:1fr 1fr}
#   .opt-grid-3{grid-template-columns:1fr 1fr}
#   .topbar,.content-shell,.hero,.steps-bar{padding-left:18px!important;padding-right:18px!important}
# }

# /* ──── MISC ──── */
# .spacer{height:1px;background:var(--border);margin:18px 0}
# .inline-badge{
#   display:inline-flex;align-items:center;gap:4px;
#   padding:3px 9px;border-radius:20px;font-size:11px;font-weight:700;
# }
# .ib-green{background:#F0FDF4;color:#16A34A;border:1px solid #86EFAC}
# .ib-amber{background:#FFFBEB;color:#B45309;border:1px solid #FCD34D}
# .ib-orange{background:#FFF7ED;color:#C2410C;border:1px solid #FDBA74}
# .ib-red{background:#FEF2F2;color:#DC2626;border:1px solid #FCA5A5}
# .ib-blue{background:#EFF6FF;color:#1D4ED8;border:1px solid #93C5FD}
            
/* map iframe */
iframe{border-radius:12px!important}
            
# /* ──── ULTIMATE DEEP STYLING HOOK FOR STREAMLIT BUTTONS ──── */

# /* 1. Targets the Pin Picker Toggle Buttons on Step 1 & Standard Base Buttons */
# div[data-testid="stBaseButton-secondary"] button {
#   background-color: #FFFFFF !important;
#   border: 1px solid #EDE8E3 !important;
#   border-radius: 10px !important;
#   color: #44403C !important;
#   font-family: 'Nunito', sans-serif !important;
#   font-weight: 700 !important;
#   font-size: 13px !important;
#   padding: 8px 16px !important;
#   height: auto !important;
#   transition: all 0.2s ease-in-out !important;
#   opacity: 1 !important; /* Forces global security default to prevent visibility drop */
# }

# div[data-testid="stBaseButton-secondary"] button:hover {
#   border-color: #FF8C00 !important;
#   background-color: #FFF0E3 !important;
#   color: #E8471E !important;
# }
            
/* ==========================================================================
   1. FIXED SECONDARY BUTTONS (PREVENTS WIDGET INTERFERENCE)
   ========================================================================== */
# /* We target standard layout blocks explicitly, completely leaving segmented wrappers alone */
# div[data-testid="stElementContainer"]:not(:has(div[data-testid="stSegmentedControl"])) div[data-testid="stBaseButton-secondary"] button {
#   background-color: #FFFFFF !important;
#   border: 1px solid #EDE8E3 !important;
#   border-radius: 10px !important;
#   color: #44403C !important;
#   font-family: 'Nunito', sans-serif !important;
#   font-weight: 700 !important;
#   font-size: 13px !important;
#   padding: 8px 16px !important;
#   height: auto !important;
#   box-shadow: none !important;
# }

# div[data-testid="stElementContainer"]:not(:has(div[data-testid="stSegmentedControl"])) div[data-testid="stBaseButton-secondary"] button:hover {
#   border-color: #FF8C00 !important;
#   background-color: #FFF0E3 !important;
#   color: #E8471E !important;
# }

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


# /* 2. PROTECTIVE EXCLUSIONS: Guard navigation workflow actions against opacity collapses */
# div[data-testid="stColumn"] button[key="s2_back"],
# div[data-testid="stColumn"] button[key="s2_next"],
# div[data-testid="stColumn"] button[key="s3_back"],
# div[data-testid="stColumn"] button[key="s3_next"],
# div[data-testid="stColumn"] button[key="step1_next"] {
#   position: relative !important;
#   opacity: 1 !important; /* Bulletproof visibility fix for Tab 2 */
#   display: inline-flex !important;
#   width: 100% !important;
#   z-index: 30 !important; /* Layers layout controls completely above option card hotspots */
# }

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

# /* ──── OVERRIDE: PERFECTLY HIDE CARD UTILITY ROW BUTTONS ──── */
# div[data-testid="stColumn"]:has(button[key^="w_"]) div.stButton,
# div[data-testid="stColumn"]:has(button[key^="t_"]) div.stButton,
# div[data-testid="stColumn"]:has(button[key^="c_"]) div.stButton,
# div[data-testid="stColumn"]:has(button[key^="f_"]) div.stButton {
#     position: absolute !important;
#     top: 0 !important;
#     left: 0 !important;
#     width: 100% !important;
#     height: 100% !important;
#     margin: 0 !important;
#     padding: 0 !important;
#     z-index: 10 !important;
# }

# div[data-testid="stColumn"] button[key^="w_"],
# div[data-testid="stColumn"] button[key^="t_"],
# div[data-testid="stColumn"] button[key^="c_"],
# div[data-testid="stColumn"] button[key^="f_"] {
#     position: absolute !important;
#     top: 0 !important;
#     left: 0 !important;
#     width: 100% !important;
#     height: 100% !important;
#     opacity: 0 !important; /* Softens standard text elements completely invisible */
#     z-index: 12 !important;
#     cursor: pointer !important;
#     margin: 0 !important;
#     padding: 0 !important;
#     border: none !important;
#     background: transparent !important;
# }

# div[data-testid="stColumn"]:has(button[key^="w_"]),
# div[data-testid="stColumn"]:has(button[key^="t_"]),
# div[data-testid="stColumn"]:has(button[key^="c_"]),
# div[data-testid="stColumn"]:has(button[key^="f_"]) {
#     min-height: 105px !important;
#     display: flex !important;
#     flex-direction: column !important;
#     justify-content: flex-start !important;
# }

/* ──── FOOTER ──── */
.footer{
  margin:0;padding:18px 36px;
  background:var(--white);border-top:1px solid var(--border);
  display:flex;justify-content:space-between;align-items:center;
  flex-wrap:wrap;gap:8px;
}
.footer-l{font-size:13px;font-weight:700;color:var(--ink3)}
.footer-r{font-size:11px;color:var(--ink4);letter-spacing:.3px}

# /* ──── RESPONSIVE ──── */
# @media(max-width:860px){
#   .opt-grid-4{grid-template-columns:1fr 1fr}
#   .opt-grid-3{grid-template-columns:1fr 1fr}
#   .topbar,.content-shell,.hero,.steps-bar{padding-left:18px!important;padding-right:18px!important}
# }

/* ──── MISC ──── */
.spacer{height:1px;background:var(--border);margin:18px 0}
# .inline-badge{
#   display:inline-flex;align-items:center;gap:4px;
#   padding:3px 9px;border-radius:20px;font-size:11px;font-weight:700;
# }
# .ib-green{background:#F0FDF4;color:#16A34A;border:1px solid #86EFAC}
# .ib-amber{background:#FFFBEB;color:#B45309;border:1px solid #FCD34D}
# .ib-orange{background:#FFF7ED;color:#C2410C;border:1px solid #FDBA74}
# .ib-red{background:#FEF2F2;color:#DC2626;border:1px solid #FCA5A5}
# .ib-blue{background:#EFF6FF;color:#1D4ED8;border:1px solid #93C5FD}

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

# /* ==================================================================
#    🏍️ GRID CHOICE BUTTONS AS TALL OPTION CARDS (.OPT-CARD)
#    ================================================================== */

# /* UNSELECTED OPTION CARD MATRIX */
# div[class*="st-key-v_choice_"] button,
# div[class*="st-key-vc_choice_"] button,
# div[class*="st-key-md_choice_"] button {
#     background-color: #FFFFFF !important;
#     border: 1px solid #E7E5E4 !important;
#     border-radius: 10px !important;
#     min-height: 86px !important; /* Generates card height parameters */
#     width: 100% !important;
#     padding: 12px 10px !important;
#     white-space: pre-line !important; /* Enables multi-line break positioning */
#     display: block !important;
#     text-align: center !important;
#     box-shadow: 0 1px 2px rgba(0,0,0,0.02) !important;
#     transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
# }

# /* Mouse hover transitions over option card choices */
# div[class*="st-key-v_choice_"] button:hover,
# div[class*="st-key-vc_choice_"] button:hover,
# div[class*="st-key-md_choice_"] button:hover {
#     border-color: #FF4B4B !important; /* Highlights brand red accents */
#     background-color: #FFFBF9 !important;
#     transform: translateY(-2px) !important;
#     box-shadow: 0 6px 14px rgba(255, 75, 75, 0.08) !important;
# }

# /* SELECTED DYNAMIC ACTIVE OPTION CARD (Matches .opt-card.selected) */
# div[class*="st-key-v_choice_"] button[data-testid="baseButton-primary"],
# div[class*="st-key-vc_choice_"] button[data-testid="baseButton-primary"],
# div[class*="st-key-md_choice_"] button[data-testid="baseButton-primary"] {
#     background-color: #FFF5F2 !important; /* Premium light orange background */
#     border: 2px solid #FF4B4B !important;  /* Active brand accent ring */
#     box-shadow: 0 4px 14px rgba(255, 75, 75, 0.14) !important;
#     transform: none !important;
# }

# /* TYPOGRAPHY METRICS INSIDE OPTION MATRIX CARDS */
# div[class*="st-key-v_choice_"] button p,
# div[class*="st-key-vc_choice_"] button p,
# div[class*="st-key-md_choice_"] button p {
#     font-size: 13px !important;
#     line-height: 1.5 !important;
#     color: #44403C !important;
#     font-weight: 500 !important;
# }

# /* Style active option text weights */
# div[class*="st-key-v_choice_"] button[data-testid="baseButton-primary"] p,
# div[class*="st-key-vc_choice_"] button[data-testid="baseButton-primary"] p,
# div[class*="st-key-md_choice_"] button[data-testid="baseButton-primary"] p {
#     color: #FF4B4B !important; /* Emphasizes selected text lines */
#     font-weight: 700 !important;
# }
            
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
              
# /* ══════════════════════════════════════════════════════════════════
#    🚀 FIX: FINAL STABLE STRUCTURAL PARENT GRID CONTAINER PURGE
#    ══════════════════════════════════════════════════════════════════ */

# /* 1. Strips away the rigid light-grey outline box forced around the columns layout */
# div[data-testid="stVerticalBlock"]:has(div[class*="st-key-w_"]) div[data-testid="stColumn"] div[data-testid="element-container"] {
#     background-color: transparent !important;
#     background: transparent !important;
#     border: none !important;
#     border-color: transparent !important;
#     box-shadow: none !important;
# }

# /* 2. Forces the inner structural wrapper of the weather buttons to match your clean pill curves */
# div[class*="st-key-w_"] button {
#     border-radius: 24px !important;
#     background-color: #FFFFFF !important;
#     border: 1px solid #E7E5E4 !important;
#     height: 38px !important;
#     min-height: 38px !important;
#     width: 100% !important;
# }

# /* 3. Active selection state blue pill transformation for weather choices */
# div[class*="st-key-w_act_"] button {
#     background-color: #EFF6FF !important;
#     border: 2px solid #2563EB !important;
#     box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12) !important;
# }

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

# /* ──── GLASSMORPHIC NEON STEPPER ──── */
# .glass-stepper-container {
#   display: flex !important;
#   flex-direction: row !important;
#   align-items: center !important;
#   justify-content: flex-start !important;
#   gap: 16px !important;
#   background: rgba(255, 255, 255, 0.06) !important;
#   border: 1px solid rgba(255, 255, 255, 0.1) !important;
#   border-radius: 12px !important;
#   padding: 4px 24px !important;
#   width: 100%;
#   overflow-x: auto;
#   backdrop-filter: blur(16px);
#   box-shadow: 0 4px 30px rgba(0, 0, 0, 0.05) !important;
#   margin-bottom: 28px !important;
# }

# .glass-step {
#   display: flex !important;
#   align-items: center !important;
#   padding: 14px 16px !important;
#   position: relative !important;
#   white-space: nowrap !important;
#   font-size: 14px !important;
#   font-weight: 700 !important;
#   transition: all 0.3s ease !important;
# }

# /* Inactive/Locked Step State */
# .glass-step.step-locked {
#   opacity: 0.35 !important;
#   color: #A8A29E !important;
# }

# /* Completed Step State */
# .glass-step.step-done {
#   opacity: 0.8 !important;
#   color: #22C55E !important;
# }

# /* Active Step State with Glow Line Indicator */
# .glass-step.step-active {
#   opacity: 1 !important;
#   color: #FF8C00 !important; /* Matches your brand color */
# }

# .glass-step.step-active::after {
#   content: "" !important;
#   position: absolute !important;
#   bottom: 0 !important;
#   left: 12px !important;
#   right: 12px !important;
#   height: 3px !important;
#   background: #FF8C00 !important;
#   border-radius: 4px 4px 0 0 !important;
#   box-shadow: 0 -2px 10px rgba(255, 140, 0, 0.8), 0 0 4px rgba(255, 140, 0, 0.5) !important;
# }

            
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



            
/* ══════════════════════════════════════════════════════════════════
   🚀 FIX: ULTIMATE BASE COLUMN CONTAINER TRANSPARENCY BYPASS
   ══════════════════════════════════════════════════════════════════ */

# /* 1. Strips away the native grey box backgrounds and borders from the 6 weather column blocks */
# div[data-testid="stVerticalBlock"]:has(div[class*="st-key-w_"]) div[data-testid="stColumn"] {
#     background-color: transparent !important;
#     background: transparent !important;
#     border: none !important;
#     box-shadow: none !important;
#     padding: 0 !important;
# }

# /* 2. Forces the inner structural wrapper of the weather buttons to match your clean pill curves */
# div[class*="st-key-w_"] button {
#     border-radius: 24px !important;
#     background-color: #FFFFFF !important;
#     border: 1px solid #E7E5E4 !important;
#     height: 38px !important;
#     min-height: 38px !important;
#     width: 100% !important;
# }

# /* 3. Active selection state blue pill transformation for weather choices */
# div[class*="st-key-w_act_"] button {
#     background-color: #EFF6FF !important;
#     border: 2px solid #2563EB !important;
#     box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12) !important;
# }

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

# ─── TOPBAR ───────────────────────────────────────────────────────
# st.markdown(f"""
# <div class="topbar">
#   <div class="brand">
#     <div class="brand-logo">🍔</div>
#     <div>
#       <div class="brand-name">Deliver<em>IQ</em></div>
#     </div>
#   </div>
#   <div style="display:flex;gap:10px;align-items:center">
#     <div style="font-size:12px;font-weight:600;color:var(--ink3);
#       background:var(--cream2);border:1px solid var(--border);
#       border-radius:8px;padding:5px 12px;">
#       🤖 Random Forest · ML Pipeline
#     </div>
#     <div class="live-chip">
#       <div class="live-dot"></div>
#       {'Live Model' if model else 'Demo Mode'}
#     </div>
#   </div>
# </div>
# """, unsafe_allow_html=True)

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
    '<span style="font-size: 13px; line-height: 1;">🤖</span>rf_pipeline.py'
    '</div>'
) + status_tag + '</div>'

brand_html = (
    '<div class="brand" style="display: flex; align-items: center; gap: 8px;">'
    '<div class="brand-logo" style="font-size: 24px;">🍔</div>'
    '<div class="brand-name" style="font-size: 22px; font-weight: 700; color: var(--ink);">'
    'Deliver<em style="color: #FF4B4B; font-style: italic;">IQ</em></div>'
    '</div>'
)

# ─── 3. RENDER SAFELY VIA STREAMLIT NATIVE COLUMNS ────────────────
topbar_container = st.container()
with topbar_container:
    # Explicitly sets up column splits (1 part brand, 2 parts spacer, 1 part badge layout)
    col_brand, col_spacer, col_badges = st.columns([1, 2, 1], vertical_alignment="center")
    
    with col_brand:
        st.markdown(brand_html, unsafe_allow_html=True)
        
    with col_badges:
        st.markdown(
            '<div style="display: flex; justify-content: flex-end;">' + dev_tags_html + '</div>', 
            unsafe_allow_html=True
        )

# Adds a clean structural separator beneath the updated elements
st.markdown('<hr style="margin: 0px 0px 20px 0px; border: 0; border-top: 1px solid var(--border); opacity: 0.3;">', unsafe_allow_html=True)


# # ─── HERO ────────────────────────────────────────────────────────
# st.markdown("""
# <div class="hero">
#   <div class="hero-inner">
#     <div class="hero-tag">🍕 AI-Powered Food Delivery Intelligence</div>
#     <div class="hero-h1">How long until<br><span>your next meal?</span></div>
#     <div class="hero-sub">
#       Input your location, pick your conditions — and let our trained ML model 
#       predict your delivery ETA with precision. Just like the apps you love, 
#       but with the science laid bare.
#     </div>
#     <div class="hero-chips">
#       <div class="hero-chip">🎯 <strong>~93%</strong> Accuracy</div>
#       <div class="hero-chip">⚡ <strong>&lt;50ms</strong> Inference</div>
#       <div class="hero-chip">🗺️ <strong>14</strong> Input Features</div>
#       <div class="hero-chip">🌆 Metropolitan · Urban · Semi-Urban</div>
#     </div>
#   </div>
# </div>
# """, unsafe_allow_html=True)

# if not model:
#     st.markdown("""
#     <div style="background:#FFFBEB;border:1px solid #FCD34D;border-left:3px solid #F59E0B;
#       padding:11px 18px;font-size:13px;font-weight:600;color:#78350F;">
#       ⚠️ Demo mode — no <code>.pkl</code> file detected. Heuristic estimates shown. 
#       Drop your model file alongside <code>app.py</code> for live predictions.
#     </div>
#     """, unsafe_allow_html=True)

# ─── HERO (Production-Grade st.html Block) ────────────────────────
# Using unique custom style elements inside st.html to prevent any global CSS overrides
# st.html("""
# <div class="hero">
#   <div class="hero-inner">
#     <div class="hero-tag">🍕 AI-Powered Food Delivery Intelligence</div>
#     <div class="hero-h1">How long until<br><span>your next meal?</span></div>
#     <div class="hero-sub">
#       Input your location, pick your conditions — and let our trained ML model 
#       predict your delivery ETA with precision. Just like the apps you love, 
#       but with the science laid bare.
#     </div>
    
#     <!-- FIX: Swapped out 'hero-bento-deck' class for a strict inline bento deck wrapper -->
#     <div style="display: flex !important; flex-direction: row !important; flex-wrap: wrap !important; justify-content: center !important; gap: 12px !important; margin-top: 28px !important; width: 100% !important;">
      
#       <!-- FIX: Uses custom-bento-card attributes instead of generic divs to fully isolate styling -->
#       <span style="background: rgba(255, 255, 255, 0.05) !important; border: 1px solid rgba(255, 255, 255, 0.15) !important; border-radius: 12px !important; padding: 8px 18px !important; font-size: 13px !important; font-weight: 600 !important; color: rgba(255, 255, 255, 0.95) !important; display: inline-flex !important; align-items: center !important; gap: 8px !important; white-space: nowrap !important; width: auto !important;">
#         🎯 <span style="color: #FFA043 !important; font-weight: 700 !important; display: inline !important;">~93%</span> Accuracy
#       </span>
      
#       <span style="background: rgba(255, 255, 255, 0.05) !important; border: 1px solid rgba(255, 255, 255, 0.15) !important; border-radius: 12px !important; padding: 8px 18px !important; font-size: 13px !important; font-weight: 600 !important; color: rgba(255, 255, 255, 0.95) !important; display: inline-flex !important; align-items: center !important; gap: 8px !important; white-space: nowrap !important; width: auto !important;">
#         ⚡ <span style="color: #FFA043 !important; font-weight: 700 !important; display: inline !important;">&lt;50ms</span> Inference
#       </span>
      
#       <span style="background: rgba(255, 255, 255, 0.05) !important; border: 1px solid rgba(255, 255, 255, 0.15) !important; border-radius: 12px !important; padding: 8px 18px !important; font-size: 13px !important; font-weight: 600 !important; color: rgba(255, 255, 255, 0.95) !important; display: inline-flex !important; align-items: center !important; gap: 8px !important; white-space: nowrap !important; width: auto !important;">
#         🗺️ <span style="color: #FFA043 !important; font-weight: 700 !important; display: inline !important;">14</span> Input Features
#       </span>
      
#       <span style="background: rgba(255, 255, 255, 0.05) !important; border: 1px solid rgba(255, 255, 255, 0.15) !important; border-radius: 12px !important; padding: 8px 18px !important; font-size: 13px !important; font-weight: 600 !important; color: rgba(255, 255, 255, 0.95) !important; display: inline-flex !important; align-items: center !important; gap: 8px !important; white-space: nowrap !important; width: auto !important;">
#         🌆 <span style="color: #FFA043 !important; font-weight: 700 !important; display: inline !important;">Metropolitan</span> · Urban · Semi-Urban
#       </span>

#     </div>
#   </div>
# </div>
# """)

# ─── HERO (Production-Grade st.html Block) ────────────────────────
# st.html("""
# <div class="hero">
#   <div class="hero-inner">
#     <div class="hero-tag">🍕 AI-Powered Food Delivery Intelligence</div>
#     <div class="hero-h1">How long until<br><span>your next meal?</span></div>
#     <div class="hero-sub">
#       Configure your route conditions and leverage production-grade machine learning to instantly predict exact delivery arrival ETAs.
#     </div>
    
#     <div class="hero-chips-container">
      
#       <span class="hero-chip-light chip-accuracy-light">
#         🎯 <strong>~93%</strong> Accuracy
#       </span>
      
#       <span class="hero-chip-light chip-inference-light">
#         ⚡ <strong>&lt;50ms</strong> Inference
#       </span>
      
#       <span class="hero-chip-light chip-features-light">
#         🗺️ <strong>14</strong> Input Features
#       </span>
      
#       <span class="hero-chip-light chip-geo-light">
#         🌆 <strong>Metropolitan</strong> · Urban · Semi-Urban
#       </span>

#     </div>
#   </div>
# </div>
# """)

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


# # ─── STEP NAVIGATOR (HTML, selection managed by buttons below) ───
# step_states = []
# for i in range(1, 5):
#     cls = "active" if s.step == i else ("done" if s.step > i else "")
#     step_states.append((i, cls))

# labels = ["📍 Location","🌤️ Conditions","🏍️ Driver & Vehicle","⚡ Predict"]
# st.markdown('<div class="steps-bar">' +
#     "".join(f'<div class="step-tab {cls}"><div class="step-num">{"✓" if cls=="done" else i}</div><div class="step-label">{lbl}</div></div>'
#             for (i,cls),lbl in zip(step_states,labels)) +
#     '</div>', unsafe_allow_html=True)

# # ─── STEP NAVIGATOR (Flat-Compiled Single-Line System) ───
# step_states = []
# for i in range(1, 5):
#     cls = "active" if s.step == i else ("done" if s.step > i else "")
#     step_states.append((i, cls))

# labels = ["📍 Location", "🌤️ Conditions", "🏍️ Driver & Vehicle", "⚡ Predict"]

# bg_colors = {"active": "#E8471E", "done": "#22C55E", "": "#EDE8E3"}
# text_colors = {"active": "#FFFFFF", "done": "#FFFFFF", "": "#78716C"}
# label_colors = {"active": "#1C1917", "done": "#78716C", "": "#A8A29E"}
# border_bottoms = {"active": "3px solid #E8471E", "done": "3px solid transparent", "": "3px solid transparent"}

# tabs_list = []
# for (i, cls), lbl in zip(step_states, labels):
#     num_display = "✓" if cls == "done" else str(i)
    
#     # CRITICAL: This HTML fragment must be a completely compressed single line string to avoid markdown parsing bugs
#     tab_html = f'<div style="display:flex;align-items:center;gap:8px;padding:12px 20px;border-bottom:{border_bottoms[cls]};white-space:nowrap;"><span style="width:24px;height:24px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;background:{bg_colors[cls]};color:{text_colors[cls]};line-height:1;flex-shrink:0;">{num_display}</span><span style="font-size:13px;font-weight:700;color:{label_colors[cls]};line-height:1;">{lbl}</span></div>'
#     tabs_list.append(tab_html)

# # Flatten everything completely into one seamless wrapper string
# full_nav_html = f'<div style="display:flex;flex-direction:row;align-items:center;justify-content:flex-start;gap:12px;background:#FFFFFF;border-bottom:1px solid #EDE8E3;padding:0 36px;width:100%;overflow-x:auto;">{"".join(tabs_list)}</div>'

# st.markdown(full_nav_html, unsafe_allow_html=True)

# ─── STEP NAVIGATOR (Premium Light-Theme Pastel System) ───
step_states = []
for i in range(1, 5):
    cls = "active" if s.step == i else ("done" if s.step > i else "")
    step_states.append((i, cls))

labels = ["📍 Location", "🌤️ Conditions", "🏍️ Driver & Vehicle", "⚡ Predict"]

# PREMIUM COLOR PALETTE TO MATCH LIGHT-THEME METRICS
bg_colors = {
    "active": "#FF7A59",       # Clean, modern coral-orange (Premium active focal anchor)
    "done": "#D1FAE5",         # Soft subtle emerald-pastel background
    "": "#F3F4F6"              # Muted neutral light-gray background
}

text_colors = {
    "active": "#FFFFFF",       # High contrast crisp white number inside active coral circle
    "done": "#065F46",         # Muted deep dark green checkmark inside pastel emerald circle
    "": "#9CA3AF"              # Muted neutral gray number text
}

label_colors = {
    "active": "#1F2937",       # Bold deep charcoal for premium legibility on the active step label
    "done": "#6B7280",         # Muted charcoal for completed steps
    "": "#9CA3AF"              # Subtle light-gray for inactive step labels
}

border_bottoms = {
    "active": "3px solid #FF7A59", # Clean coral accent indicator underline matching active badge
    "done": "3px solid transparent", 
    "": "3px solid transparent"
}

tabs_list = []
for (i, cls), lbl in zip(step_states, labels):
    num_display = "✓" if cls == "done" else str(i)
    
    # CRITICAL: Keeping string completely flat and single-line to avoid any Streamlit layout breakages
    tab_html = f'<div style="display:flex;align-items:center;gap:8px;padding:12px 20px;border-bottom:{border_bottoms[cls]};white-space:nowrap;"><span style="width:24px;height:24px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;background:{bg_colors[cls]};color:{text_colors[cls]};line-height:1;flex-shrink:0;">{num_display}</span><span style="font-size:13px;font-weight:700;color:{label_colors[cls]};line-height:1;">{lbl}</span></div>'
    tabs_list.append(tab_html)

# Flatten everything cleanly into the parent border navigation ribbon
full_nav_html = f'<div style="display:flex;flex-direction:row;align-items:center;justify-content:flex-start;gap:12px;background:#FFFFFF;border-bottom:1px solid #E2E8F0;padding:0 36px;width:100%;overflow-x:auto;">{"".join(tabs_list)}</div>'

st.markdown(full_nav_html, unsafe_allow_html=True)


# # ─── STEP NAVIGATOR (Render-Insulated st.html System) ───
# # Use explicit text descriptions. Icons are injected securely via HTML character tokens.
# labels = [
#     "&#128205; Location", 
#     "&#127381; Conditions", 
#     "&#127949; Driver & Vehicle", 
#     "&#9889; Predict"
# ]
# tabs_list = []

# for idx, lbl in enumerate(labels, start=1):
#     if s.step == idx:
#         state_class = "step-active"
#     elif s.step > idx:
#         state_class = "step-done"
#     else:
#         state_class = "step-locked"
        
#     # Standardizing layout strings to avoid Streamlit container manipulation
#     tab_html = f'<div class="glass-step {state_class}"><span>{lbl}</span></div>'
#     tabs_list.append(tab_html)

# # Wrap inside a completely un-phased layout row
# full_nav_html = f'<div class="glass-stepper-container">{"".join(tabs_list)}</div>'

# # FIX: Switch out st.markdown for pure html ingestion
# st.html(full_nav_html)



# ─── MAIN CONTENT ────────────────────────────────────────────────
# st.markdown('<div class="content-shell">', unsafe_allow_html=True)

# main_col, result_col = st.columns([11, 8], gap="large")

# # ─── MAIN CONTENT (High-Density Dashboard Structure) ───
# st.markdown('<div class="content-shell">', unsafe_allow_html=True)

# # 11:8 grid creates an asymmetrical layout that separates inputs from outputs perfectly
# main_col, result_col = st.columns([11, 8], gap="large")

# with main_col:
#     # Card wrapper to isolate input variables cleanly
#     st.markdown('''
#     <div class="fcard">
#         <div class="fcard-head">
#             <div class="fcard-icon" style="background:#FFF0E3;color:var(--brand)">📍</div>
#             <div>
#                 <div class="fcard-title">Delivery Route Configuration</div>
#                 <div class="fcard-desc">Specify origin restaurant zone and destination drop point</div>
#             </div>
#         </div>
#     </div>
#     ''', unsafe_allow_html=True)
    
#     # ─── Place your actual interactive Streamlit inputs inside this column block! ───
#     # Example placeholder for your interactive elements:
#     restaurant = st.selectbox("Select Restaurant Zone", ["Zone Alpha", "Zone Beta", "Downtown Hub"])
#     destination = st.text_input("Destination Address / Coordinates")

# with result_col:
#     # Sidebar widget that keeps prediction data floating prominently
#     st.markdown('''
#     <div class="fcard" style="border-color:var(--brand2); background:linear-gradient(to bottom, #FFFFFF, var(--cream2))">
#         <div class="fcard-head">
#             <div class="fcard-icon" style="background:rgba(232,71,30,0.1);color:var(--brand)">🔮</div>
#             <div>
#                 <div class="fcard-title">Live ML ETA Engine</div>
#                 <div class="fcard-desc">Model predictions refresh instantly on feature update</div>
#             </div>
#         </div>
#         <div style="padding:40px 20px; text-align:center;">
#             <div style="font-size:12px; font-weight:700; color:var(--ink3); text-transform:uppercase; letter-spacing:1px;">Estimated Delivery Time</div>
#             <div style="font-size:48px; font-weight:900; color:var(--brand); margin:12px 0; font-family:'Bricolage Grotesque', sans-serif;">-- : --</div>
#             <div style="font-size:12px; color:var(--ink4)">Awaiting complete layer feature details...</div>
#         </div>
#     </div>
#     ''', unsafe_allow_html=True)

# ─── MAIN CONTENT (High-Density Dashboard Structure) ───
# st.markdown('<div class="content-shell">', unsafe_allow_html=True)

# main_col, result_col = st.columns([11, 8], gap="large")

# ─── MAIN CONTENT (High-Density Dashboard Structure) ───
# st.markdown('<div class="content-shell">', unsafe_allow_html=True)

# 11:8 grid layout distribution
main_col, result_col = st.columns([11, 8], gap="large")

# with main_col:
#     # STEP A: Open the Card Wrapper (Do NOT close the fcard-body div!)
#     st.markdown('''
#     <div class="fcard">
#         <div class="fcard-head">
#             <div class="fcard-icon" style="background:#FFF0E3;color:var(--brand)">📍</div>
#             <div>
#                 <div class="fcard-title">Delivery Route Configuration</div>
#                 <div class="fcard-desc">Specify origin restaurant zone and destination drop point</div>
#             </div>
#         </div>
#         <div class="fcard-body">
#     ''', unsafe_allow_html=True)
    
#     # STEP B: Native Streamlit components now render safely nested inside the card background canvas
#     restaurant = st.selectbox("Select Restaurant Zone", ["Zone Alpha", "Zone Beta", "Downtown Hub"])
#     destination = st.text_input("Destination Address / Coordinates")
    
#     # STEP C: Explicitly close the layout containers after your inputs
#     st.markdown('</div></div>', unsafe_allow_html=True)

# with result_col:
#     # Keeps your prediction block floating neatly on the right hand side
#     st.markdown('''
#     <div class="fcard" style="border-color:var(--brand2); background:linear-gradient(to bottom, #FFFFFF, var(--cream2))">
#         <div class="fcard-head">
#             <div class="fcard-icon" style="background:rgba(232,71,30,0.1);color:var(--brand)">🔮</div>
#             <div>
#                 <div class="fcard-title">Live ML ETA Engine</div>
#                 <div class="fcard-desc">Model predictions refresh instantly on feature update</div>
#             </div>
#         </div>
#         <div style="padding:40px 20px; text-align:center;">
#             <div style="font-size:12px; font-weight:700; color:var(--ink3); text-transform:uppercase; letter-spacing:1px;">Estimated Delivery Time</div>
#             <div style="font-size:48px; font-weight:900; color:var(--brand); margin:12px 0; font-family:'Bricolage Grotesque', sans-serif;">-- : --</div>
#             <div style="font-size:12px; color:var(--ink4)">Awaiting complete layer feature details...</div>
#         </div>
#     </div>
#     ''', unsafe_allow_html=True)

# ══════════════════════════════════════════════
# LEFT  —  STEP CONTENT
# ══════════════════════════════════════════════
# with main_col:

#     # ── STEP 1: LOCATION ─────────────────────
#     if s.step == 1:
#         st.markdown("""
#         <div class="section-title">📍 Where's your order going?</div>
#         <div class="section-sub">Select the restaurant and your delivery location on the map — 
#         or search by name. Click to drop pins.</div>
#         """, unsafe_allow_html=True)

#         # Map card
#         st.markdown("""
#         <div class="fcard">
#           <div class="fcard-head">
#             <div class="fcard-icon" style="background:#FFF0E3;">🗺️</div>
#             <div>
#               <div class="fcard-title">Interactive Map</div>
#               <div class="fcard-desc">Click to pin · Search to navigate · Route shown automatically</div>
#             </div>
#           </div>
#           <div class="fcard-body">
#         """, unsafe_allow_html=True)

#         # Pin mode selector
#         pin_r, pin_d = st.columns(2)
#         with pin_r:
#             if st.button(
#                 f"{'🔵 ' if s.pin_mode=='restaurant' else ''}📍 Set Restaurant Pin",
#                 use_container_width=True,
#                 key="btn_pin_r"
#             ):
#                 s.pin_mode = "restaurant"
#         with pin_d:
#             if st.button(
#                 f"{'🟠 ' if s.pin_mode=='delivery' else ''}📦 Set Delivery Pin",
#                 use_container_width=True,
#                 key="btn_pin_d"
#             ):
#                 s.pin_mode = "delivery"

#         pin_hint = ("🔵 Click map to set <strong>Restaurant</strong> location"
#                     if s.pin_mode == "restaurant"
#                     else "🟠 Click map to set <strong>Delivery</strong> location")
#         st.markdown(f'<div style="background:var(--cream2);border:1px solid var(--border2);border-radius:8px;padding:9px 14px;font-size:12px;font-weight:600;color:var(--ink2);margin:8px 0;">{pin_hint}</div>', unsafe_allow_html=True)

#         # Map rendering
#         try:
#             import folium
#             from streamlit_folium import st_folium

#             clat = (s.rest_lat + s.del_lat) / 2
#             clon = (s.rest_lon + s.del_lon) / 2

#             m = folium.Map(location=[clat,clon], zoom_start=13, tiles=None)
#             folium.TileLayer(
#                 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',
#                 attr='CartoDB Voyager', name='Voyager'
#             ).add_to(m)

#             # Restaurant marker (blue)
#             folium.Marker(
#                 [s.rest_lat, s.rest_lon],
#                 tooltip="🍽️ Restaurant",
#                 popup=f"Restaurant<br>{s.rest_lat:.4f}, {s.rest_lon:.4f}",
#                 icon=folium.Icon(color='blue', icon='cutlery', prefix='fa')
#             ).add_to(m)

#             # Delivery marker (orange/red)
#             folium.Marker(
#                 [s.del_lat, s.del_lon],
#                 tooltip="📦 Delivery",
#                 popup=f"Delivery<br>{s.del_lat:.4f}, {s.del_lon:.4f}",
#                 icon=folium.Icon(color='orange', icon='map-marker', prefix='fa')
#             ).add_to(m)

#             # Dashed route
#             folium.PolyLine(
#                 [[s.rest_lat,s.rest_lon],[s.del_lat,s.del_lon]],
#                 color='#E8471E', weight=2.5, opacity=.7, dash_array='8 5'
#             ).add_to(m)

#             # Search plugin
#             try:
#                 from folium.plugins import Geocoder
#                 Geocoder(collapsed=False, position='topright').add_to(m)
#             except Exception:
#                 pass

#             map_result = st_folium(m, width="100%", height=320, key="map_main")

#             if map_result and map_result.get("last_clicked"):
#                 c = map_result["last_clicked"]
#                 if s.pin_mode == "restaurant":
#                     s.rest_lat = round(c["lat"], 6)
#                     s.rest_lon = round(c["lng"], 6)
#                     s.pin_mode = "delivery"
#                 else:
#                     s.del_lat = round(c["lat"], 6)
#                     s.del_lon = round(c["lng"], 6)
#                     s.pin_mode = "restaurant"

#         except ImportError:
#             st.markdown("""
#             <div style="background:var(--cream2);border:1.5px dashed var(--border2);
#               border-radius:10px;padding:22px;text-align:center;font-size:13px;color:var(--ink3)">
#               🗺️ Map requires <code>folium</code> + <code>streamlit-folium</code><br>
#               <span style="font-size:11px">pip install folium streamlit-folium</span>
#             </div>
#             """, unsafe_allow_html=True)

#         st.markdown('</div></div>', unsafe_allow_html=True)

#         # Manual coordinate inputs
#         st.markdown("""
#         <div class="fcard">
#           <div class="fcard-head">
#             <div class="fcard-icon" style="background:#EFF6FF;">🎯</div>
#             <div>
#               <div class="fcard-title">Fine-tune Coordinates</div>
#               <div class="fcard-desc">Edit manually or use the map above</div>
#             </div>
#           </div>
#           <div class="fcard-body">
#         """, unsafe_allow_html=True)

#         st.markdown('<div style="font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:1.5px;color:var(--ink4);margin-bottom:8px;">🍽️ Restaurant Location</div>', unsafe_allow_html=True)
#         cr1,cr2 = st.columns(2)
#         with cr1:
#             s.rest_lat = st.number_input("Latitude", value=float(s.rest_lat), format="%.6f", step=.001, key="rlat")
#         with cr2:
#             s.rest_lon = st.number_input("Longitude", value=float(s.rest_lon), format="%.6f", step=.001, key="rlon")

#         st.markdown('<div style="font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:1.5px;color:var(--ink4);margin:12px 0 8px;">📦 Delivery Location</div>', unsafe_allow_html=True)
#         cd1,cd2 = st.columns(2)
#         with cd1:
#             s.del_lat = st.number_input("Latitude ", value=float(s.del_lat), format="%.6f", step=.001, key="dlat")
#         with cd2:
#             s.del_lon = st.number_input("Longitude ", value=float(s.del_lon), format="%.6f", step=.001, key="dlon")

#         dist = haversine(s.rest_lat,s.rest_lon,s.del_lat,s.del_lon)
#         st.markdown(f"""
#         <div class="dist-pill">
#           <span class="dist-pill-label">📐 Straight-line distance</span>
#           <span><span class="dist-pill-val">{dist:.2f}</span> <span class="dist-pill-unit">km</span></span>
#         </div>
#         """, unsafe_allow_html=True)
#         st.markdown('</div></div>', unsafe_allow_html=True)

#         st.markdown('<div style="height:8px"></div>', unsafe_allow_html=True)
#         if st.button("Continue to Conditions →", use_container_width=True, key="step1_next"):
#             s.step = 2
#             st.rerun()

# # ══════════════════════════════════════════════
# # LEFT COLUMN  —  DYNAMIC STEP ROUTING
# # ══════════════════════════════════════════════
# with main_col:

    # # ── STEP 1: LOCATION ─────────────────────
    # if s.step == 1:
    #     st.markdown("""
    #     <div class="section-title">📍 Where's your order going?</div>
    #     <div class="section-sub">Select the restaurant and your delivery location on the map — or search by name. Click to drop pins.</div>
    #     """, unsafe_allow_html=True)

    #     # Card 1: Form Selection
    #     st.markdown('''
    #     <div class="fcard">
    #         <div class="fcard-head">
    #             <div class="fcard-icon" style="background:#FFF0E3;color:var(--brand)">📍</div>
    #             <div>
    #                 <div class="fcard-title">Delivery Route Configuration</div>
    #                 <div class="fcard-desc">Specify origin restaurant zone and destination drop point</div>
    #             </div>
    #         </div>
    #         <div class="fcard-body">
    #     ''', unsafe_allow_html=True)
        
    #     # Only declared once inside the correct operational step scope
    #     restaurant = st.selectbox("Select Restaurant Zone", ["Zone Alpha", "Zone Beta", "Downtown Hub"], key="route_restaurant_select")
    #     destination = st.text_input("Destination Address / Coordinates", key="route_destination_input")
    #     st.markdown('</div></div>', unsafe_allow_html=True)

    #     # Card 2: Interactive Map Panel
    #     st.markdown("""
    #     <div class="fcard">
    #       <div class="fcard-head">
    #         <div class="fcard-icon" style="background:#FFF0E3;">🗺️</div>
    #         <div>
    #           <div class="fcard-title">Interactive Map</div>
    #           <div class="fcard-desc">Click to pin · Search to navigate · Route shown automatically</div>
    #         </div>
    #       </div>
    #       <div class="fcard-body">
    #     """, unsafe_allow_html=True)

    #     pin_r, pin_d = st.columns(2)
    #     with pin_r:
    #         if st.button(f"{'🔵 ' if s.pin_mode=='restaurant' else ''}📍 Set Restaurant Pin", use_container_width=True, key="btn_pin_r"):
    #             s.pin_mode = "restaurant"
    #     with pin_d:
    #         if st.button(f"{'🟠 ' if s.pin_mode=='delivery' else ''}📦 Set Delivery Pin", use_container_width=True, key="btn_pin_d"):
    #             s.pin_mode = "delivery"

    #     pin_hint = ("🔵 Click map to set <strong>Restaurant</strong> location" if s.pin_mode == "restaurant" else "🟠 Click map to set <strong>Delivery</strong> location")
    #     st.markdown(f'<div style="background:var(--cream2);border:1px solid var(--border2);border-radius:8px;padding:9px 14px;font-size:12px;font-weight:600;color:var(--ink2);margin:8px 0;">{pin_hint}</div>', unsafe_allow_html=True)

    #     try:
    #         import folium
    #         from streamlit_folium import st_folium

    #         clat = (s.rest_lat + s.del_lat) / 2
    #         clon = (s.rest_lon + s.del_lon) / 2

    #         m = folium.Map(location=[clat, clon], zoom_start=13, tiles=None)
    #         folium.TileLayer('https://{s}://{z}/{x}/{y}{r}.png', attr='CartoDB Voyager', name='Voyager').add_to(m)

    #         folium.Marker([s.rest_lat, s.rest_lon], tooltip="🍽️ Restaurant", icon=folium.Icon(color='blue', icon='cutlery', prefix='fa')).add_to(m)
    #         folium.Marker([s.del_lat, s.del_lon], tooltip="📦 Delivery", icon=folium.Icon(color='orange', icon='map-marker', prefix='fa')).add_to(m)
    #         folium.PolyLine([[s.rest_lat, s.rest_lon], [s.del_lat, s.del_lon]], color='#E8471E', weight=2.5, opacity=.7, dash_array='8 5').add_to(m)

    #         map_result = st_folium(m, width="100%", height=320, key="map_main")

    #         if map_result and map_result.get("last_clicked"):
    #             c = map_result["last_clicked"]
    #             if s.pin_mode == "restaurant":
    #                 s.rest_lat = round(c["lat"], 6)
    #                 s.rest_lon = round(c["lng"], 6)
    #                 s.pin_mode = "delivery"
    #             else:
    #                 s.del_lat = round(c["lat"], 6)
    #                 s.del_lon = round(c["lng"], 6)
    #                 s.pin_mode = "restaurant"
    #     except ImportError:
    #         st.markdown('<div style="padding:22px;text-align:center;color:var(--ink3)">🗺️ Map requires folium modules</div>', unsafe_allow_html=True)

    #     st.markdown('</div></div>', unsafe_allow_html=True)

    #     # Card 3: Coordinate Readout
    #     st.markdown("""
    #     <div class="fcard">
    #       <div class="fcard-head">
    #         <div class="fcard-icon" style="background:#EFF6FF;">🎯</div>
    #         <div>
    #           <div class="fcard-title">Fine-tune Coordinates</div>
    #           <div class="fcard-desc">Edit manually or use the map above</div>
    #         </div>
    #       </div>
    #       <div class="fcard-body">
    #     """, unsafe_allow_html=True)

    #     st.markdown('<div style="font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:1.5px;color:var(--ink4);margin-bottom:8px;">🍽️ Restaurant Location</div>', unsafe_allow_html=True)
    #     cr1, cr2 = st.columns(2)
    #     with cr1:
    #         s.rest_lat = st.number_input("Latitude", value=float(s.rest_lat), format="%.6f", step=.001, key="rlat")
    #     with cr2:
    #         s.rest_lon = s.rest_lon = st.number_input("Longitude", value=float(s.rest_lon), format="%.6f", step=.001, key="rlon")

    #     st.markdown('<div style="font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:1.5px;color:var(--ink4);margin:12px 0 8px;">📦 Delivery Location</div>', unsafe_allow_html=True)
    #     cd1, cd2 = st.columns(2)
    #     with cd1:
    #         s.del_lat = st.number_input("Latitude ", value=float(s.del_lat), format="%.6f", step=.001, key="dlat")
    #     with cd2:
    #         s.del_lon = st.number_input("Longitude ", value=float(s.del_lon), format="%.6f", step=.001, key="dlon")

    #     dist = haversine(s.rest_lat, s.rest_lon, s.del_lat, s.del_lon)
    #     st.markdown(f"""
    #     <div class="dist-pill">
    #       <span class="dist-pill-label">📐 Straight-line distance</span>
    #       <span><span class="dist-pill-val">{dist:.2f}</span> <span class="dist-pill-unit">km</span></span>
    #     </div>
    #     """, unsafe_allow_html=True)
    #     st.markdown('</div></div>', unsafe_allow_html=True)

    #     st.markdown('<div style="height:12px"></div>', unsafe_allow_html=True)
    #     if st.button("Continue to Conditions →", use_container_width=True, key="step1_next"):
    #         s.step = 2
    #         st.rerun()

    # # ── STEP 1: LOCATION ─────────────────────
    # if s.step == 1:
    #     st.markdown("""
    #     <div class="section-title">📍 Where's your order going?</div>
    #     <div class="section-sub">Select the restaurant and your delivery location on the map — or search by name. Click to drop pins.</div>
    #     """, unsafe_allow_html=True)

    #     # ─── CARD 1: ROUTE CONFIGURATION ───
    #     # Native bordered container creates a styled white card around everything inside it
    #     with st.container(border=True):
    #         st.markdown('''
    #         <div class="fcard-inline-header">
    #             <div class="fcard-icon" style="background:#FFF0E3;color:var(--brand);padding:6px 10px;border-radius:8px;">📍</div>
    #             <div>
    #                 <div style="font-size:14px;font-weight:700;color:var(--ink);line-height:1.2;">Delivery Route Configuration</div>
    #                 <div style="font-size:11px;color:var(--ink4);margin-top:2px;">Specify origin restaurant zone and destination drop point</div>
    #             </div>
    #         </div>
    #         ''', unsafe_allow_html=True)

    # # ── STEP 1: LOCATION ─────────────────────
    # if s.step == 1:
    #      # 🚀 MOVE THE SPACER HERE: Right below the typography text but BEFORE the card container
    #     # st.write("") # Quick native Streamlit empty layout row anchor
    #     # st.markdown('<div style="margin-top: 14px; display: block; clear: both;"></div>', unsafe_allow_html=True)
    #     st.markdown("""
    #     <div class="section-title">📍 Where's your order going?</div>
    #     <div class="section-sub">Select the restaurant and your delivery location on the map — or search by name. Click to drop pins.</div>
    #     """, unsafe_allow_html=True)

    #     # # FIX: Inserts an explicit spatial buffer to create a clean gap below the subtext
    #     # st.markdown('<div style="height: 16px;"></div>', unsafe_allow_html=True)

    #     # # 🚀 MOVE THE SPACER HERE: Right below the typography text but BEFORE the card container
    #     # st.write("") # Quick native Streamlit empty layout row anchor
    #     # st.markdown('<div style="margin-top: 14px; display: block; clear: both;"></div>', unsafe_allow_html=True)

    #     # ─── CARD 1: ROUTE CONFIGURATION ───
    #     with st.container(border=True):
    #         st.markdown('''
    #         <div class="fcard-inline-header">
    #             <div class="fcard-icon" style="background:#FFF0E3;color:var(--brand);padding:6px 10px;border-radius:8px;">📍</div>
    #             <div>
    #                 <div style="font-size:14px;font-weight:700;color:var(--ink);line-height:1.2;">Delivery Route Configuration</div>
    #                 <div style="font-size:11px;color:var(--ink4);margin-top:2px;">Specify origin restaurant zone and destination drop point</div>
    #             </div>
    #         </div>
    #         ''', unsafe_allow_html=True)
            
    #         # The rest of your card 1 selectbox inputs follow here natively...
            
    #         restaurant = st.selectbox("Select Restaurant Zone", ["Zone Alpha", "Zone Beta", "Downtown Hub"], key="route_restaurant_select")
    #         destination = st.text_input("Destination Address / Coordinates", key="route_destination_input")

    #     # ─── CARD 2: INTERACTIVE MAP PANEL ───
    #     with st.container(border=True):
    #         st.markdown('''
    #         <div class="fcard-inline-header">
    #             <div class="fcard-icon" style="background:#FFF0E3;padding:6px 10px;border-radius:8px;">🗺️</div>
    #             <div>
    #                 <div style="font-size:14px;font-weight:700;color:var(--ink);line-height:1.2;">Interactive Map</div>
    #                 <div style="font-size:11px;color:var(--ink4);margin-top:2px;">Click to pin · Search to navigate · Route shown automatically</div>
    #             </div>
    #         </div>
    #         ''', unsafe_allow_html=True)
            
    #         pin_r, pin_d = st.columns(2)
    #         with pin_r:
    #             if st.button(f"{'🔵 ' if s.pin_mode=='restaurant' else ''}📍 Set Restaurant Pin", use_container_width=True, key="btn_pin_r"):
    #                 s.pin_mode = "restaurant"
    #         with pin_d:
    #             if st.button(f"{'🟠 ' if s.pin_mode=='delivery' else ''}📦 Set Delivery Pin", use_container_width=True, key="btn_pin_d"):
    #                 s.pin_mode = "delivery"

    #         pin_hint = ("🔵 Click map to set <strong>Restaurant</strong> location" if s.pin_mode == "restaurant" else "🟠 Click map to set <strong>Delivery</strong> location")
    #         st.markdown(f'<div style="background:var(--cream2);border:1px solid var(--border2);border-radius:8px;padding:9px 14px;font-size:12px;font-weight:600;color:var(--ink2);margin:8px 0 16px 0;">{pin_hint}</div>', unsafe_allow_html=True)

    #         try:
    #             import folium
    #             from streamlit_folium import st_folium

    #             clat = (s.rest_lat + s.del_lat) / 2
    #             clon = (s.rest_lon + s.del_lon) / 2

    #             m = folium.Map(location=[clat, clon], zoom_start=13, tiles=None)
    #             folium.TileLayer('https://{s}://{z}/{x}/{y}{r}.png', attr='CartoDB Voyager', name='Voyager').add_to(m)

    #             folium.Marker([s.rest_lat, s.rest_lon], tooltip="🍽️ Restaurant", icon=folium.Icon(color='blue', icon='cutlery', prefix='fa')).add_to(m)
    #             folium.Marker([s.del_lat, s.del_lon], tooltip="📦 Delivery", icon=folium.Icon(color='orange', icon='map-marker', prefix='fa')).add_to(m)
    #             folium.PolyLine([[s.rest_lat, s.rest_lon], [s.del_lat, s.del_lon]], color='#E8471E', weight=2.5, opacity=.7, dash_array='8 5').add_to(m)

    #             map_result = st_folium(m, width="100%", height=320, key="map_main")

    #             if map_result and map_result.get("last_clicked"):
    #                 c = map_result["last_clicked"]
    #                 if s.pin_mode == "restaurant":
    #                     s.rest_lat = round(c["lat"], 6)
    #                     s.rest_lon = round(c["lng"], 6)
    #                     s.pin_mode = "delivery"
    #                 else:
    #                     s.del_lat = round(c["lat"], 6)
    #                     s.del_lon = round(c["lng"], 6)
    #                     s.pin_mode = "restaurant"
    #         except ImportError:
    #             st.markdown('<div style="padding:22px;text-align:center;color:var(--ink3)">🗺️ Map requires folium modules</div>', unsafe_allow_html=True)

    #     # ─── CARD 3: COORDINATE TOOLBOX ───
    #     with st.container(border=True):
    #         st.markdown('''
    #         <div class="fcard-inline-header">
    #             <div class="fcard-icon" style="background:#EFF6FF;padding:6px 10px;border-radius:8px;">🎯</div>
    #             <div>
    #                 <div style="font-size:14px;font-weight:700;color:var(--ink);line-height:1.2;">Fine-tune Coordinates</div>
    #                 <div style="font-size:11px;color:var(--ink4);margin-top:2px;">Edit manually or use the map above</div>
    #             </div>
    #         </div>
    #         ''', unsafe_allow_html=True)
            
    #         st.markdown('<div style="font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:1.5px;color:var(--ink4);margin-bottom:8px;">🍽️ Restaurant Location</div>', unsafe_allow_html=True)
    #         cr1, cr2 = st.columns(2)
    #         with cr1:
    #             s.rest_lat = st.number_input("Latitude", value=float(s.rest_lat), format="%.6f", step=.001, key="rlat")
    #         with cr2:
    #             s.rest_lon = st.number_input("Longitude", value=float(s.rest_lon), format="%.6f", step=.001, key="rlon")

    #         st.markdown('<div style="font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:1.5px;color:var(--ink4);margin:16px 0 8px 0;">📦 Delivery Location</div>', unsafe_allow_html=True)
    #         cd1, cd2 = st.columns(2)
    #         with cd1:
    #             s.del_lat = st.number_input("Latitude ", value=float(s.del_lat), format="%.6f", step=.001, key="dlat")
    #         with cd2:
    #             s.del_lon = st.number_input("Longitude ", value=float(s.del_lon), format="%.6f", step=.001, key="dlon")

    #         dist = haversine(s.rest_lat, s.rest_lon, s.del_lat, s.del_lon)
    #         st.markdown(f"""
    #         <div class="dist-pill" style="display:flex;align-items:center;justify-content:space-between;background:#F0FDF4;border:1px solid #BBF7D0;border-radius:10px;padding:12px 16px;margin-top:18px;">
    #           <span style="font-size:13px;font-weight:700;color:#16A34A;">📐 Straight-line distance</span>
    #           <span><span style="font-family:\'Bricolage Grotesque\',sans-serif;font-size:18px;font-weight:800;color:#15803D;">{dist:.2f}</span> <span style="font-size:12px;font-weight:700;color:#16A34A;">km</span></span>
    #         </div>
    #         """, unsafe_allow_html=True)

    #     # Progression Button
    #     st.markdown('<div style="height:14px"></div>', unsafe_allow_html=True)
    #     if st.button("Continue to Conditions →", use_container_width=True, key="step1_next"):
    #         s.step = 2
    #         st.rerun()

    # # ── STEP 1: LOCATION (State-Protected Search Engine) ─────────────────────
    # if s.step == 1:
    #     st.markdown("""
    #     <div class="section-title">📍 Where's your order going?</div>
    #     <div class="section-sub">Type your location in the search bars below to choose from smart dropdown suggestions, or tap directly on the map surface.</div>
    #     """, unsafe_allow_html=True)

    #     from streamlit_searchbox import st_searchbox
    #     from geopy.geocoders import Photon # Upgraded to Photon engine: High-volume, instant response open-API
        
    #     geolocator = Photon(user_agent="deliveriq_enterprise_analytics_2026")

    #     # Insulated type-ahead autocomplete lookup block
    #     def address_autocomplete_lookup(search_term: str):
    #         if not search_term or len(search_term) < 3:
    #             return []
    #         try:
    #             # Queries Photon (high-speed backend engine) for structural city/colony matches
    #             locations = geolocator.geocode(search_term, exactly_one=False, timeout=3, limit=5)
    #             if locations:
    #                 results_list = []
    #                 for loc in locations:
    #                     # Clean label details extraction filter
    #                     addr_str = str(loc.address)
    #                     coords_tuple = (float(loc.latitude), float(loc.longitude))
    #                     results_list.append((addr_str, coords_tuple))
    #                 return results_list
    #         except Exception:
    #             return []
    #         return []

    #     # MASTER CARD CONTAINER
    #     with st.container(border=True):
    #         st.markdown('''
    #         <div class="fcard-inline-header">
    #             <div class="fcard-icon" style="background:#FFF0E3;color:var(--brand);padding:6px 10px;border-radius:8px;">🗺️</div>
    #             <div>
    #                 <div style="font-size:14px;font-weight:700;color:var(--ink);line-height:1.2;">Interactive Route Planner</div>
    #                 <div style="font-size:11px;color:var(--ink4);margin-top:2px;">Suggestions populate instantly below your characters — click to drop pins</div>
    #             </div>
    #         </div>
    #         ''', unsafe_allow_html=True)
            
    #         # Autocomplete Text Input Row Layout
    #         search_col1, search_col2 = st.columns(2)
            
    #         with search_col1:
    #             restaurant_selection = st_searchbox(
    #                 address_autocomplete_lookup,
    #                 label="🍽️ Search Restaurant Address Hub",
    #                 key="rest_autocomplete_v3",
    #                 clear_on_submit=False,
    #                 edit_after_submit="option"
    #             )
    #             if restaurant_selection:
    #                 # Updates parameters safely in state without breaking active loops
    #                 s.rest_lat, s.rest_lon = restaurant_selection

    #         with search_col2:
    #             delivery_selection = st_searchbox(
    #                 address_autocomplete_lookup,
    #                 label="📦 Search Delivery Target Point",
    #                 key="del_autocomplete_v3",
    #                 clear_on_submit=False,
    #                 edit_after_submit="option"
    #             )
    #             if delivery_selection:
    #                 s.del_lat, s.del_lon = delivery_selection

    #         st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)

    #         # Manual pin mode buttons row configuration
    #         pin_r, pin_d = st.columns(2)
    #         with pin_r:
    #             if st.button(f"{'🔵 ' if s.pin_mode=='restaurant' else ''}📍 Pin Restaurant Mode", use_container_width=True, key="btn_pin_r"):
    #                 s.pin_mode = "restaurant"
    #         with pin_d:
    #             if st.button(f"{'🟠 ' if s.pin_mode=='delivery' else ''}📦 Pin Delivery Mode", use_container_width=True, key="btn_pin_d"):
    #                 s.pin_mode = "delivery"

    #         pin_hint = ("🔵 Active: Manual map canvas clicks position the **Restaurant Hub**" if s.pin_mode == "restaurant" else "🟠 Active: Manual map canvas clicks position the **Delivery Location**")
    #         st.info(pin_hint)

    #         # # Folium Map Canvas Core block configuration execution
    #         # try:
    #         #     import folium
    #         #     from streamlit_folium import st_folium

    #         #     clat = (s.rest_lat + s.del_lat) / 2
    #         #     clon = (s.rest_lon + s.del_lon) / 2

    #         #     # Connect state variables natively to allow seamless panning transitions
    #         #     m = folium.Map(location=[clat, clon], zoom_start=13)
    #         #     folium.TileLayer('OpenStreetMap').add_to(m)

    #         #     folium.Marker([s.rest_lat, s.rest_lon], tooltip="🍽️ Restaurant", icon=folium.Icon(color='blue', icon='cutlery', prefix='fa')).add_to(m)
    #         #     folium.Marker([s.del_lat, s.del_lon], tooltip="📦 Delivery Point", icon=folium.Icon(color='orange', icon='map-marker', prefix='fa')).add_to(m)
    #         #     folium.PolyLine([[s.rest_lat, s.rest_lon], [s.del_lat, s.del_lon]], color='#E8471E', weight=2.5, opacity=.7, dash_array='8 5').add_to(m)

    #         #     # Passing explicit coordinates tracks tracking transformations correctly
    #         #     map_result = st_folium(m, center=[clat, clon], width="100%", height=360, key="map_main")

    #         #     # Handle direct manual clicking on map canvas safely
    #         #     if map_result and map_result.get("last_clicked"):
    #         #         c = map_result["last_clicked"]
    #         #         if s.pin_mode == "restaurant":
    #         #             s.rest_lat, s.rest_lon = round(c["lat"], 6), round(c["lng"], 6)
    #         #             s.pin_mode = "delivery"
    #         #         else:
    #         #             s.del_lat, s.del_lon = round(c["lat"], 6), round(c["lng"], 6)
    #         #             s.pin_mode = "restaurant"
    #         #         st.rerun()

    #         # except ImportError:
    #         #     st.error("Missing map framework libraries files")

    #         # ─── INSULATED STATE-SAFE MAP GRID ENGINE ───
    #         try:
    #             import folium
    #             from streamlit_folium import st_folium

    #             # Coerce values safely to floats to guarantee canvas rendering layers succeed
    #             clat = (float(s.rest_lat) + float(s.del_lat)) / 2
    #             clon = (float(s.rest_lon) + float(s.del_lon)) / 2

    #             # Connect variables natively to center parameters to allow panning transformations
    #             m = folium.Map(location=[clat, clon], zoom_start=13)
    #             folium.TileLayer('OpenStreetMap').add_to(m)

    #             # Markers map directly to live operational session coordinates numbers 
    #             folium.Marker([float(s.rest_lat), float(s.rest_lon)], tooltip="🍽️ Restaurant", icon=folium.Icon(color='blue', icon='cutlery', prefix='fa')).add_to(m)
    #             folium.Marker([float(s.del_lat), float(s.del_lon)], tooltip="📦 Delivery Point", icon=folium.Icon(color='orange', icon='map-marker', prefix='fa')).add_to(m)
    #             folium.PolyLine([[float(s.rest_lat), float(s.rest_lon)], [float(s.del_lat), float(s.del_lon)]], color='#E8471E', weight=2.5, opacity=.7, dash_array='8 5').add_to(m)

    #             # CRITICAL CHANGE: We pass returned_objects=[] to tell folium to ONLY track raw user actions in-place
    #             map_result = st_folium(
    #                 m, 
    #                 center=[clat, clon],
    #                 width="100%", 
    #                 height=360, 
    #                 key="map_main"
    #             )

    #             # Initialize permanent backend layout tracking registers if not present
    #             if "processed_click_id" not in s: 
    #                 s.processed_click_id = ""

    #             # Insulated Event Capture: Resolves coordinates map shifts safely without creating rerun traps
    #             if map_result and map_result.get("last_clicked"):
    #                 click_data = map_result["last_clicked"]
    #                 # Generate a unique string signature matching this exact geographical click instance
    #                 click_sig = f"{click_data['lat']:.5f}_{click_data['lng']:.5f}"

    #                 # Only alter data elements if this click signature differs from the previously handled action
    #                 if click_sig != s.processed_click_id:
    #                     s.processed_click_id = click_sig
                        
    #                     click_lat = round(click_data["lat"], 6)
    #                     click_lon = round(click_data["lng"], 6)

    #                     if s.pin_mode == "restaurant":
    #                         s.rest_lat = click_lat
    #                         s.rest_lon = click_lon
    #                         s.pin_mode = "delivery"  # Switches mode focus smoothly
    #                     else:
    #                         s.del_lat = click_lat
    #                         s.del_lon = click_lon
    #                         s.pin_mode = "restaurant" # Resets mode focus smoothly
                        
    #                     # Replacing manual st.rerun with context mutations stops infinite thread loops instantly!

    #         except ImportError:
    #             st.error("Missing map framework libraries files")

    #         # Calculations readouts pill display footer
    #         dist = haversine(s.rest_lat, s.rest_lon, s.del_lat, s.del_lon)
    #         st.markdown(f"""
    #         <div class="dist-pill" style="display:flex;align-items:center;justify-content:space-between;background:#F0FDF4;border:1px solid #BBF7D0;border-radius:10px;padding:12px 16px;margin-top:16px;">
    #           <span style="font-size:13px;font-weight:700;color:#16A34A;">📐 Calculated Route Distance</span>
    #           <span><span style="font-family:\'Bricolage Grotesque\',sans-serif;font-size:18px;font-weight:800;color:#15803D;">{dist:.2f}</span> <span style="font-size:12px;font-weight:700;color:#16A34A;">km</span></span>
    #         </div>
    #         """, unsafe_allow_html=True)

    #     # Advanced coordinate tracking accordion (Preserved for backend data matrix compilation)
    #     st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)
    #     with st.expander("🛠️ Advanced Coordinate Details (ML Core Features)"):
    #         cr1, cr2 = st.columns(2)
    #         with cr1: s.rest_lat = st.number_input("Restaurant Latitude", value=float(s.rest_lat), format="%.6f", key="rlat")
    #         with cr2: s.rest_lon = st.number_input("Restaurant Longitude", value=float(s.rest_lon), format="%.6f", key="rlon")
    #         cd1, cd2 = st.columns(2)
    #         with cd1: s.del_lat = st.number_input("Delivery Latitude", value=float(s.del_lat), format="%.6f", key="dlat")
    #         with cd2: s.del_lon = st.number_input("Delivery Longitude", value=float(s.del_lon), format="%.6f", key="dlon")

    #     st.markdown('<div style="height:14px"></div>', unsafe_allow_html=True)
    #     if st.button("Continue to Conditions →", use_container_width=True, key="step1_next"):
    #         s.step = 2
    #         st.rerun()

    # # ── STEP 1: LOCATION (State-Protected Decoupled Search Engine) ───────────
    # if s.step == 1:
    #     st.markdown("""
    #     <div class="section-title">📍 Where's your order going?</div>
    #     <div class="section-sub">Type your location in the search bars below to choose from smart dropdown suggestions, or tap directly on the map surface.</div>
    #     """, unsafe_allow_html=True)

    #     from streamlit_searchbox import st_searchbox
    #     from geopy.geocoders import Photon
    #     import folium
    #     from streamlit_folium import st_folium
        
    #     geolocator = Photon(user_agent="deliveriq_enterprise_analytics_2026")

    #     def address_autocomplete_lookup(search_term: str):
    #         if not search_term or len(search_term) < 3:
    #             return []
    #         try:
    #             locations = geolocator.geocode(search_term, exactly_one=False, timeout=3, limit=5)
    #             if locations:
    #                 return [(str(loc.address), (float(loc.latitude), float(loc.longitude))) for loc in locations]
    #         except Exception:
    #             return []
    #         return []

    #     # MASTER CARD CONTAINER
    #     with st.container(border=True):
    #         st.markdown('''
    #         <div class="fcard-inline-header">
    #             <div class="fcard-icon" style="background:#FFF0E3;color:var(--brand);padding:6px 10px;border-radius:8px;">🗺️</div>
    #             <div>
    #                 <div style="font-size:14px;font-weight:700;color:var(--ink);line-height:1.2;">Interactive Route Planner</div>
    #                 <div style="font-size:11px;color:var(--ink4);margin-top:2px;">Suggestions populate instantly below your characters — click to drop pins</div>
    #             </div>
    #         </div>
    #         ''', unsafe_allow_html=True)
            
    #         search_col1, search_col2 = st.columns(2)
            
    #         with search_col1:
    #             restaurant_selection = st_searchbox(
    #                 address_autocomplete_lookup,
    #                 label="🍽️ Search Restaurant Address Hub",
    #                 key="rest_autocomplete_v4",
    #                 clear_on_submit=False,
    #                 edit_after_submit="option"
    #             )
    #             # FIX: Only overwrite state if the user explicitly SELECTS a dropdown card suggestion!
    #             if restaurant_selection is not None and restaurant_selection != (s.rest_lat, s.rest_lon):
    #                 s.rest_lat, s.rest_lon = restaurant_selection

    #         with search_col2:
    #             delivery_selection = st_searchbox(
    #                 address_autocomplete_lookup,
    #                 label="📦 Search Delivery Target Point",
    #                 key="del_autocomplete_v4",
    #                 clear_on_submit=False,
    #                 edit_after_submit="option"
    #             )
    #             # FIX: Only overwrite state if the user explicitly SELECTS a dropdown card suggestion!
    #             if delivery_selection is not None and delivery_selection != (s.del_lat, s.del_lon):
    #                 s.del_lat, s.del_lon = delivery_selection

    #         st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)

    #         pin_r, pin_d = st.columns(2)
    #         with pin_r:
    #             if st.button(f"{'🔵 ' if s.pin_mode=='restaurant' else ''}📍 Pin Restaurant Mode", use_container_width=True, key="btn_pin_r"):
    #                 s.pin_mode = "restaurant"
    #         with pin_d:
    #             if st.button(f"{'🟠 ' if s.pin_mode=='delivery' else ''}📦 Pin Delivery Mode", use_container_width=True, key="btn_pin_d"):
    #                 s.pin_mode = "delivery"

    #         pin_hint = ("🔵 Active: Manual map clicks position the **Restaurant Hub**" if s.pin_mode == "restaurant" else "🟠 Active: Manual map clicks position the **Delivery Location**")
    #         st.info(pin_hint)

    #         # Map Processing Layout Engine
    #         clat = (float(s.rest_lat) + float(s.del_lat)) / 2
    #         clon = (float(s.rest_lon) + float(s.del_lon)) / 2

    #         m = folium.Map(location=[clat, clon], zoom_start=13)
    #         folium.TileLayer('OpenStreetMap').add_to(m)

    #         folium.Marker([float(s.rest_lat), float(s.rest_lon)], tooltip="🍽️ Restaurant", icon=folium.Icon(color='blue', icon='cutlery', prefix='fa')).add_to(m)
    #         folium.Marker([float(s.del_lat), float(s.del_lon)], tooltip="📦 Delivery Point", icon=folium.Icon(color='orange', icon='map-marker', prefix='fa')).add_to(m)
    #         folium.PolyLine([[float(s.rest_lat), float(s.rest_lon)], [float(s.del_lat), float(s.del_lon)]], color='#E8471E', weight=2.5, opacity=.7, dash_array='8 5').add_to(m)

    #         # Render active map frame configuration canvas
    #         # map_result = st_folium(m, center=[clat, clon], width="100%", height=360, key="map_main")

    #         # FIX: Clean signature evaluation layer traps clicks without triggering searchbox clearance errors
    #         # if map_result and map_result.get("last_clicked"):
    #         #     click_lat = round(map_result["last_clicked"]["lat"], 6)
    #         #     click_lon = round(map_result["last_clicked"]["lng"], 6)
    #         #     click_sig = f"{click_lat}_{click_lon}"

    #         #     if "processed_click_id" not in s: 
    #         #         s.processed_click_id = ""

    #         #     if click_sig != s.processed_click_id:
    #         #         s.processed_click_id = click_sig
                    
    #         #         if s.pin_mode == "restaurant":
    #         #             s.rest_lat, s.rest_lon = click_lat, click_lon
    #         #             s.pin_mode = "delivery"
    #         #         else:
    #         #             s.del_lat, s.del_lon = click_lat, click_lon
    #         #             s.pin_mode = "restaurant"
    #         #         st.rerun()

    #         # ─── INSULATED MAP PROCESSING ENGINE (No Auto-Flipping State Bugs) ───
    #         map_result = st_folium(m, center=[clat, clon], width="100%", height=360, key="map_main")

    #         if map_result and map_result.get("last_clicked"):
    #             click_lat = round(map_result["last_clicked"]["lat"], 6)
    #             click_lon = round(map_result["last_clicked"]["lng"], 6)
    #             click_sig = f"{click_lat}_{click_lon}"

    #             if "processed_click_id" not in s: 
    #                 s.processed_click_id = ""

    #             # Execute coordinate adjustments ONLY on a brand new click event signature
    #             if click_sig != s.processed_click_id:
    #                 s.processed_click_id = click_sig
                    
    #                 # FIX: Updates the coordinates for the chosen mode but STAYS in that mode
    #                 if s.pin_mode == "restaurant":
    #                     s.rest_lat = click_lat
    #                     s.rest_lon = click_lon
    #                     st.toast("🎯 Restaurant pin positioned successfully!", icon="🔵")
    #                 else:
    #                     s.del_lat = click_lat
    #                     s.del_lon = click_lon
    #                     st.toast("🎯 Delivery target pin positioned successfully!", icon="🟠")
                    
    #                 # Forces exactly one layout synchronization refresh 
    #                 st.rerun()

    #         # Distance Summary Display Pill
    #         dist = haversine(s.rest_lat, s.rest_lon, s.del_lat, s.del_lon)
    #         st.markdown(f"""
    #         <div class="dist-pill" style="display:flex;align-items:center;justify-content:space-between;background:#F0FDF4;border:1px solid #BBF7D0;border-radius:10px;padding:12px 16px;margin-top:16px;">
    #           <span style="font-size:13px;font-weight:700;color:#16A34A;">📐 Calculated Route Distance</span>
    #           <span><span style="font-family:\'Bricolage Grotesque\',sans-serif;font-size:18px;font-weight:800;color:#15803D;">{dist:.2f}</span> <span style="font-size:12px;font-weight:700;color:#16A34A;">km</span></span>
    #         </div>
    #         """, unsafe_allow_html=True)

    #     # Tech specs expander
    #     st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)
    #     with st.expander("🛠️ Advanced Coordinate Details (ML Core Features)"):
    #         cr1, cr2 = st.columns(2)
    #         with cr1: s.rest_lat = st.number_input("Restaurant Latitude", value=float(s.rest_lat), format="%.6f", key="rlat")
    #         with cr2: s.rest_lon = st.number_input("Restaurant Longitude", value=float(s.rest_lon), format="%.6f", key="rlon")
    #         cd1, cd2 = st.columns(2)
    #         with cd1: s.del_lat = st.number_input("Delivery Latitude", value=float(s.del_lat), format="%.6f", key="dlat")
    #         with cd2: s.del_lon = st.number_input("Delivery Longitude", value=float(s.del_lon), format="%.6f", key="dlon")

    #     st.markdown('<div style="height:14px"></div>', unsafe_allow_html=True)
    #     if st.button("Continue to Conditions →", use_container_width=True, key="step1_next"):
    #         s.step = 2
    #         st.rerun()

# ══════════════════════════════════════════════
# LEFT COLUMN  —  DYNAMIC STEP ROUTING
# ══════════════════════════════════════════════
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

        # st.markdown("""
        # <div class="section-title">📍 Where's your order going?</div>
        # <div class="section-sub">Specify your pickup and drop-off hubs to calculate live routes and delivery ETAs.</div>
        # """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="section-title" style="display: flex; align-items: center; gap: 8px; line-height: 1; margin-top: 4px;">
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
                # elif current_rest == (28.495, 77.089) and current_del == (28.482, 77.095): 
                #     active_preset_selection = "🚀 Cyber City Sprint"
                # FIX: Updated matching values to line up with the 3-decimal place outputs of Cyber City
                elif current_rest == (28.495, 77.089) and current_del == (28.482, 77.094): 
                    active_preset_selection = "🚀 Cyber City Sprint"
                elif current_rest == (28.568, 77.219) and current_del == (28.546, 77.263):
                    active_preset_selection = "🛵 South Ext. Hub Run"

            # # 3-Column Layout: Left for controls, Middle to push to the side, Right for the small button
            # col_presets, col_spacer, col_btn = st.columns([5.5, 1.0, 1.5], gap="small", vertical_alignment="bottom")

            # with col_presets:
            #     st.markdown("""
            #     <div style="font-size: 11px; font-weight: 700; color: #64748B; letter-spacing: 1.5px; text-transform: uppercase; margin: 0 0 10px 0; line-height: 1;">
            #         ⚡ Quick Presets
            #     </div>
            #     """, unsafe_allow_html=True)
                
            #     chosen_preset = st.segmented_control(
            #         label="Scenario Shortcuts",
            #         options=list(PRESET_OPTIONS.keys()),
            #         default=active_preset_selection,
            #         label_visibility="collapsed",
            #         key="scenario_preset_switch"
            #     )

            # with col_btn:
            #     # Target native Streamlit button containers to shrink height and reduce large internal padding
            #     st.markdown("""
            #     <style>
            #         div[data-testid="stBaseButton-secondary"] {
            #             padding: 0px !important;
            #         }
            #         div[data-testid="stBaseButton-secondary"] button {
            #             height: 40px !important;
            #             min-height: 40px !important;
            #             padding: 0px 12px !important;
            #             font-size: 13px !important;
            #             margin-top: 0px !important;
            #         }
            #     </style>
            #     """, unsafe_allow_html=True)
                
            #     if st.button("🧹 Clear Pins", use_container_width=True, key="canvas_reset_btn"):
            #         s.map_rest_lat, s.map_rest_lon, s.rest_search_text = None, None, "Not Selected"
            #         s.map_del_lat, s.map_del_lon, s.del_search_text = None, None, "Not Selected"
            #         s.click_count = 0
            #         s.rest_key_version += 1 
            #         s.del_key_version += 1  
            #         st.rerun()

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

            # with col_btn:
            #     # Target the exact container structure to shrink the button size and remove extra padding
            #     st.markdown("""
            #     <style>
            #         div[data-testid="stColumn"]:nth-of-type(2) div[data-testid="stBaseButton-secondary"] {
            #             padding: 0px !important;
            #         }
            #         div[data-testid="stColumn"]:nth-of-type(2) div[data-testid="stBaseButton-secondary"] button {
            #             height: 40px !important;
            #             min-height: 40px !important;
            #             padding: 0px 12px !important;
            #             font-size: 13px !important;
            #             margin-top: 0px !important;
            #         }
            #     </style>
            #     """, unsafe_allow_html=True)
                
            #     if st.button("🧹 Clear Pins", use_container_width=True, key="canvas_reset_btn"):
            #         s.map_rest_lat, s.map_rest_lon, s.rest_search_text = None, None, "Not Selected"
            #         s.map_del_lat, s.map_del_lon, s.del_search_text = None, None, "Not Selected"
            #         s.click_count = 0
            #         s.rest_key_version += 1 
            #         s.del_key_version += 1  
            #         st.rerun()

            # with col_btn:
            #     # Cleaner code with styles offloaded directly to the global master stylesheet
            #     if st.button("🗑️", use_container_width=True, key="canvas_reset_btn"):
            #         s.map_rest_lat, s.map_rest_lon, s.rest_search_text = None, None, "Not Selected"
            #         s.map_del_lat, s.map_del_lon, s.del_search_text = None, None, "Not Selected"
            #         s.click_count = 0
            #         s.rest_key_version += 1 
            #         s.del_key_version += 1  
            #         st.rerun()



            # Updates both coordinates and text boxes, then stops the loop
            if chosen_preset and chosen_preset != active_preset_selection:
                data = PRESET_OPTIONS[chosen_preset]
                s.map_rest_lat, s.map_rest_lon, s.rest_search_text = data["rest"]
                s.map_del_lat, s.map_del_lon, s.del_search_text = data["del"]
                s.click_count = 2 
                s.rest_key_version += 1
                s.del_key_version += 1
                st.rerun()

            st.markdown("<div style='margin-bottom: 24px;'></div>", unsafe_allow_html=True)

        # with st.container(border=False):
        #     header_left, header_right = st.columns([2.2, 0.8], gap="small")
            
            # with header_left:
                # st.markdown("""
                # <div style="display: flex; align-items: center; gap: 8px; line-height: 1; margin-top: 4px;">
                #     <span style="font-size:15px; font-weight:700; color:#1A1A1A; white-space: nowrap;">🗺️ Interactive Route Planner</span>
                #     <div class="custom-tooltip">
                #         <span class="info-trigger">i</span>
                #         <div class="tooltip-text">Click directly on the map! Click #1 plots Restaurant (📍 Orange). Click #2 plots Destination (🏁 Purple).</div>
                #     </div>
                # </div>
                # """, unsafe_allow_html=True)
                
            # with header_right:
            #     # UX Reset: Allows swapping between manual overwrites and clean canvases 
            #     # if st.button("🧹 Clear & Reset Pins", use_container_width=True, key="canvas_reset_btn"):
            #     #     s.rest_lat, s.rest_lon, s.rest_search_text = None, None, "Not Selected"
            #     #     s.del_lat, s.del_lon, s.del_search_text = None, None, "Not Selected"
            #     #     s.click_count = 0
            #     #     st.rerun()

            #     if st.button("🧹 Clear & Reset Pins", use_container_width=True, key="canvas_reset_btn"):
            #         s.rest_lat, s.rest_lon, s.rest_search_text = None, None, "Not Selected"
            #         s.del_lat, s.del_lon, s.del_search_text = None, None, "Not Selected"
            #         s.click_count = 0
            #         s.rest_key_version += 1 # Forces widget re-render
            #         s.del_key_version += 1  # Forces widget re-render
            #         st.rerun()
            
            # with header_right:
            #     # Open an isolated CSS namespace container around the reset block
            #     st.markdown('<div class="mini-reset-wrapper">', unsafe_allow_html=True)
                
            #     if st.button("🧹 Clear Pins", use_container_width=True, key="canvas_reset_btn"):
            #         s.map_rest_lat, s.map_rest_lon, s.rest_search_text = None, None, "Not Selected"
            #         s.map_del_lat, s.map_del_lon, s.del_search_text = None, None, "Not Selected"
            #         s.click_count = 0
            #         s.rest_key_version += 1 
            #         s.del_key_version += 1  
            #         st.rerun()
                    
            #     st.markdown('</div>', unsafe_allow_html=True)


            # st.markdown("<hr style='margin: 12px 0 8px 0; border: 0; border-top: 1px solid #E2E8F0;'>", unsafe_allow_html=True)
            

            #             # ─── INSTANT SCENARIO PRESETS ENGINE ───────────────────────────
            # PRESET_OPTIONS = {
            #     "⚡ CP to Karol Bagh": {
            #         "rest": (28.6304, 77.2177, "Connaught Place, New Delhi"),
            #         "del": (28.6514, 77.1907, "Karol Bagh, New Delhi")
            #     },
            #     "🚀 Cyber City Sprint": {
            #         "rest": (28.4952, 77.0890, "DLF Cyber City, Gurgaon"),
            #         "del": (28.4815, 77.0945, "DLF Phase 3, Gurgaon")
            #     },
            #     "🛵 South Ext. Hub Run": {
            #         "rest": (28.5683, 77.2194, "South Extension, New Delhi"),
            #         "del": (28.5457, 77.2631, "Kalkaji, New Delhi")
            #     }
            # }

            # # Evaluate preset matches securely against master standalone variables
            # active_preset_selection = None
            # if s.map_rest_lat is not None and s.map_del_lat is not None:
            #     current_rest = (round(float(s.map_rest_lat), 3), round(float(s.map_rest_lon), 3))
            #     current_del = (round(float(s.map_del_lat), 3), round(float(s.map_del_lon), 3))

            #     # if current_rest == (28.630, 77.218) and current_del == (28.651, 77.191):
            #     #     active_preset_selection = "⚡ CP to Karol Bagh"
            #     # elif current_rest == (28.495, 77.089) and current_del == (28.482, 77.095):
            #     #     active_preset_selection = "🚀 Cyber City Sprint"
            #     # elif current_rest == (28.568, 77.219) and current_del == (28.546, 77.263):
            #     #     active_preset_selection = "🛵 South Ext. Hub Run"

            #                     # FIX: Updated matching conditions to look for the rounded coordinates (3 decimal places)
            #     if current_rest == (28.630, 77.218) and current_del == (28.651, 77.191):
            #         active_preset_selection = "⚡ CP to Karol Bagh"
            #     elif current_rest == (28.495, 77.089) and current_del == (28.482, 77.095): # Matches Cyber City's rounded states perfectly
            #         active_preset_selection = "🚀 Cyber City Sprint"
            #     elif current_rest == (28.568, 77.219) and current_del == (28.546, 77.263):
            #         active_preset_selection = "🛵 South Ext. Hub Run"


            # st.markdown("""
            # <div style="font-size: 11px; font-weight: 700; color: #64748B; letter-spacing: 1.5px; text-transform: uppercase; margin: 14px 0 10px 0; line-height: 1;">
            #     ⚡ Quick Presets
            # </div>
            # """, unsafe_allow_html=True)

            # chosen_preset = st.segmented_control(
            #     label="Scenario Shortcuts",
            #     options=list(PRESET_OPTIONS.keys()),
            #     default=active_preset_selection,
            #     label_visibility="collapsed",
            #     key="scenario_preset_switch"
            # )

            # # Updates both coordinates and text boxes, then stops the loop
            # if chosen_preset and chosen_preset != active_preset_selection:
            #     data = PRESET_OPTIONS[chosen_preset]
            #     s.map_rest_lat, s.map_rest_lon, s.rest_search_text = data["rest"]
            #     s.map_del_lat, s.map_del_lon, s.del_search_text = data["del"]
            #     s.click_count = 2 
            #     s.rest_key_version += 1
            #     s.del_key_version += 1
            #     st.rerun()

            #             # ─── INSTANT SCENARIO PRESETS ──────────────────────────────────────
            # PRESET_OPTIONS = {
            #     "⚡ CP to Karol Bagh": {
            #         "rest": (28.6304, 77.2177, "Connaught Place, New Delhi"),
            #         "del": (28.6514, 77.1907, "Karol Bagh, New Delhi")
            #     },
            #     "🚀 Cyber City Sprint": {
            #         "rest": (28.4952, 77.0890, "DLF Cyber City, Gurgaon"),
            #         "del": (28.4815, 77.0945, "DLF Phase 3, Gurgaon")
            #     },
            #     "🛵 South Ext. Hub Run": {
            #         "rest": (28.5683, 77.2194, "South Extension, New Delhi"),
            #         "del": (28.5457, 77.2631, "Kalkaji, New Delhi")
            #     }
            # }

            # # FIX: Pre-evaluate active selection targeting our master geographic variables
            # active_preset_selection = None
            # if s.map_rest_lat is not None and s.map_del_lat is not None:
            #     current_rest = (round(float(s.map_rest_lat), 3), round(float(s.map_rest_lon), 3))
            #     current_del = (round(float(s.map_del_lat), 3), round(float(s.map_del_lon), 3))

            #     if current_rest == (28.630, 77.218) and current_del == (28.651, 77.191):
            #         active_preset_selection = "⚡ CP to Karol Bagh"
            #     elif current_rest == (28.495, 77.089) and current_del == (28.482, 77.095):
            #         active_preset_selection = "🚀 Cyber City Sprint"
            #     elif current_rest == (28.568, 77.219) and current_del == (28.546, 77.263):
            #         active_preset_selection = "🛵 South Ext. Hub Run"

            # st.markdown("""
            # <div style="font-size: 11px; font-weight: 700; color: #64748B; letter-spacing: 1.5px; text-transform: uppercase; margin: 14px 0 10px 0; line-height: 1;">
            #     ⚡ Quick Presets
            # </div>
            # """, unsafe_allow_html=True)

            # chosen_preset = st.segmented_control(
            #     label="Scenario Shortcuts",
            #     options=list(PRESET_OPTIONS.keys()),
            #     default=active_preset_selection,
            #     label_visibility="collapsed",
            #     key="scenario_preset_switch"
            # )

            # # FIX: Only trigger state overwrite and rerun if user clicks a *different* preset
            # if chosen_preset and chosen_preset != active_preset_selection:
            #     data = PRESET_OPTIONS[chosen_preset]
            #     s.map_rest_lat, s.map_rest_lon, s.rest_search_text = data["rest"]
            #     s.map_del_lat, s.map_del_lon, s.del_search_text = data["del"]
            #     s.click_count = 2 
            #     s.rest_key_version += 1
            #     s.del_key_version += 1
            #     st.rerun()

            # st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)

            # # ─── INSTANT SCENARIO PRESETS ───
            # PRESET_OPTIONS = {
            #     "⚡ CP to Karol Bagh": {
            #         "rest": (28.6304, 77.2177, "Connaught Place, New Delhi"),
            #         "del": (28.6514, 77.1907, "Karol Bagh, New Delhi")
            #     },
            #     "🚀 Cyber City Sprint": {
            #         "rest": (28.4952, 77.0890, "DLF Cyber City, Gurgaon"),
            #         "del": (28.4815, 77.0945, "DLF Phase 3, Gurgaon")
            #     },
            #     "🛵 South Ext. Hub Run": {
            #         "rest": (28.5683, 77.2194, "South Extension, New Delhi"),
            #         "del": (28.5457, 77.2631, "Kalkaji, New Delhi")
            #     }
            # }

            # active_preset_selection = None
            # if s.rest_lat and s.del_lat:
            #     current_rest = (round(float(s.rest_lat), 3), round(float(s.rest_lon), 3))
            #     current_del = (round(float(s.del_lat), 3), round(float(s.del_lon), 3))

            #     if current_rest == (28.630, 77.218) and current_del == (28.651, 77.191):
            #         active_preset_selection = "⚡ CP to Karol Bagh"
            #     elif current_rest == (28.495, 77.089) and current_del == (28.482, 77.095):
            #         active_preset_selection = "🚀 Cyber City Sprint"
            #     elif current_rest == (28.568, 77.219) and current_del == (28.546, 77.263):
            #         active_preset_selection = "🛵 South Ext. Hub Run"

            # st.markdown("""
            # <div style="font-size: 11px; font-weight: 700; color: #64748B; letter-spacing: 1.5px; text-transform: uppercase; margin: 14px 0 10px 0; line-height: 1;">
            #     ⚡ Quick Presets
            # </div>
            # """, unsafe_allow_html=True)

            # chosen_preset = st.segmented_control(
            #     label="Scenario Shortcuts",
            #     options=list(PRESET_OPTIONS.keys()),
            #     default=active_preset_selection,
            #     label_visibility="collapsed",
            #     key="scenario_preset_switch"
            # )

            # # if chosen_preset and chosen_preset != active_preset_selection:
            # #     data = PRESET_OPTIONS[chosen_preset]
            # #     s.rest_lat, s.rest_lon, s.rest_search_text = data["rest"]
            # #     s.del_lat, s.del_lon, s.del_search_text = data["del"]
            # #     s.click_count = 2 
            # #     st.rerun()

            # if chosen_preset and chosen_preset != active_preset_selection:
            #     data = PRESET_OPTIONS[chosen_preset]
            #     s.map_rest_lat, s.map_rest_lon, s.rest_search_text = data["rest"]
            #     s.map_del_lat, s.map_del_lon, s.del_search_text = data["del"]
            #     s.click_count = 2 
            #     s.rest_key_version += 1
            #     s.del_key_version += 1
            #     st.rerun()


            # st.markdown("<div style='margin-bottom: 4px;'></div>", unsafe_allow_html=True)
            
            # ─── LIVE LOCATION STATE CARDS (PRE-MAP VIEWPORT OVERVIEW) ───
            # Dynamically shows the current coordinates/resolved strings above the canvas
            loc_col1, loc_col2 = st.columns(2)
            with loc_col1:
                st.markdown(f"""
                <div style="background: #FFF7ED; border: 1px solid #FFEDD5; padding: 10px 14px; border-radius: 8px;">
                    <div style="font-size: 10px; font-weight: 700; color: #C2410C; text-transform: lowercase; letter-spacing: 0.5px;">📍 _pickup_hub</div>
                    <div style="font-size: 13px; font-weight: 600; color: #1E293B; margin-top: 2px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" title="{s.rest_search_text}">{s.rest_search_text}</div>
                </div>
                """, unsafe_allow_html=True)
                
            with loc_col2:
                st.markdown(f"""
                <div style="background: #FAF5FF; border: 1px solid #F3E8FF; padding: 10px 14px; border-radius: 8px;">
                    <div style="font-size: 10px; font-weight: 700; color: #6B21A8; text-transform: lowercase; letter-spacing: 0.5px;">🏁 _dropoff_hub</div>
                    <div style="font-size: 13px; font-weight: 600; color: #1E293B; margin-top: 2px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" title="{s.del_search_text}">{s.del_search_text}</div>
                </div>
                """, unsafe_allow_html=True)
                
            st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

# with main_col:
#     # ── STEP 1: LOCATION (Bi-Directional Key-Insulated Engine) ───────────────
#     if s.step == 1:
#         st.markdown("""
#         <div class="section-title">📍 Where's your order going?</div>
#         <div class="section-sub">Specify your pickup and drop-off hubs to calculate live routes and delivery ETAs.</div>
#         """, unsafe_allow_html=True)

#         # st.markdown("""
#         # <div class="section-title">📍 Where's your order going?</div>
#         # """, unsafe_allow_html=True)

#         st.markdown("<br>", unsafe_allow_html=True)

#         # st.markdown("""
#         # <div class="section-title">📍 Where's your order going?</div>
#         # <div class="section-sub">Type your location in the search bars below to choose from smart dropdown suggestions, or tap directly on the map surface.</div>
#         # """, unsafe_allow_html=True)

#         # # FIXED: Added wrapper div with an explicit margin-top to break away from the navigation tab ceiling
#         # st.markdown("""
#         # <div class="step-header-wrapper" style="margin-top: 24px; margin-bottom: 24px;">
#         #     <div class="section-title">📍 Where's your order going?</div>
#         #     <div class="section-sub">Type your location in the search bars below to choose from smart dropdown suggestions, or tap directly on the map surface.</div>
#         # </div>
#         # """, unsafe_allow_html=True)

#         from streamlit_searchbox import st_searchbox
#         from geopy.geocoders import Photon
#         import folium
#         from streamlit_folium import st_folium
        
#         geolocator = Photon(user_agent="deliveriq_enterprise_analytics_2026")

#         # if "rest_search_text" not in s: s.rest_search_text = "Connaught Place, New Delhi"
#         # if "del_search_text" not in s: s.del_search_text = "Punjabi Bagh, New Delhi"

#         # ─── UPDATE THIS INSIDE YOUR IF s.step == 1: BLOCK ───
#         if "rest_search_text" not in s: 
#             s.rest_search_text = "Connaught Place, New Delhi"
#         if "del_search_text" not in s: 
#             s.del_search_text = "Karol Bagh, New Delhi"


#         def address_autocomplete_lookup(search_term: str):
#             if not search_term or len(search_term) < 3:
#                 return []
#             try:
#                 locations = geolocator.geocode(search_term, exactly_one=False, timeout=3, limit=5)
#                 if locations:
#                     return [(str(loc.address), (float(loc.latitude), float(loc.longitude))) for loc in locations]
#             except Exception:
#                 return []
#             return []

        # # MASTER CARD CONTAINER
        # with st.container(border=True):
        #     st.markdown('''
        #     <div class="fcard-inline-header">
        #         <div class="fcard-icon" style="background:#FFF0E3;color:var(--brand);padding:6px 10px;border-radius:8px;">🗺️</div>
        #         <div>
        #             <div style="font-size:14px;font-weight:700;color:var(--ink);line-height:1.2;">Interactive Route Planner</div>
        #             <div style="font-size:11px;color:var(--ink4);margin-top:2px;">Type an address or click the map canvas directly—both input models stay perfectly synced</div>
        #         </div>
        #     </div>
        #     ''', unsafe_allow_html=True)
            
        #     search_col1, search_col2 = st.columns(2)
            
        #     with search_col1:
        #         # FIX: Binding the key to a dynamic string clears out old text values on map click
        #         restaurant_selection = st_searchbox(
        #             address_autocomplete_lookup,
        #             label="🍽️ Search Restaurant Address Hub",
        #             default=s.rest_search_text,
        #             key=f"rest_box_instance_{s.rest_box_id}",
        #             clear_on_submit=False,
        #             edit_after_submit="option"
        #         )
        #         if restaurant_selection is not None and isinstance(restaurant_selection, tuple):
        #             if restaurant_selection != (s.rest_lat, s.rest_lon):
        #                 s.rest_lat, s.rest_lon = restaurant_selection
        #                 s.rest_search_text = "📍 Custom Searched Hub Location"

        #     with search_col2:
        #         # FIX: Binding the key to a dynamic string clears out old text values on map click
        #         delivery_selection = st_searchbox(
        #             address_autocomplete_lookup,
        #             label="📦 Search Delivery Target Point",
        #             default=s.del_search_text,
        #             key=f"del_box_instance_{s.del_box_id}",
        #             clear_on_submit=False,
        #             edit_after_submit="option"
        #         )
        #         if delivery_selection is not None and isinstance(delivery_selection, tuple):
        #             if delivery_selection != (s.del_lat, s.del_lon):
        #                 s.del_lat, s.del_lon = delivery_selection
        #                 s.del_search_text = "📍 Custom Searched Destination"

        #     st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)

        #     pin_r, pin_d = st.columns(2)
        #     with pin_r:
        #         if st.button(f"{'🔵 ' if s.pin_mode=='restaurant' else ''}📍 Pin Restaurant Mode", use_container_width=True, key="btn_pin_r"):
        #             s.pin_mode = "restaurant"
        #     with pin_d:
        #         if st.button(f"{'🟠 ' if s.pin_mode=='delivery' else ''}📦 Pin Delivery Mode", use_container_width=True, key="btn_pin_d"):
        #             s.pin_mode = "delivery"

        #     pin_hint = ("🔵 Active: Manual map clicks position the **Restaurant Hub**" if s.pin_mode == "restaurant" else "🟠 Active: Manual map clicks position the **Delivery Location**")
        #     st.info(pin_hint)

        #     # Map Processing Layout Engine
        #     clat = (float(s.rest_lat) + float(s.del_lat)) / 2
        #     clon = (float(s.rest_lon) + float(s.del_lon)) / 2

        #     m = folium.Map(location=[clat, clon], zoom_start=13)
        #     folium.TileLayer('OpenStreetMap').add_to(m)

        #     folium.Marker([float(s.rest_lat), float(s.rest_lon)], tooltip="🍽️ Restaurant", icon=folium.Icon(color='blue', icon='cutlery', prefix='fa')).add_to(m)
        #     folium.Marker([float(s.del_lat), float(s.del_lon)], tooltip="📦 Delivery Point", icon=folium.Icon(color='orange', icon='map-marker', prefix='fa')).add_to(m)
        #     folium.PolyLine([[float(s.rest_lat), float(s.rest_lon)], [float(s.del_lat), float(s.del_lon)]], color='#E8471E', weight=2.5, opacity=.7, dash_array='8 5').add_to(m)

        #     map_result = st_folium(m, center=[clat, clon], width="100%", height=360, key="map_main")

        #     if map_result and map_result.get("last_clicked"):
        #         click_lat = round(map_result["last_clicked"]["lat"], 6)
        #         click_lon = round(map_result["last_clicked"]["lng"], 6)
        #         click_sig = f"{click_lat}_{click_lon}"

        #         if "processed_click_id" not in s: 
        #             s.processed_click_id = ""

        #         if click_sig != s.processed_click_id:
        #             s.processed_click_id = click_sig
                    
        #             if s.pin_mode == "restaurant":
        #                 s.rest_lat, s.rest_lon = click_lat, click_lon
        #                 s.rest_search_text = f"🎯 Map: {click_lat:.4f}, {click_lon:.4f}"
        #                 # FIX ACTION: Incrementing the ID forces the searchbox component to clear its cache!
        #                 s.rest_box_id += 1 
        #                 st.toast("Hub coordinate updated via map click!", icon="🔵")
        #             else:
        #                 s.del_lat, s.del_lon = click_lat, click_lon
        #                 s.del_search_text = f"🎯 Map: {click_lat:.4f}, {click_lon:.4f}"
        #                 # FIX ACTION: Incrementing the ID forces the searchbox component to clear its cache!
        #                 s.del_box_id += 1
        #                 st.toast("Destination coordinate updated via map click!", icon="🟠")
                    
        #             st.rerun()

        #     dist = haversine(s.rest_lat, s.rest_lon, s.del_lat, s.del_lon)
        #     st.markdown(f"""
        #     <div class="dist-pill" style="display:flex;align-items:center;justify-content:space-between;background:#F0FDF4;border:1px solid #BBF7D0;border-radius:10px;padding:12px 16px;margin-top:16px;">
        #       <span style="font-size:13px;font-weight:700;color:#16A34A;">📐 Calculated Route Distance</span>
        #       <span><span style="font-family:\'Bricolage Grotesque\',sans-serif;font-size:18px;font-weight:800;color:#15803D;">{dist:.2f}</span> <span style="font-size:12px;font-weight:700;color:#16A34A;">km</span></span>
        #     </div>
        #     """, unsafe_allow_html=True)

        # # MASTER CARD CONTAINER (FIXED: Perfectly contained map bounds)
        # with st.container(border=True):
        #     st.markdown('''
        #     <div class="fcard-inline-header">
        #         <div class="fcard-icon" style="background:#FFF0E3; color:var(--brand); padding:6px 10px; border-radius:8px; float:left; margin-right:12px;">🗺️</div>
        #         <div>
        #             <div style="font-size:14px; font-weight:700; color:var(--ink); line-height:1.2;">Interactive Route Planner</div>
        #             <div style="font-size:11px; color:var(--ink4); margin-top:2px;">Type an address or click the map canvas directly—both input models stay perfectly synced</div>
        #         </div>
        #         <div style="clear:both;"></div>
        #     </div>
        #     ''', unsafe_allow_html=True)

        # # MASTER CARD CONTAINER (FIXED: Cleaned string logic with zero broken comment strings)
        # with st.container(border=True):
        #     st.markdown("""
        #     <div class="fcard-inline-header" style="display: flex; align-items: center; justify-content: space-between; width: 100%;">
        #         <div style="display: flex; align-items: center; gap: 12px;">
        #             <div class="fcard-icon" style="background:#FFF0E3; padding:6px 10px; border-radius:8px; display: flex; align-items: center; justify-content: center;">🗺️</div>
        #             <div>
        #                 <div style="display: flex; align-items: center; gap: 6px;">
        #                     <span style="font-size:14px; font-weight:700; color:#1C1917; line-height:1.2;">Interactive Route Planner</span>
        #                     <div class="custom-tooltip">
        #                         <span class="info-trigger">i</span>
        #                         <div class="tooltip-text">Type an address or click the map canvas directly—both input models stay perfectly synced.</div>
        #                     </div>
        #                 </div>
        #             </div>
        #         </div>
        #     </div>
        #     """, unsafe_allow_html=True)

        # # MASTER CARD CONTAINER (FIXED: Flex alignment baseline update)
        # with st.container(border=True):
        #     st.markdown("""
        #     <div class="fcard-inline-header" style="display: flex; align-items: center; justify-content: space-between; width: 100%;">
        #         <div style="display: flex; align-items: center; gap: 12px;">
        #             <div class="fcard-icon" style="background:#FFF0E3; padding:6px 10px; border-radius:8px; display: flex; align-items: center; justify-content: center;">🗺️</div>
        #             <div>
        #                 <!-- FIXED: Changed parent wrapper to display flex with inline center item alignment -->
        #                 <div style="display: flex; align-items: center; gap: 8px; line-height: 1;">
        #                     <span style="font-size:14px; font-weight:700; color:#1C1917;">Interactive Route Planner</span>
        #                     <div class="custom-tooltip">
        #                         <span class="info-trigger">i</span>
        #                         <div class="tooltip-text">Type an address or click the map canvas directly—both input models stay perfectly synced.</div>
        #                     </div>
        #                 </div>
        #             </div>
        #         </div>
        #     </div>
        #     """, unsafe_allow_html=True)

        # # MASTER CARD CONTAINER (FIXED: Flex alignment baseline update)
        # with st.container(border=True):
        #     st.markdown("""
        #     <div class="fcard-inline-header" style="display: flex; align-items: center; justify-content: space-between; width: 100%;">
        #         <div style="display: flex; align-items: center; gap: 12px;">
        #             <div class="fcard-icon" style="background:#FFF0E3; padding:6px 10px; border-radius:8px; display: flex; align-items: center; justify-content: center;">🗺️</div>
        #             <div>
        #                 <!-- FIXED: Changed parent wrapper to display flex with inline center item alignment -->
        #                 <div style="display: flex; align-items: center; gap: 8px; line-height: 1;">
        #                     <span style="font-size:14px; font-weight:700; color:#1C1917;">Interactive Route Planner</span>
        #                     <div class="custom-tooltip">
        #                         <span class="info-trigger">i</span>
        #                         <div class="tooltip-text">Type an address or click the map canvas directly—both input models stay perfectly synced.</div>
        #                     </div>
        #                 </div>
        #             </div>
        #         </div>
        #     </div>
        #     """, unsafe_allow_html=True)

        # # MASTER CARD CONTAINER
        # with st.container(border=True):
        #     # Header Row with Native Segmented Control
        #     header_left, header_right = st.columns([3, 2])
        #     with header_left:
        #         st.markdown("""
        #         <div style="display: flex; align-items: center; gap: 8px; line-height: 1; padding-top: 4px;">
        #             <span style="font-size:15px; font-weight:700; color:#1C1917;">🗺️ Interactive Route Planner</span>
        #             <div class="custom-tooltip">
        #                 <span class="info-trigger">i</span>
        #                 <div class="tooltip-text">Type an address or click the map canvas directly—both input models stay perfectly synced.</div>
        #             </div>
        #         </div>
        #         """, unsafe_allow_html=True)
            
        #     with header_right:
        #         # MODERN TOGGLE SWITCH (Replaces the large manual buttons)
        #         chosen_mode = st.segmented_control(
        #             label="Input Method Selector",
        #             options=["🔍 Search Hubs", "📍 Tap on Map"],
        #             default="🔍 Search Hubs",
        #             label_visibility="collapsed",
        #             key="mode_toggle_switch"
        #         )

        #     st.markdown("<hr style='margin: 12px 0; border: 0; border-top: 1px solid #E7E5E4;'>", unsafe_allow_html=True)

        #     # ─── STATE MANAGEMENT SYNC ───
        #     is_rest_map_click = getattr(s, "rest_map_active", False)
        #     is_del_map_click = getattr(s, "del_map_active", False)

        # # MASTER CARD CONTAINER
        # with st.container(border=True):
        #     # Header Row with Native Segmented Control
        #     header_left, header_right = st.columns([3, 2])
        #     with header_left:
        #         st.markdown("""
        #         <div style="display: flex; align-items: center; gap: 8px; line-height: 1; padding-top: 4px;">
        #             <span style="font-size:15px; font-weight:700; color:#1C1917;">🗺️ Interactive Route Planner</span>
        #             <div class="custom-tooltip">
        #                 <span class="info-trigger">i</span>
        #                 <div class="tooltip-text">Type an address or click the map canvas directly—both input models stay perfectly synced.</div>
        #             </div>
        #         </div>
        #         """, unsafe_allow_html=True)
            
        #     with header_right:
        #         # MODERN TOGGLE SWITCH (Replaces the large manual buttons)
        #         chosen_mode = st.segmented_control(
        #             label="Input Method Selector",
        #             options=["🔍 Search Hubs", "📍 Tap on Map"],
        #             default="🔍 Search Hubs",
        #             label_visibility="collapsed",
        #             key="mode_toggle_switch"
        #         )

        #     st.markdown("<hr style='margin: 12px 0 8px 0; border: 0; border-top: 1px solid #E7E5E4;'>", unsafe_allow_html=True)

        # # MASTER CARD CONTAINER
        # with st.container(border=True):
        #     # FIX: Tighter column ratio ([1, 1] instead of) pulls the buttons much closer to the left text
        #     header_left, header_right = st.columns([1, 1], gap="small")
            
        #     with header_left:
        #         # FIX: Added specific 'margin-top: 6px;' inline to match the native height of st.segmented_control
        #         st.markdown("""
        #         <div style="display: flex; align-items: center; gap: 8px; line-height: 1; margin-top: 6px;">
        #             <span style="font-size:15px; font-weight:700; color:#1C1917; white-space: nowrap;">🗺️ Interactive Route Planner</span>
        #             <div class="custom-tooltip">
        #                 <span class="info-trigger">i</span>
        #                 <div class="tooltip-text">Type an address or click the map canvas directly—both input models stay perfectly synced.</div>
        #             </div>
        #         </div>
        #         """, unsafe_allow_html=True)

        # # MASTER CARD CONTAINER
        # with st.container(border=False):
        #     # Keep the expansive columns ratio to preserve the extreme-right alignment
        #     header_left, header_right = st.columns([1.5, 1.0], gap="small")
            
        #     with header_left:
        #         # FIX: Decreased margin-top from 12px to 4px to lift the title into a centered baseline alignment
        #         st.markdown("""
        #         <div style="display: flex; align-items: center; gap: 8px; line-height: 1; margin-top: -6px;">
        #             <span style="font-size:15px; font-weight:700; color:#1A1A1A; white-space: nowrap;">🗺️ Interactive Route Planner</span>
        #             <div class="custom-tooltip">
        #                 <span class="info-trigger">i</span>
        #                 <div class="tooltip-text">Type an address or click the map canvas directly—both input models stay perfectly synced.</div>
        #             </div>
        #         </div>
        #         """, unsafe_allow_html=True)
                
        #     with header_right:
        #         # ─── NATIVE SEGMENTED TOGGLE ENGINE WITH ISOLATED TRACKING ───
        #         chosen_mode = st.segmented_control(
        #             label="Input Method Selector",
        #             options=["🔍 Search Hubs", "📍 Tap on Map"],
        #             default="🔍 Search Hubs",
        #             label_visibility="collapsed",
        #             key="mode_toggle_switch"
        #         )

        #     st.markdown("<hr style='margin: 12px 0 8px 0; border: 0; border-top: 1px solid #E2E8F0;'>", unsafe_allow_html=True)

            
            # with header_right:
            #     # MODERN TOGGLE SWITCH
            #     chosen_mode = st.segmented_control(
            #         label="Input Method Selector",
            #         options=["🔍 Search Hubs", "📍 Tap on Map"],
            #         default="🔍 Search Hubs",
            #         label_visibility="collapsed",
            #         key="mode_toggle_switch"
            #     )

            # with header_right:
            #     # ─── CUSTOM INPUT METHOD PILL TOGGLE ───
            #     if "mode_toggle_switch" not in st.session_state:
            #         st.session_state.mode_toggle_switch = "🔍 Search Hubs"
                
            #     # Render an elegant horizontal frame box using clean single-line inline styles
            #     st.html("""
            #     <style>
            #     .custom-pill-track {
            #         display: inline-flex !important;
            #         background-color: #F1F5F9 !important;
            #         border: 1px solid #E2E8F0 !important;
            #         border-radius: 30px !important;
            #         padding: 4px !important;
            #         gap: 4px !important;
            #         align-items: center !important;
            #     }
            #     .custom-pill-btn {
            #         border: none !important;
            #         border-radius: 24px !important;
            #         font-size: 13px !important;
            #         font-weight: 600 !important;
            #         padding: 6px 16px !important;
            #         cursor: pointer !important;
            #         transition: all 0.2s ease !important;
            #     }
            #     .pill-active {
            #         background-color: #FFFFFF !important;
            #         color: #0F172A !important;
            #         font-weight: 700 !important;
            #         box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.06) !important;
            #     }
            #     .pill-inactive {
            #         background-color: transparent !important;
            #         color: #64748B !important;
            #     }
            #     .pill-inactive:hover {
            #         color: #1E293B !important;
            #         background-color: rgba(0, 0, 0, 0.04) !important;
            #     }
            #     </style>
            #     """)

            #     # Render active selection layouts via lightweight micro-HTML macros
            #     is_search = st.session_state.mode_toggle_switch == "🔍 Search Hubs"
            #     search_class = "pill-active" if is_search else "pill-inactive"
            #     map_class = "pill-inactive" if is_search else "pill-active"

            #     # Use a lightweight flex container track row
            #     click_action = st.html(f"""
            #     <div class="custom-pill-track">
            #         <button class="custom-pill-btn {search_class}" onclick="window.parent.postMessage({{type: 'streamlit:setComponentValue', value: 'search'}}, '*')">🔍 Search Hubs</button>
            #         <button class="custom-pill-btn {map_class}" onclick="window.parent.postMessage({{type: 'streamlit:setComponentValue', value: 'map'}}, '*')">📍 Tap on Map</button>
            #     </div>
            #     """)
                
            #     # Map active layout value back to state bindings
            #     chosen_mode = st.session_state.mode_toggle_switch

            # with header_right:
            #     # ─── NATIVE CLICKABLE CUSTOM PILL TOGGLE ENGINE ───
            #     if "mode_toggle_switch" not in st.session_state:
            #         st.session_state.mode_toggle_switch = "🔍 Search Hubs"

            #     # Check for inbound click parameters fired from our custom HTML elements
            #     query_params = st.query_params
            #     if "set_input_mode" in query_params:
            #         target_mode = query_params["set_input_mode"]
            #         # Map the quick-slug values back to your exact operational string states
            #         new_state = "🔍 Search Hubs" if target_mode == "search" else "📍 Tap on Map"
                    
            #         if st.session_state.mode_toggle_switch != new_state:
            #             st.session_state.mode_toggle_switch = new_state
            #             # Clear out the parameter string instantly to keep the browser URL pristine
            #             del st.query_params["set_input_mode"]
            #             st.rerun()

            #     # Render your precise light-theme layout style metrics
            #     st.html("""
            #     <style>
            #     .custom-pill-track {
            #         display: inline-flex !important;
            #         background-color: #F1F5F9 !important;
            #         border: 1px solid #E2E8F0 !important;
            #         border-radius: 30px !important;
            #         padding: 4px !important;
            #         gap: 4px !important;
            #         align-items: center !important;
            #         float: right !important; /* Locks it clean against your right layout margin */
            #     }
            #     .custom-pill-btn {
            #         border: none !important;
            #         border-radius: 24px !important;
            #         font-size: 13px !important;
            #         font-weight: 600 !important;
            #         padding: 6px 16px !important;
            #         text-decoration: none !important; /* Ensures the click element behaves like a button */
            #         display: inline-flex !important;
            #         align-items: center !important;
            #         justify-content: center !important;
            #         cursor: pointer !important;
            #         transition: all 0.2s ease !important;
            #     }
            #     .pill-active {
            #         background-color: #FFFFFF !important;
            #         color: #0F172A !important;
            #         font-weight: 700 !important;
            #         box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.06) !important;
            #     }
            #     .pill-inactive {
            #         background-color: transparent !important;
            #         color: #64748B !important;
            #     }
            #     .pill-inactive:hover {
            #         color: #1E293B !important;
            #         background-color: rgba(0, 0, 0, 0.04) !important;
            #     }
            #     </style>
            #     """)

            #     # Evaluate active state layout selections
            #     is_search = st.session_state.mode_toggle_switch == "🔍 Search Hubs"
            #     search_class = "pill-active" if is_search else "pill-inactive"
            #     map_class = "pill-inactive" if is_search else "pill-active"

            #     # Force target="_self" right into anchor links to securely communicate with the Python thread
            #     st.html(f"""
            #     <div class="custom-pill-track">
            #         <a class="custom-pill-btn {search_class}" href="?set_input_mode=search" target="_self">🔍 Search Hubs</a>
            #         <a class="custom-pill-btn {map_class}" href="?set_input_mode=map" target="_self">📍 Tap on Map</a>
            #     </div>
            #     """)
                
            #     # Map active tracker layout value back downstream into your core framework components
            #     chosen_mode = st.session_state.mode_toggle_switch

            # with header_right:
            #     # ─── NATIVE SEGMENTED TOGGLE ENGINE WITH ISOLATED TRACKING ───
            #     # Wrap inside a unique container key to provide a clean path for the stylesheet
            #     with st.container(key="input_mode_toggle_container"):
            #         chosen_mode = st.segmented_control(
            #             label="Input Method Selector",
            #             options=["🔍 Search Hubs", "📍 Tap on Map"],
            #             default="🔍 Search Hubs",
            #             label_visibility="collapsed",
            #             key="mode_toggle_switch"
            #         )


            # st.markdown("<hr style='margin: 12px 0 8px 0; border: 0; border-top: 1px solid #E7E5E4;'>", unsafe_allow_html=True)


            # # ─── INSTANT SCENARIO PRESETS ─────────────────────────────────────
            # preset_col1, preset_col2, preset_col3 = st.columns([1, 1, 1])
            
            # with preset_col1:
            #     if st.button("⚡ CP to Karol Bagh", key="preset_cp_kb", use_container_width=True, type="secondary"):
            #         s.rest_lat, s.rest_lon = 28.6304, 77.2177
            #         s.rest_search_text = "Connaught Place, New Delhi"
            #         s.del_lat, s.del_lon = 28.6514, 77.1907
            #         s.del_search_text = "Karol Bagh, New Delhi"
            #         # Reset mapping states and force input boxes refresh
            #         s.rest_map_active, s.del_map_active = False, False
            #         s.rest_box_id += 1
            #         s.del_box_id += 1
            #         st.rerun()

            # with preset_col2:
            #     if st.button("🚀 Cyber City Sprint", key="preset_cyber_city", use_container_width=True, type="secondary"):
            #         s.rest_lat, s.rest_lon = 28.4952, 77.0890
            #         s.rest_search_text = "DLF Cyber City, Gurgaon"
            #         s.del_lat, s.del_lon = 28.4815, 77.0945
            #         s.del_search_text = "DLF Phase 3, Gurgaon"
            #         s.rest_map_active, s.del_map_active = False, False
            #         s.rest_box_id += 1
            #         s.del_box_id += 1
            #         st.rerun()

            # with preset_col3:
            #     if st.button("🛵 South Ext. Hub Run", key="preset_south_ext", use_container_width=True, type="secondary"):
            #         s.rest_lat, s.rest_lon = 28.5683, 77.2194
            #         s.rest_search_text = "South Extension, New Delhi"
            #         s.del_lat, s.del_lon = 28.5457, 77.2631
            #         s.del_search_text = "Kalkaji, New Delhi"
            #         s.rest_map_active, s.del_map_active = False, False
            #         s.rest_box_id += 1
            #         s.del_box_id += 1
            #         st.rerun()

            # st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)

            # # ─── INSTANT SCENARIO PRESETS (VIA SLEEK LIGHT SEGMENTED CONTROL) ───
            # # Define options mapping with exact data states
            # PRESET_OPTIONS = {
            #     "⚡ CP to Karol Bagh": {
            #         "rest": (28.6304, 77.2177, "Connaught Place, New Delhi"),
            #         "del": (28.6514, 77.1907, "Karol Bagh, New Delhi")
            #     },
            #     "🚀 Cyber City Sprint": {
            #         "rest": (28.4952, 77.0890, "DLF Cyber City, Gurgaon"),
            #         "del": (28.4815, 77.0945, "DLF Phase 3, Gurgaon")
            #     },
            #     "🛵 South Ext. Hub Run": {
            #         "rest": (28.5683, 77.2194, "South Extension, New Delhi"),
            #         "del": (28.5457, 77.2631, "Kalkaji, New Delhi")
            #     }
            # }

            # # Pre-evaluate matching coordinates to keep the control synced with state
            # active_preset_selection = None
            # current_rest = (round(float(getattr(s, "rest_lat", 0)), 3), round(float(getattr(s, "rest_lon", 0)), 3))
            # current_del = (round(float(getattr(s, "del_lat", 0)), 3), round(float(getattr(s, "del_lon", 0)), 3))

            # if current_rest == (28.630, 77.218) and current_del == (28.651, 77.191):
            #     active_preset_selection = "⚡ CP to Karol Bagh"
            # elif current_rest == (28.495, 77.089) and current_del == (28.482, 77.095):
            #     active_preset_selection = "🚀 Cyber City Sprint"
            # elif current_rest == (28.568, 77.219) and current_del == (28.546, 77.263):
            #     active_preset_selection = "🛵 South Ext. Hub Run"

            # # Render the premium, light-accent pill selector layout
            # chosen_preset = st.segmented_control(
            #     label="Scenario Shortcuts",
            #     options=list(PRESET_OPTIONS.keys()),
            #     default=active_preset_selection,
            #     label_visibility="collapsed",
            #     key="scenario_preset_switch"
            # )

            # # Trigger instantaneous state updates if the user switches presets
            # if chosen_preset and chosen_preset != active_preset_selection:
            #     data = PRESET_OPTIONS[chosen_preset]
            #     s.rest_lat, s.rest_lon, s.rest_search_text = data["rest"]
            #     s.del_lat, s.del_lon, s.del_search_text = data["del"]
            #     s.rest_map_active, s.del_map_active = False, False
            #     s.rest_box_id += 1
            #     s.del_box_id += 1
            #     st.rerun()

            # st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)

            #             # ─── INSTANT SCENARIO PRESETS (VIA SLEEK LIGHT SEGMENTED CONTROL) ───
            # # Define options mapping with exact data states
            # PRESET_OPTIONS = {
            #     "⚡ CP to Karol Bagh": {
            #         "rest": (28.6304, 77.2177, "Connaught Place, New Delhi"),
            #         "del": (28.6514, 77.1907, "Karol Bagh, New Delhi")
            #     },
            #     "🚀 Cyber City Sprint": {
            #         "rest": (28.4952, 77.0890, "DLF Cyber City, Gurgaon"),
            #         "del": (28.4815, 77.0945, "DLF Phase 3, Gurgaon")
            #     },
            #     "🛵 South Ext. Hub Run": {
            #         "rest": (28.5683, 77.2194, "South Extension, New Delhi"),
            #         "del": (28.5457, 77.2631, "Kalkaji, New Delhi")
            #     }
            # }

            # # Pre-evaluate matching coordinates to keep the control synced with state
            # active_preset_selection = None
            # current_rest = (round(float(getattr(s, "rest_lat", 0)), 3), round(float(getattr(s, "rest_lon", 0)), 3))
            # current_del = (round(float(getattr(s, "del_lat", 0)), 3), round(float(getattr(s, "del_lon", 0)), 3))

            # if current_rest == (28.630, 77.218) and current_del == (28.651, 77.191):
            #     active_preset_selection = "⚡ CP to Karol Bagh"
            # elif current_rest == (28.495, 77.089) and current_del == (28.482, 77.095):
            #     active_preset_selection = "🚀 Cyber City Sprint"
            # elif current_rest == (28.568, 77.219) and current_del == (28.546, 77.263):
            #     active_preset_selection = "🛵 South Ext. Hub Run"

            # # FIX: Added clean minimalist uppercase section title to separate the rows
            # st.markdown("""
            # <div style="font-size: 11px; font-weight: 700; color: #64748B; letter-spacing: 1.5px; text-transform: uppercase; margin: 14px 0 10px 0; line-height: 1;">
            #     ⚡ Quick Presets
            # </div>
            # """, unsafe_allow_html=True)

            # # Render the premium, light-accent pill selector layout
            # chosen_preset = st.segmented_control(
            #     label="Scenario Shortcuts",
            #     options=list(PRESET_OPTIONS.keys()),
            #     default=active_preset_selection,
            #     label_visibility="collapsed",
            #     key="scenario_preset_switch"
            # )

            # # Trigger instantaneous state updates if the user switches presets
            # if chosen_preset and chosen_preset != active_preset_selection:
            #     data = PRESET_OPTIONS[chosen_preset]
            #     s.rest_lat, s.rest_lon, s.rest_search_text = data["rest"]
            #     s.del_lat, s.del_lon, s.del_search_text = data["del"]
            #     s.rest_map_active, s.del_map_active = False, False
            #     s.rest_box_id += 1
            #     s.del_box_id += 1
            #     st.rerun()

            # st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)


            # # ─── INSTANT SCENARIO PRESETS (WITH LIVE HIGHLIGHT STATE) ─────────
            # preset_col1, preset_col2, preset_col3 = st.columns(3)
            
            # # Pre-evaluate matching coordinates to detect active state
            # is_cp_active = (round(float(getattr(s, "rest_lat", 0)), 3) == 28.630 and 
            #                 round(float(getattr(s, "del_lat", 0)), 3) == 28.651)
                            
            # is_cyber_active = (round(float(getattr(s, "rest_lat", 0)), 3) == 28.495 and 
            #                    round(float(getattr(s, "del_lat", 0)), 3) == 28.482)
                               
            # is_south_active = (round(float(getattr(s, "rest_lat", 0)), 3) == 28.568 and 
            #                    round(float(getattr(s, "del_lat", 0)), 3) == 28.546)

            # with preset_col1:
            #     # Type changes dynamically to 'primary' if active coordinates match this preset
            #     cp_btn_type = "primary" if is_cp_active else "secondary"
            #     if st.button("⚡ CP to Karol Bagh", key="preset_cp_kb", use_container_width=True, type=cp_btn_type):
            #         s.rest_lat, s.rest_lon = 28.6304, 77.2177
            #         s.rest_search_text = "Connaught Place, New Delhi"
            #         s.del_lat, s.del_lon = 28.6514, 77.1907
            #         s.del_search_text = "Karol Bagh, New Delhi"
            #         s.rest_map_active, s.del_map_active = False, False
            #         s.rest_box_id += 1
            #         s.del_box_id += 1
            #         st.rerun()

            # with preset_col2:
            #     cyber_btn_type = "primary" if is_cyber_active else "secondary"
            #     if st.button("🚀 Cyber City Sprint", key="preset_cyber_city", use_container_width=True, type=cyber_btn_type):
            #         s.rest_lat, s.rest_lon = 28.4952, 77.0890
            #         s.rest_search_text = "DLF Cyber City, Gurgaon"
            #         s.del_lat, s.del_lon = 28.4815, 77.0945
            #         s.del_search_text = "DLF Phase 3, Gurgaon"
            #         s.rest_map_active, s.del_map_active = False, False
            #         s.rest_box_id += 1
            #         s.del_box_id += 1
            #         st.rerun()

            # with preset_col3:
            #     south_btn_type = "primary" if is_south_active else "secondary"
            #     if st.button("🛵 South Ext. Hub Run", key="preset_south_ext", use_container_width=True, type=south_btn_type):
            #         s.rest_lat, s.rest_lon = 28.5683, 77.2194
            #         s.rest_search_text = "South Extension, New Delhi"
            #         s.del_lat, s.del_lon = 28.5457, 77.2631
            #         s.del_search_text = "Kalkaji, New Delhi"
            #         s.rest_map_active, s.del_map_active = False, False
            #         s.rest_box_id += 1
            #         s.del_box_id += 1
            #         st.rerun()

            # st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)

                        # ─── STATE MANAGEMENT SYNC (ZERO-CLICK MULTI-TAP ENGINE) ───
            # # Dynamically determine pin mode by measuring populated coordinates 
            # if s.rest_lat is None:
            #     s.pin_mode = "restaurant"
            # elif s.del_lat is None:
            #     s.pin_mode = "delivery"
            # else:
            #     # If both are dropped, clicking the map again resets the cycle from the restaurant
            #     s.pin_mode = "restaurant"

            # # Safe native layout initialization
            # search_col1, search_col2 = st.columns(2)

            # # --- RESTAURANT INPUT (COLUMN 1) ---
            # with search_col1:
            #     # Render searchbox directly so it is always present as a backup alternative
            #     restaurant_selection = st_searchbox(
            #         address_autocomplete_lookup,
            #         label="🍽️ From: Restaurant Hub", 
            #         placeholder="Search or Click Map Directly...", 
            #         default=s.rest_search_text if s.rest_search_text else "",
            #         key=f"rest_box_instance_{getattr(s, 'rest_box_id', 1)}",
            #         clear_on_submit=False,
            #         edit_after_submit="option"
            #     )
                
            #     # Intercept text-search updates and instantly synchronize session states
            #     if restaurant_selection is not None and isinstance(restaurant_selection, tuple):
            #         if restaurant_selection != (s.rest_lat, s.rest_lon):
            #             s.rest_lat, s.rest_lon = restaurant_selection[1][0], restaurant_selection[1][1]
            #             s.rest_search_text = str(restaurant_selection[0])
            #             s.click_count = 1 if s.del_lat is None else 2
            #             st.rerun()

            # # --- DELIVERY INPUT (COLUMN 2) ---
            # with search_col2:
            #     # Render searchbox directly so it is always present as a backup alternative
            #     delivery_selection = st_searchbox(
            #         address_autocomplete_lookup,
            #         label="📦 To: Delivery Destination", 
            #         placeholder="Search or Click Map Directly...", 
            #         default=s.del_search_text if s.del_search_text else "",
            #         key=f"del_box_instance_{getattr(s, 'del_box_id', 1)}",
            #         clear_on_submit=False,
            #         edit_after_submit="option"
            #     )
                
            #     # Intercept text-search updates and instantly synchronize session states
            #     if delivery_selection is not None and isinstance(delivery_selection, tuple):
            #         if delivery_selection != (s.del_lat, s.del_lon):
            #             s.del_lat, s.del_lon = delivery_selection[1][0], delivery_selection[1][1]
            #             s.del_search_text = str(delivery_selection[0])
            #             s.click_count = 2
            #             st.rerun()

            # # ─── REALTIME DOM COLOR BRIDGE (PIN ACTION INDICATOR) ───
            # # Visually alerts the developer or user about which placement vector is currently active
            # import streamlit.components.v1 as components
            
            # is_r_active = (s.pin_mode == "restaurant")
            # is_d_active = (s.pin_mode == "delivery")
            
            # js_color_bridge = f"""
            # <script>
            # const doc = window.parent.document;
            # // Select the dynamic info containers we rendered in the prior step
            # const labels = doc.querySelectorAll('div[data-testid="stMarkdownContainer"] p');
            # labels.forEach(lbl => {{
            #     if (lbl.innerText.includes("Pickup Restaurant")) {{
            #         lbl.parentElement.style.borderLeft = "{'4px solid #F97316' if is_r_active else '1px solid #FFEDD5'}";
            #     }}
            #     if (lbl.innerText.includes("Delivery Destination")) {{
            #         lbl.parentElement.style.borderLeft = "{'4px solid #A855F7' if is_d_active else '1px solid #F3E8FF'}";
            #     }}
            # }});
            # </script>
            # """
            # components.html(js_color_bridge, height=0, width=0)

            # # ─── STATE MANAGEMENT SYNC ───
            # is_rest_map_click = getattr(s, "rest_map_active", False)
            # is_del_map_click = getattr(s, "del_map_active", False)


            # if chosen_mode == "📍 Tap on Map":
            #     # Automatically manage which pinning engine is active on the map canvas
            #     if not is_rest_map_click:
            #         s.pin_mode = "restaurant"
            #     elif not is_del_map_click:
            #         s.pin_mode = "delivery"
            #     else:
            #         s.pin_mode = "restaurant" # Default fallback
            # else:
            #     s.pin_mode = None

            # # ── REMOVED THE TOP OPENING DIV THAT WAS BREAKING LAYOUT ───────────────
            
            # # Safe native layout initialization
            # search_col1, search_col2 = st.columns(2)

            # # --- RESTAURANT INPUT (COLUMN 1) ---
            # with search_col1:
            #     # FIX: Removed the separate HTML markup block to avoid the double-box bug
                
            #     if chosen_mode == "📍 Tap on Map" and not is_rest_map_click:
            #         st.info("🍽️ Tap on the map below to set the **Restaurant Pin**", icon="📍")
                
            #     elif is_rest_map_click:
            #         # ... Keep your existing map click rendering logic here ...
            #         pass
            #     else:
            #         # FIX: The label parameter now hosts your title securely so it stacks perfectly
            #         restaurant_selection = st_searchbox(
            #             address_autocomplete_lookup,
            #             label="🍽️ From: Restaurant", 
            #             placeholder="Select Restaurant Hub...", 
            #             default=s.rest_search_text,
            #             key=f"rest_box_instance_{s.rest_box_id}",
            #             clear_on_submit=False,
            #             edit_after_submit="option"
            #         )
            #         if restaurant_selection is not None and isinstance(restaurant_selection, tuple):
            #             if restaurant_selection != (s.rest_lat, s.rest_lon):
            #                 s.rest_lat, s.rest_lon = restaurant_selection
            #                 s.rest_search_text = "📍 Custom Searched Hub Location"

            # # --- DELIVERY INPUT (COLUMN 2) ---
            # with search_col2:
            #     # FIX: Removed the separate HTML markup block to avoid the double-box bug
                
            #     if chosen_mode == "📍 Tap on Map" and is_rest_map_click and not is_del_map_click:
            #         st.info("📦 Tap on the map below to set the **Delivery Pin**", icon="📍")
                
            #     elif chosen_mode == "📍 Tap on Map" and not is_rest_map_click and not is_del_map_click:
            #         st.info("Waiting for Restaurant Pin...", icon="⏳")

            #     elif is_del_map_click:
            #         # ... Keep your existing map click rendering logic here ...
            #         pass
            #     else:
            #         # FIX: The label parameter now hosts your title securely so it stacks perfectly
            #         delivery_selection = st_searchbox(
            #             address_autocomplete_lookup,
            #             label="📦 To: Delivery Destination", 
            #             placeholder="Select Dropoff Zone...", 
            #             default=s.del_search_text,
            #             key=f"del_box_instance_{s.del_box_id}",
            #             clear_on_submit=False,
            #             edit_after_submit="option"
            #         )
            #         if delivery_selection is not None and isinstance(delivery_selection, tuple):
            #             if delivery_selection != (s.del_lat, s.del_lon):
            #                 s.del_lat, s.del_lon = delivery_selection
            #                 s.del_search_text = "📍 Custom Searched Destination"

            # # Safe native layout initialization
            # search_col1, search_col2 = st.columns(2)

            # # --- RESTAURANT INPUT (COLUMN 1) ---
            # with search_col1:
            #     # We wrap the content safely inside a closed, insulated HTML card block
            #     st.markdown("""
            #     <div style="
            #         background-color: #ffffff;
            #         border: 1px solid #e2e8f0;
            #         border-radius: 12px;
            #         padding: 16px;
            #         box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            #     ">
            #         <label style="font-size: 14px; font-weight: 600; color: #334155; display: inline-block; margin-bottom: 8px;">🍽️ From: Restaurant</label>
            #     </div>
            #     """, unsafe_allow_html=True)
                
            #     if chosen_mode == "📍 Tap on Map" and not is_rest_map_click:
            #         st.info("🍽️ Tap on the map below to set the **Restaurant Pin**", icon="📍")
                
            #     elif is_rest_map_click:
            #         # ... Keep your existing map click rendering logic here ...
            #         pass
            #     else:
            #         restaurant_selection = st_searchbox(
            #             address_autocomplete_lookup,
            #             label="", 
            #             placeholder="Select Restaurant Hub...", 
            #             default=s.rest_search_text,
            #             key=f"rest_box_instance_{s.rest_box_id}",
            #             clear_on_submit=False,
            #             edit_after_submit="option"
            #         )
            #         if restaurant_selection is not None and isinstance(restaurant_selection, tuple):
            #             if restaurant_selection != (s.rest_lat, s.rest_lon):
            #                 s.rest_lat, s.rest_lon = restaurant_selection
            #                 s.rest_search_text = "📍 Custom Searched Hub Location"

            # # --- DELIVERY INPUT (COLUMN 2) ---
            # with search_col2:
            #     # We wrap the content safely inside a closed, insulated HTML card block
            #     st.markdown("""
            #     <div style="
            #         background-color: #ffffff;
            #         border: 1px solid #e2e8f0;
            #         border-radius: 12px;
            #         padding: 16px;
            #         box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            #     ">
            #         <label style="font-size: 14px; font-weight: 600; color: #334155; display: inline-block; margin-bottom: 8px;">📦 To: Delivery Destination</label>
            #     </div>
            #     """, unsafe_allow_html=True)
                
            #     if chosen_mode == "📍 Tap on Map" and is_rest_map_click and not is_del_map_click:
            #         st.info("📦 Tap on the map below to set the **Delivery Pin**", icon="📍")
                
            #     elif chosen_mode == "📍 Tap on Map" and not is_rest_map_click and not is_del_map_click:
            #         st.info("Waiting for Restaurant Pin...", icon="⏳")

            #     elif is_del_map_click:
            #         # ... Keep your existing map click rendering logic here ...
            #         pass
            #     else:
            #         delivery_selection = st_searchbox(
            #             address_autocomplete_lookup,
            #             label="", 
            #             placeholder="Select Dropoff Zone...", 
            #             default=s.del_search_text,
            #             key=f"del_box_instance_{s.del_box_id}",
            #             clear_on_submit=False,
            #             edit_after_submit="option"
            #         )
            #         if delivery_selection is not None and isinstance(delivery_selection, tuple):
            #             if delivery_selection != (s.del_lat, s.del_lon):
            #                 s.del_lat, s.del_lon = delivery_selection
            #                 s.del_search_text = "📍 Custom Searched Destination"

            # # ─── UNIFIED GPS ROW ENGINE ───
            # search_col1, search_col2 = st.columns(2)
            
            # # --- RESTAURANT INPUT (COLUMN 1) ---
            # with search_col1:
            #     if chosen_mode == "📍 Tap on Map" and not is_rest_map_click:
            #         # Clean native warning banner instructing the click event
            #         st.info("🍽️ Tap on the map below to set the **Restaurant Pin**", icon="📍")
                
            #     elif is_rest_map_click:
            #         st.markdown(f"""
            #         <div style="margin-bottom: 12px;">
            #             <label style="font-size: 11px; font-weight: 700; color: var(--ink3); text-transform: uppercase; letter-spacing: 0.5px; display: block; margin-bottom: 8px;">🍽️ Restaurant Address Hub</label>
            #             <div style="background: #F0F9FF; border: 1px solid #0EA5E9; border-radius: 8px; padding: 10px 14px; font-size: 13px; font-weight: 600; color: #0369A1; display: flex; align-items: center; justify-content: space-between;">
            #                 <span>{s.rest_search_text}</span>
            #                 <span style="font-size: 11px; background: #0EA5E9; color: white; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Map Pin</span>
            #             </div>
            #         </div>
            #         """, unsafe_allow_html=True)
                    
            #         if st.button("✏️ Clear Pin & Use Search", key="clear_rest_map_pin", type="secondary", use_container_width=True):
            #             s.rest_search_text = "Connaught Place, New Delhi"
            #             s.rest_map_active = False
            #             s.rest_box_id += 1
                        
            #             if "processed_click_id" in s: s.processed_click_id = ""
            #             if "map_master_canvas" in s and s["map_master_canvas"] is not None:
            #                 if "last_clicked" in s["map_master_canvas"]: s["map_master_canvas"]["last_clicked"] = None
            #             st.rerun()
            #     else:
            #         restaurant_selection = st_searchbox(
            #             address_autocomplete_lookup,
            #             label="🍽️ From: Restaurant",
            #             default=s.rest_search_text,
            #             key=f"rest_box_instance_{s.rest_box_id}",
            #             clear_on_submit=False,
            #             edit_after_submit="option"
            #         )
            #         if restaurant_selection is not None and isinstance(restaurant_selection, tuple):
            #             if restaurant_selection != (s.rest_lat, s.rest_lon):
            #                 s.rest_lat, s.rest_lon = restaurant_selection
            #                 s.rest_search_text = "📍 Custom Searched Hub Location"

            # # --- DELIVERY INPUT (COLUMN 2) ---
            # with search_col2:
            #     if chosen_mode == "📍 Tap on Map" and is_rest_map_click and not is_del_map_click:
            #         # Guide user to drop second pin once first pin is locked in
            #         st.info("📦 Tap on the map below to set the **Delivery Pin**", icon="📍")
                
            #     elif chosen_mode == "📍 Tap on Map" and not is_rest_map_click and not is_del_map_click:
            #         # Secondary placeholder when restaurant takes priority
            #         st.info("Waiting for Restaurant Pin...", icon="⏳")

            #     elif is_del_map_click:
            #         st.markdown(f"""
            #         <div style="margin-bottom: 12px;">
            #             <label style="font-size: 11px; font-weight: 700; color: var(--ink3); text-transform: uppercase; letter-spacing: 0.5px; display: block; margin-bottom: 8px;">📦 Delivery Target Point</label>
            #             <div style="background: #FFF7ED; border: 1px solid #F97316; border-radius: 8px; padding: 10px 14px; font-size: 13px; font-weight: 600; color: #C2410C; display: flex; align-items: center; justify-content: space-between;">
            #                 <span>{s.del_search_text}</span>
            #                 <span style="font-size: 11px; background: #F97316; color: white; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Map Pin</span>
            #             </div>
            #         </div>
            #         """, unsafe_allow_html=True)
                    
            #         if st.button("✏️ Clear Pin & Use Search", key="clear_del_map_pin", type="secondary", use_container_width=True):
            #             s.del_search_text = "Karol Bagh, New Delhi"
            #             s.del_map_active = False
            #             s.del_box_id += 1
                        
            #             if "processed_click_id" in s: s.processed_click_id = ""
            #             if "map_master_canvas" in s and s["map_master_canvas"] is not None:
            #                 if "last_clicked" in s["map_master_canvas"]: s["map_master_canvas"]["last_clicked"] = None
            #             st.rerun()
            #     else:
            #         delivery_selection = st_searchbox(
            #             address_autocomplete_lookup,
            #             label="📦 To: Delivery Destination",
            #             default=s.del_search_text,
            #             key=f"del_box_instance_{s.del_box_id}",
            #             clear_on_submit=False,
            #             edit_after_submit="option"
            #         )
            #         if delivery_selection is not None and isinstance(delivery_selection, tuple):
            #             if delivery_selection != (s.del_lat, s.del_lon):
            #                 s.del_lat, s.del_lon = delivery_selection
            #                 s.del_search_text = "📍 Custom Searched Destination"
           
            # search_col1, search_col2 = st.columns(2)
    
            # # with search_col1:
            # #     restaurant_selection = st_searchbox(
            # #         address_autocomplete_lookup,
            # #         label="🍽️ Search Restaurant Address Hub",
            # #         default=s.rest_search_text,
            # #         key=f"rest_box_instance_{s.rest_box_id}",
            # #         clear_on_submit=False,
            # #         edit_after_submit="option"
            # #     )
            # #     if restaurant_selection is not None and isinstance(restaurant_selection, tuple):
            # #         if restaurant_selection != (s.rest_lat, s.rest_lon):
            # #             s.rest_lat, s.rest_lon = restaurant_selection
            # #             s.rest_search_text = "📍 Custom Searched Hub Location"
            # # with search_col2:
            # #     delivery_selection = st_searchbox(
            # #         address_autocomplete_lookup,
            # #         label="📦 Search Delivery Target Point",
            # #         default=s.del_search_text,
            # #         key=f"del_box_instance_{s.del_box_id}",
            # #         clear_on_submit=False,
            # #         edit_after_submit="option"
            # #     )
            # #     if delivery_selection is not None and isinstance(delivery_selection, tuple):
            # #         if delivery_selection != (s.del_lat, s.del_lon):
            # #             s.del_lat, s.del_lon = delivery_selection
            # #             s.del_search_text = "📍 Custom Searched Destination"

            # with search_col1:
            #     restaurant_selection = st_searchbox(
            #         address_autocomplete_lookup,
            #         label="🍽️ Search Restaurant Address Hub",
            #         default=s.rest_search_text,
            #         key=f"rest_box_instance_{s.rest_box_id}",
            #         clear_on_submit=False,
            #         edit_after_submit="option"
            #     )
            #     if restaurant_selection is not None and isinstance(restaurant_selection, tuple):
            #         if restaurant_selection != (s.rest_lat, s.rest_lon):
            #             s.rest_lat, s.rest_lon = restaurant_selection
            #             # FIX: If selected via dropdown typing, track the actual label tuple structure if available, or fall back cleanly
            #             s.rest_search_text = "📍 Custom Searched Hub Location"
            
            # with search_col2:
            #     delivery_selection = st_searchbox(
            #         address_autocomplete_lookup,
            #         label="📦 Search Delivery Target Point",
            #         default=s.del_search_text,
            #         key=f"del_box_instance_{s.del_box_id}",
            #         clear_on_submit=False,
            #         edit_after_submit="option"
            #     )
            #     if delivery_selection is not None and isinstance(delivery_selection, tuple):
            #         if delivery_selection != (s.del_lat, s.del_lon):
            #             s.del_lat, s.del_lon = delivery_selection
            #             # FIX: Updates search baseline state directly
            #             s.del_search_text = "📍 Custom Searched Destination"
                        
            # st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)
            # pin_r, pin_d = st.columns(2)
            # with pin_r:
            #     if st.button(f"{'🔵 ' if s.pin_mode=='restaurant' else ''}📍 Pin Restaurant Mode", use_container_width=True, key="btn_pin_r"):
            #         s.pin_mode = "restaurant"
            # with pin_d:
            #     if st.button(f"{'🟠 ' if s.pin_mode=='delivery' else ''}📦 Pin Delivery Mode", use_container_width=True, key="btn_pin_d"):
            #         s.pin_mode = "delivery"

            # # ─── EXTRACTION & LAYOUT ENGINE ───
            # # Check if current state reflects a typed address or a physical map pin click
            # is_rest_map_click = "🎯 Map:" in str(s.rest_search_text)
            # is_del_map_click = "🎯 Map:" in str(s.del_search_text)

            # search_col1, search_col2 = st.columns(2)
    
            # with search_col1:
            #     if is_rest_map_click:
            #         st.markdown(f"""
            #         <div style="margin-bottom: 22px;">
            #             <label style="font-size: 11px; font-weight: 700; color: var(--ink3); text-transform: uppercase; letter-spacing: 0.5px; display: block; margin-bottom: 8px;">🍽️ Restaurant Address Hub</label>
            #             <div style="background: #F0F9FF; border: 1px solid #0EA5E9; border-radius: 8px; padding: 10px 14px; font-size: 13px; font-weight: 600; color: #0369A1; display: flex; align-items: center; justify-content: space-between;">
            #                 <span>{s.rest_search_text}</span>
            #                 <span style="font-size: 11px; background: #0EA5E9; color: white; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Map Pin</span>
            #             </div>
            #         </div>
            #         """, unsafe_allow_html=True)
            #         # FIXED: Removed size="small", using default type instead
            #         if st.button("✏️ Change to Text Search Mode", key="clear_rest_map_pin", type="secondary"):
            #             s.rest_search_text = "Connaught Place, New Delhi"
            #             s.rest_box_id += 1
            #             st.rerun()
            #     else:
            #         restaurant_selection = st_searchbox(
            #             address_autocomplete_lookup,
            #             label="🍽️ Search Restaurant Address Hub",
            #             default=s.rest_search_text,
            #             key=f"rest_box_instance_{s.rest_box_id}",
            #             clear_on_submit=False,
            #             edit_after_submit="option"
            #         )
            #         if restaurant_selection is not None and isinstance(restaurant_selection, tuple):
            #             if restaurant_selection != (s.rest_lat, s.rest_lon):
            #                 s.rest_lat, s.rest_lon = restaurant_selection
            #                 s.rest_search_text = "📍 Custom Searched Hub Location"

            # with search_col2:
            #     if is_del_map_click:
            #         st.markdown(f"""
            #         <div style="margin-bottom: 22px;">
            #             <label style="font-size: 11px; font-weight: 700; color: var(--ink3); text-transform: uppercase; letter-spacing: 0.5px; display: block; margin-bottom: 8px;">📦 Delivery Target Point</label>
            #             <div style="background: #FFF7ED; border: 1px solid #F97316; border-radius: 8px; padding: 10px 14px; font-size: 13px; font-weight: 600; color: #C2410C; display: flex; align-items: center; justify-content: space-between;">
            #                 <span>{s.del_search_text}</span>
            #                 <span style="font-size: 11px; background: #F97316; color: white; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Map Pin</span>
            #             </div>
            #         </div>
            #         """, unsafe_allow_html=True)
            #         # FIXED: Removed size="small", using default type instead
            #         if st.button("✏️ Change to Text Search Mode", key="clear_del_map_pin", type="secondary"):
            #             s.del_search_text = "Karol Bagh, New Delhi"
            #             s.del_box_id += 1
            #             st.rerun()
            #     else:
            #         delivery_selection = st_searchbox(
            #             address_autocomplete_lookup,
            #             label="📦 Search Delivery Target Point",
            #             default=s.del_search_text,
            #             key=f"del_box_instance_{s.del_box_id}",
            #             clear_on_submit=False,
            #             edit_after_submit="option"
            #         )
            #         if delivery_selection is not None and isinstance(delivery_selection, tuple):
            #             if delivery_selection != (s.del_lat, s.del_lon):
            #                 s.del_lat, s.del_lon = delivery_selection
            #                 s.del_search_text = "📍 Custom Searched Destination"
                        
            # st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)
            # pin_r, pin_d = st.columns(2)
            # with pin_r:
            #     if st.button(f"{'🔵 ' if s.pin_mode=='restaurant' else ''}📍 Pin Restaurant Mode", use_container_width=True, key="btn_pin_r"):
            #         s.pin_mode = "restaurant"
            # with pin_d:
            #     if st.button(f"{'🟠 ' if s.pin_mode=='delivery' else ''}📦 Pin Delivery Mode", use_container_width=True, key="btn_pin_d"):
            #         s.pin_mode = "delivery"

            # ─── EXTRACTION & LAYOUT ENGINE ───
            # Identify if the text is a custom search label or a pinpoint address name 
            # We initialize these flags based on whether the string looks like an address placeholder or user string
            # is_rest_map_click = getattr(s, "rest_map_active", False)
            # is_del_map_click = getattr(s, "del_map_active", False)

            # search_col1, search_col2 = st.columns(2)
    
            # with search_col1:
            #     if is_rest_map_click:
            #         st.markdown(f"""
            #         <div style="margin-bottom: 12px;">
            #             <label style="font-size: 11px; font-weight: 700; color: var(--ink3); text-transform: uppercase; letter-spacing: 0.5px; display: block; margin-bottom: 8px;">🍽️ Restaurant Address Hub</label>
            #             <div style="background: #F0F9FF; border: 1px solid #0EA5E9; border-radius: 8px; padding: 10px 14px; font-size: 13px; font-weight: 600; color: #0369A1; display: flex; align-items: center; justify-content: space-between;">
            #                 <span>{s.rest_search_text}</span>
            #                 <span style="font-size: 11px; background: #0EA5E9; color: white; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Map Pin</span>
            #             </div>
            #         </div>
            #         """, unsafe_allow_html=True)
                    
            #         if st.button("✏️ Change to Text Search Mode", key="clear_rest_map_pin", type="secondary", use_container_width=True):
            #             s.rest_search_text = "Connaught Place, New Delhi"
            #             s.rest_map_active = False
            #             s.rest_box_id += 1
                        
            #             # CRITICAL FIX: Explicitly purge cached coordinates from the map object's internal state memory
            #             if "processed_click_id" in s:
            #                 s.processed_click_id = ""
            #             if "map_master_canvas" in s and s["map_master_canvas"] is not None:
            #                 if "last_clicked" in s["map_master_canvas"]:
            #                     s["map_master_canvas"]["last_clicked"] = None
                                
            #             st.rerun()
            #     else:
            #         restaurant_selection = st_searchbox(
            #             address_autocomplete_lookup,
            #             # label="🍽️ Search Restaurant Address Hub",
            #             label="🍽️ From: Restaurant",
            #             default=s.rest_search_text,
            #             key=f"rest_box_instance_{s.rest_box_id}",
            #             clear_on_submit=False,
            #             edit_after_submit="option"
            #         )
            #         if restaurant_selection is not None and isinstance(restaurant_selection, tuple):
            #             if restaurant_selection != (s.rest_lat, s.rest_lon):
            #                 s.rest_lat, s.rest_lon = restaurant_selection
            #                 s.rest_search_text = "📍 Custom Searched Hub Location"

            # with search_col2:
            #     if is_del_map_click:
            #         st.markdown(f"""
            #         <div style="margin-bottom: 12px;">
            #             <label style="font-size: 11px; font-weight: 700; color: var(--ink3); text-transform: uppercase; letter-spacing: 0.5px; display: block; margin-bottom: 8px;">📦 Delivery Target Point</label>
            #             <div style="background: #FFF7ED; border: 1px solid #F97316; border-radius: 8px; padding: 10px 14px; font-size: 13px; font-weight: 600; color: #C2410C; display: flex; align-items: center; justify-content: space-between;">
            #                 <span>{s.del_search_text}</span>
            #                 <span style="font-size: 11px; background: #F97316; color: white; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Map Pin</span>
            #             </div>
            #         </div>
            #         """, unsafe_allow_html=True)
                    
            #         if st.button("✏️ Change to Text Search Mode", key="clear_del_map_pin", type="secondary", use_container_width=True):
            #             s.del_search_text = "Karol Bagh, New Delhi"
            #             s.del_map_active = False
            #             s.del_box_id += 1
                        
            #             # CRITICAL FIX: Explicitly purge cached coordinates from the map object's internal state memory
            #             if "processed_click_id" in s:
            #                 s.processed_click_id = ""
            #             if "map_master_canvas" in s and s["map_master_canvas"] is not None:
            #                 if "last_clicked" in s["map_master_canvas"]:
            #                     s["map_master_canvas"]["last_clicked"] = None
                                
            #             st.rerun()

            #     else:
            #         delivery_selection = st_searchbox(
            #             address_autocomplete_lookup,
            #             # label="📦 Search Delivery Target Point",
            #             label="📦 To: Delivery Destination",
            #             default=s.del_search_text,
            #             key=f"del_box_instance_{s.del_box_id}",
            #             clear_on_submit=False,
            #             edit_after_submit="option"
            #         )
            #         if delivery_selection is not None and isinstance(delivery_selection, tuple):
            #             if delivery_selection != (s.del_lat, s.del_lon):
            #                 s.del_lat, s.del_lon = delivery_selection
            #                 s.del_search_text = "📍 Custom Searched Destination"


            # st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)
            # pin_r, pin_d = st.columns(2)
            # with pin_r:
            #     if st.button(f"{'🔵 ' if s.pin_mode=='restaurant' else ''}📍 Pin Restaurant Mode", use_container_width=True, key="btn_pin_r"):
            #         s.pin_mode = "restaurant"
            # with pin_d:
            #     if st.button(f"{'🟠 ' if s.pin_mode=='delivery' else ''}📦 Pin Delivery Mode", use_container_width=True, key="btn_pin_d"):
            #         s.pin_mode = "delivery"
                    
            # pin_hint = ("🔵 Active: Manual map clicks position the **Restaurant Hub**" if s.pin_mode == "restaurant" else "🟠 Active: Manual map clicks position the **Delivery Location**")
            # st.info(pin_hint)

            # st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)
            # pin_r, pin_d = st.columns(2)
            
            # with pin_r:
            #     # DYNAMIC COLOR ENGAGEMENT: If active, use primary style (grows brand accent)
            #     is_r_active = s.pin_mode == "restaurant"
            #     if st.button(
            #         f"{'🔵 ' if is_r_active else ''}📍 Pin Restaurant Mode", 
            #         use_container_width=True, 
            #         key="btn_pin_r",
            #         type="primary" if is_r_active else "secondary"
            #     ):
            #         s.pin_mode = "restaurant"
            #         st.rerun()
                    
            # with pin_d:
            #     # DYNAMIC COLOR ENGAGEMENT: If active, use primary style (grows brand accent)
            #     is_d_active = s.pin_mode == "delivery"
            #     if st.button(
            #         f"{'🟠 ' if is_d_active else ''}📦 Pin Delivery Mode", 
            #         use_container_width=True, 
            #         key="btn_pin_d",
            #         type="primary" if is_d_active else "secondary"
            #     ):
            #         s.pin_mode = "delivery"
            #         st.rerun()

            # st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)
            # pin_r, pin_d = st.columns(2)
            
            # is_r_active = (s.pin_mode == "restaurant")
            # is_d_active = (s.pin_mode == "delivery")

            # with pin_r:
            #     if st.button(
            #         f"{'🔵 ' if is_r_active else ''}📍 Pin Restaurant Mode", 
            #         use_container_width=True, 
            #         key="btn_pin_r"
            #     ):
            #         s.pin_mode = "restaurant"
            #         st.rerun()
                    
            # with pin_d:
            #     if st.button(
            #         f"{'🟠 ' if is_d_active else ''}📦 Pin Delivery Mode", 
            #         use_container_width=True, 
            #         key="btn_pin_d"
            #     ):
            #         s.pin_mode = "delivery"
            #         st.rerun()

            # # ─── REALTIME DOM COLOR BRIDGE ───
            # # Dynamically inject attribute markers into the target frame buttons based on state rules
            # import streamlit.components.v1 as components
            
            # js_color_bridge = f"""
            # <script>
            # const buttons = window.parent.document.querySelectorAll('button');
            # buttons.forEach(btn => {{
            #     if (btn.innerText.includes("Pin Restaurant Mode")) {{
            #         btn.setAttribute("p-mode", "{'active-rest' if is_r_active else 'inactive'}");
            #     }}
            #     if (btn.innerText.includes("Pin Delivery Mode")) {{
            #         btn.setAttribute("p-mode", "{'active-del' if is_d_active else 'inactive'}");
            #     }}
            # }});
            # </script>
            # """
            # components.html(js_color_bridge, height=0, width=0)
            
            # # Map Processing Layout Engine
            # clat = (float(s.rest_lat) + float(s.del_lat)) / 2
            # clon = (float(s.rest_lon) + float(s.del_lon)) / 2
            # m = folium.Map(location=[clat, clon], zoom_start=13)
            # folium.TileLayer('OpenStreetMap').add_to(m)
            # folium.Marker([float(s.rest_lat), float(s.rest_lon)], tooltip="🍽️ Restaurant", icon=folium.Icon(color='blue', icon='cutlery', prefix='fa')).add_to(m)
            # folium.Marker([float(s.del_lat), float(s.del_lon)], tooltip="📦 Delivery Point", icon=folium.Icon(color='orange', icon='map-marker', prefix='fa')).add_to(m)
            # folium.PolyLine([[float(s.rest_lat), float(s.rest_lon)], [float(s.del_lat), float(s.del_lon)]], color='#E8471E', weight=2.5, opacity=.7, dash_array='8 5').add_to(m)
            
            # # CRITICAL CORRECTION: Map is rendered directly within the structural container frame
            # map_result = st_folium(m, center=[clat, clon], width="100%", height=360, key="map_main")
            
            # if map_result and map_result.get("last_clicked"):
            #     click_lat = round(map_result["last_clicked"]["lat"], 6)
            #     click_lon = round(map_result["last_clicked"]["lng"], 6)
            #     click_sig = f"{click_lat}_{click_lon}"
            #     if "processed_click_id" not in s: 
            #         s.processed_click_id = ""
            #     if click_sig != s.processed_click_id:
            #         s.processed_click_id = click_sig
            #         if s.pin_mode == "restaurant":
            #             s.rest_lat, s.rest_lon = click_lat, click_lon
            #             s.rest_search_text = f"🎯 Map: {click_lat:.4f}, {click_lon:.4f}"
            #             s.rest_box_id += 1 
            #             st.toast("Hub coordinate updated via map click!", icon="🔵")
            #         else:
            #             s.del_lat, s.del_lon = click_lat, click_lon
            #             s.del_search_text = f"🎯 Map: {click_lat:.4f}, {click_lon:.4f}"
            #             s.del_box_id += 1
            #             st.toast("Destination coordinate updated via map click!", icon="🟠")
            #         st.rerun()

            # # ─── EXTRACTION & LAYOUT ENGINE (ABSOLUTE MEMORY ISOLATION) ───
            # # Calculate route midpoint for absolute centering fallbacks
            # clat = (float(s.rest_lat) + float(s.del_lat)) / 2
            # clon = (float(s.rest_lon) + float(s.del_lon)) / 2
            
            # # Map object initialization
            # m = folium.Map(location=[clat, clon], zoom_start=12)
            # folium.TileLayer('OpenStreetMap').add_to(m)
            
            # # Add dynamic map pins
            # folium.Marker(
            #     [float(s.rest_lat), float(s.rest_lon)], 
            #     tooltip="🍽️ Restaurant Hub", 
            #     icon=folium.Icon(color='blue', icon='cutlery', prefix='fa')
            # ).add_to(m)
            
            # folium.Marker(
            #     [float(s.del_lat), float(s.del_lon)], 
            #     tooltip="📦 Delivery Target Point", 
            #     icon=folium.Icon(color='orange', icon='map-marker', prefix='fa')
            # ).add_to(m)
            
            # # Draw the route line vector between points
            # folium.PolyLine(
            #     [[float(s.rest_lat), float(s.rest_lon)], [float(s.del_lat), float(s.del_lon)]], 
            #     color='#E8471E', 
            #     weight=3, 
            #     opacity=.8, 
            #     dash_array='8 5'
            # ).add_to(m)
            
            # # CRITICAL STATE ENGINE FIX: Dynamic key format forces an absolute component instance refresh 
            # # whenever a user switches between map pinning and text search modes.
            # map_instance_key = f"map_canvas_state_{getattr(s, 'rest_map_active', False)}_{getattr(s, 'del_map_active', False)}"
            
            # map_result = st_folium(
            #     m, 
            #     center=[clat, clon], 
            #     width="100%", 
            #     height=360, 
            #     key=map_instance_key
            # )
            
            # # Handle user map-click interactions cleanly
            # if map_result and map_result.get("last_clicked"):
            #     click_lat = round(map_result["last_clicked"]["lat"], 6)
            #     click_lon = round(map_result["last_clicked"]["lng"], 6)
            #     click_sig = f"{click_lat}_{click_lon}"
                
            #     if "processed_click_id" not in s: 
            #         s.processed_click_id = ""
                    
            #     # Verify that this is an intentional, new user click event
            #     if click_sig != s.processed_click_id:
            #         s.processed_click_id = click_sig
                    
            #         # ─── REVERSE GEOCODING ENGINE ───
            #         try:
            #             location_obj = geolocator.reverse((click_lat, click_lon), timeout=3)
            #             if location_obj and getattr(location_obj, "address", None):
            #                 address_parts = [part.strip() for part in location_obj.address.split(",") if part.strip()]
            #                 if len(address_parts) >= 2:
            #                     place_display_name = f"{address_parts[0]}, {address_parts[1]}"
            #                 elif len(address_parts) == 1:
            #                     place_display_name = f"{address_parts[0]}"
            #                 else:
            #                     place_display_name = f"Coordinates: {click_lat:.4f}, {click_lon:.4f}"
            #             else:
            #                 place_display_name = f"Coordinates: {click_lat:.4f}, {click_lon:.4f}"
            #         except Exception:
            #             place_display_name = f"Coordinates: {click_lat:.4f}, {click_lon:.4f}"
                    
            #         # Update coordinates and active layout view states instantly
            #         if s.pin_mode == "restaurant":
            #             s.rest_lat, s.rest_lon = click_lat, click_lon
            #             s.rest_search_text = place_display_name
            #             s.rest_map_active = True  
            #             st.toast(f"Hub updated to {place_display_name}!", icon="🔵")
            #         else:
            #             s.del_lat, s.del_lon = click_lat, click_lon
            #             s.del_search_text = place_display_name
            #             s.del_map_active = True  
            #             st.toast(f"Destination updated to {place_display_name}!", icon="🟠")
                    
            #         st.rerun()

            # # ─── STATE MANAGEMENT SYNC (ZERO-CLICK MULTI-TAP ENGINE) ───
            # if "click_count" not in s:
            #     s.click_count = 0

            # # Initialize component keys to force searchbox updates on map clicks
            # if "rest_key_version" not in s:
            #     s.rest_key_version = 1
            # if "del_key_version" not in s:
            #     s.del_key_version = 1

            # if s.rest_lat is None:
            #     s.pin_mode = "restaurant"
            # elif s.del_lat is None:
            #     s.pin_mode = "delivery"
            # else:
            #     s.pin_mode = "restaurant"

            # # Safe native layout initialization
            # search_col1, search_col2 = st.columns(2)

            # # --- RESTAURANT INPUT (COLUMN 1) ---
            # with search_col1:
            #     restaurant_selection = st_searchbox(
            #         address_autocomplete_lookup,
            #         label="🍽️ From: Restaurant Hub", 
            #         placeholder="Search or Click Map Directly...", 
            #         default=s.rest_search_text if s.rest_search_text else "",
            #         key=f"rest_box_instance_v_{s.rest_key_version}",
            #         clear_on_submit=False,
            #         edit_after_submit="option"
            #     )
                
            #     if restaurant_selection is not None and isinstance(restaurant_selection, tuple):
            #         if restaurant_selection != (s.rest_lat, s.rest_lon):
            #             s.rest_lat, s.rest_lon = restaurant_selection
            #             s.rest_search_text = "📍 Custom Searched Hub Location"
            #             s.click_count = 1 if s.del_lat is None else 2
            #             st.rerun()

            # # --- DELIVERY INPUT (COLUMN 2) ---
            # with search_col2:
            #     delivery_selection = st_searchbox(
            #         address_autocomplete_lookup,
            #         label="📦 To: Delivery Destination", 
            #         placeholder="Search or Click Map Directly...", 
            #         default=s.del_search_text if s.del_search_text else "",
            #         key=f"del_box_instance_v_{s.del_key_version}",
            #         clear_on_submit=False,
            #         edit_after_submit="option"
            #     )
                
            #     if delivery_selection is not None and isinstance(delivery_selection, tuple):
            #         if delivery_selection != (s.del_lat, s.del_lon):
            #             s.del_lat, s.del_lon = delivery_selection
            #             s.del_search_text = "📍 Custom Searched Destination"
            #             s.click_count = 2
            #             st.rerun()

            # # ─── EXTRACTION & LAYOUT ENGINE (ABSOLUTE MEMORY ISOLATION) ───
            # if s.rest_lat is not None and s.del_lat is not None:
            #     clat = (float(s.rest_lat) + float(s.del_lat)) / 2
            #     clon = (float(s.rest_lon) + float(s.del_lon)) / 2
            #     zoom_fallback = 12
            # elif s.rest_lat is not None:
            #     clat, clon = float(s.rest_lat), float(s.rest_lon)
            #     zoom_fallback = 13
            # elif s.del_lat is not None:
            #     clat, clon = float(s.del_lat), float(s.del_lon)
            #     zoom_fallback = 13
            # else:
            #     clat, clon = 28.6139, 77.2090  
            #     zoom_fallback = 11

            # m = folium.Map(
            #     location=[clat, clon], 
            #     zoom_start=zoom_fallback,
            #     tiles='CartoDB positron', 
            #     attr='&copy; <a href="https://openstreetmap.org">OpenStreetMap</a> contributors &copy; <a href="https://carto.com">CARTO</a>'
            # )

            # if s.rest_lat is not None:
            #     folium.Marker(
            #         [float(s.rest_lat), float(s.rest_lon)], 
            #         tooltip="🍽️ Pickup Restaurant Hub", 
            #         icon=folium.Icon(color='orange', icon='cutlery', prefix='fa')
            #     ).add_to(m)

            # if s.del_lat is not None:
            #     folium.Marker(
            #         [float(s.del_lat), float(s.del_lon)], 
            #         tooltip="📦 Delivery Destination Point", 
            #         icon=folium.Icon(color='purple', icon='home', prefix='fa')
            #     ).add_to(m)

            # if s.rest_lat is not None and s.del_lat is not None:
            #     folium.PolyLine(
            #         [[float(s.rest_lat), float(s.rest_lon)], [float(s.del_lat), float(s.del_lon)]], 
            #         color='#FF4B4B', 
            #         weight=4, 
            #         opacity=0.9, 
            #         dash_array='6 4'
            #     ).add_to(m)

            # # A static map key guarantees that the map state is modified seamlessly in place
            # map_result = st_folium(
            #     m, 
            #     center=[clat, clon], 
            #     width="100%", 
            #     height=380, 
            #     key="zero_click_delivery_canvas"
            # )

            # # ─── USER INTERACTION DISPATCHER ───
            # if map_result and map_result.get("last_clicked"):
            #     click_lat = round(map_result["last_clicked"]["lat"], 6)
            #     click_lon = round(map_result["last_clicked"]["lng"], 6)
            #     click_sig = f"{click_lat}_{click_lon}"
                
            #     if "processed_click_id" not in s: 
            #         s.processed_click_id = ""
                    
            #     if click_sig != s.processed_click_id:
            #         s.processed_click_id = click_sig
                    
            #         try:
            #             location_obj = geolocator.reverse((click_lat, click_lon), timeout=3)
            #             if location_obj and getattr(location_obj, "address", None):
            #                 address_parts = [part.strip() for part in location_obj.address.split(",") if part.strip()]
            #                 place_display_name = f"{address_parts[0]}, {address_parts[1]}" if len(address_parts) >= 2 else address_parts[0]
            #             else:
            #                 place_display_name = f"{click_lat:.4f}, {click_lon:.4f}"
            #         except Exception:
            #             place_display_name = f"{click_lat:.4f}, {click_lon:.4f}"
                    
            #         # ─── INCREMENTAL STATE COUNTER FLOW ───
            #         if s.click_count == 0 or s.click_count >= 2:
            #             s.rest_lat, s.rest_lon = click_lat, click_lon
            #             s.rest_search_text = place_display_name
            #             s.del_lat, s.del_lon = None, None  
            #             s.del_search_text = "Not Selected"
            #             s.click_count = 1
            #             # Force-refresh the restaurant input field's internal cache
            #             s.rest_key_version += 1 
            #             st.toast(f"Restaurant plotted at {place_display_name}!", icon="📍")
            #         else:
            #             s.del_lat, s.del_lon = click_lat, click_lon
            #             s.del_search_text = place_display_name
            #             s.click_count = 2
            #             # Force-refresh the delivery input field's internal cache
            #             s.del_key_version += 1 
            #             st.toast(f"Destination plotted at {place_display_name}!", icon="🏁")
                        
            #         st.rerun()

            # # ─── REALTIME CALCULATED MILEAGE FOOTER ───
            # if s.rest_lat is not None and s.del_lat is not None:
            #     dist = haversine(s.rest_lat, s.rest_lon, s.del_lat, s.del_lon)
            # else:
            #     dist = 0.00

            # st.markdown(f"""
            # <div class="dist-pill" style="display:flex; align-items:center; justify-content:space-between; background:#F0FDF4; border:1px solid #BBF7D0; border-radius:10px; padding:12px 16px; margin-top:16px; margin-bottom:12px;">
            # <span style="font-size:13px; font-weight:700; color:#16A34A;">📐 Calculated Route Distance</span>
            # <span><span style="font-family:'Bricolage Grotesque',sans-serif; font-size:18px; font-weight:800; color:#15803D;">{dist:.2f}</span> <span style="font-size:12px; font-weight:700; color:#16A34A;">km</span></span>
            # </div>
            # """, unsafe_allow_html=True)

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

            #             # ─── NATIVE FLOATING CONFIGURATION OVERLAY DECK ───────────────────
            # # Renders the text boxes natively. The global CSS engine will pick them up automatically.
            # with st.container():
            #     search_col1, search_col2 = st.columns(2, gap="medium")

            #     with search_col1:
            #         restaurant_selection = st_searchbox(
            #             address_autocomplete_lookup,
            #             label="🍽️ Pickup Restaurant Hub",
            #             placeholder="🔍 Type or Click Map Directly...", 
            #             default=None, 
            #             key=f"rest_box_instance_v_{s.rest_key_version}",
            #             clear_on_submit=False,
            #             edit_after_submit="option"
            #         )
                    
            #         if restaurant_selection is not None and isinstance(restaurant_selection, tuple):
            #             if restaurant_selection != (s.map_rest_lat, s.map_rest_lon):
            #                 s.map_rest_lat, s.map_rest_lon = restaurant_selection
            #                 s.rest_search_text = "📍 Custom Searched Hub"
            #                 s.click_count = 1 if s.map_del_lat is None else 2
            #                 s.rest_key_version += 1 
            #                 st.rerun()

            #     with search_col2:
            #         delivery_selection = st_searchbox(
            #             address_autocomplete_lookup,
            #             label="📦 Delivery Destination Target",
            #             placeholder="🔍 Type or Click Map Directly...", 
            #             default=None, 
            #             key=f"del_box_instance_v_{s.del_key_version}",
            #             clear_on_submit=False,
            #             edit_after_submit="option"
            #         )
                    
            #         if delivery_selection is not None and isinstance(delivery_selection, tuple):
            #             if delivery_selection != (s.map_del_lat, s.map_del_lon):
            #                 s.map_del_lat, s.map_del_lon = delivery_selection
            #                 s.del_search_text = "📍 Custom Searched Destination"
            #                 s.click_count = 2
            #                 s.del_key_version += 1 
            #                 st.rerun()




            #             # ─── MODERNIZED GLASSMORPHIC INPUT DECK ───────────────────────────
            # # Wraps your interactive search boxes inside a unified modern wrapper
            # with st.container(key="glass_input_deck_container"):
            #     st.markdown('<div class="glass-input-deck">', unsafe_allow_html=True)
                
            #     search_col1, search_col2 = st.columns(2, gap="medium")

            #     with search_col1:
            #         restaurant_selection = st_searchbox(
            #             address_autocomplete_lookup,
            #             label="🍽️ Pickup Restaurant", 
            #             placeholder="Search or Click Map Directly...", 
            #             default=s.rest_search_text if s.rest_search_text else "",
            #             key=f"rest_box_instance_v_{s.rest_key_version}",
            #             clear_on_submit=False,
            #             edit_after_submit="option"
            #         )
            #         if restaurant_selection is not None and isinstance(restaurant_selection, tuple):
            #             if restaurant_selection != (s.map_rest_lat, s.map_rest_lon):
            #                 s.map_rest_lat, s.map_rest_lon = restaurant_selection
            #                 s.rest_search_text = "📍 Custom Searched Hub"
            #                 s.click_count = 1 if s.map_del_lat is None else 2
            #                 st.rerun()

            #     with search_col2:
            #         delivery_selection = st_searchbox(
            #             address_autocomplete_lookup,
            #             label="📦 Delivery Destination", 
            #             placeholder="Search or Click Map Directly...", 
            #             default=s.del_search_text if s.del_search_text else "",
            #             key=f"del_box_instance_v_{s.del_key_version}",
            #             clear_on_submit=False,
            #             edit_after_submit="option"
            #         )
            #         if delivery_selection is not None and isinstance(delivery_selection, tuple):
            #             if delivery_selection != (s.map_del_lat, s.map_del_lon):
            #                 s.map_del_lat, s.map_del_lon = delivery_selection
            #                 s.del_search_text = "📍 Custom Searched Destination"
            #                 s.click_count = 2
            #                 st.rerun()
                            
            #     st.markdown('</div>', unsafe_allow_html=True)

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
                    
                    # try:
                    #     location_obj = geolocator.reverse((click_lat, click_lon), timeout=3)
                    #     if location_obj and getattr(location_obj, "address", None):
                    #         address_parts = [p.strip() for p in location_obj.address.split(",") if p.strip()]
                    #         place_display_name = f"{address_parts[0]}, {address_parts[1]}" if len(address_parts) >= 2 else address_parts[0]
                    #     else:
                    #         place_display_name = f"{click_lat:.4f}, {click_lon:.4f}"
                    # except Exception:
                    #     place_display_name = f"{click_lat:.4f}, {click_lon:.4f}"

                    #                     # ─── REVERSE GEOCODING ENGINE ADDRESS STRING REPAIR ───
                    # try:
                    #     location_obj = geolocator.reverse((click_lat, click_lon), timeout=3)
                    #     if location_obj and getattr(location_obj, "address", None):
                    #         address_parts = [p.strip() for p in location_obj.address.split(",") if p.strip()]
                    #         # FIX: Combined with a safe join to prevent array list multiplication strings
                    #         place_display_name = ", ".join(address_parts[:2]) if len(address_parts) >= 2 else address_parts[0]
                    #     else:
                    #         place_display_name = f"{click_lat:.4f}, {click_lon:.4f}"
                    # except Exception:
                    #     place_display_name = f"{click_lat:.4f}, {click_lon:.4f}"

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
                        
                    st.rerun()

            # ─── 5. DISTANCE EVALUATION CALCULATOR FOOTER ─────────────────────────
            if s.map_rest_lat is not None and s.map_del_lat is not None:
                dist = haversine(s.map_rest_lat, s.map_rest_lon, s.map_del_lat, s.map_del_lon)
            else:
                dist = 0.00

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
                    
                    # Native toggle widget
                    show_coordinates = st.toggle(
                        label="", 
                        value=False, 
                        key="hud_matrix_coord_reveal_tgl"
                    )
                    
                    st.markdown("</div>", unsafe_allow_html=True)

            # lower_col1, lower_col2 = st.columns([6.3, 1.7], gap="small", vertical_alignment="center")

            # with lower_col1:
            #     # Calculate active routing status securely against master state variables
            #     # Checking both None conditions and "Not Selected" string fallbacks guarantees accuracy
            #     has_rest = s.map_rest_lat is not None and s.rest_search_text != "Not Selected"
            #     has_del = s.map_del_lat is not None and s.del_search_text != "Not Selected"

            #     if has_rest and has_del:
            #         status_text = "✓ Route locked in successfully"
            #         status_color = "#15803D"  # Crisp dark emerald green
            #         status_bg = "#F0FDF4"     # Soft green tint
            #         status_border = "#BBF7D0"
            #     else:
            #         status_text = "⏳ Awaiting map coordinate selections..."
            #         status_color = "#64748B"  # Muted slate gray text matching your shortcuts
            #         status_bg = "#F8FAFC"     # Premium light gray tint matching unselected presets
            #         status_border = "#E2E8F0" # Soft slate gray border line

            #     # Render an elegant, full-width status confirmation badge banner
            #     st.markdown(f"""
            #     <div class="dist-pill" style="display:flex; align-items:center; background:{status_bg}; border:1px solid {status_border}; border-radius:10px; padding:0 16px; margin: 12px 0 0 0; height:44px; width:100%; box-sizing:border-box;">
            #       <span style="font-size:13.5px; font-weight:700; color:{status_color}; white-space:nowrap; letter-spacing: -0.1px;">{status_text}</span>
            #     </div>
            #     """, unsafe_allow_html=True)

            # with lower_col1:
            #     # Calculate active routing status securely against master state variables
            #     has_rest = s.map_rest_lat is not None and s.rest_search_text != "Not Selected"
            #     has_del = s.map_del_lat is not None and s.del_search_text != "Not Selected"

            #     if has_rest and has_del:
            #         status_text = "✓ Route locked in successfully"
            #         status_class = "state-locked"
            #         status_color = "#15803D"  # Crisp dark emerald green
            #         status_bg = "#F0FDF4"     # Soft green tint
            #         status_border = "#BBF7D0"
            #     else:
            #         status_text = "⏳ Awaiting map coordinate selections..."
            #         status_class = "state-empty"
            #         status_color = "#475569"  # Deep slate text
            #         status_bg = "#F8FAFC"     # Premium light gray tint matching unselected presets
            #         status_border = "#E2E8F0" # Soft slate gray border line

            #     # Render an elegant, full-width status confirmation badge banner with hardcoded specific classes
            #     st.markdown(f"""
            #     <style>
            #         /* 1. Reset and target the locked active route status state class */
            #         div.dist-pill.state-locked {{
            #             background: #F0FDF4 !important;
            #             background-color: #F0FDF4 !important;
            #             border: 1px solid #BBF7D0 !important;
            #         }}
            #         div.dist-pill.state-locked span {{
            #             color: #15803D !important;
            #         }}
                    
            #         /* 2. Target the cleared/empty awaiting selections fallback class explicitly to kill the global green bleed */
            #         div.dist-pill.state-empty {{
            #             background: #F8FAFC !important;
            #             background-color: #F8FAFC !important;
            #             border: 1px solid #E2E8F0 !important;
            #         }}
            #         div.dist-pill.state-empty span {{
            #             color: #475569 !important;
            #         }}
            #     </style>
                
            #     <div class="dist-pill {status_class}" style="display:flex; align-items:center; background:{status_bg} !important; border:1px solid {status_border} !important; border-radius:10px; padding:0 16px; margin: 12px 0 0 0; height:44px; width:100%; box-sizing:border-box;">
            #       <span style="font-size:13.5px !important; font-weight:700 !important; color:{status_color} !important; white-space:nowrap; letter-spacing: -0.1px;">{status_text}</span>
            #     </div>
            #     """, unsafe_allow_html=True)


            # with lower_col2:
            #     # 1. Nest a micro 2-column grid inside the right slot to lock elements side-by-side natively
            #     # [5.5, 2.5] provides an elegant proportional split between the text length and the switch pill
            #     toggle_txt_col, toggle_sw_col = st.columns([5.5, 2.5], gap="small", vertical_alignment="center")
                
            #     with toggle_txt_col:
            #         # Locally styled text block to match your premium uppercase typography specs
            #         st.markdown("""
            #         <style>
            #             div.toggle-text-left-box {
            #                 margin-top: 10px !important; /* Vertically aligns the text baseline with the banner */
            #                 width: 100%;
            #                 text-align: right; /* Keeps it tight and tidy next to the switch track button */
            #             }
            #             div.toggle-text-left-box span {
            #                 font-size: 11px !important;
            #                 font-weight: 700 !important;
            #                 color: #64748B !important;
            #                 text-transform: uppercase !important;
            #                 letter-spacing: 0.8px !important;
            #                 white-space: nowrap !important;
            #             }
            #             /* Optional: Dynamic orange highlight text swap when the switch is active */
            #             div[data-testid="stColumn"]:has(input[aria-checked="true"]) ~ div div.toggle-text-left-box span,
            #             body:has(input[aria-checked="true"]) div.toggle-text-left-box span {
            #                 /* Fallback coloring handled smoothly through standard layout overrides */
            #             }
            #         </style>
            #         <div class="toggle-text-left-box">
            #             <span>ML Features</span>
            #         </div>
            #         """, unsafe_allow_html=True)
                    
            #     with toggle_sw_col:
            #         # Clean styling to strip out extra padding from Streamlit's native toggle widget frame
            #         st.markdown("""
            #         <style>
            #             div.compact-toggle-box {
            #                 margin-top: 14px !important; /* Vertically centers the switch track slider perfectly */
            #             }
            #             div.compact-toggle-box div[data-testid="stToggle"] {
            #                 padding: 0px !important;
            #                 margin: 0px !important;
            #             }
            #             /* Completely collapse any empty built-in text fields to prevent layout ghosting */
            #             div.compact-toggle-box div[data-testid="stToggle"] label p {
            #                 display: none !important;
            #             }
            #         </style>
            #         <div class="compact-toggle-box">
            #         """, unsafe_allow_html=True)
                    
            #         # Native toggle widget with label collapsed to guarantee perfect horizontal alignment
            #         show_coordinates = st.toggle(
            #             label="", 
            #             value=False, 
            #             key="hud_matrix_coord_reveal_tgl"
            #         )
                    
            #         st.markdown("</div>", unsafe_allow_html=True)

            # with lower_col2:
            #     # Local style overrides to center the toggle without a card box
            #     st.markdown("""
            #         <style>
            #         /* Target the specific toggle column container */
            #         div[data-testid="stColumn"]:nth-of-type(2) div[data-testid="stElementContainer"] div[data-testid="stToggle"] {
            #             /* INCREASED VERTICAL MARGIN: Lifted from 18px to 22px to center perfectly against the banner text line */
            #             margin: 32px 0 0 0 !important; 
            #             padding: 0px !important;
            #             display: flex !important;
            #             align-items: center !important;
            #         }
                    
            #         /* Custom typography tweaks for the native toggle label text */
            #         div[data-testid="stColumn"]:nth-of-type(2) div[data-testid="stElementContainer"] div[data-testid="stToggle"] label p {
            #             font-size: 11px !important;
            #             font-weight: 700 !important;
            #             color: #64748B !important;
            #             text-transform: uppercase !important;
            #             letter-spacing: 0.8px !important;
            #             margin: 0px 0px 0px 8px !important;
            #             padding: 0px !important;
            #         }
                    
            #         /* Dynamic orange highlight text swap when the switch is active */
            #         div[data-testid="stColumn"]:nth-of-type(2) div[data-testid="stElementContainer"] div[data-testid="stToggle"]:has(input[aria-checked="true"]) label p {
            #             color: #E8471E !important;
            #         }
            #         </style>
            #     """, unsafe_allow_html=True)
                
            #     # Modern native toggle widget used directly on a completely transparent background
            #     show_coordinates = st.toggle(
            #         label="ML Features", 
            #         value=False, 
            #         key="hud_matrix_coord_reveal_tgl",
            #         label_visibility="visible"
            #     )

            # ─── FULL WIDTH CONDITIONAL RENDERING GRID ───
            if show_coordinates:
                st.markdown("<div style='margin-top:16px;'></div>", unsafe_allow_html=True)
                
                # Full Width Row 1: Restaurant Parameters
                col_lat1, col_lon1 = st.columns(2, gap="medium")
                with col_lat1:
                    st.number_input(
                        "Restaurant Latitude", 
                        value=float(s.map_rest_lat) if s.map_rest_lat else 0.0,
                        format="%.6f",
                        key="numerical_input_rest_lat"
                    )
                with col_lon1:
                    st.number_input(
                        "Restaurant Longitude", 
                        value=float(s.map_rest_lon) if s.map_rest_lon else 0.0,
                        format="%.6f",
                        key="numerical_input_rest_lon"
                    )
                
                # Full Width Row 2: Delivery Destination Parameters
                col_lat2, col_lon2 = st.columns(2, gap="medium")
                with col_lat2:
                    st.number_input(
                        "Delivery Latitude", 
                        value=float(s.map_del_lat) if s.map_del_lat else 0.0,
                        format="%.6f",
                        key="numerical_input_del_lat"
                    )
                with col_lon2:
                    st.number_input(
                        "Delivery Longitude", 
                        value=float(s.map_del_lon) if s.map_del_lon else 0.0,
                        format="%.6f",
                        key="numerical_input_del_lon"
                    )

            # ─── ADDED VERTICAL BREATHING ROOM ABOVE CONTINUE BUTTON ───
            # Injects 24 pixels of structural clean whitespace below the banner block row
            st.markdown("<div style='margin-bottom: 24px;'></div>", unsafe_allow_html=True)




            # # ─── FULL-WIDTH HORIZONTAL CLEAR BUTTON (THEME INTEGRATION) ───
            # st.markdown("""
            # <style>
            #     /* Target the secondary button wrapper */
            #     div.unified-horizontal-clear-container [data-testid="stBaseButton-secondary"] button {
            #         width: 100% !important;
            #         height: 40px !important;
            #         min-height: 40px !important;
            #         max-height: 40px !important;
            #         margin: 12px 0 4px 0 !important;
            #         padding: 0px 16px !important;
                    
            #         /* Soft colored tint layout to coordinate with your orange/red theme accents */
            #         background-color: #FFF5F2 !important;
            #         background: #FFF5F2 !important;
            #         border: 1px solid #FCD3C7 !important;
            #         border-radius: 8px !important;
            #         box-shadow: none !important;
                    
            #         display: flex !important;
            #         align-items: center !important;
            #         justify-content: center !important;
            #         transition: all 0.2s ease-in-out !important;
            #     }
                
            #     /* Hover transition states updating background fills */
            #     div.unified-horizontal-clear-container [data-testid="stBaseButton-secondary"] button:hover {
            #         background-color: #FFEAE3 !important;
            #         background: #FFEAE3 !important;
            #         border-color: #F9A894 !important;
            #     }
                
            #     /* Typography color match using the primary red/orange hexadecimal values */
            #     div.unified-horizontal-clear-container [data-testid="stBaseButton-secondary"] button p,
            #     div.unified-horizontal-clear-container [data-testid="stBaseButton-secondary"] button span {
            #         color: #E8471E !important;
            #         font-size: 13px !important;
            #         font-weight: 700 !important;
            #         line-height: 40px !important;
            #         margin: 0px !important;
            #         padding: 0px !important;
            #     }
                
            #     /* Darker color accent transition on mouse hover */
            #     div.unified-horizontal-clear-container [data-testid="stBaseButton-secondary"] button:hover p {
            #         color: #CD3713 !important;
            #     }
            # </style>
            # <div class="unified-horizontal-clear-container">
            # """, unsafe_allow_html=True)

            # # Native full-width clear action button
            # trigger_map_clear = st.button("🧹 Clear Pins from Map Layout", use_container_width=True, key="canvas_bottom_clear_btn")

            # st.markdown("</div>", unsafe_allow_html=True)

            # # Process state scrubbing immediately inside the active server loop
            # if trigger_map_clear:
            #     s.map_rest_lat, s.map_rest_lon, s.rest_search_text = None, None, "Not Selected"
            #     s.map_del_lat, s.map_del_lon, s.del_search_text = None, None, "Not Selected"
            #     s.click_count = 0
            #     s.rest_key_version += 1 
            #     s.del_key_version += 1  
            #     st.rerun()

            # # ─── 4. MAP CLICK ACTION DISPATCHER & LOGIC ENGINE ────────────────────
            # if map_result and map_result.get("last_clicked"):
            #     click_lat = round(map_result["last_clicked"]["lat"], 6)
            #     click_lon = round(map_result["last_clicked"]["lng"], 6)
            #     click_sig = f"{click_lat}_{click_lon}"
                
            #     if "processed_click_id" not in s: 
            #         s.processed_click_id = ""
                    
            #     if click_sig != s.processed_click_id:
            #         s.processed_click_id = click_sig
                    
            #         # try:
            #         #     location_obj = geolocator.reverse((click_lat, click_lon), timeout=3)
            #         #     if location_obj and getattr(location_obj, "address", None):
            #         #         address_parts = [p.strip() for p in location_obj.address.split(",") if p.strip()]
            #         #         place_display_name = f"{address_parts[0]}, {address_parts[1]}" if len(address_parts) >= 2 else address_parts[0]
            #         #     else:
            #         #         place_display_name = f"{click_lat:.4f}, {click_lon:.4f}"
            #         # except Exception:
            #         #     place_display_name = f"{click_lat:.4f}, {click_lon:.4f}"

            #         #                     # ─── REVERSE GEOCODING ENGINE ADDRESS STRING REPAIR ───
            #         # try:
            #         #     location_obj = geolocator.reverse((click_lat, click_lon), timeout=3)
            #         #     if location_obj and getattr(location_obj, "address", None):
            #         #         address_parts = [p.strip() for p in location_obj.address.split(",") if p.strip()]
            #         #         # FIX: Combined with a safe join to prevent array list multiplication strings
            #         #         place_display_name = ", ".join(address_parts[:2]) if len(address_parts) >= 2 else address_parts[0]
            #         #     else:
            #         #         place_display_name = f"{click_lat:.4f}, {click_lon:.4f}"
            #         # except Exception:
            #         #     place_display_name = f"{click_lat:.4f}, {click_lon:.4f}"

            #                             # ─── REVERSE GEOCODING ENGINE ADDRESS STRING REPAIR ───
            #         try:
            #             location_obj = geolocator.reverse((click_lat, click_lon), timeout=3)
            #             if location_obj and getattr(location_obj, "address", None):
            #                 address_parts = [p.strip() for p in location_obj.address.split(",") if p.strip()]
            #                 # Combines the top address fragments natively with clean string separators
            #                 place_display_name = ", ".join(address_parts[:2]) if len(address_parts) >= 2 else address_parts[0]
            #             else:
            #                 place_display_name = f"{click_lat:.4f}, {click_lon:.4f}"
            #         except Exception:
            #             place_display_name = f"{click_lat:.4f}, {click_lon:.4f}"


                    
            #         # Core Click Routing Alternator
            #         if s.click_count == 0 or s.click_count >= 2:
            #             s.map_rest_lat, s.map_rest_lon = click_lat, click_lon
            #             s.rest_search_text = place_display_name
                        
            #             s.map_del_lat, s.map_del_lon = None, None  # Wipe destination to force second drop context
            #             s.del_search_text = "Not Selected"
            #             s.click_count = 1
            #             s.rest_key_version += 1 # Force clear search box text cache
            #         else:
            #             s.map_del_lat, s.map_del_lon = click_lat, click_lon
            #             s.del_search_text = place_display_name
            #             s.click_count = 2
            #             s.del_key_version += 1  # Force clear search box text cache
                        
            #         st.rerun()

            # # ─── 5. DISTANCE EVALUATION CALCULATOR FOOTER ─────────────────────────
            # if s.map_rest_lat is not None and s.map_del_lat is not None:
            #     dist = haversine(s.map_rest_lat, s.map_rest_lon, s.map_del_lat, s.map_del_lon)
            # else:
            #     dist = 0.00

            # st.markdown(f"""
            # <div class="dist-pill" style="display:flex; align-items:center; justify-content:space-between; background:#F0FDF4; border:1px solid #BBF7D0; border-radius:10px; padding:12px 16px; margin-top:16px; margin-bottom:12px;">
            #   <span style="font-size:13px; font-weight:700; color:#16A34A;">📐 Calculated Route Distance</span>
            #   <span><span style="font-family:'Bricolage Grotesque',sans-serif; font-size:18px; font-weight:800; color:#15803D;">{dist:.2f}</span> <span style="font-size:12px; font-weight:700; color:#16A34A;">km</span></span>
            # </div>
            # """, unsafe_allow_html=True)


            # # ─── EXTRACTION & LAYOUT ENGINE (ABSOLUTE MEMORY ISOLATION) ───
            # # Calculate route midpoint for absolute centering fallbacks
            # clat = (float(s.rest_lat) + float(s.del_lat)) / 2
            # clon = (float(s.rest_lon) + float(s.del_lon)) / 2
            
            # # Map object initialization with modern, minimal CartoDB tiles
            # # Options: 'CartoDB positron' (Sleek Light) or 'CartoDB dark_matter' (Sleek Dark)
            # m = folium.Map(
            #     location=[clat, clon], 
            #     zoom_start=12,
            #     tiles='CartoDB positron', # Clean luxury backdrop
            #     attr='&copy; <a href="https://openstreetmap.org">OpenStreetMap</a> contributors &copy; <a href="https://carto.com">CARTO</a>'
            # )
            
            # # Add dynamic premium map pins matching your food-tech color scheme
            # folium.Marker(
            #     [float(s.rest_lat), float(s.rest_lon)], 
            #     tooltip="🍽️ Restaurant Hub", 
            #     icon=folium.Icon(color='blue', icon='cutlery', prefix='fa')
            # ).add_to(m)
            
            # folium.Marker(
            #     [float(s.del_lat), float(s.del_lon)], 
            #     tooltip="📦 Delivery Target Point", 
            #     icon=folium.Icon(color='red', icon='map-marker', prefix='fa') # Switched to clear high-contrast red
            # ).add_to(m)
            
            # # Draw a modern, precise route line vector between points
            # folium.PolyLine(
            #     [[float(s.rest_lat), float(s.rest_lon)], [float(s.del_lat), float(s.del_lon)]], 
            #     color='#FF4B4B', # Vivid primary color to stand out on the muted map canvas
            #     weight=4, 
            #     opacity=0.9, 
            #     dash_array='6 4'
            # ).add_to(m)
            
            # # CRITICAL STATE ENGINE FIX: Dynamic key format forces an absolute component instance refresh 
            # # whenever a user switches between map pinning and text search modes.
            # map_instance_key = f"map_canvas_state_{getattr(s, 'rest_map_active', False)}_{getattr(s, 'del_map_active', False)}"
            
            # map_result = st_folium(
            #     m, 
            #     center=[clat, clon], 
            #     width="100%", 
            #     height=360, 
            #     key=map_instance_key
            # )
            
            # # Handle user map-click interactions cleanly
            # if map_result and map_result.get("last_clicked"):
            #     click_lat = round(map_result["last_clicked"]["lat"], 6)
            #     click_lon = round(map_result["last_clicked"]["lng"], 6)
            #     click_sig = f"{click_lat}_{click_lon}"
                
            #     if "processed_click_id" not in s: 
            #         s.processed_click_id = ""
                    
            #     # Verify that this is an intentional, new user click event
            #     if click_sig != s.processed_click_id:
            #         s.processed_click_id = click_sig
                    
            #         # ─── REVERSE GEOCODING ENGINE ───
            #         try:
            #             location_obj = geolocator.reverse((click_lat, click_lon), timeout=3)
            #             if location_obj and getattr(location_obj, "address", None):
            #                 address_parts = [part.strip() for part in location_obj.address.split(",") if part.strip()]
            #                 if len(address_parts) >= 2:
            #                     place_display_name = f"{address_parts[0]}, {address_parts[1]}"
            #                 elif len(address_parts) == 1:
            #                     place_display_name = f"{address_parts[0]}"
            #                 else:
            #                     place_display_name = f"Coordinates: {click_lat:.4f}, {click_lon:.4f}"
            #             else:
            #                 place_display_name = f"Coordinates: {click_lat:.4f}, {click_lon:.4f}"
            #         except Exception:
            #             place_display_name = f"Coordinates: {click_lat:.4f}, {click_lon:.4f}"
                    
            #         # Update coordinates and active layout view states instantly
            #         if s.pin_mode == "restaurant":
            #             s.rest_lat, s.rest_lon = click_lat, click_lon
            #             s.rest_search_text = place_display_name
            #             s.rest_map_active = True  
            #             st.toast(f"Hub updated to {place_display_name}!", icon="🔵")
            #         else:
            #             s.del_lat, s.del_lon = click_lat, click_lon
            #             s.del_search_text = place_display_name
            #             s.del_map_active = True  
            #             st.toast(f"Destination updated to {place_display_name}!", icon="🟠")
                    
            #         st.rerun()

            
            # dist = haversine(s.rest_lat, s.rest_lon, s.del_lat, s.del_lon)
            # # st.markdown(f"""
            # # <div class="dist-pill" style="display:flex; align-items:center; justify-content:space-between; background:#F0FDF4; border:1px solid #BBF7D0; border-radius:10px; padding:12px 16px; margin-top:16px;">
            # #   <span style="font-size:13px; font-weight:700; color:#16A34A;">📐 Calculated Route Distance</span>
            # #   <span><span style="font-family:'Bricolage Grotesque',sans-serif; font-size:18px; font-weight:800; color:#15803D;">{dist:.2f}</span> <span style="font-size:12px; font-weight:700; color:#16A34A;">km</span></span>
            # # </div>
            # # """, unsafe_allow_html=True)
            # st.markdown(f"""
            # <div class="dist-pill" style="display:flex; align-items:center; justify-content:space-between; background:#F0FDF4; border:1px solid #BBF7D0; border-radius:10px; padding:12px 16px; margin-top:16px; margin-bottom:12px;">
            #   <span style="font-size:13px; font-weight:700; color:#16A34A;">📐 Calculated Route Distance</span>
            #   <span><span style="font-family:'Bricolage Grotesque',sans-serif; font-size:18px; font-weight:800; color:#15803D;">{dist:.2f}</span> <span style="font-size:12px; font-weight:700; color:#16A34A;">km</span></span>
            # </div>
            # """, unsafe_allow_html=True)

        # # Advanced options panel
        # st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)
        # with st.expander("🛠️ Advanced Coordinate Details (ML Core Features)"):
        #     cr1, cr2 = st.columns(2)
        #     with cr1: st.number_input("Restaurant Latitude", format="%.6f", key="rest_lat")
        #     with cr2: st.number_input("Restaurant Longitude", format="%.6f", key="rest_lon")
        #     cd1, cd2 = st.columns(2)
        #     with cd1: st.number_input("Delivery Latitude", format="%.6f", key="del_lat")
        #     with cd2: st.number_input("Delivery Longitude", format="%.6f", key="del_lon")

        # st.markdown('<div style="height:14px"></div>', unsafe_allow_html=True)
        # if st.button("Continue to Conditions →", use_container_width=True, key="step1_next"):
        #     s.step = 2
        #     st.rerun()

        # # Advanced options panel
        # st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)
        # with st.expander("🛠️ Advanced Coordinate Details (ML Core Features)"):
        #     st.markdown("""
        #         <style>
        #         div[data-testid="stExpander"] div[data-testid="stMarkdownContainer"] label {
        #             font-size: 11px !important;
        #             font-weight: 700 !important;
        #             color: var(--ink3) !important;
        #             text-transform: uppercase !important;
        #             letter-spacing: 0.5px !important;
        #             margin-bottom: 4px !important;
        #         }
        #         </style>
        #     """, unsafe_allow_html=True)

            # cr1, cr2 = st.columns(2)
            # # with cr1: st.number_input("Restaurant Latitude", format="%.6f", value=float(s.rest_lat), key="rest_lat")
            # # Apply the same logic to the Restaurant latitude block
            # with cr1:
            #     st.number_input(
            #         "Restaurant Latitude", 
            #         format="%.6f", 
            #         value=float(s.rest_lat) if s.rest_lat is not None else 28.6304, 
            #         key="rest_lat"
            #     )

            # with cr2: st.number_input("Restaurant Longitude", format="%.6f", value=float(s.rest_lon), key="rest_lon")
            # cd1, cd2 = st.columns(2)
            # # with cd1: st.number_input("Delivery Latitude", format="%.6f", value=float(s.del_lat), key="del_lat")
            # # --- SAFE MANUAL OVERRIDE COORDINATE FIELDS ---
            # # Evaluates safe numerical defaults if session pins are set to None
            # with cd1: 
            #     st.number_input(
            #         "Delivery Latitude", 
            #         format="%.6f", 
            #         value=float(s.del_lat) if s.del_lat is not None else 28.6139, 
            #         key="del_lat"
            #     )

            # with cd2: st.number_input("Delivery Longitude", format="%.6f", value=float(s.del_lon), key="del_lon")

            # Update manual overrides to mirror the standalone variables
            # cr1, cr2 = st.columns(2)
            # with cr1:
            #     st.number_input("Restaurant Latitude", format="%.6f", value=float(s.map_rest_lat) if s.map_rest_lat is not None else 28.6304, key="rest_lat")
            # with cr2:
            #     st.number_input("Restaurant Longitude", format="%.6f", value=float(s.map_rest_lon) if s.map_rest_lon is not None else 77.2177, key="rest_lon")

            # cd1, cd2 = st.columns(2)
            # with cd1:
            #     st.number_input("Delivery Latitude", format="%.6f", value=float(s.map_del_lat) if s.map_del_lat is not None else 28.6139, key="del_lat")
            # with cd2:
            #     st.number_input("Delivery Longitude", format="%.6f", value=float(s.map_del_lon) if s.map_del_lon is not None else 77.2090, key="del_lon")

            # # --- SAFE MANUAL OVERRIDE COORDINATE FIELDS ---
            # cr1, cr2 = st.columns(2)
            
            # # Restaurant Coordinates
            # with cr1:
            #     st.number_input(
            #         "Restaurant Latitude", 
            #         format="%.6f", 
            #         value=float(s.rest_lat) if s.rest_lat is not None else 28.6304, 
            #         key="rest_lat"
            #     )
            # with cr2: 
            #     st.number_input(
            #         "Restaurant Longitude", 
            #         format="%.6f", 
            #         value=float(s.rest_lon) if s.rest_lon is not None else 77.2177, 
            #         key="rest_lon"
            #     )

            # cd1, cd2 = st.columns(2)
            
            # # Delivery Coordinates
            # with cd1: 
            #     st.number_input(
            #         "Delivery Latitude", 
            #         format="%.6f", 
            #         value=float(s.del_lat) if s.del_lat is not None else 28.6139, 
            #         key="del_lat"
            #     )
            # with cd2: 
            #     st.number_input(
            #         "Delivery Longitude", 
            #         format="%.6f", 
            #         value=float(s.del_lon) if s.del_lon is not None else 77.2090, 
            #         key="del_lon"
            #     )


        # # FIX: The navigation action buttons must sit outside all card containers to render correctly
        # st.markdown('<div style="height:20px;"></div>', unsafe_allow_html=True)
        # if st.button("Continue to Conditions →", use_container_width=True, type="primary", key="step1_next"):
        #     s.step = 2
        #     st.rerun()

        # # ── PURE INLINE ALIGNMENT ENGINE (ZEROOVERHEAD) ───────────────────────
        # # This global block isolates your primary button style structure 
        # # and forces its alignment position flush against the right margin.
        # st.html("""
        # <style>
        # /* Force the button wrapper element container to push fully to the right */
        # div[data-testid="stVerticalBlock"] > div:has(button[key="step1_next"]) {
        #     display: flex !important;
        #     justify-content: flex-end !important;
        #     width: 100% !important;
        #     margin-top: -5px !important; /* Pulls the button slightly higher */
        # }
        
        # /* Ensure the button maintains its native shape and does not stretch */
        # button[key="step1_next"] {
        #     width: auto !important;
        #     min-width: max-content !important;
        #     white-space: nowrap !important;
        # }
        # </style>
        # """)

        # # # Pure native button definition—completely decoupled from structural column splits
        # # if st.button("Continue to Conditions →", use_container_width=False, type="primary", key="step1_next"):
        # #     s.step = 2
        # #     st.rerun()

        # # ── PURE NATIVE GRID ALIGNMENT ENGINE ─────────────────────────────────
        # # Using an explicit, wide column distribution to provide exact layout room
        # nav_spacer_col, nav_btn_col = st.columns([4.2, 1.8])
        
        # with nav_btn_col:
        #     # We wrap the native button in a tiny HTML block to pull its layout slightly higher
        #     st.html("<div style='margin-top: -12px;'></div>")
            
        #     # Setting use_container_width=False lets it size down tightly to the exact width of the text on one line
        #     if st.button("Continue to Conditions →", use_container_width=False, type="primary", key="step1_next"):
        #         s.step = 2
        #         st.rerun()

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



        #         # Navigation container structural spacing
        # st.markdown('<div style="height:15px;"></div>', unsafe_allow_html=True)
        
        # # ── ABSOLUTE TARGETED KEYED CONTAINER ISOLATION ENGINE ─────────────
        # st.markdown("""
        # <style>
        # /* Target the native container that explicitly wraps our keyed navigation block */
        # div[data-element-type="container"]:has(button[key="step1_next"]) {
        #     border: none !important;
        #     padding: 0 !important;
        #     background: transparent !important;
        #     display: flex !important;
        #     justify-content: flex-end !important;
        #     width: 100% !important;
        # }

        # /* Force direct layout, single-line text formatting, and branding red onto this button */
        # div[data-element-type="container"]:has(button[key="step1_next"]) button[data-testid*="BaseButton"] {
        #     background-color: #FF4B4B !important;
        #     color: white !important;
        #     font-family: 'Source Sans Pro', -apple-system, sans-serif !important;
        #     font-size: 14px !important;
        #     font-weight: 600 !important;
        #     padding: 10px 24px !important;
        #     border-radius: 8px !important;
        #     border: none !important;
        #     white-space: nowrap !important;
        #     word-break: keep-all !important;
        #     width: auto !important;
        #     min-width: max-content !important;
        #     display: inline-flex !important;
        #     align-items: center !important;
        #     justify-content: center !important;
        #     transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        #     box-shadow: 0 2px 5px rgba(255, 75, 75, 0.15) !important;
        # }
        
        # /* Premium hover glow interaction isolated strictly to this block path */
        # div[data-element-type="container"]:has(button[key="step1_next"]) button[data-testid*="BaseButton"]:hover {
        #     background-color: #FF3333 !important;
        #     box-shadow: 0 0 14px rgba(255, 75, 75, 0.5) !important;
        #     transform: translateY(-1px) !important;
        # }

        # div[data-element-type="container"]:has(button[key="step1_next"]) button[data-testid*="BaseButton"]:active {
        #     transform: translateY(1px) !important;
        # }
        # </style>
        # """, unsafe_allow_html=True)

        # # 1. Native columns grid push alignment strategy
        # _, nav_btn_col = st.columns([3.2, 1.8])
        
        # with nav_btn_col:
        #     # 2. Putting it inside a keyed container allows the CSS engine to locate it perfectly 
        #     with st.container(border=False):
        #         if st.button("Continue to Conditions →", key="step1_next", use_container_width=True, type="secondary"):
        #             s.step = 2
        #             st.rerun()



        # Ensure the key ends with '_next' to turn it red and prevent layout swelling
        # if st.button("Continue to Conditions →", use_container_width=True, key="step1_next"):
        #     s.step = 2
        #     st.rerun()


    # # ── STEP 2: CONDITIONS ───────────────────
    # elif s.step == 2:
    #     st.markdown("""
    #     <div class="section-title">🌤️ What's the situation outside?</div>
    #     <div class="section-sub">Real-world conditions heavily influence delivery time. Pick what applies right now.</div>
    #     """, unsafe_allow_html=True)

    #     # WEATHER card
    #     st.markdown("""
    #     <div class="fcard">
    #       <div class="fcard-head">
    #         <div class="fcard-icon" style="background:#FFF0E3;">🌦️</div>
    #         <div>
    #           <div class="fcard-title">Weather Conditions</div>
    #           <div class="fcard-desc">Current weather at time of order</div>
    #         </div>
    #       </div>
    #       <div class="fcard-body">
    #     """, unsafe_allow_html=True)

    #     weather_opts = [
    #         ("☀️","Sunny","Clear skies"),
    #         ("☁️","Cloudy","Overcast"),
    #         ("🌫️","Fog","Low visibility"),
    #         ("💨","Windy","Strong gusts"),
    #         ("⛈️","Stormy","Rain & thunder"),
    #         ("🌪️","Sandstorms","Dust/sand"),
    #     ]
    #     w_cols = st.columns(6)
    #     for i,(icon,label,sub) in enumerate(weather_opts):
    #         sel = "selected" if s.weather==label else ""
    #         with w_cols[i]:
    #             st.markdown(f"""
    #             <div class="opt-card {sel}" style="min-height:80px">
    #               <div class="opt-card-icon">{icon}</div>
    #               <div class="opt-card-label">{label}</div>
    #             </div>
    #             """, unsafe_allow_html=True)
    #             if st.button(label, key=f"w_{label}", use_container_width=True,
    #                          help=sub):
    #                 s.weather = label
    #                 st.rerun()

    #     st.markdown('</div></div>', unsafe_allow_html=True)

    #     # TRAFFIC card
    #     st.markdown("""
    #     <div class="fcard">
    #       <div class="fcard-head">
    #         <div class="fcard-icon" style="background:#FEF2F2;">🚦</div>
    #         <div>
    #           <div class="fcard-title">Road Traffic Density</div>
    #           <div class="fcard-desc">Current traffic on the likely route</div>
    #         </div>
    #       </div>
    #       <div class="fcard-body">
    #     """, unsafe_allow_html=True)

    #     traffic_opts = [
    #         ("🟢","Low","Open roads, smooth flow"),
    #         ("🟡","Medium","Moderate traffic"),
    #         ("🟠","High","Heavy congestion"),
    #         ("🔴","Jam","Gridlock / standstill"),
    #     ]
    #     t_cols = st.columns(4)
    #     for i,(dot,label,desc) in enumerate(traffic_opts):
    #         sel = "selected" if s.traffic==label else ""
    #         with t_cols[i]:
    #             st.markdown(f"""
    #             <div class="opt-card {sel}">
    #               <div class="opt-card-icon">{dot}</div>
    #               <div class="opt-card-label">{label}</div>
    #               <div class="opt-card-sub">{desc}</div>
    #             </div>
    #             """, unsafe_allow_html=True)
    #             if st.button(label, key=f"t_{label}", use_container_width=True):
    #                 s.traffic = label
    #                 st.rerun()

    #     st.markdown('</div></div>', unsafe_allow_html=True)

    #     # CITY + FESTIVAL card
    #     st.markdown("""
    #     <div class="fcard">
    #       <div class="fcard-head">
    #         <div class="fcard-icon" style="background:#F0FDF4;">🏙️</div>
    #         <div>
    #           <div class="fcard-title">City Type &amp; Festival Period</div>
    #           <div class="fcard-desc">Urban density and special-event flags</div>
    #         </div>
    #       </div>
    #       <div class="fcard-body">
    #     """, unsafe_allow_html=True)

    #     st.markdown('<div style="font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:1.5px;color:var(--ink4);margin-bottom:8px">City Type</div>', unsafe_allow_html=True)
    #     city_opts=[("🏙️","Metropolitian","Major metro city"),("🏘️","Urban","Mid-size city"),("🌾","Semi-Urban","Small town/suburb")]
    #     c_cols=st.columns(3)
    #     for i,(icon,label,desc) in enumerate(city_opts):
    #         sel="selected" if s.city==label else ""
    #         with c_cols[i]:
    #             st.markdown(f'<div class="opt-card {sel}"><div class="opt-card-icon">{icon}</div><div class="opt-card-label">{label}</div><div class="opt-card-sub">{desc}</div></div>',unsafe_allow_html=True)
    #             if st.button(label,key=f"c_{label}",use_container_width=True): s.city=label; st.rerun()

    #     st.markdown('<div style="font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:1.5px;color:var(--ink4);margin:14px 0 8px">Festival / Special Event?</div>', unsafe_allow_html=True)
    #     f_cols=st.columns(2)
    #     fest_opts=[("🔘","No","Normal day"),("🎉","Yes","Festival/holiday — extra busy!")]
    #     for i,(icon,label,desc) in enumerate(fest_opts):
    #         sel="selected" if s.festival==label else ""
    #         with f_cols[i]:
    #             st.markdown(f'<div class="opt-card {sel}"><div class="opt-card-icon">{icon}</div><div class="opt-card-label">{desc}</div></div>',unsafe_allow_html=True)
    #             if st.button(label,key=f"f_{label}",use_container_width=True): s.festival=label; st.rerun()

    #     st.markdown('</div></div>', unsafe_allow_html=True)

    #     nav1,nav2 = st.columns(2)
    #     with nav1:
    #         if st.button("← Back to Location", use_container_width=True, key="s2_back"): s.step=1; st.rerun()
    #     with nav2:
    #         if st.button("Continue to Driver & Vehicle →", use_container_width=True, key="s2_next"): s.step=3; st.rerun()

# # ─── STEP 2: CONDITIONS ───────────────────
#     elif s.step == 2:
#         st.markdown("""
#         <div style="margin-top: 14px; margin-bottom: 24px;">
#             <div class="section-title" style="font-family:'Bricolage Grotesque',sans-serif; font-size:24px; font-weight:800; color:var(--ink); margin-bottom:4px;">🌤️ What's the situation outside?</div>
#             <div class="section-sub" style="font-size:13px; color:var(--ink3); line-height:1.5;">Real-world conditions heavily influence delivery time. Pick what applies right now.</div>
#         </div>
#         """, unsafe_allow_html=True)

#         # ─── WEATHER SECTION ───
#         st.markdown("""
#         <div class="fcard" style="margin-bottom:20px;">
#           <div class="fcard-head" style="display:flex; align-items:center; gap:10px; border-bottom: 1px solid #EDE8E3; padding-bottom:12px; margin-bottom:16px;">
#             <div class="fcard-icon" style="background:#FFF0E3; padding:4px 8px; border-radius:6px;">🌦️</div>
#             <div>
#               <div class="fcard-title" style="font-family:'Bricolage Grotesque',sans-serif; font-size:14px; font-weight:700;">Weather Conditions</div>
#               <div class="fcard-desc" style="font-size:11px; color:var(--ink4);">Current weather at time of order</div>
#             </div>
#           </div>
#         """, unsafe_allow_html=True)

#         weather_opts = [
#             ("☀️","Sunny","Clear skies"),
#             ("☁️","Cloudy","Overcast"),
#             ("🌫️","Fog","Low visibility"),
#             ("💨","Windy","Strong gusts"),
#             ("⛈️","Stormy","Rain & thunder"),
#             ("🌪️","Sandstorms","Dust/sand"),
#         ]
#         w_cols = st.columns(6)
#         for i,(icon,label,sub) in enumerate(weather_opts):
#             sel = "selected" if s.weather==label else ""
#             with w_cols[i]:
#                 st.markdown(f"""
#                 <div class="opt-card {sel}" style="padding:16px 8px; text-align:center; border:1px solid #EDE8E3; border-radius:10px; min-height:92px;">
#                   <div class="opt-card-icon" style="font-size:22px; margin-bottom:6px;">{icon}</div>
#                   <div class="opt-card-label">{label}</div>
#                 </div>
#                 """, unsafe_allow_html=True)
#                 # The transparent native button captures the click event over the whole card area
#                 if st.button(label, key=f"w_{label}", use_container_width=True):
#                     s.weather = label
#                     st.rerun()
#         st.markdown('</div>', unsafe_allow_html=True)

#         # ─── TRAFFIC SECTION ───
#         st.markdown("""
#         <div class="fcard" style="margin-bottom:20px;">
#           <div class="fcard-head" style="display:flex; align-items:center; gap:10px; border-bottom: 1px solid #EDE8E3; padding-bottom:12px; margin-bottom:16px;">
#             <div class="fcard-icon" style="background:#FEF2F2; padding:4px 8px; border-radius:6px;">🚦</div>
#             <div>
#               <div class="fcard-title" style="font-family:'Bricolage Grotesque',sans-serif; font-size:14px; font-weight:700;">Road Traffic Density</div>
#               <div class="fcard-desc" style="font-size:11px; color:var(--ink4);">Current traffic on the likely route</div>
#             </div>
#           </div>
#         """, unsafe_allow_html=True)

#         traffic_opts = [
#             ("🟢","Low","Open roads, smooth flow"),
#             ("🟡","Medium","Moderate traffic"),
#             ("🟠","High","Heavy congestion"),
#             ("🔴","Jam","Gridlock / standstill"),
#         ]
#         t_cols = st.columns(4)
#         for i,(dot,label,desc) in enumerate(traffic_opts):
#             sel = "selected" if s.traffic==label else ""
#             with t_cols[i]:
#                 st.markdown(f"""
#                 <div class="opt-card {sel}" style="padding:14px; text-align:center; border:1px solid #EDE8E3; border-radius:10px; min-height:102px;">
#                   <div class="opt-card-icon" style="font-size:20px; margin-bottom:4px;">{dot}</div>
#                   <div class="opt-card-label" style="margin-bottom:2px;">{label}</div>
#                   <div class="opt-card-sub" style="font-size:10px; color:var(--ink3); line-height:1.2;">{desc}</div>
#                 </div>
#                 """, unsafe_allow_html=True)
#                 if st.button(label, key=f"t_{label}", use_container_width=True):
#                     s.traffic = label
#                     st.rerun()
#         st.markdown('</div>', unsafe_allow_html=True)

#         # ─── CITY + FESTIVAL SECTION ───
#         st.markdown("""
#         <div class="fcard" style="margin-bottom:28px;">
#           <div class="fcard-head" style="display:flex; align-items:center; gap:10px; border-bottom: 1px solid #EDE8E3; padding-bottom:12px; margin-bottom:16px;">
#             <div class="fcard-icon" style="background:#F0FDF4; padding:4px 8px; border-radius:6px;">🏙️</div>
#             <div>
#               <div class="fcard-title" style="font-family:'Bricolage Grotesque',sans-serif; font-size:14px; font-weight:700;">City Type &amp; Festival Period</div>
#               <div class="fcard-desc" style="font-size:11px; color:var(--ink4);">Urban density and special-event flags</div>
#             </div>
#           </div>
#         """, unsafe_allow_html=True)

#         st.markdown('<div style="font-size:11px; font-weight:800; text-transform:uppercase; letter-spacing:1.2px; color:var(--ink3); margin-bottom:10px;">City Type</div>', unsafe_allow_html=True)
#         city_opts=[("🏙️","Metropolitan","Major metro city"),("🏘️","Urban","Mid-size city"),("🌾","Semi-Urban","Small town/suburb")]
#         c_cols=st.columns(3)
#         for i,(icon,label,desc) in enumerate(city_opts):
#             sel="selected" if s.city==label else ""
#             with c_cols[i]:
#                 st.markdown(f"""
#                 <div class="opt-card {sel}" style="padding:14px; text-align:center; border:1px solid #EDE8E3; border-radius:10px; min-height:102px;">
#                     <div class="opt-card-icon" style="font-size:20px; margin-bottom:4px;">{icon}</div>
#                     <div class="opt-card-label" style="margin-bottom:2px;">{label}</div>
#                     <div class="opt-card-sub" style="font-size:10px; color:var(--ink3); line-height:1.2;">{desc}</div>
#                 </div>
#                 """, unsafe_allow_html=True)
#                 if st.button(label, key=f"c_{label}", use_container_width=True): 
#                     s.city=label
#                     st.rerun()

#         st.markdown('<div style="font-size:11px; font-weight:800; text-transform:uppercase; letter-spacing:1.2px; color:var(--ink3); margin:20px 0 10px;">Festival / Special Event?</div>', unsafe_allow_html=True)
#         f_cols=st.columns(2)
#         fest_opts=[("🔘","No","Normal day"),("🎉","Yes","Festival/holiday — extra busy!")]
#         for i,(icon,label,desc) in enumerate(fest_opts):
#             sel="selected" if s.festival==label else ""
#             with f_cols[i]:
#                 st.markdown(f"""
#                 <div class="opt-card {sel}" style="padding:16px 14px; text-align:center; border:1px solid #EDE8E3; border-radius:10px; min-height:76px; display:flex; align-items:center; justify-content:center; gap:12px;">
#                     <div class="opt-card-icon" style="font-size:22px;">{icon}</div>
#                     <div style="text-align:left;">
#                         <div class="opt-card-label">{label}</div>
#                         <div style="font-size:10px; color:var(--ink3); margin-top:1px;">{desc}</div>
#                     </div>
#                 </div>
#                 """, unsafe_allow_html=True)
#                 if st.button(label, key=f"f_{label}", use_container_width=True): 
#                     s.festival=label
#                     st.rerun()
#         st.markdown('</div>', unsafe_allow_html=True)

# # ─── STEP 2: CONDITIONS (FIXED ENCLOSURES & ZERO HOVER TOOLTIPS) ─────────
#     elif s.step == 2:
#         st.markdown("""
#         <div style="margin-top: 14px; margin-bottom: 24px;">
#             <div class="section-title">🌤️ What's the situation outside?</div>
#             <div class="section-sub">Real-world conditions heavily influence delivery time. Pick what applies right now.</div>
#         </div>
#         """, unsafe_allow_html=True)

#         # ─── WEATHER SECTION (FIXED: Columns sit inside the card body) ───
#         st.markdown("""
#         <div class="fcard">
#           <div class="fcard-head">
#             <div class="fcard-icon" style="background:#FFF0E3;">🌦️</div>
#             <div>
#               <div class="fcard-title">Weather Conditions</div>
#               <div class="fcard-desc">Current weather at time of order</div>
#             </div>
#           </div>
#           <div class="fcard-body">
#         """, unsafe_allow_html=True)

#         weather_opts = [
#             ("☀️","Sunny","Clear skies"),
#             ("☁️","Cloudy","Overcast"),
#             ("🌫️","Fog","Low visibility"),
#             ("💨","Windy","Strong gusts"),
#             ("⛈️","Stormy","Rain & thunder"),
#             ("🌪️","Sandstorms","Dust/sand"),
#         ]
#         w_cols = st.columns(6)
#         for i,(icon,label,sub) in enumerate(weather_opts):
#             is_active = s.weather == label
#             btn_text = f"{icon} {label}\n{sub}"
            
#             with w_cols[i]:
#                 # Dynamic key toggles state tracking without triggering a hover tooltip box
#                 btn_key = f"w_act_{label}" if is_active else f"w_opt_{label}"
#                 if st.button(btn_text, key=btn_key, use_container_width=True):
#                     s.weather = label
#                     st.rerun()
#         st.markdown('</div></div>', unsafe_allow_html=True)

#         # ─── TRAFFIC SECTION (FIXED: Columns sit inside the card body) ───
#         st.markdown("""
#         <div class="fcard">
#           <div class="fcard-head">
#             <div class="fcard-icon" style="background:#FEF2F2;">🚦</div>
#             <div>
#               <div class="fcard-title">Road Traffic Density</div>
#               <div class="fcard-desc">Current traffic on the likely route</div>
#             </div>
#           </div>
#           <div class="fcard-body">
#         """, unsafe_allow_html=True)

#         traffic_opts = [
#             ("🟢","Low","Open roads, smooth flow"),
#             ("🟡","Medium","Moderate traffic"),
#             ("🟠","High","Heavy congestion"),
#             ("🔴","Jam","Gridlock / standstill"),
#         ]
#         t_cols = st.columns(4)
#         for i,(dot,label,desc) in enumerate(traffic_opts):
#             is_active = s.traffic == label
#             btn_text = f"{dot} {label}\n{desc}"
            
#             with t_cols[i]:
#                 btn_key = f"t_act_{label}" if is_active else f"t_opt_{label}"
#                 if st.button(btn_text, key=btn_key, use_container_width=True):
#                     s.traffic = label
#                     st.rerun()
#         st.markdown('</div></div>', unsafe_allow_html=True)

#         # ─── CITY + FESTIVAL SECTION (FIXED: Columns sit inside the card body) ───
#         st.markdown("""
#         <div class="fcard">
#           <div class="fcard-head">
#             <div class="fcard-icon" style="background:#F0FDF4;">🏙️</div>
#             <div>
#               <div class="fcard-title">City Type &amp; Festival Period</div>
#               <div class="fcard-desc">Urban density and special-event flags</div>
#             </div>
#           </div>
#           <div class="fcard-body">
#         """, unsafe_allow_html=True)

#         st.markdown('<div class="section-badge-label">City Type</div>', unsafe_allow_html=True)
#         city_opts=[("🏙️","Metropolitan","Major metro city"),("🏘️","Urban","Mid-size city"),("🌾","Semi-Urban","Small town/suburb")]
#         c_cols=st.columns(3)
#         for i,(icon,label,desc) in enumerate(city_opts):
#             is_active = s.city == label
#             btn_text = f"{icon} {label}\n{desc}"
#             with c_cols[i]:
#                 btn_key = f"c_act_{label}" if is_active else f"c_opt_{label}"
#                 if st.button(btn_text, key=btn_key, use_container_width=True): 
#                     s.city=label
#                     st.rerun()

#         st.markdown('<div class="section-badge-label" style="margin-top:20px;">Festival / Special Event?</div>', unsafe_allow_html=True)
#         f_cols=st.columns(2)
#         fest_opts=[("🔘","No","Normal operational day"),("🎉","Yes","Festival/holiday surge")]
#         for i,(icon,label,desc) in enumerate(fest_opts):
#             is_active = s.festival == label
#             btn_text = f"{icon} {label}\n{desc}"
#             with f_cols[i]:
#                 btn_key = f"f_act_{label}" if is_active else f"f_opt_{label}"
#                 if st.button(btn_text, key=btn_key, use_container_width=True): 
#                     s.festival=label
#                     st.rerun()
#         st.markdown('</div></div>', unsafe_allow_html=True)

#         # ─── NAVIGATION PROGRESSION BAR ───
#         nav1, nav2 = st.columns(2)
#         with nav1:
#             if st.button("← Back to Location", use_container_width=True, key="s2_back", type="secondary"): 
#                 s.step=1
#                 st.rerun()
#         with nav2:
#             if st.button("Continue to Driver & Vehicle →", use_container_width=True, key="s2_next", type="primary"): 
#                 s.step=3
#                 st.rerun()

# # ─── STEP 2: CONDITIONS (FIXED ENCLOSURES & SELECTED HIGHLIGHT ENGINE) ───
#     elif s.step == 2:
#         # FIXED: Padding wrapper consistency syncing with Step 1 top padding layouts
#         st.markdown("""
#         <div class="step-header-wrapper" style="padding-top: 4px; margin-bottom: 24px;">
#             <div class="section-title">🌤️ What's the situation outside?</div>
#             <div class="section-sub">Real-world conditions heavily influence delivery time. Pick what applies right now.</div>
#         </div>
#         """, unsafe_allow_html=True)

#         # ─── WEATHER SECTION (FIXED: 2-Row Layout to Avoid Layout Squishing) ───
#         st.markdown("""
#         <div class="fcard">
#           <div class="fcard-head">
#             <div class="fcard-icon" style="background:#FFF0E3;">🌦️</div>
#             <div>
#               <div class="fcard-title">Weather Conditions</div>
#               <div class="fcard-desc">Current weather at time of order</div>
#             </div>
#           </div>
#           <div class="fcard-body">
#         """, unsafe_allow_html=True)

#         weather_opts = [
#             ("☀️","Sunny","Clear skies"),
#             ("☁️","Cloudy","Overcast"),
#             ("🌫️","Fog","Low visibility"),
#             ("💨","Windy","Strong gusts"),
#             ("⛈️","Stormy","Rain & thunder"),
#             ("🌪️","Sandstorms","Dust/sand"),
#         ]
        
#         # FIXED: Splits the 6 options into a grid of 3x2 to prevent cramped layout columns
#         w_row1 = st.columns(3)
#         w_row2 = st.columns(3)
#         all_w_cols = w_row1 + w_row2
        
#         for i, (icon, label, sub) in enumerate(weather_opts):
#             is_active = (s.weather == label)
#             btn_text = f"{icon} {label}\n{sub}"
            
#             with all_w_cols[i]:
#                 # CSS parser uses the precise '_act_' string anchor to apply selected borders
#                 btn_key = f"w_act_{label}" if is_active else f"w_opt_{label}"
#                 if st.button(btn_text, key=btn_key, use_container_width=True):
#                     s.weather = label
#                     st.rerun()
#         st.markdown('</div></div>', unsafe_allow_html=True)

#         # ─── TRAFFIC SECTION ───
#         st.markdown("""
#         <div class="fcard">
#           <div class="fcard-head">
#             <div class="fcard-icon" style="background:#FEF2F2;">🚦</div>
#             <div>
#               <div class="fcard-title">Road Traffic Density</div>
#               <div class="fcard-desc">Current traffic on the likely route</div>
#             </div>
#           </div>
#           <div class="fcard-body">
#         """, unsafe_allow_html=True)

#         traffic_opts = [
#             ("🟢","Low","Open roads, smooth flow"),
#             ("🟡","Medium","Moderate traffic"),
#             ("🟠","High","Heavy congestion"),
#             ("🔴","Jam","Gridlock / standstill"),
#         ]
#         t_cols = st.columns(4)
#         for i, (dot, label, desc) in enumerate(traffic_opts):
#             is_active = (s.traffic == label)
#             btn_text = f"{dot} {label}\n{desc}"
            
#             with t_cols[i]:
#                 btn_key = f"t_act_{label}" if is_active else f"t_opt_{label}"
#                 if st.button(btn_text, key=btn_key, use_container_width=True):
#                     s.traffic = label
#                     st.rerun()
#         st.markdown('</div></div>', unsafe_allow_html=True)

#         # ─── CITY + FESTIVAL SECTION ───
#         st.markdown("""
#         <div class="fcard">
#           <div class="fcard-head">
#             <div class="fcard-icon" style="background:#F0FDF4;">🏙️</div>
#             <div>
#               <div class="fcard-title">City Type &amp; Festival Period</div>
#               <div class="fcard-desc">Urban density and special-event flags</div>
#             </div>
#           </div>
#           <div class="fcard-body">
#         """, unsafe_allow_html=True)

#         st.markdown('<div class="section-badge-label">City Type</div>', unsafe_allow_html=True)
#         city_opts = [
#             ("🏙️","Metropolitan","Major metro city"),
#             ("🏘️","Urban","Mid-size city"),
#             ("🌾","Semi-Urban","Small town/suburb")
#         ]
#         c_cols = st.columns(3)
#         for i, (icon, label, desc) in enumerate(city_opts):
#             is_active = (s.city == label)
#             btn_text = f"{icon} {label}\n{desc}"
#             with c_cols[i]:
#                 btn_key = f"c_act_{label}" if is_active else f"c_opt_{label}"
#                 if st.button(btn_text, key=btn_key, use_container_width=True): 
#                     s.city = label
#                     st.rerun()

#         st.markdown('<div class="section-badge-label" style="margin-top:24px;">Festival / Special Event?</div>', unsafe_allow_html=True)
#         f_cols = st.columns(2)
#         fest_opts = [
#             ("🔘","No","Normal operational day"),
#             ("🎉","Yes","Festival/holiday surge")
#         ]
#         for i, (icon, label, desc) in enumerate(fest_opts):
#             is_active = (s.festival == label)
#             btn_text = f"{icon} {label}\n{desc}"
#             with f_cols[i]:
#                 btn_key = f"f_act_{label}" if is_active else f"f_opt_{label}"
#                 if st.button(btn_text, key=btn_key, use_container_width=True): 
#                     s.festival = label
#                     st.rerun()
#         st.markdown('</div></div>', unsafe_allow_html=True)

#         # ─── NAVIGATION PROGRESSION BAR ───
#         nav1, nav2 = st.columns(2)
#         with nav1:
#             if st.button("← Back to Location", use_container_width=True, key="s2_back", type="secondary"): 
#                 s.step = 1
#                 st.rerun()
#         with nav2:
#             if st.button("Continue to Driver & Vehicle →", use_container_width=True, key="s2_next", type="primary"): 
#                 s.step = 3
#                 st.rerun()

# # ─── STEP 2: CONDITIONS (FIXED ENCLOSURES & MAXIMUM COMPRESSION CODES) ───
#     elif s.step == 2:
#         st.markdown("""
#         <div class="step-header-wrapper" style="padding-top: 4px; margin-bottom: 24px;">
#             <div class="section-title">🌤️ What's the situation outside?</div>
#             <div class="section-sub">Real-world environmental factors heavily influence delivery time prediction.</div>
#         </div>
#         """, unsafe_allow_html=True)

#         # UNIFIED HIGH DENSITY MASTER BLOCK CONTAINER
#         with st.container():
            
#             # ── ROW 1: WEATHER ──
#             st.markdown('<div class="compact-row-title">🌦️ Weather Conditions</div>', unsafe_allow_html=True)
#             weather_opts = [("☀️ Sunny", "Sunny"), ("☁️ Cloudy", "Cloudy"), ("🌫️ Fog", "Fog"), ("💨 Windy", "Windy"), ("⛈️ Stormy", "Stormy"), ("🌪️ Sand", "Sandstorms")]
#             w_cols = st.columns(6)
#             for i, (btn_text, label) in enumerate(weather_opts):
#                 is_active = (s.weather == label)
#                 with w_cols[i]:
#                     btn_key = f"w_act_{label}" if is_active else f"w_opt_{label}"
#                     if st.button(btn_text, key=btn_key, use_container_width=True):
#                         s.weather = label
#                         st.rerun()

#             st.markdown('<div class="compact-row-divider"></div>', unsafe_allow_html=True)

#             # ── ROW 2: TRAFFIC ──
#             st.markdown('<div class="compact-row-title">🚦 Road Traffic Density</div>', unsafe_allow_html=True)
#             traffic_opts = [("🟢 Low", "Low"), ("🟡 Medium", "Medium"), ("🟠 High", "High"), ("🔴 Jam", "Jam")]
#             t_cols = st.columns(4)
#             for i, (btn_text, label) in enumerate(traffic_opts):
#                 is_active = (s.traffic == label)
#                 with t_cols[i]:
#                     btn_key = f"t_act_{label}" if is_active else f"t_opt_{label}"
#                     if st.button(btn_text, key=btn_key, use_container_width=True):
#                         s.traffic = label
#                         st.rerun()

#             st.markdown('<div class="compact-row-divider"></div>', unsafe_allow_html=True)

#             # ── ROW 3: CITY ENVIRONMENT ──
#             st.markdown('<div class="compact-row-title">🏙️ City Type Environment</div>', unsafe_allow_html=True)
#             city_opts = [("🏙️ Metropolitan", "Metropolitan"), ("🏘️ Urban", "Urban"), ("🌾 Semi-Urban", "Semi-Urban")]
#             c_cols = st.columns(3)
#             for i, (btn_text, label) in enumerate(city_opts):
#                 is_active = (s.city == label)
#                 with c_cols[i]:
#                     btn_key = f"c_act_{label}" if is_active else f"c_opt_{label}"
#                     if st.button(btn_text, key=btn_key, use_container_width=True): 
#                         s.city = label
#                         st.rerun()

#             st.markdown('<div class="compact-row-divider"></div>', unsafe_allow_html=True)

#             # ── ROW 4: FESTIVAL SURGES ──
#             st.markdown('<div class="compact-row-title">🎉 Festival / Holiday Period?</div>', unsafe_allow_html=True)
#             fest_opts = [("🔘 No Holiday", "No"), ("🎉 Yes, Holiday Surge", "Yes")]
#             f_cols = st.columns(2)
#             for i, (btn_text, label) in enumerate(fest_opts):
#                 is_active = (s.festival == label)
#                 with f_cols[i]:
#                     btn_key = f"f_act_{label}" if is_active else f"f_opt_{label}"
#                     if st.button(btn_text, key=btn_key, use_container_width=True): 
#                         s.festival = label
#                         st.rerun()

#         # ─── NAVIGATION PROGRESSION ACTIONS ROW ───
#         st.markdown('<div style="margin-top: 24px;"></div>', unsafe_allow_html=True)
#         nav1, nav2 = st.columns(2)
#         with nav1:
#             if st.button("← Back to Location", use_container_width=True, key="s2_back", type="secondary"): 
#                 s.step = 1
#                 st.rerun()
#         with nav2:
#             if st.button("Continue to Driver & Vehicle →", use_container_width=True, key="s2_next", type="primary"): 
#                 s.step = 3
#                 st.rerun()

# # ─── STEP 2: CONDITIONS (FIXED ENCLOSURES & MAXIMUM COMPRESSION CODES) ───
#     elif s.step == 2:
#         st.markdown("""
#         <div class="step-header-wrapper" style="padding-top: 4px; margin-bottom: 24px;">
#             <div class="section-title">🌤️ What's the situation outside?</div>
#             <div class="section-sub">Real-world environmental factors heavily influence delivery time prediction.</div>
#         </div>
#         """, unsafe_allow_html=True)

#         # UNIFIED HIGH DENSITY MASTER BLOCK CONTAINER
#         with st.container():
            
#             # ── ROW 1: WEATHER ──
#             st.markdown('<div class="compact-row-title">🌦️ Weather Conditions</div>', unsafe_allow_html=True)
#             weather_opts = [
#                 ("☀️ Sunny", "Sunny"), ("☁️ Cloudy", "Cloudy"), ("🌫️ Fog", "Fog"), 
#                 ("💨 Windy", "Windy"), ("⛈️ Stormy", "Stormy"), ("🌪️ Sand", "Sandstorms")
#             ]
#             w_cols = st.columns(6, gap="small")
#             for i, (btn_text, label) in enumerate(weather_opts):
#                 is_active = (s.weather == label)
#                 with w_cols[i]:
#                     btn_type = "primary" if is_active else "secondary"
#                     if st.button(btn_text, key=f"w_btn_{label}", type=btn_type, use_container_width=True):
#                         s.weather = label
#                         st.rerun()

#             st.markdown('<div class="compact-row-divider"></div>', unsafe_allow_html=True)

#             # ── ROW 2: TRAFFIC ──
#             st.markdown('<div class="compact-row-title">🚦 Road Traffic Density</div>', unsafe_allow_html=True)
#             traffic_opts = [("🟢 Low", "Low"), ("🟡 Medium", "Medium"), ("🟠 High", "High"), ("🔴 Jam", "Jam")]
#             t_cols = st.columns(4, gap="small")
#             for i, (btn_text, label) in enumerate(traffic_opts):
#                 is_active = (s.traffic == label)
#                 with t_cols[i]:
#                     btn_type = "primary" if is_active else "secondary"
#                     if st.button(btn_text, key=f"t_btn_{label}", type=btn_type, use_container_width=True):
#                         s.traffic = label
#                         st.rerun()

#             st.markdown('<div class="compact-row-divider"></div>', unsafe_allow_html=True)

#             # ── ROW 3: CITY ENVIRONMENT ──
#             st.markdown('<div class="compact-row-title">🏙️ City Type Environment</div>', unsafe_allow_html=True)
#             city_opts = [("🏙️ Metropolitan", "Metropolitan"), ("🏘️ Urban", "Urban"), ("🌾 Semi-Urban", "Semi-Urban")]
#             c_cols = st.columns(3, gap="small")
#             for i, (btn_text, label) in enumerate(city_opts):
#                 is_active = (s.city == label)
#                 with c_cols[i]:
#                     btn_type = "primary" if is_active else "secondary"
#                     if st.button(btn_text, key=f"c_btn_{label}", type=btn_type, use_container_width=True): 
#                         s.city = label
#                         st.rerun()

#             st.markdown('<div class="compact-row-divider"></div>', unsafe_allow_html=True)

#             # ── ROW 4: FESTIVAL SURGES ──
#             st.markdown('<div class="compact-row-title">🎉 Festival / Holiday Period?</div>', unsafe_allow_html=True)
#             fest_opts = [("🔘 No Holiday", "No"), ("🎉 Yes, Holiday Surge", "Yes")]
#             f_cols = st.columns(2, gap="small")
#             for i, (btn_text, label) in enumerate(fest_opts):
#                 is_active = (s.festival == label)
#                 with f_cols[i]:
#                     btn_type = "primary" if is_active else "secondary"
#                     if st.button(btn_text, key=f"f_btn_{label}", type=btn_type, use_container_width=True): 
#                         s.festival = label
#                         st.rerun()

#         # ─── NAVIGATION PROGRESSION ACTIONS ROW ───
#         st.markdown('<div style="margin-top: 24px;"></div>', unsafe_allow_html=True)
#         nav1, nav2 = st.columns(2, gap="medium")
#         with nav1:
#             if st.button("← Back to Location", use_container_width=True, key="s2_back", type="secondary"): 
#                 s.step = 1
#                 st.rerun()
#         with nav2:
#             if st.button("Continue to Driver & Vehicle →", use_container_width=True, key="s2_next", type="primary"): 
#                 s.step = 3
#                 st.rerun()

# ─── STEP 2: CONDITIONS (FIXED ENCLOSURES & MAXIMUM COMPRESSION CODES) ───
    elif s.step == 2:
        # st.markdown("""
        # <div class="step-header-wrapper" style="padding-top: 4px; margin-bottom: 24px;">
        #     <div class="section-title">🌤️ What's the situation outside?</div>
        #     <div class="section-sub">Real-world environmental factors heavily influence delivery time prediction.</div>
        # </div>
        # """, unsafe_allow_html=True)

        # st.markdown("""
        # <div class="section-title">🌤️ What's the situation outside?</div>
        # <div class="section-sub">Real-world environmental factors heavily influence delivery time prediction.</div>
        # """, unsafe_allow_html=True)

        st.markdown("""
        <div class="section-title" style="display: flex; align-items: center; gap: 8px; line-height: 1; margin-top: 4px;">
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
    # elif s.step == 3:
    #     st.markdown("""
    #     <div class="section-title">🏍️ Driver & Vehicle Details</div>
    #     <div class="section-sub">Delivery partner profile and vehicle type affect speed and reliability.</div>
    #     """, unsafe_allow_html=True)

    #     # Vehicle type card
    #     st.markdown("""
    #     <div class="fcard">
    #       <div class="fcard-head">
    #         <div class="fcard-icon" style="background:#FFF0E3;">🚗</div>
    #         <div>
    #           <div class="fcard-title">Vehicle Type</div>
    #           <div class="fcard-desc">What is the delivery partner riding?</div>
    #         </div>
    #       </div>
    #       <div class="fcard-body">
    #     """, unsafe_allow_html=True)

    #     veh_opts=[
    #         ("🏍️","motorcycle","Fastest on city roads"),
    #         ("🛵","scooter","Nimble & efficient"),
    #         ("⚡","electric_scooter","Eco-friendly & steady"),
    #         ("🚲","bicycle","Short-range, slow"),
    #     ]
    #     v_cols=st.columns(4)
    #     for i,(icon,key,desc) in enumerate(veh_opts):
    #         label=key.replace("_"," ").title()
    #         sel="selected" if s.vehicle_type==key else ""
    #         with v_cols[i]:
    #             st.markdown(f'<div class="opt-card {sel}"><div class="opt-card-icon">{icon}</div><div class="opt-card-label">{label}</div><div class="opt-card-sub">{desc}</div></div>',unsafe_allow_html=True)
    #             if st.button(label,key=f"v_{key}",use_container_width=True): s.vehicle_type=key; st.rerun()

    #     st.markdown('</div></div>', unsafe_allow_html=True)

    #     # Vehicle condition + concurrent deliveries
    #     st.markdown("""
    #     <div class="fcard">
    #       <div class="fcard-head">
    #         <div class="fcard-icon" style="background:#F0FDF4;">🔧</div>
    #         <div>
    #           <div class="fcard-title">Vehicle Condition &amp; Concurrent Orders</div>
    #           <div class="fcard-desc">Condition score 0–3 · Number of parallel deliveries</div>
    #         </div>
    #       </div>
    #       <div class="fcard-body">
    #     """, unsafe_allow_html=True)

    #     st.markdown('<div style="font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:1.5px;color:var(--ink4);margin-bottom:8px">Vehicle Condition</div>', unsafe_allow_html=True)
    #     cond_opts=[("💀","0","Poor — needs repair"),("⚠️","1","Fair — functional"),("✅","2","Good — well maintained"),("🏆","3","Excellent — new/premium")]
    #     cond_cols=st.columns(4)
    #     for i,(icon,val,desc) in enumerate(cond_opts):
    #         sel="selected" if s.vehicle_condition==int(val) else ""
    #         with cond_cols[i]:
    #             st.markdown(f'<div class="opt-card {sel}"><div class="opt-card-icon">{icon}</div><div class="opt-card-label">{desc.split(" — ")[0]}</div><div class="opt-card-sub">{desc.split(" — ")[1]}</div></div>',unsafe_allow_html=True)
    #             if st.button(desc.split(" — ")[0],key=f"vc_{val}",use_container_width=True): s.vehicle_condition=int(val); st.rerun()

    #     st.markdown('<div style="font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:1.5px;color:var(--ink4);margin:14px 0 8px">Concurrent Deliveries</div>', unsafe_allow_html=True)
    #     md_opts=[("1️⃣","0","Single order"),("2️⃣","1","2 orders"),("3️⃣","2","3 orders"),("4️⃣","3","4 orders")]
    #     md_cols=st.columns(4)
    #     for i,(icon,val,desc) in enumerate(md_opts):
    #         sel="selected" if s.multiple_deliveries==int(val) else ""
    #         with md_cols[i]:
    #             st.markdown(f'<div class="opt-card {sel}"><div class="opt-card-icon">{icon}</div><div class="opt-card-sub">{desc}</div></div>',unsafe_allow_html=True)
    #             if st.button(desc,key=f"md_{val}",use_container_width=True): s.multiple_deliveries=int(val); st.rerun()

    #     st.markdown('</div></div>', unsafe_allow_html=True)

    #     # Driver profile
    #     st.markdown("""
    #     <div class="fcard">
    #       <div class="fcard-head">
    #         <div class="fcard-icon" style="background:#EFF6FF;">👤</div>
    #         <div>
    #           <div class="fcard-title">Driver Profile</div>
    #           <div class="fcard-desc">Age, rating, and order time</div>
    #         </div>
    #       </div>
    #       <div class="fcard-body">
    #     """, unsafe_allow_html=True)

    #     da_col, dr_col, dt_col = st.columns(3)
    #     with da_col:
    #         s.age = st.number_input("Driver Age", min_value=18, max_value=65, value=int(s.age), step=1)
    #     with dr_col:
    #         s.rating = st.slider("Driver Rating ★", 1.0, 5.0, float(s.rating), 0.1)
    #         r_full=int(s.rating)
    #         st.markdown(f'<div style="font-size:14px;color:#F59E0B;letter-spacing:1px">{"★"*r_full}{"☆"*(5-r_full)} <span style="font-size:12px;font-weight:700;color:var(--ink2)">{s.rating:.1f}</span></div>',unsafe_allow_html=True)
    #     with dt_col:
    #         s.time_ordered = st.text_input("Order Time (HH:MM)", value=str(s.time_ordered), help="24-hr format e.g. 14:30")

    #     st.markdown('</div></div>', unsafe_allow_html=True)

    #     nav3a,nav3b=st.columns(2)
    #     with nav3a:
    #         if st.button("← Back to Conditions",use_container_width=True,key="s3_back"): s.step=2; st.rerun()
    #     with nav3b:
    #         if st.button("Review & Predict →",use_container_width=True,key="s3_next"): s.step=4; st.rerun()

    # ── STEP 3: DRIVER & VEHICLE (CLEAN LAYOUT MATRIX OVERRIDES) ───
    elif s.step == 3:
        st.markdown("""
        <div class="step-header-wrapper" style="padding-top: 4px; margin-bottom: 24px;">
            <div class="section-title">🏍️ Driver & Vehicle Details</div>
            <div class="section-sub">Delivery partner profile and vehicle type affect speed and reliability.</div>
        </div>
        """, unsafe_allow_html=True)

        # ── CONTAINER 1: VEHICLE TYPE ──
        st.markdown("""
        <div class="fcard-head">
            <div class="fcard-icon" style="background:#FFF0E3;">🚗</div>
            <div>
                <div class="fcard-title">Vehicle Type</div>
                <div class="fcard-desc">What is the delivery partner riding?</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.container(border=True): # Uses clean native frames
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
                    btn_type = "primary" if is_active else "secondary"
                    # Pass the multi-line formatting text content straight to the button
                    btn_content = f"{icon}\n{label}\n{desc}"
                    if st.button(btn_content, key=f"v_grid_{key}", type=btn_type, use_container_width=True): 
                        s.vehicle_type = key
                        st.rerun()

        st.markdown('<div style="margin-top: 24px;"></div>', unsafe_allow_html=True)

        # ── CONTAINER 2: VEHICLE CONDITION & ORDERS ──
        st.markdown("""
        <div class="fcard-head">
            <div class="fcard-icon" style="background:#F0FDF4;">🔧</div>
            <div>
                <div class="fcard-title">Vehicle Condition &amp; Concurrent Orders</div>
                <div class="fcard-desc">Condition score 0–3 · Number of parallel deliveries</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

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
                    btn_type = "primary" if is_active else "secondary"
                    btn_content = f"{icon}\n{title}\n{desc}"
                    if st.button(btn_content, key=f"vc_grid_{val}", type=btn_type, use_container_width=True): 
                        s.vehicle_condition = int(val)
                        st.rerun()

            st.markdown('<div class="compact-row-divider"></div>', unsafe_allow_html=True)

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
                    btn_type = "primary" if is_active else "secondary"
                    btn_content = f"{icon}\n{title}"
                    if st.button(btn_content, key=f"md_grid_{val}", type=btn_type, use_container_width=True): 
                        s.multiple_deliveries = int(val)
                        st.rerun()

        st.markdown('<div style="margin-top: 24px;"></div>', unsafe_allow_html=True)

        # # ── CONTAINER 3: DRIVER PROFILE ──
        # st.markdown("""
        # <div class="fcard-head">
        #     <div class="fcard-icon" style="background:#EFF6FF;">👤</div>
        #     <div>
        #         <div class="fcard-title">Driver Profile</div>
        #         <div class="fcard-desc">Age, rating, and order time</div>
        #     </div>
        # </div>
        # """, unsafe_allow_html=True)

        # with st.container(border=True):
        #     da_col, dr_col, dt_col = st.columns(3, gap="medium")
        #     with da_col:
        #         s.age = st.number_input("Driver Age", min_value=18, max_value=65, value=int(s.age), step=1)
        #     with dr_col:
        #         st.markdown('<div class="slider-label-spec">Driver Rating ★</div>', unsafe_allow_html=True)
        #         s.rating = st.slider("Driver Rating ★", 1.0, 5.0, float(s.rating), 0.1, label_visibility="collapsed")
        #         r_full = int(s.rating)
        #         st.markdown(f'<div style="font-size:14px;color:#F59E0B;letter-spacing:1px;margin-top:6px;">{"★"*r_full}{"☆"*(5-r_full)} <span style="font-size:12px;font-weight:700;color:#64748B">{s.rating:.1f}</span></div>', unsafe_allow_html=True)
        #     with dt_col:
        #         s.time_ordered = st.text_input("Order Time (HH:MM)", value=str(s.time_ordered), help="24-hr format e.g. 14:30")

        # ── CONTAINER 3: DRIVER PROFILE ──
        st.markdown("""
        <div class="fcard-head">
            <div class="fcard-icon" style="background:#EFF6FF;">👤</div>
            <div>
                <div class="fcard-title">Driver Profile</div>
                <div class="fcard-desc">Age, rating, and order time</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.container(border=True):
            da_col, dr_col, dt_col = st.columns(3, gap="medium")
            with da_col:
                s.age = st.number_input("Driver Age", min_value=18, max_value=65, value=int(s.age), step=1)
                
            # with dr_col:
            #     st.markdown('<div class="slider-label-spec">Driver Rating ★</div>', unsafe_allow_html=True)
            #     s.rating = st.slider("Driver Rating ★", 1.0, 5.0, float(s.rating), 0.1, label_visibility="collapsed")
            #     r_full = int(s.rating)
            #     st.markdown(f'<div style="font-size:14px;color:#F59E0B;letter-spacing:1px;margin-top:6px;">{"★"*r_full}{"☆"*(5-r_full)} <span style="font-size:12px;font-weight:700;color:#64748B">{s.rating:.1f}</span></div>', unsafe_allow_html=True)

            with dr_col:
                st.markdown('<div class="slider-label-spec">Driver Rating ★</div>', unsafe_allow_html=True)
                s.rating = st.slider("Driver Rating ★", 1.0, 5.0, float(s.rating), 0.1, label_visibility="collapsed")
                r_full = int(s.rating)
                
                # 🚀 FIXED: Added "slider-stars-wrapper" class block container for perfect alignment tracking
                st.markdown(f"""
                <div class="slider-stars-wrapper">
                    <div class="star-rating-row">
                        {"★"*r_full}{"☆"*(5-r_full)} 
                        <span class="star-rating-val">{s.rating:.1f}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
            with dt_col:
                # 🚀 NATIVE CLOCK STYLE INPUT CONVERSION
                import datetime
                
                # 1. Fallback handler checks if state contains a string timestamp and parses it into a time object
                if isinstance(s.time_ordered, str):
                    try:
                        h, m = map(int, s.time_ordered.split(":"))
                        init_time = datetime.time(h, m)
                    except ValueError:
                        init_time = datetime.time(11, 15) # Standard default fallback
                elif isinstance(s.time_ordered, datetime.time):
                    init_time = s.time_ordered
                else:
                    init_time = datetime.time(11, 15)

                # 2. Render the clock element
                picked_time = st.time_input("Order Time", value=init_time)
                
                # 3. Store the time object back into state (or format as "HH:MM" string if your ML model requires a string string format)
                s.time_ordered = picked_time.strftime("%H:%M") 

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
  
    # # ── STEP 4: PREDICT ──────────────────────
    # elif s.step == 4:
    #     dist=haversine(s.rest_lat,s.rest_lon,s.del_lat,s.del_lon)

    #     st.markdown("""
    #     <div class="section-title">⚡ All set — let's predict!</div>
    #     <div class="section-sub">Review your inputs below, then hit Predict to get the ML-powered ETA.</div>
    #     """, unsafe_allow_html=True)

    #     # ── Review summary table ──
    #     tb_badge=TRAFFIC_BADGE.get(s.traffic,"ib-blue")
    #     st.markdown(f"""
    #     <div class="fcard">
    #       <div class="fcard-head">
    #         <div class="fcard-icon" style="background:#FFF0E3;">📋</div>
    #         <div>
    #           <div class="fcard-title">Order Snapshot</div>
    #           <div class="fcard-desc">Everything the model will use</div>
    #         </div>
    #       </div>
    #       <div class="fcard-body">
    #         <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
    #           <div style="background:var(--cream2);border-radius:10px;padding:11px 14px">
    #             <div style="font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--ink4)">📐 Distance</div>
    #             <div style="font-size:18px;font-weight:800;color:var(--ink);margin-top:3px">{dist:.2f} <span style="font-size:13px;font-weight:500;color:var(--ink3)">km</span></div>
    #           </div>
    #           <div style="background:var(--cream2);border-radius:10px;padding:11px 14px">
    #             <div style="font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--ink4)">🕐 Order Time</div>
    #             <div style="font-size:18px;font-weight:800;color:var(--ink);margin-top:3px">{s.time_ordered}</div>
    #           </div>
    #           <div style="background:var(--cream2);border-radius:10px;padding:11px 14px">
    #             <div style="font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--ink4)">{WEATHER_ICON.get(s.weather,"🌤️")} Weather</div>
    #             <div style="font-size:15px;font-weight:700;color:var(--ink);margin-top:3px">{s.weather}</div>
    #           </div>
    #           <div style="background:var(--cream2);border-radius:10px;padding:11px 14px">
    #             <div style="font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--ink4)">🚦 Traffic</div>
    #             <div style="margin-top:5px"><span class="inline-badge {tb_badge}">{s.traffic}</span></div>
    #           </div>
    #           <div style="background:var(--cream2);border-radius:10px;padding:11px 14px">
    #             <div style="font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--ink4)">{VEH_ICON.get(s.vehicle_type,"🛵")} Vehicle</div>
    #             <div style="font-size:15px;font-weight:700;color:var(--ink);margin-top:3px">{s.vehicle_type.replace("_"," ").title()}</div>
    #           </div>
    #           <div style="background:var(--cream2);border-radius:10px;padding:11px 14px">
    #             <div style="font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--ink4)">⭐ Driver Rating</div>
    #             <div style="font-size:15px;font-weight:700;color:#F59E0B;margin-top:3px">{"★"*int(s.rating)}{"☆"*(5-int(s.rating))} {s.rating:.1f}</div>
    #           </div>
    #           <div style="background:var(--cream2);border-radius:10px;padding:11px 14px">
    #             <div style="font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--ink4)">🏙️ City</div>
    #             <div style="font-size:15px;font-weight:700;color:var(--ink);margin-top:3px">{s.city}</div>
    #           </div>
    #           <div style="background:var(--cream2);border-radius:10px;padding:11px 14px">
    #             <div style="font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--ink4)">🎉 Festival</div>
    #             <div style="font-size:15px;font-weight:700;color:var(--ink);margin-top:3px">{'🎉 Active' if s.festival=="Yes" else '— None'}</div>
    #           </div>
    #         </div>
    #       </div>
    #     </div>
    #     """, unsafe_allow_html=True)

    #     # back_col, pred_col = st.columns([1,2])
    #     # with back_col:
    #     #     if st.button("← Edit Details", use_container_width=True, key="s4_back"): s.step=3; st.rerun()
    #     # with pred_col:
    #     #     st.markdown('<div class="pred-btn-wrap">', unsafe_allow_html=True)
    #     #     predict_hit = st.button("🚀 Predict My Delivery Time!", use_container_width=True, key="predict_btn")
    #     #     st.markdown('</div>', unsafe_allow_html=True)

    #     # ─── NAVIGATION PROGRESSION ACTIONS ROW (STANDARDIZED) ───
    #     back_col, pred_col = st.columns([1, 2], gap="medium")
    #     with back_col:
    #         # Replaced "s4_back" key with final structured key identifier
    #         if st.button("← Edit Details", use_container_width=True, key="action_nav_back_to_3", type="secondary"): 
    #             s.step = 3
    #             st.rerun()
    #     with pred_col:
    #         # 🚀 FIXED: Removed custom HTML wrap string entirely and set type to primary
    #         predict_hit = st.button("🚀 Predict My Delivery Time!", use_container_width=True, key="action_nav_predict", type="primary")

    #     if predict_hit:
    #         # Build input dataframe exactly matching model training
    #         input_df = pd.DataFrame({
    #             'Restaurant_latitude':         [s.rest_lat],
    #             'Restaurant_longitude':        [s.rest_lon],
    #             'Delivery_location_latitude':  [s.del_lat],
    #             'Delivery_location_longitude': [s.del_lon],
    #             'Time_Orderd':                 [s.time_ordered],
    #             'Delivery_person_Age':         [int(s.age)],
    #             'Delivery_person_Ratings':     [float(s.rating)],
    #             'Vehicle_condition':           [int(s.vehicle_condition)],
    #             'multiple_deliveries':         [int(s.multiple_deliveries)],
    #             'Weather_conditions':          [s.weather],
    #             'Type_of_vehicle':             [s.vehicle_type],
    #             'Festival':                    [s.festival],
    #             'City':                        [s.city],
    #             'Road_traffic_density':        [s.traffic],
    #         })

    #         with st.spinner("🧠 Running ML inference…"):
    #             time.sleep(0.45)
    #             if model:
    #                 try:
    #                     s.prediction = float(model.predict(input_df)[0])
    #                     s.demo_mode = False
    #                 except Exception as e:
    #                     # heuristic fallback
    #                     p = {"Jam":18,"High":10,"Medium":4,"Low":0}
    #                     w = {"Stormy":12,"Sandstorms":10,"Fog":8,"Windy":4,"Cloudy":2,"Sunny":0}
    #                     base = max(10, dist*4.2 + (30-s.age*0.15) + (5-s.rating)*3.5)
    #                     s.prediction = base + p.get(s.traffic,0) + w.get(s.weather,0) + (8 if s.festival=="Yes" else 0) + s.multiple_deliveries*3
    #                     s.demo_mode = True
    #                     st.warning(f"Model error ({str(e)[:60]}…) — demo estimate shown.")
    #             else:
    #                 p={"Jam":18,"High":10,"Medium":4,"Low":0}
    #                 w={"Stormy":12,"Sandstorms":10,"Fog":8,"Windy":4,"Cloudy":2,"Sunny":0}
    #                 base=max(10,dist*4.2+(30-s.age*0.15)+(5-s.rating)*3.5)
    #                 s.prediction=base+p.get(s.traffic,0)+w.get(s.weather,0)+(8 if s.festival=="Yes" else 0)+s.multiple_deliveries*3
    #                 s.demo_mode=True

    #         import random
    #         s.phrase_idx = random.randint(0, len(PHRASES)-1)

    # ── STEP 4: PREDICT ──────────────────────
    elif s.step == 4:
        dist=haversine(s.rest_lat,s.rest_lon,s.del_lat,s.del_lon)

        st.markdown("""
        <div class="section-title">⚡ All set — let's predict!</div>
        <div class="section-sub">Review your inputs below, then hit Predict to get the ML-powered ETA.</div>
        """, unsafe_allow_html=True)

        # ── Review summary table ──
        tb_badge=TRAFFIC_BADGE.get(s.traffic,"ib-blue")
        st.markdown(f"""
        <div class="fcard">
          <div class="fcard-head">
            <div class="fcard-icon" style="background:#FFF0E3;">📋</div>
            <div>
              <div class="fcard-title">Order Snapshot</div>
              <div class="fcard-desc">Everything the model will use</div>
            </div>
          </div>
          <div class="fcard-body">
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
              <div style="background:var(--cream2);border-radius:10px;padding:11px 14px">
                <div style="font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--ink4)">📐 Distance</div>
                <div style="font-size:18px;font-weight:800;color:var(--ink);margin-top:3px">{dist:.2f} <span style="font-size:13px;font-weight:500;color:var(--ink3)">km</span></div>
              </div>
              <div style="background:var(--cream2);border-radius:10px;padding:11px 14px">
                <div style="font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--ink4)">🕐 Order Time</div>
                <div style="font-size:18px;font-weight:800;color:var(--ink);margin-top:3px">{s.time_ordered}</div>
              </div>
              <div style="background:var(--cream2);border-radius:10px;padding:11px 14px">
                <div style="font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--ink4)">{WEATHER_ICON.get(s.weather,"🌤️")} Weather</div>
                <div style="font-size:15px;font-weight:700;color:var(--ink);margin-top:3px">{s.weather}</div>
              </div>
              <div style="background:var(--cream2);border-radius:10px;padding:11px 14px">
                <div style="font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--ink4)">🚦 Traffic</div>
                <div style="margin-top:5px"><span class="inline-badge {tb_badge}">{s.traffic}</span></div>
              </div>
              <div style="background:var(--cream2);border-radius:10px;padding:11px 14px">
                <div style="font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--ink4)">{VEH_ICON.get(s.vehicle_type,"🛵")} Vehicle</div>
                <div style="font-size:15px;font-weight:700;color:var(--ink);margin-top:3px">{s.vehicle_type.replace("_"," ").title()}</div>
              </div>
              <div style="background:var(--cream2);border-radius:10px;padding:11px 14px">
                <div style="font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--ink4)">⭐ Driver Rating</div>
                <div style="font-size:15px;font-weight:700;color:#F59E0B;margin-top:3px">{"★"*int(s.rating)}{"☆"*(5-int(s.rating))} {s.rating:.1f}</div>
              </div>
              <div style="background:var(--cream2);border-radius:10px;padding:11px 14px">
                <div style="font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--ink4)">🏙️ City</div>
                <div style="font-size:15px;font-weight:700;color:var(--ink);margin-top:3px">{s.city}</div>
              </div>
              <div style="background:var(--cream2);border-radius:10px;padding:11px 14px">
                <div style="font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--ink4)">🎉 Festival</div>
                <div style="font-size:15px;font-weight:700;color:var(--ink);margin-top:3px">{'🎉 Active' if s.festival=="Yes" else '— None'}</div>
              </div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # back_col, pred_col = st.columns([1,2])
        # with back_col:
        #     if st.button("← Edit Details", use_container_width=True, key="s4_back"): s.step=3; st.rerun()
        # with pred_col:
        #     st.markdown('<div class="pred-btn-wrap">', unsafe_allow_html=True)
        #     predict_hit = st.button("🚀 Predict My Delivery Time!", use_container_width=True, key="predict_btn")
        #     st.markdown('</div>', unsafe_allow_html=True)

        # ─── NAVIGATION PROGRESSION ACTIONS ROW (STANDARDIZED) ───
        back_col, pred_col = st.columns([1, 2], gap="medium")
        with back_col:
            # Replaced "s4_back" key with final structured key identifier
            if st.button("← Edit Details", use_container_width=True, key="action_nav_back_to_3", type="secondary"): 
                s.step = 3
                st.rerun()
        with pred_col:
            # 🚀 FIXED: Removed custom HTML wrap string entirely and set type to primary
            predict_hit = st.button("🚀 Predict My Delivery Time!", use_container_width=True, key="action_nav_predict", type="primary")

        if predict_hit:
            # Build input dataframe exactly matching model training
            input_df = pd.DataFrame({
                'Restaurant_latitude':         [s.rest_lat],
                'Restaurant_longitude':        [s.rest_lon],
                'Delivery_location_latitude':  [s.del_lat],
                'Delivery_location_longitude': [s.del_lon],
                'Time_Orderd':                 [s.time_ordered],
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

            with st.spinner("🧠 Running ML inference…"):
                time.sleep(0.45)
                if model:
                    try:
                        s.prediction = float(model.predict(input_df)[0])
                        s.demo_mode = False
                    except Exception as e:
                        # heuristic fallback
                        p = {"Jam":18,"High":10,"Medium":4,"Low":0}
                        w = {"Stormy":12,"Sandstorms":10,"Fog":8,"Windy":4,"Cloudy":2,"Sunny":0}
                        base = max(10, dist*4.2 + (30-s.age*0.15) + (5-s.rating)*3.5)
                        s.prediction = base + p.get(s.traffic,0) + w.get(s.weather,0) + (8 if s.festival=="Yes" else 0) + s.multiple_deliveries*3
                        s.demo_mode = True
                        st.warning(f"Model error ({str(e)[:60]}…) — demo estimate shown.")
                else:
                    p={"Jam":18,"High":10,"Medium":4,"Low":0}
                    w={"Stormy":12,"Sandstorms":10,"Fog":8,"Windy":4,"Cloudy":2,"Sunny":0}
                    base=max(10,dist*4.2+(30-s.age*0.15)+(5-s.rating)*3.5)
                    s.prediction=base+p.get(s.traffic,0)+w.get(s.weather,0)+(8 if s.festival=="Yes" else 0)+s.multiple_deliveries*3
                    s.demo_mode=True

            import random
            s.phrase_idx = random.randint(0, len(PHRASES)-1)

# ─── RIGHT COLUMN  —  DYNAMIC SUMMARY DASHBOARD ──────────────────────────────
with result_col:

    # # Inject an isolated structural layout puller
    # # This brings the entire column upwards to line up with the Interactive Route Planner
    # st.html("""
    # <style>
    # /* Target the vertical structural block wrapper inside the right-hand column container */
    # div[data-testid="stColumn"]:last-child div[data-testid="stVerticalBlock"] {
    #     margin-top: -62px !important; /* Pulls the block up perfectly by matching the header height */
    # }
    
    # @media (max-width: 768px) {
    #     /* Reset on small/mobile screens so columns stack vertically without overlapping */
    #     div[data-testid="stColumn"]:last-child div[data-testid="stVerticalBlock"] {
    #         margin-top: 0px !important;
    #     }
    # }
    # </style>
    # """)

    #     # ── BULLETPROOF ELEMENT-TARGETED SIDEBAR PULLER ────────────────────────
    # # Targets the exact column structure holding your summary card (.fcard) 
    # # to completely eliminate layout leakage into your address boxes
    # st.html("""
    # <style>
    # /* Locate the vertical layout block wrapper that houses our custom fcard block */
    # div[data-testid="stColumn"]:has(.fcard) div[data-testid="stVerticalBlock"] {
    #     margin-top: -62px !important; /* Pulls the summary box up perfectly */
    # }
    
    # @media (max-width: 768px) {
    #     /* Disable vertical adjustments on small mobile screens */
    #     div[data-testid="stColumn"]:has(.fcard) div[data-testid="stVerticalBlock"] {
    #         margin-top: 0px !important;
    #     }
    # }
    # </style>
    # """)

    # ── DYNAMIC RENDERING ALIGNMENT SCHEDULER ──────────────────────────────
    # Changes margin adjustments based on the active step to prevent vertical overlaps
    dynamic_margin = "-62px" if s.step == 1 else "-10px"

    st.html(f"""
    <style>
    /* Target the exact vertical layout column container holding our summary fcard */
    div[data-testid="stColumn"]:has(.fcard) div[data-testid="stVerticalBlock"] {{
        margin-top: {dynamic_margin} !important; /* Dynamically balances headers across all steps */
    }}
    
    @media (max-width: 768px) {{
        /* Disable custom vertical shifts on mobile screens to keep layouts stacking correctly */
        div[data-testid="stColumn"]:has(.fcard) div[data-testid="stVerticalBlock"] {{
            margin-top: 0px !important;
        }}
    }}
    </style>
    """)

    if s.prediction is not None:
        pred = s.prediction
        lo = max(1, pred * 0.88)
        hi = pred * 1.14
        conf = min(97, max(68, 93 - haversine(s.rest_lat,s.rest_lon,s.del_lat,s.del_lon)*0.6))

        # ETA category
        if pred < 25:   cat,cat_col,cat_emoji = "Express","ib-green","⚡"
        elif pred < 40: cat,cat_col,cat_emoji = "On Schedule","ib-blue","✅"
        elif pred < 55: cat,cat_col,cat_emoji = "Standard","ib-amber","🕐"
        else:           cat,cat_col,cat_emoji = "Delayed","ib-red","⚠️"

        try:
            arrive = (datetime.strptime(s.time_ordered,"%H:%M") + timedelta(minutes=pred)).strftime("%I:%M %p")
        except Exception:
            arrive = "—"

        phrase = PHRASES[s.phrase_idx % len(PHRASES)].format(int(pred))
        demo_note = ' <span style="font-size:10px;opacity:.6">(demo)</span>' if s.demo_mode else ""

        # st.markdown(f"""
        # <div class="result-outer">
        #   <div class="result-inner">
        #     <div class="result-emoji">🛵</div>
        #     <div class="result-tagline">ML Predicted ETA{demo_note}</div>
        #     <div class="result-big" style="font-family:'Bricolage Grotesque',sans-serif; font-weight:800; letter-spacing:-2px;">{int(pred)}</div>
        #     <div class="result-unit">minutes</div>
        #     <div class="result-phrase">{phrase}</div>
        #     <div style="margin-bottom:14px">
        #       <span class="inline-badge {cat_col}">{cat_emoji} {cat}</span>
        #     </div>
        #     <div class="result-row">
        #       <div class="result-chip">🕐 Best <strong>{int(lo)} min</strong></div>
        #       <div class="result-chip">📍 Expected <strong>{int(pred)} min</strong></div>
        #       <div class="result-chip">⏱️ Worst <strong>{int(hi)} min</strong></div>
        #     </div>
        #     <div class="conf-bar-wrap">
        #       <div class="conf-row"><span>Confidence</span><span>{conf:.0f}%</span></div>
        #       <div class="conf-track"><div class="conf-fill" style="width:{conf}%"></div></div>
        #     </div>
        #     <div class="arrive-note">🕐 Arrives approx. <strong>{arrive}</strong></div>
        #   </div>
        # </div>
        # """, unsafe_allow_html=True)

        # st.markdown(f"""
        #   <div class="result-card">
        #     <div class="rc-inner">

        #       <span class="rc-emoji">🛵</span>

        #       <div class="rc-eyebrow">
        #         ML Predicted ETA{demo_note}
        #       </div>

        #       <div class="rc-number">
        #         {int(pred)}
        #       </div>

        #       <div class="rc-unit">
        #         minutes
        #       </div>

        #       <div class="rc-phrase">
        #         {phrase}
        #       </div>

        #       <div style="margin-bottom:14px">
        #         <span class="inline-badge {cat_col}">
        #           {cat_emoji} {cat}
        #         </span>
        #       </div>

        #       <div class="rc-chips">
        #         <div class="rc-chip">
        #           🕐 Best <strong>{int(lo)} min</strong>
        #         </div>

        #         <div class="rc-chip">
        #           📍 Expected <strong>{int(pred)} min</strong>
        #         </div>

        #         <div class="rc-chip">
        #           ⏱️ Worst <strong>{int(hi)} min</strong>
        #         </div>
        #       </div>

        #       <div class="rc-conf-row">
        #         <span>Confidence</span>
        #         <span>{conf:.0f}%</span>
        #       </div>

        #       <div class="rc-conf-track">
        #         <div class="rc-conf-fill" style="width:{conf}%"></div>
        #       </div>

        #       <div class="rc-arrive">
        #         🕐 Arrives approx. <strong>{arrive}</strong>
        #       </div>

        #     </div>
        #   </div>
        #   """, unsafe_allow_html=True)


        card_html = f"""
          <div class="result-card">
            <div class="rc-inner">

              <span class="rc-emoji">🛵</span>

              <div class="rc-eyebrow">
                ML Predicted ETA{demo_note}
              </div>

              <div class="rc-number">
                {int(pred)}
              </div>

              <div class="rc-unit">
                minutes
              </div>

              <div class="rc-phrase">
                {phrase}
              </div>

              <div style="margin-bottom:14px">
                <span class="inline-badge {cat_col}">
                  {cat_emoji} {cat}
                </span>
              </div>

              <div class="rc-chips">
                <div class="rc-chip">
                  🕐 Best <strong>{int(lo)} min</strong>
                </div>

                <div class="rc-chip">
                  📍 Expected <strong>{int(pred)} min</strong>
                </div>

                <div class="rc-chip">
                  ⏱️ Worst <strong>{int(hi)} min</strong>
                </div>
              </div>

              <div class="rc-conf-row">
                <span>Confidence</span>
                <span>{conf:.0f}%</span>
              </div>

              <div class="rc-conf-track">
                <div class="rc-conf-fill" style="width:{conf}%"></div>
              </div>

              <div class="rc-arrive">
                🕐 Arrives approx. <strong>{arrive}</strong>
              </div>

            </div>
          </div>
          """
        st.html(card_html)


        # card_html = f"""
        # <div class="result-card">
        # <div class="rc-inner">
        # <span class="rc-emoji">🛵</span>
        # <div class="rc-eyebrow">ML Predicted ETA</div>
        # <div class="rc-number">{int(pred)}</div>
        # <div class="rc-unit">minutes</div>
        # <div class="rc-phrase">Test Phrase</div>
        # </div>
        # </div>
        # """

        # st.html(card_html)
        # from textwrap import dedent

        # st.markdown(
        #     dedent(f"""
        #     <div class="result-card">
        #         <div class="rc-inner">

        #             <span class="rc-emoji">🛵</span>

        #             <div class="rc-number">{int(pred)}</div>

        #             <div class="rc-unit">minutes</div>

        #         </div>
        #     </div>
        #     """),
        #     unsafe_allow_html=True
        # )

        # st.markdown('<div class="result-card"><h1>HELLO</h1></div>', unsafe_allow_html=True)
        # st.markdown("""
        #   <div class="result-card">
        #   HELLO
        #   <div>WORLD</div>
        #   </div>
        #   """, unsafe_allow_html=True)
        
        # st.markdown("""
        #   <div style="
        #   background:red;
        #   color:white;
        #   padding:20px;
        #   font-size:30px;
        #   ">
        #   TEST CARD
        #   </div>
        #   """, unsafe_allow_html=True)

        # Impact analysis (FIXED: Color map matches token system definitions directly)
        dist2 = haversine(s.rest_lat,s.rest_lon,s.del_lat,s.del_lon)
        impacts=[
            ("📐","Distance",    min(100,dist2*11),"var(--brand)", f"{dist2:.1f}km"),
            ("🚦","Traffic",     {"Low":10,"Medium":38,"High":68,"Jam":100}.get(s.traffic,50),"var(--brand2)",s.traffic),
            ("🌤️","Weather",    {"Sunny":5,"Cloudy":18,"Windy":30,"Fog":52,"Sandstorms":70,"Stormy":92}.get(s.weather,20),"#F59E0B",s.weather),
            ("⭐","Driver",      int((5-s.rating)/4*80)+8,"var(--brand3)",f"★{s.rating:.1f}"),
            ("🏙️","City",       {"Metropolitian":80,"Metropolitan":80,"Urban":48,"Semi-Urban":22}.get(s.city,50),"#6366F1",s.city.split("-")[0]),
        ]
        st.markdown("""
        <div class="fcard" style="margin-top:14px">
          <div class="fcard-head" style="display:flex; align-items:center; gap:10px; border-bottom: 1px solid #EDE8E3; padding-bottom:12px; margin-bottom:14px;">
            <div class="fcard-icon" style="background:#FFF0E3; padding:4px 8px; border-radius:6px;">📊</div>
            <div class="fcard-title" style="font-family:'Bricolage Grotesque',sans-serif; font-size:14px; font-weight:700;">Impact Breakdown</div>
          </div>
          <div class="fcard-body">
        """, unsafe_allow_html=True)
        for icon,name,pct,color,val in impacts:
            st.markdown(f"""
            <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; font-size:13px;">
              <span class="impact-icon" style="margin-right:8px;">{icon}</span>
              <span class="impact-name" style="flex:1; font-weight:600; color:var(--ink2);">{name}</span>
              <div class="impact-track" style="flex:2; background:#E5E7EB; height:6px; border-radius:4px; margin:0 12px; position:relative; overflow:hidden;">
                <div class="impact-bar" style="width:{pct}%; background:{color}; height:100%; border-radius:4px;"></div>
              </div>
              <span class="impact-val" style="font-weight:700; color:var(--ink); text-align:right; min-width:50px;">{val}</span>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div></div>', unsafe_allow_html=True)

        # Tips Processing Engine
        tips=[]
        if s.traffic=="Jam": tips.append(("🔴","#FEF2F2","<strong>Traffic gridlock.</strong> Consider alerting your customer to a likely delay."))
        if s.weather in ["Stormy","Sandstorms"]: tips.append(("⛈️","#FFF7ED",f"<strong>{s.weather}.</strong> Delivery safety may be impacted — factor in delays."))
        if s.festival=="Yes": tips.append(("🎉","#FFF7ED","<strong>Festival surge.</strong> High demand + packed roads — expect slower service."))
        if s.rating<3.5: tips.append(("⭐","#FFFBEB","<strong>Low-rated driver.</strong> Assign a higher-rated partner for better reliability."))
        if s.multiple_deliveries>1: tips.append(("📦","#EFF6FF",f"<strong>{s.multiple_deliveries+1} concurrent orders.</strong> Estimated time includes multiple stops."))
        if dist2>8: tips.append(("📏","#F0FDF4",f"<strong>Long route ({dist2:.1f}km).</strong> Motorcycle fastest — avoid bicycle."))
        if s.vehicle_condition==0: tips.append(("🔧","#FEF2F2","<strong>Poor vehicle condition</strong> may impact reliability and speed."))
        if not tips: tips.append(("✅","#F0FDF4","<strong>All conditions optimal.</strong> Smooth delivery expected — no issues flagged!"))

        st.markdown("""
        <div class="fcard" style="margin-top:14px">
          <div class="fcard-head" style="display:flex; align-items:center; gap:10px; border-bottom: 1px solid #EDE8E3; padding-bottom:12px; margin-bottom:14px;">
            <div class="fcard-icon" style="background:#FFF0E3; padding:4px 8px; border-radius:6px;">💡</div>
            <div class="fcard-title" style="font-family:'Bricolage Grotesque',sans-serif; font-size:14px; font-weight:700;">Smart Insights</div>
          </div>
          <div class="fcard-body">
        """, unsafe_allow_html=True)
        for icon,bg,text in tips[:5]:
            st.markdown(f"""
            <div class="tip-row" style="display:flex; align-items:flex-start; gap:12px; margin-bottom:10px; font-size:13px; line-height:1.4;">
              <div class="tip-badge" style="background:{bg}; padding:4px 8px; border-radius:6px; font-size:14px;">{icon}</div>
              <div class="tip-text" style="color:var(--ink2);">{text}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div></div>', unsafe_allow_html=True)

        if st.button("🔄 New Prediction", use_container_width=True, key="reset_btn"):
            s.prediction = None
            s.step = 1
            st.rerun()

    # else:
    #     # Friendly placeholder with step context
    #     step_hints = {
    #         1: ("🗺️","Drop your pins","Select restaurant and delivery location on the map in Step 1."),
    #         2: ("🌤️","Set the scene","Pick weather, traffic and city type in Step 2."),
    #         3: ("🏍️","Driver details","Add driver profile and vehicle info in Step 3."),
    #         4: ("🚀","Ready to go!","Hit the big Predict button to get your ETA."),
    #     }
    #     emoji,title,sub = step_hints.get(s.step,("🛵","Let's go!","Complete all steps to get a prediction."))
    #     st.markdown(f"""
    #     <div class="placeholder">
    #       <span class="placeholder-emoji">{emoji}</span>
    #       <div class="placeholder-title">{title}</div>
    #       <div class="placeholder-sub">{sub}</div>
    #     </div>
    #     """, unsafe_allow_html=True)

    #     # Mini summary of what's been filled
    #     dist3 = haversine(s.rest_lat,s.rest_lon,s.del_lat,s.del_lon)
        
    #     # # FIXED: Explicit inline row styles added and open markdown block perfectly closed with balancing tags
    #     # st.markdown(f"""
    #     # <div class="fcard" style="margin-top:14px">
    #     #   <div class="fcard-head" style="display:flex; align-items:center; gap:10px; border-bottom: 1px solid #EDE8E3; padding-bottom:12px; margin-bottom:14px;">
    #     #     <div class="fcard-icon" style="background:var(--cream2); padding:4px 8px; border-radius:6px;">📝</div>
    #     #     <div class="fcard-title" style="font-family:'Bricolage Grotesque',sans-serif; font-size:14px; font-weight:700;">Your Settings So Far</div>
    #     #   </div>
    #     #   <div class="fcard-body">
    #     #     <div class="impact-row"><span class="impact-icon">📐</span><span class="impact-name" style="width:auto;flex:1">Route Distance</span><span class="impact-val">{dist3:.2f} km</span></div>
    #     #     <div class="impact-row"><span class="impact-icon">{WEATHER_ICON.get(s.weather,"🌤️")}</span><span class="impact-name" style="width:auto;flex:1">Weather</span><span class="impact-val">{s.weather}</span></div>
    #     #     <div class="impact-row"><span class="impact-icon">🚦</span><span class="impact-name" style="width:auto;flex:1">Traffic</span><span class="impact-val"><span class="inline-badge {TRAFFIC_BADGE.get(s.traffic,'ib-blue')}">{s.traffic}</span></span></div>
    #     #     <div class="impact-row"><span class="impact-icon">{VEH_ICON.get(s.vehicle_type,"🛵")}</span><span class="impact-name" style="width:auto;flex:1">Vehicle</span><span class="impact-val">{s.vehicle_type.replace("_"," ").title()}</span></div>
    #     #     <div class="impact-row"><span class="impact-icon">⭐</span><span class="impact-name" style="width:auto;flex:1">Driver Rating</span><span class="impact-val">{s.rating:.1f} / 5</span></div>
    #     #   </div>
    #     # </div>
    #     # """, unsafe_allow_html=True)
        
    #     # CLEANED: Relying on dedicated global structures without mixed structural overrides
    #     st.markdown(f"""
    #     <div class="fcard">
    #       <div class="fcard-head">
    #         <div class="fcard-icon" style="background: #FAF8F5;">📝</div>
    #         <div class="fcard-title" style="font-family: 'Bricolage Grotesque', sans-serif;">Your Settings So Far</div>
    #       </div>
    #       <div class="fcard-body">
    #         <div class="impact-row">
    #           <span class="impact-icon">📐</span>
    #           <span class="impact-name">Route Distance</span>
    #           <span class="impact-val">{dist3:.2f} km</span>
    #         </div>
    #         <div class="impact-row">
    #           <span class="impact-icon">{WEATHER_ICON.get(s.weather, "🌤️")}</span>
    #           <span class="impact-name">Weather</span>
    #           <span class="impact-val">{s.weather}</span>
    #         </div>
    #         <div class="impact-row">
    #           <span class="impact-icon">🚦</span>
    #           <span class="impact-name">Traffic</span>
    #           <span class="impact-val"><span class="inline-badge {TRAFFIC_BADGE.get(s.traffic, 'ib-blue')}">{s.traffic}</span></span>
    #         </div>
    #         <div class="impact-row">
    #           <span class="impact-icon">{VEH_ICON.get(s.vehicle_type, "🛵")}</span>
    #           <span class="impact-name">Vehicle</span>
    #           <span class="impact-val">{s.vehicle_type.replace("_", " ").title()}</span>
    #         </div>
    #         <div class="impact-row">
    #           <span class="impact-icon">⭐</span>
    #           <span class="impact-name">Driver Rating</span>
    #           <span class="impact-val">{s.rating:.1f} / 5</span>
    #         </div>
    #       </div>
    #     </div>
    #     """, unsafe_allow_html=True)

    # else:
    #     # Mini summary of what's been filled
    #     dist3 = haversine(s.rest_lat,s.rest_lon,s.del_lat,s.del_lon)

    #     # CLEANED: Relying on dedicated global structures without mixed structural overrides
    #     st.markdown(f"""
    #     <div class="fcard" style="margin-top: 0px;">
    #     <div class="fcard-head" style="display:flex; align-items:center; gap:10px; border-bottom: 1px solid #EDE8E3; padding-bottom:12px; margin-bottom:14px;">
    #         <div class="fcard-icon" style="background: #FAF8F5; padding:4px 8px; border-radius:6px;">📝</div>
    #         <div class="fcard-title" style="font-family: 'Bricolage Grotesque', sans-serif; font-size:14px; font-weight:700;">Your Settings So Far</div>
    #     </div>
    #     <div class="fcard-body">
    #         <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; font-size:13px;">
    #         <span class="impact-icon" style="margin-right:8px;">📐</span>
    #         <span class="impact-name" style="flex:1; font-weight:600; color:var(--ink2);">Route Distance</span>
    #         <span class="impact-val" style="font-weight:700; color:var(--ink); text-align:right;">{dist3:.2f} km</span>
    #         </div>
    #         <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; font-size:13px;">
    #         <span class="impact-icon" style="margin-right:8px;">{WEATHER_ICON.get(s.weather, "🌤️")}</span>
    #         <span class="impact-name" style="flex:1; font-weight:600; color:var(--ink2);">Weather</span>
    #         <span class="impact-val" style="font-weight:700; color:var(--ink); text-align:right;">{s.weather}</span>
    #         </div>
    #         <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; font-size:13px;">
    #         <span class="impact-icon" style="margin-right:8px;">🚦</span>
    #         <span class="impact-name" style="flex:1; font-weight:600; color:var(--ink2);">Traffic</span>
    #         <span class="impact-val" style="font-weight:700; color:var(--ink); text-align:right;"><span class="inline-badge {TRAFFIC_BADGE.get(s.traffic, 'ib-blue')}">{s.traffic}</span></span>
    #         </div>
    #         <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; font-size:13px;">
    #         <span class="impact-icon" style="margin-right:8px;">{VEH_ICON.get(s.vehicle_type, "🛵")}</span>
    #         <span class="impact-name" style="flex:1; font-weight:600; color:var(--ink2);">Vehicle</span>
    #         <span class="impact-val" style="font-weight:700; color:var(--ink); text-align:right;">{s.vehicle_type.replace("_", " ").title()}</span>
    #         </div>
    #         <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; font-size:13px;">
    #         <span class="impact-icon" style="margin-right:8px;">⭐</span>
    #         <span class="impact-name" style="flex:1; font-weight:600; color:var(--ink2);">Driver Rating</span>
    #         <span class="impact-val" style="font-weight:700; color:var(--ink); text-align:right;">{s.rating:.1f} / 5</span>
    #         </div>
    #     </div>
    #     </div>
    #     """, unsafe_allow_html=True)

    else:
        # Mini summary of what's been filled
        dist3 = haversine(s.rest_lat, s.rest_lon, s.del_lat, s.del_lon)

        # ── STATE INTERACTION ENGINE: PRE-COMPUTE STRINGS BEFORE RENDER ──
        is_weather_set = s.step >= 2
        is_traffic_set = s.step >= 2
        is_vehicle_set = s.step >= 3
        is_rating_set  = s.step >= 3

        # Extract Icons into standalone immutable variables
        weather_icon_char = WEATHER_ICON.get(s.weather, "🌤️")
        vehicle_icon_char = VEH_ICON.get(s.vehicle_type, "🛵")

        # 1. Weather Block
        if is_weather_set:
            weather_label = str(s.weather)
            weather_badge_style = "background: #FFF7ED; border: 1px solid #FFEDD5; color: #C2410C; font-weight: 700; padding: 3px 10px; border-radius: 20px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.3px;"
        else:
            weather_label = f"Auto-Default: {s.weather}"
            weather_badge_style = "opacity: 0.55; border: 1px dashed #cbd5e1; background: #f8fafc; color: #64748b; font-weight: 500; padding: 3px 10px; border-radius: 20px; font-size: 11px;"

        # # 2. Traffic Block
        # if is_traffic_set:
        #     traffic_badge_class = f"inline-badge {TRAFFIC_BADGE.get(s.traffic, 'ib-blue')}"
        #     traffic_row_style = "opacity: 1.0;"
        #     traffic_html_element = f'<span class="{traffic_badge_class}">{s.traffic}</span>'
        # else:
        #     traffic_row_style = "opacity: 0.55;"
        #     traffic_html_element = '<span style="border: 1px dashed #cbd5e1; background: #f8fafc; color: #64748b; font-weight: 500; padding: 3px 10px; border-radius: 20px; font-size: 11px;">Auto-Default: ' + str(s.traffic) + '</span>'

        # 2. Traffic Block Refinement
        if is_traffic_set:
            traffic_badge_class = f"inline-badge {TRAFFIC_BADGE.get(s.traffic, 'ib-blue')}"
            traffic_row_style = "" # No parent-level opacity needed
            traffic_html_element = f'<span class="{traffic_badge_class}">{s.traffic}</span>'
        else:
            traffic_row_style = "" # Removed opacity: 0.55 from here to keep label fully dark
            # Opacity is now moved directly into the badge's local inline style style below:
            traffic_html_element = f'<span style="opacity: 0.55; border: 1px dashed #cbd5e1; background: #f8fafc; color: #64748b; font-weight: 500; padding: 3px 10px; border-radius: 20px; font-size: 11px;">Auto-Default: {s.traffic}</span>'

        # 3. Vehicle Block
        clean_vehicle_name = s.vehicle_type.replace("_", " ").title()
        if is_vehicle_set:
            vehicle_label = str(clean_vehicle_name)
            vehicle_badge_style = "background: #F1F5F9; border: 1px solid #E2E8F0; color: #334155; font-weight: 700; padding: 3px 10px; border-radius: 20px; font-size: 11px;"
        else:
            vehicle_label = f"Auto-Default: {clean_vehicle_name}"
            vehicle_badge_style = "opacity: 0.55; border: 1px dashed #cbd5e1; background: #f8fafc; color: #64748b; font-weight: 500; padding: 3px 10px; border-radius: 20px; font-size: 11px;"

        # 4. Driver Rating Block
        if is_rating_set:
            rating_label = f"{s.rating:.1f} / 5"
            rating_badge_style = "background: #FEF3C7; border: 1px solid #FDE68A; color: #92400E; font-weight: 700; padding: 3px 10px; border-radius: 20px; font-size: 11px;"
        else:
            rating_label = f"Auto-Default: {s.rating:.1f} / 5"
            rating_badge_style = "opacity: 0.55; border: 1px dashed #cbd5e1; background: #f8fafc; color: #64748b; font-weight: 500; padding: 3px 10px; border-radius: 20px; font-size: 11px;"

        # # ── ABSOLUTE RAW HTML STRING PARSING ENGINE ──
        # # Constructed as an immutable layout block passed to st.html()
        # card_layout_html = f"""
        # <div class="fcard" style="margin-top: 0px;">
        #     <div class="fcard-head" style="display:flex; align-items:center; gap:10px; border-bottom: 1px solid #EDE8E3; padding-bottom:12px; margin-bottom:14px;">
        #         <div class="fcard-icon" style="background: #FAF8F5; padding:4px 8px; border-radius:6px;">📝</div>
        #         <div class="fcard-title" style="font-family: 'Bricolage Grotesque', sans-serif; font-size:14px; font-weight:700;">Your Settings So Far</div>
        #     </div>
        #     <div class="fcard-body">
                
        #         <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; font-size:13px;">
        #             <span class="impact-icon" style="margin-right:8px;">📐</span>
        #             <span class="impact-name" style="flex:1; font-weight:600; color:var(--ink2);">Route Distance</span>
        #             <span class="impact-val" style="font-weight:700; color:var(--ink); text-align:right;">{dist3:.2f} km</span>
        #         </div>
                
        #         <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; font-size:13px;">
        #             <span class="impact-icon" style="margin-right:8px;">{weather_icon_char}</span>
        #             <span class="impact-name" style="flex:1; font-weight:600; color:var(--ink2);">Weather</span>
        #             <span class="impact-val" style="text-align:right;">
        #                 <span style="{weather_badge_style}">{weather_label}</span>
        #             </span>
        #         </div>
                
        #         <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; font-size:13px; {traffic_row_style}">
        #             <span class="impact-icon" style="margin-right:8px;">🚦</span>
        #             <span class="impact-name" style="flex:1; font-weight:600; color:var(--ink2);">Traffic</span>
        #             <span class="impact-val" style="text-align:right;">
        #                 {traffic_html_element}
        #             </span>
        #         </div>
                
        #         <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; font-size:13px;">
        #             <span class="impact-icon" style="margin-right:8px;">{vehicle_icon_char}</span>
        #             <span class="impact-name" style="flex:1; font-weight:600; color:var(--ink2);">Vehicle</span>
        #             <span class="impact-val" style="text-align:right;">
        #                 <span style="{vehicle_badge_style}">{vehicle_label}</span>
        #             </span>
        #         </div>
                
        #         <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; font-size:13px;">
        #             <span class="impact-icon" style="margin-right:8px;">⭐</span>
        #             <span class="impact-name" style="flex:1; font-weight:600; color:var(--ink2);">Driver Rating</span>
        #             <span class="impact-val" style="text-align:right;">
        #                 <span style="{rating_badge_style}">{rating_label}</span>
        #             </span>
        #         </div>
        #     </div>
        # </div>
        # """
        
        # # Execute pure HTML render block bypass
        # st.html(card_layout_html)

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
                
                <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; font-size:13px;">
                    <span class="impact-icon" style="margin-right:8px;">📐</span>
                    <span class="impact-name" style="flex:1; font-weight:600; color:var(--ink2);">Route Distance</span>
                    <span class="impact-val" style="font-weight:700; color:var(--ink); text-align:right;">{dist3:.2f} km</span>
                </div>
                
                <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; font-size:13px;">
                    <span class="impact-icon" style="margin-right:8px;">{weather_icon_char}</span>
                    <span class="impact-name" style="flex:1; font-weight:600; color:var(--ink2);">Weather</span>
                    <span class="impact-val" style="text-align:right;">
                        <span style="{weather_badge_style}">{weather_label}</span>
                    </span>
                </div>
                
                <div class="impact-row" style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; font-size:13px; {traffic_row_style}">
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

        
        # 2. FIX: Expanded, full-depth vector layout extending right up to the action buttons
        if inline_vector_src:
            st.html(f"""
            <div class="external-vector-route" style="
                width: 100% !important;
                display: flex !important;
                justify-content: center !important;
                align-items: flex-start !important;
                padding-top: 120px; /* Generates a clean breath gap below the card */
                opacity: 0.85;     /* Boosts opacity so line details stand out clearly */
                margin-bottom: 20px;
            ">
                <img src="{inline_vector_src}" style="
                    width: 100% !important;        /* Forces image to span the full right column width */
                    height: auto !important;
                    max-height: 280px !important;  /* Increases height allowance to stretch the visual depth downwards */
                    object-fit: contain !important;
                    pointer-events: none !important;
                " alt="Delivery Route Visualization Layer">
            </div>
            """)




# st.markdown('</div>', unsafe_allow_html=True)  # content-shell

# ─── FOOTER ───────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  <span class="footer-l">🍔 DeliverIQ · ML Food Delivery Intelligence</span>
  <span class="footer-r">Random Forest · 14-feature pipeline · Trained on real delivery data</span>
</div>
""", unsafe_allow_html=True)