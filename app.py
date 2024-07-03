# importing libaries
import streamlit as st
import requests, os, uuid, json
from dotenv import load_dotenv
from streamlit.components.v1 import html
import streamlit as st
from colour import Color



load_dotenv()
## Title of the streamlit app
st.write('# Language Translator :male-technologist: ')
st.write(""" Hey :wave: 

Hey This is an application of Azure AI service called Translator.

Choose a language to get started :smiley: 

 """)

# A scrollable side bar showing past translations

# Load the values from .env
key = os.get.environ['KEY']
endpoint = os.environ['ENDPOINT']
location = os.environ['LOCATION']

with st.sidebar:
    target_language = st.selectbox('Avaliable Languages', ['English', 'Sinhala', 'Hindi', 'Japanese', 'Russian', 'Korean', 'Spanish'])
    if target_language == 'English':
        target_language = 'en'
    elif target_language == 'Sinhala':
        target_language = 'si'
    elif target_language == 'Hindi':
        target_language = 'hi'
    elif target_language == 'Japanese':
        target_language = 'ja'
    elif target_language == 'Russian':
        target_language = 'ru'
    elif target_language == 'Korean':
        target_language = 'ko'
    elif target_language == 'Spanish':
        target_language = 'es'

# color_range = list(Color("red").range_to(Color("green"),101))


# Two columns to show translation and input text
t1, t2 = st.columns(2)

# Indicate that we want to translate and the API version (3.0) and the target language
path = '/translate?api-version=3.0'
# Add the target language parameter
target_language_parameter = '&to=' + target_language
# Create the full URL
constructed_url = endpoint + path + target_language_parameter

# Set up the header information, which includes our subscription key
headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}
translated_text = ''
lst = []
with t1:
    st.markdown('#### Your Input text')
    inp_text = st.text_input(" ", "Hello, I'm Trnaslator", key=1)
    if st.button('Translate', key=23):
        # Create the body of the request with the text to be translated
        body = [{ 'text': inp_text }]
        # Make the call using post
        translator_request = requests.post(constructed_url, headers=headers, json=body)
        # Retrieve the JSON response
        translator_response = translator_request.json()
        # Retrieve the translation
        translated_text = translator_response[0]['translations'][0]['text']
        lst.append(f"Your text: {inp_text}" + '\n' + f"Translated text: {translated_text}")

    
with t2:
    st.markdown('#### Translated text')
    # st.markdown("<font color=%s>THIS TEXT WILL CHANGE COLOR</font>" \
    # %Color("red"), unsafe_allow_html=True)
    if translated_text != '':
        st.markdown(f'<p style="font-size:16px;padding:8.75px;"> </p>', unsafe_allow_html=True)
        #st.text(translated_text)
        st.markdown(f'<p style="background-color:#D4F1F4;padding:10px;font-size:16px;border-radius:2%;">{translated_text}</p>', unsafe_allow_html=True)
    


# with st.sidebar:
#     st.markdown("### History")

#     for i in lst:
#         lorem = (
#             f"""
#             <p>{i}</p>
#             """
#             #    * 10
#         )

#     html(lorem, height=400, scrolling=True)