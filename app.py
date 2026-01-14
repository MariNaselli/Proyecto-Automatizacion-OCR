import streamlit as st
import pytesseract
from PIL import Image

# Usamos la ruta directa para evitar el error de "tesseract no se reconoce"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.title("Mi Primer Automatizador OCR")

archivo = st.file_uploader("Subí una imagen", type=["jpg", "png", "jpeg"])

if archivo is not None:
    img = Image.open(archivo)
    st.image(img, caption="Imagen cargada")
    
    # Extraer el texto
    with st.spinner('Leyendo...'):
        texto = pytesseract.image_to_string(img, lang='spa')
        st.write("### Texto detectado:")
        st.success(texto)