from google import genai
from google.genai import types
import streamlit as st

client = genai.Client(api_key=["GEMINI_API_KEY"])

# -------- SESSION STATE --------
if "user" not in st.session_state:
    st.session_state.user = None

if "cart" not in st.session_state:
    st.session_state.cart = []

# -------- PRODUCT DATA --------
products = {
    "Dell Inspiron 15": {"price": 55000, "desc": "Intel i5, 16GB RAM"},
    "HP Pavilion 14": {"price": 60000, "desc": "Lightweight, Intel i5"},
    "Lenovo IdeaPad Slim 5": {"price": 58000, "desc": "Ryzen 5, good battery"},
    "MacBook Air M1": {"price": 75000, "desc": "Premium, long battery"},
    "iPhone 13": {"price": 60000, "desc": "A15 chip, great camera"},
    "Samsung S21 FE": {"price": 45000, "desc": "Great display"},
    "OnePlus Nord CE 3": {"price": 28000, "desc": "Fast charging"},
    "Redmi Note 13 Pro": {"price": 25000, "desc": "Budget camera"},
    "Apple Watch SE": {"price": 29000, "desc": "Fitness tracking"},
    "Fire-Boltt Ninja": {"price": 2000, "desc": "Bluetooth calling"},
}

# ---------------- LOGIN PAGE ----------------
if not st.session_state.user:
    st.title("Login - SmartCart")

    username = st.text_input("Enter your name")

    if st.button("Login"):
        if username.strip():
            st.session_state.user = username
            st.success(f"Welcome {username} 👋")
            st.rerun()
        else:
            st.warning("Please enter your name")

# ---------------- MAIN APP ----------------
else:
    st.title("SmartCart - AI Shopping Assistant")

    # Logout
    if st.button("Logout"):
        st.session_state.user = None
        st.session_state.cart = []
        st.rerun()

    st.write(f"Logged in as: {st.session_state.user}")

    # -------- PRODUCTS --------
    st.subheader("Available Products")

    for product, details in products.items():
        price = details["price"]
        desc = details["desc"]

        col1, col2 = st.columns([3, 1])

        with col1:
            st.write(f"{product} - ₹{price} ({desc})")

        with col2:
            if st.button("Add to Cart", key=product):
                st.session_state.cart.append((product, price))
                st.success(f"{product} added to cart")

    # -------- CART --------
    st.subheader("Your Cart")

    total = 0

    if st.session_state.cart:
        for index, (item, price) in enumerate(st.session_state.cart):
            col1, col2 = st.columns([3, 1])

            with col1:
                st.write(f"{item} - ₹{price}")

            with col2:
                if st.button("Remove", key=f"remove_{index}"):
                    st.session_state.cart.pop(index)
                    st.rerun()

            total += price

        st.write(f"### Total: ₹{total}")

        if st.button("Clear Cart"):
            st.session_state.cart = []
            st.success("Cart cleared")

    else:
        st.write("Your cart is empty")

    # -------- AI CHAT --------
    st.subheader("Ask AI")

    query = st.chat_input("Ask about gadgets")

    if query:
        with st.chat_message("user"):
            st.write(query)

        with st.spinner("Thinking..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                config=types.GenerateContentConfig(
                    system_instruction=f"""
You are a helpful shopping assistant of an online store suggesting gadgets. 
Your tasks: 
1. Answer product questions 
2. Suggest products based on budget 
3. Compare products if user asks 
- Prefer recommending products from the store inventory. 
- If the user asks for a brand/model or specification that is not available in the inventory, politely say it is not available.
 - Then suggest the closest alternative product from the inventory with similar features.

Available products:
{products}
Be friendly and give clear suggestions.
"""
                ),
                contents=query
            )

        with st.chat_message("assistant"):
            st.write(response.text)