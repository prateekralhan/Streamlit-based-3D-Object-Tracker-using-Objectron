import streamlit as st
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_objectron = mp.solutions.objectron

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def object_tracking_image(uploaded_image, downloaded_image, model_name, num_objects):
    IMAGE_FILES=[]
    IMAGE_FILES.append(uploaded_image)
    with mp_objectron.Objectron(static_image_mode=True,
                            max_num_objects=num_objects,
                            min_detection_confidence=0.5,
                            model_name=str(model_name)) as objectron:
        for idx, file in enumerate(IMAGE_FILES):
            image = cv2.imread(file)
            results = objectron.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            if not results.detected_objects:
              print(f'No box landmarks detected on {file}')
              continue
            print(f'Box landmarks of {file}:')
        annotated_image = image.copy()
        for detected_object in results.detected_objects:
            mp_drawing.draw_landmarks(
              annotated_image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
            mp_drawing.draw_axis(annotated_image, detected_object.rotation,
                               detected_object.translation)
            cv2.imwrite(downloaded_image, annotated_image)


@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def download_success():
    st.balloons()
    st.success('✅ Download Successful !!')
