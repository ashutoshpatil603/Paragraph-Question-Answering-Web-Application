# -*- coding: utf-8 -*-
import torch
#import cdqa
#cdqa_pipeline.to('cpu')

import joblib
import requests
import streamlit as st

#st.set_option('deprecation.showfileUploaderEncoding',False)

@st.cache(allow_output_mutation = True)
def load_model():
    m_jlib = joblib.load('QAmodel5_jlib')
    return m_jlib

def welcome():
    return "Welcome in WebApp"


def Prediction(text,question):
    model = load_model()
    prediction= model.question_answering(text,question)
    return prediction


def main():
    
    
    st.title("Question Answering WebApp")
    st.text("Please Enter the paragraphs")
    text = st.text_input("Enter your paragraph here.....")
    st.text("Please Enter the question")
    question = st.text_input("Enter your question ....")
    

    if text and question :
        st.write("Response :")
        with st.spinner('Searching for answers......'):
            prediction = Prediction(text,question)
            st.write("Question : {}".format(question))
            st.write("Answer : {}".format(prediction))
        st.write("")
        

if __name__ == '__main__':
    main()
