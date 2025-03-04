import streamlit as st
import requests
from io import BytesIO
from PIL import Image

# ✅ Replace with your valid Hugging Face API token
HUGGING_FACE_TOKEN = "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"

# ✅ Correct API endpoint for FLUX.1-schnell model (Fixed missing quote)
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"

# ✅ Function to generate the logo
def generate_logo(prompt):
    headers = {"Authorization": f"Bearer {HUGGING_FACE_TOKEN}"}
    payload = {"inputs": prompt}  # FLUX model expects only the prompt
    
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    elif response.status_code == 403:
        st.error("⚠️ 403 Forbidden: Ensure you have accepted the model terms on Hugging Face.")
    elif response.status_code == 429:
        st.error("⚠️ 429 Too Many Requests: API rate limit exceeded. Try again later.")
    else:
        st.error(f"⚠️ API Error {response.status_code}: {response.text}")
    return None

# ✅ Streamlit interface
def main():
    st.title("🎨 AI Logo Generator (FLUX.1-schnell)")

    # Instructions
    st.write("Enter a description of the logo you want, and the AI will generate it for you!")

    # User input
    prompt = st.text_input("🔤 Enter your logo description:", "A futuristic tech logo")

    # Generate button
    if st.button("🚀 Generate Logo"):
        st.write("⏳ Generating your logo... Please wait.")
        image = generate_logo(prompt)

        if image:
            st.image(image, caption="✅ Generated Logo", use_column_width=True)

# ✅ Run the app
if __name__ == "__main__":
    main()
