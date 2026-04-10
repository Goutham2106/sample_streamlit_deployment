import streamlit as st

# ---- Page Config ----
st.set_page_config(page_title="Packers & Movers", page_icon="🚚", layout="centered")

# ---- Custom CSS ----
st.markdown("""
<style>
/* Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #eef2f3, #dfe9f3);
}

/* Card Style */
.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

/* Title */
.title {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    color: #1f4e79;
}

/* Button */
.stButton>button {
    background-color: #1f4e79;
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
    color: #003366;
}
</style>
""", unsafe_allow_html=True)

# ---- Header ----
st.markdown('<div class="title">🚚 Packers & Movers Billing System</div>', unsafe_allow_html=True)

# ---- Input Card ----
st.markdown('<div class="card">', unsafe_allow_html=True)

w = st.number_input("📦 Enter weight (in quintals):", min_value=0)
c_type = st.selectbox("🏠 Select type:", ["domestic", "commercial"])
d = st.number_input("📍 Enter distance (in km):", min_value=0)

st.markdown('</div>', unsafe_allow_html=True)

# ---- Button ----
if st.button("💰 Calculate Bill"):

    price = 0

    # Weight charge
    if w <= 10:
        weight_price = w * 50
    elif w <= 30:
        weight_price = (10 * 50) + (w - 10) * 75
    else:
        weight_price = (10 * 50) + (20 * 75) + (w - 30) * 100

    # Commercial charge
    commercial_charge = 300 if c_type == "commercial" else 0

    # Distance charge
    if d <= 15:
        distance_price = d * 100
    elif d <= 45:
        distance_price = (15 * 100) + (d - 15) * 125
    else:
        distance_price = (15 * 100) + (30 * 125) + (d - 45) * 150

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
