import streamlit as st

st.title("🚚 Packers & Movers Billing System")

# User Inputs
w = st.number_input("Enter weight (in quintals):", min_value=0)
c_type = st.selectbox("Select connection type:", ["domestic", "commercial"])
d = st.number_input("Enter distance (in km):", min_value=0)

if st.button("Calculate Bill"):
    
    price = 0

    # Weight charge
    if w <= 10:
        price = w * 50
    elif w <= 30:
        price = (10 * 50) + (w - 10) * 75
    else:
        price = (10 * 50) + (20 * 75) + (w - 30) * 100

    # Commercial charge
    if c_type == "commercial":
        price += 300

    # Distance charge
    distance_price = 0

    if d <= 15:
        distance_price = d * 100
    elif d <= 45:
        distance_price = (15 * 100) + (d - 15) * 125
    else:
        distance_price = (15 * 100) + (30 * 125) + (d - 45) * 150

    total = price + distance_price

    st.success(f"💰 Total Amount: ₹{total}")
