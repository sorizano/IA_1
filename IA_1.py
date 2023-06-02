import streamlit as st
import cv2

# Configurar la página de la aplicación
st.title("Activar Cámara")

# Mostrar los textos "UNSA" y "Gabriela Salas"
st.write("UNSA", "Gabriela Salas")

# Botón para activar la cámara
activar_camara = st.button("Activar Cámara")

# Verificar si se ha activado la cámara
if activar_camara:
    # Inicializar la captura de video desde la cámara
    cap = cv2.VideoCapture(0)

    # Bucle para capturar y mostrar los fotogramas de la cámara
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Mostrar el fotograma capturado
        st.image(frame, channels="BGR")

        # Verificar si se ha presionado el botón de detener
        if st.button("Detener"):
            break

    # Liberar los recursos de la cámara
    cap.release()
