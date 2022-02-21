#-*- coding: utf-8 -*-
"""
@author:MD.Nazmuddoha Ansary
"""
from __future__ import print_function
#---------------------------------------------------------------
# imports
#---------------------------------------------------------------
from coreLib.ocr import BHOCR
from coreLib.utils import LOG_INFO
import os
import matplotlib.pyplot as plt
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import cv2
import tensorflow as tf
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import base64
import numpy as np
import cv2
import pytesseract
#-------------------------------------------
# using gpu
#--------------------------------------------
gpu_devices = tf.config.experimental.list_physical_devices('GPU')
if any(gpu_devices):
    tf.config.experimental.set_memory_growth(gpu_devices[0], True)

#--------------------------------------------------
# main
#--------------------------------------------------
def get_data_url(img_path):
    file_ = open(img_path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url


def main():
    # intro
    st.set_page_config(layout="wide")
    st.title("bnhocr: Handwritten text recognition demo")
    
    with st.sidebar:
        st.markdown("**About bnhocr**")
        st.markdown("bnhocr: Handwritten Bangla text recognition Demo by team **Ovijatrik**.")
        st.markdown("---")
        st.markdown("**in association with:**")
        st.markdown(f'<img src="data:image/gif;base64,{get_data_url("resources/apsis.png")}" alt="apsis">'+'   [apsis solutions limited](https://apsissolutions.com/)',unsafe_allow_html=True)
        st.markdown(f'<img src="data:image/gif;base64,{get_data_url("resources/bai.png")}" alt="bengali ai">'+'   [Bengali.AI](https://bengali.ai/)',unsafe_allow_html=True)
        st.markdown("---")

    # canvas
    st.markdown("*draw a word in the canvas*")
    st.sidebar.header("Configuration")      
    realtime_update = st.sidebar.checkbox("Update in realtime", True) 
    # Create a canvas component
    canvas_result = st_canvas(
        fill_color="rgb(255,255,255)",  # Fixed fill color with some opacity
        stroke_width=5,
        stroke_color="rgb(0,0,0)",
        background_color="rgb(255,255,255)",
        background_image=None,
        update_streamlit=realtime_update,
        height=150,
        drawing_mode="freedraw",
        display_toolbar=st.sidebar.checkbox("Display toolbar", True),
        key="main",
    )
    
    if st.button("Predict"):
        if canvas_result.image_data is not None:
            with st.spinner('Loading model...'):
                ocr=BHOCR("models/model.h5")
    
            with st.spinner('Analyzing...'):
                img=np.asarray(canvas_result.image_data).astype(np.uint8)
                cv2.imwrite("tests/data.png",img)
                st.write("Image saved at:tests/data.png")
                img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                res = pytesseract.image_to_string(img, lang='ben', config='--psm 6')
                st.write(f"Tesseract Recognition Before Transformation:",res.split("\n")[0])
                text,img=ocr.infer(img)
                st.image(img,caption="Grapheme Transformation Result")
                st.write(f"Tesseract Recognition After Transformation:",text)
                
        else:
            st.write("Please Draw a word first!!!")



if __name__ == '__main__':  
    main()