import streamlit as st

# ---- Page Config ----
st.set_page_config(page_title="Packers & Movers", page_icon="🚚", layout="centered")

# ---- Custom CSS ----
st.markdown("""
<style>

/* Full Background Image */
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1601584115197-04ecc0da31d7");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: black;
}

/* Light Overlay */
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.85);
    z-index: 0;
}

/* Card Style */
.card {
    background: rgba(255, 255, 255, 0.95);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.2);
    margin-bottom: 20px;
    position: relative;
    z-index: 1;
    color: black;
}

/* Title */
.title {
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    color: black;
    margin-bottom: 20px;
    position: relative;
    z-index: 1;
}

/* Labels */
label, .stMarkdown, .stText, .stNumberInput, .stSelectbox {
    color: black !important;
}

/* Button */
.stButton>button {
    background-color: #0a2a43;
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-size: 16px;
}

/* Result Box */
.result {
    background-color: #e6f2ff;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    color: black;
}

</style>
""", unsafe_allow_html=True)

# ---- Title ----
st.markdown('<div class="title">🚚 Packers & Movers Billing System</div>', unsafe_allow_html=True)

# ---- Input Card ----
st.markdown('<div class="card">', unsafe_allow_html=True)

w = st.number_input("📦 Enter weight (in quintals):", min_value=0)
c_type = st.selectbox("🏠 Select type:", ["domestic", "commercial"])
d = st.number_input("📍 Enter distance (in km):", min_value=0)

st.markdown('</div>', unsafe_allow_html=True)

# ---- Button ----
if st.button("💰 Calculate Bill"):

    # Weight Charge
    if w <= 10:
        weight_price = w * 50
    elif w <= 30:
        weight_price = (10 * 50) + (w - 10) * 75
    else:
        weight_price = (10 * 50) + (20 * 75) + (w - 30) * 100

    # Commercial Charge
    commercial_charge = 300 if c_type == "commercial" else 0

    # Distance Charge
    if d <= 15:
        distance_price = d * 100
    elif d <= 45:
        distance_price = (15 * 100) + (d - 15) * 125
    else:
        distance_price = (15 * 100) + (30 * 125) + (d - 45) * 150

    # Total
    total = weight_price + distance_price + commercial_charge

    # ---- Output Card ----
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="result">
    💵 Total Amount: ₹{total}
    </div>
    """, unsafe_allow_html=True)

    st.write("### 📊 Bill Breakdown")
    st.write(f"Weight Charge: ₹{weight_price}")
    st.write(f"Distance Charge: ₹{distance_price}")
    st.write(f"Commercial Charge: ₹{commercial_charge}")

    st.markdown('</div>', unsafe_allow_html=True)
