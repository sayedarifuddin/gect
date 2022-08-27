import streamlit as st
import language_tool_python

@st.cache(allow_output_mutation=True)
def get_model():
    tool = language_tool_python.LanguageToolPublicAPI('en-US')
    return tool

tool = get_model()

st.markdown("<h1 style='text-align: center; color: green;'>Grammar Error Counter (en-US)</h1>", unsafe_allow_html=True)

with st.form(key='my_form'):
    #prompt = st.text_area(label='Type something...', value="")
    prompt = st.markdown('Streamlit is **_really_ cool**.')
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        m = tool.check(prompt)
        st.write(len(m))
