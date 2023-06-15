import streamlit as st
import torch
from PIL import Image
from streamlit_drawable_canvas import st_canvas
from torchvision import transforms

from . import config

# Load the model
model = torch.load(config.MODEL_PATH, map_location="cpu")
model.eval()

st.title("Handwritten Digit Classifier")

option = st.selectbox("Choose an input method", ("Upload an image", "Draw a digit"))

if option == "Upload an image":
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        # Preprocess the image
        transform = transforms.Compose(
            [
                transforms.Grayscale(),
                transforms.Resize((28, 28)),
                transforms.ToTensor(),
                transforms.Normalize((0.5,), (0.5,)),
            ]
        )
        image = transform(image)
        image = image.unsqueeze(0)

        # Flatten the image
        image = image.view(image.size(0), -1)

        if st.button("Predict"):
            with torch.no_grad():
                output = model(image)
                _, predicted = torch.max(output.data, 1)
                st.write(f"Predicted Number: {predicted.item()}")

elif option == "Draw a digit":

    # Create columns
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        # Specify canvas parameters in application
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
            stroke_width=10,
            stroke_color="#ffffff",
            background_color="#000000",
            height=300,
            width=300,
            drawing_mode="freedraw",
            key="canvas",
        )

    if canvas_result.image_data is not None:
        img = Image.fromarray(canvas_result.image_data.astype("uint8"), "RGB")
        img = img.convert("1")  # Convert to grayscale

        # Preprocess the image
        transform = transforms.Compose(
            [
                transforms.Grayscale(),
                transforms.Resize((28, 28)),
                transforms.ToTensor(),
                transforms.Normalize((0.5,), (0.5,)),
            ]
        )
        image = transform(img)
        image = image.unsqueeze(0)
        image = image.unsqueeze(0)

        # Flatten the image
        image = image.view(image.size(0), -1)

        if st.button("Predict"):
            with torch.no_grad():
                output = model(image)
                _, predicted = torch.max(output.data, 1)
                st.write(f"Predicted Number: {predicted.item()}")
