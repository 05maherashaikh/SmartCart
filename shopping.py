from google import genai
from google.genai import types
import streamlit as st

client = genai.Client(api_key="AIzaSyBX1KYZBY-2wFULqNMaTa_8sIUuHn-QiU4")

st.title("SmartCart - AI Gadget Shopping Assistant")

st.write("Your AI guide for laptops, smartphones, smartwatches, and gadgets.")

available_categories = {
    #Laptops
    "Dell Inspiron 15": "₹55,000 - Good for students, Intel i5, 16GB RAM",
    "HP Pavilion 14": "₹60,000 - Lightweight, Intel i5, 16GB RAM",
    "Lenovo IdeaPad Slim 5": "₹58,000 - Ryzen 5 processor, good battery",
    "Apple MacBook Air M1": "₹75,000 - Premium laptop with long battery life",
    "ASUS Vivobook 15": "₹52,000 - Intel i5 processor, slim design, good for everyday use",
    "Acer Aspire 5": "₹57,999 - Intel i5 12th Gen, 8GB RAM, 512GB SSD, good multitasking laptop",

    #  Smartphones
"iPhone 13": "₹60,000 - A15 chip, excellent camera, premium performance",
"Samsung Galaxy S21 FE": "₹45,000 - Powerful processor and great display",
"OnePlus Nord CE 3": "₹28,000 - Fast charging and smooth performance",
"Redmi Note 13 Pro": "₹25,000 - Budget phone with strong camera",
"Realme Narzo 60": "₹18,000 - Affordable phone for everyday use",

#  Smart Watches
"Apple Watch SE": "₹29,000 - Fitness tracking and iPhone integration",
"Samsung Galaxy Watch 4": "₹20,000 - Health tracking and Wear OS",
"Noise ColorFit Pro 4": "₹3,500 - Budget smartwatch with fitness tracking",
"Fire-Boltt Ninja Call Pro": "₹2,000 - Bluetooth calling smartwatch",
"boAt Wave Call": "₹2,500 - Stylish smartwatch with calling feature",

#  Earbuds
"Apple AirPods Pro": "₹22,000 - Premium earbuds with noise cancellation",
"Samsung Galaxy Buds 2": "₹10,000 - Good sound and ANC",
"boAt Airdopes 141": "₹1,500 - Budget earbuds with strong battery",
"OnePlus Nord Buds": "₹2,800 - Clear sound and fast pairing",
"Realme Buds Air 3": "₹3,500 - ANC earbuds with good bass",

}

query = st.chat_input("Ask me about laptops")

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
{available_categories}

Be friendly and give clear suggestions.
"""
             ),
            contents=query
        )

    # show AI response
    with st.chat_message("assistant"):
        st.write(response.text)