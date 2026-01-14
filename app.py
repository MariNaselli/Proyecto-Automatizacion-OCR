import streamlit as st
import pytesseract
from PIL import Image
import shutil

st.set_page_config(page_title="OCR Pro", page_icon="📝")

tesseract_path = shutil.which("tesseract")

if not tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.title("Transcriptor Automático")
st.write("Convierte el contenido de tus imágenes en texto para descargar.")

archivo = st.file_uploader("Selecciona una imagen (JPG, PNG)", type=["jpg", "png", "jpeg"])

if archivo is not None:
    img = Image.open(archivo)
    
    st.image(img, use_container_width=True, caption="Imagen cargada")
    
    st.divider()
    
    with st.spinner('Procesando...'):
        try:
            
            texto = pytesseract.image_to_string(img, lang='spa+eng')
            
            if texto.strip():
                
                st.text_area("Texto Detectado:", texto, height=400)
                
                st.download_button(
                    label="⬇️ Descargar Texto",
                    data=texto,
                    file_name="resultado_ocr.txt",
                    mime="text/plain"
                )
            else:
                st.warning("No se encontró texto en la imagen.")
        except Exception as e:
            st.error(f"Error técnico: {e}")
            

