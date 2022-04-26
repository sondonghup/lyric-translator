import streamlit as st
import translator as tq

st.set_page_config(page_title = '2조')

text = st.text_area("Enter text:",height=None,max_chars=None,key=None,help="Enter your text here -")
st.write("****")

if st.button('Translate Sentence'):
    st.write(" ")
    st.write(" ")
    if text == "":
        st.warning('Please **enter text** for translation')

    else:
      a = tq.add(3,4)
      print(a)
      #translated = translator.translate_eng(text)
      #translated = translated.replace("<|endoftext|>", "")
      #translated = GoogleTranslator(source=option1,target=option2).translate(text=text)
      #st.write("Translated text -")
      #st.info(str(translated))        
