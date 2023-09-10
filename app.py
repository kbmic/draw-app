from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas


drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("freedraw", "circle" ))

stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)

stroke_color = st.sidebar.color_picker("Stroke color hex: ")

bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
  
    height=150,
    drawing_mode=drawing_mode,
    key="canvas",
)

