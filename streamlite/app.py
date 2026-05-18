import streamlit as st
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
from utils.styles import GLOBAL_CSS, navbar

st.set_page_config(
    page_title="SkinScan AI",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────
st.markdown(navbar("home"), unsafe_allow_html=True)

# ── Hero ─────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
    <div class="hero-eyebrow">AI-powered skincare intelligence</div>
    <div class="hero-title">Skin<em>Scan</em></div>
    <div class="hero-sub">
        Analyze ingredient interactions and discover which products suit
        your skin — powered by machine learning trained on real skincare data.
    </div>
    <div class="hero-badge-row">
        <div class="hero-badge"><span class="dot dot-pink"></span> Random Forest · Task A</div>
        <div class="hero-badge"><span class="dot dot-green"></span> Multi-label ML · Task B</div>
        <div class="hero-badge"><span class="dot dot-blue"></span> 9,510 real products</div>
        <div class="hero-badge"><span class="dot dot-pink"></span> 99% Recall</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Task Cards ───────────────────────────────────────────────────
st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="home-card home-card-pink">
        <div class="home-card-icon">🧪</div>
        <div class="home-card-title">Ingredient Conflict Detector</div>
        <div class="home-card-desc">
            Select two skincare ingredients and predict whether they
            interact safely — powered by a Random Forest classifier
            trained on physicochemical properties and 11 engineered
            interaction features.
        </div>
        <div style="margin-bottom:1.4rem;">
            <span class="home-card-chip">Binary classification</span>
            <span class="home-card-chip">Random Forest</span>
            <span class="home-card-chip">Physicochemical features</span>
            <span class="home-card-chip">4,371 pairs</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="cta-btn">', unsafe_allow_html=True)
    if st.button("Go to Conflict Detector →", key="btn_conflict"):
        st.switch_page("pages/product_compatibility.py")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="home-card home-card-green">
        <div class="home-card-icon">✨</div>
        <div class="home-card-title">Skin Compatibility Analyzer</div>
        <div class="home-card-desc">
            Upload a product ingredient label or paste the list.
            Get instant skin type suitability and skin concern
            predictions — trained on 9,510 real skincare products
            using TF-IDF text features.
        </div>
        <div style="margin-bottom:1.4rem;">
            <span class="home-card-chip">Multi-label classification</span>
            <span class="home-card-chip">TF-IDF + ML</span>
            <span class="home-card-chip">5 skin types</span>
            <span class="home-card-chip">6 concerns</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="cta-btn-green cta-btn">', unsafe_allow_html=True)
    if st.button("Go to Skin Analyzer →", key="btn_skin"):
        st.switch_page("pages/skin_compatibility.py")
    st.markdown("</div>", unsafe_allow_html=True)

# ── How it works ─────────────────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="font-size:0.68rem;font-weight:700;letter-spacing:0.18em;
            text-transform:uppercase;color:var(--pink-400);margin-bottom:0.5rem;">
    How it works
</div>
<div style="font-family:'Playfair Display',serif;font-size:1.8rem;font-weight:600;
            color:var(--ink);margin-bottom:0.3rem;">
    From ingredients to insights
</div>
<div style="font-size:0.84rem;color:var(--ink-mid);margin-bottom:2rem;">
    in milliseconds
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
steps = [
    ("📷", "01", "Upload or Enter",   "Upload an ingredient image or paste the ingredient list directly"),
    ("🤖", "02", "ML Prediction",     "Model analyzes physicochemical properties and interactions"),
    ("📊", "03", "See Results",       "Get skin type suitability, conflict predictions & confidence"),
    ("💡", "04", "Make Decisions",    "Choose products that actually suit your unique skin"),
]
for col, (icon, num, title, desc) in zip([c1, c2, c3, c4], steps):
    with col:
        st.markdown(f"""
        <div class="how-step">
            <div class="how-num">{num}</div>
            <div class="how-icon">{icon}</div>
            <div class="how-title">{title}</div>
            <div class="how-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# ── Model Specs ───────────────────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="font-size:0.68rem;font-weight:700;letter-spacing:0.18em;
            text-transform:uppercase;color:var(--pink-400);margin-bottom:0.5rem;">
    Under the hood
</div>
<div style="font-family:'Playfair Display',serif;font-size:1.8rem;font-weight:600;
            color:var(--ink);margin-bottom:1.5rem;">
    Our Models
</div>
""", unsafe_allow_html=True)

m1, m2 = st.columns(2, gap="large")
with m1:
    st.markdown("""
    <div class="model-spec">
        <div class="model-spec-title">🧪 Task A — Conflict Classifier</div>
        <div class="model-row"><span class="model-key">Model</span><span class="model-val-pink">Random Forest (n=100)</span></div>
        <div class="model-row"><span class="model-key">Task type</span><span class="model-val">Binary classification</span></div>
        <div class="model-row"><span class="model-key">Input</span><span class="model-val">Physicochemical features + 11 engineered</span></div>
        <div class="model-row"><span class="model-key">Imbalance handling</span><span class="model-val">SMOTE on training set</span></div>
        <div class="model-row"><span class="model-key">Recall (conflict)</span><span class="model-val-pink">0.99</span></div>
        <div class="model-row"><span class="model-key">ROC-AUC</span><span class="model-val-pink">0.9933</span></div>
        <div class="model-row"><span class="model-key">Output</span><span class="model-val">Safe / Conflict + confidence</span></div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="model-spec">
        <div class="model-spec-title">✨ Task B — Skin Predictor</div>
        <div class="model-row"><span class="model-key">Model</span><span class="model-val-green">Multi-label ML classifier</span></div>
        <div class="model-row"><span class="model-key">Task type</span><span class="model-val">Multi-class + multi-label</span></div>
        <div class="model-row"><span class="model-key">Input</span><span class="model-val">Ingredient text via TF-IDF</span></div>
        <div class="model-row"><span class="model-key">Training data</span><span class="model-val">9,510 real products</span></div>
        <div class="model-row"><span class="model-key">Skin types</span><span class="model-val-green">5 (Dry, Oily, Normal, Combo, Sensitive)</span></div>
        <div class="model-row"><span class="model-key">Concerns</span><span class="model-val-green">6 (Acne, Dryness, Redness…)</span></div>
        <div class="model-row"><span class="model-key">Output</span><span class="model-val">Suitability scores per skin type</span></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # close page-wrap
st.markdown('<div class="page-footer">© 2025 SkinScan AI — Not a substitute for professional dermatological advice</div>', unsafe_allow_html=True)
