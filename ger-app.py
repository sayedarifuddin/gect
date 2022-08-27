import streamlit as st
import language_check from language_tool_python


@st.cache(allow_output_mutation=True)
def get_model():
    tool = language_check.LanguageToolPublicAPI('en-US')
    return tool


tool = get_model()

with st.form(key='my_form'):
    prompt = st.text_area(label='Enter sentence', value=" ")
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        #m = tool.correct(prompt)
        #st.write(m)
        
        m = tool.check(prompt)
        st.write(len(m))
