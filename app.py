import streamlit as st
import cv2
import os
from PIL import Image
from app_funcs import *

st.set_page_config(
    page_title="3D Object Tracker",
    page_icon="💫",
    layout="centered",
    initial_sidebar_state="auto",
)

top_image = Image.open('static/banner_top.png')
bottom_image = Image.open('static/banner_bottom.png')
main_image = Image.open('static/main_banner.png')

upload_path = "uploads/"
download_path = "downloads/"

st.sidebar.image(top_image,use_column_width='auto')
segmentation_type = st.sidebar.selectbox('Select 3D Object Tracking type 🎯',["Image","Live Feed"])
st.sidebar.image(bottom_image,use_column_width='auto')

st.image(main_image,use_column_width='auto')
st.title("☕📷 3D Object Tracker 👞🪑")
col1,col2 = st.columns(2)
with col1:
    model_name = st.radio(
     "Please select your object for tracking",
     ('Shoe', 'Chair', 'Cup', 'Camera'))
with col2:
    num_objects = st.slider('Please select max. no. of objects for detection', 1, 20, 5)

if model_name and num_objects and segmentation_type == "Image":
    st.info('✨ Supports all popular image formats 📷 - PNG, JPG, BMP 😉')
    uploaded_file = st.file_uploader("Upload Image 🖼", type=["png","jpg","bmp","jpeg"])
    if uploaded_file is not None:
        with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
            f.write((uploaded_file).getbuffer())
        with st.spinner(f"Working... 💫"):
            uploaded_image = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
            downloaded_image = os.path.abspath(os.path.join(download_path,str("output_"+uploaded_file.name)))
            object_tracking_image(uploaded_image, downloaded_image, model_name, num_objects)
            print("Output Image: ", downloaded_image)
            final_image = Image.open(downloaded_image)
            print("Opening ",final_image)
            st.markdown("---")
            st.image(final_image, caption='This is how your final image looks like 😉')
            with open(downloaded_image, "rb") as file:
                if uploaded_file.name.endswith('.jpg') or uploaded_file.name.endswith('.JPG'):
                    if st.download_button(
                                            label="Download Output Image 📷",
                                            data=file,
                                            file_name=str("output_"+uploaded_file.name),
                                            mime='image/jpg'
                                         ):
                        download_success()

                if uploaded_file.name.endswith('.jpeg') or uploaded_file.name.endswith('.JPEG'):
                    if st.download_button(
                                            label="Download output Image 📷",
                                            data=file,
                                            file_name=str("output_"+uploaded_file.name),
                                            mime='image/jpeg'
                                         ):
                        download_success()

                if uploaded_file.name.endswith('.png') or uploaded_file.name.endswith('.PNG'):
                    if st.download_button(
                                            label="Download output Image 📷",
                                            data=file,
                                            file_name=str("output_"+uploaded_file.name),
                                            mime='image/png'
                                         ):
                        download_success()

                if uploaded_file.name.endswith('.bmp') or uploaded_file.name.endswith('.BMP'):
                    if st.download_button(
                                            label="Download output Image 📷",
                                            data=file,
                                            file_name=str("output_"+uploaded_file.name),
                                            mime='image/bmp'
                                         ):
                        download_success()
    else:
        st.warning('⚠ Please upload your Image file 😯')


if model_name and num_objects and segmentation_type == "Live Feed":
    st.info('✨ The Live Feed from Web-Camera will take some time to load up 🎦')
    live_feed = st.checkbox('Start Web-Camera ✅')
    FRAME_WINDOW = st.image([])
    cap = cv2.VideoCapture(0)

    if live_feed:
        with mp_objectron.Objectron(static_image_mode=False,
                            max_num_objects=num_objects,
                            min_detection_confidence=0.5,
                            min_tracking_confidence=0.5,
                            model_name=str(model_name)) as objectron:
            while cap.isOpened():
                _, frame = cap.read()
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = objectron.process(image)

                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                if results.detected_objects:
                    print("Detected")
                    for detected_object in results.detected_objects:
                        mp_drawing.draw_landmarks(
                            image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
                FRAME_WINDOW.image(rescale_frame(image, percent=150))
    else:
        cap.release()
        cv2.destroyAllWindows()
        st.warning('⚠ The Web-Camera is currently disabled. 😯')

st.markdown("<br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=3D Object Tracker WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a></center><hr>", unsafe_allow_html=True)
