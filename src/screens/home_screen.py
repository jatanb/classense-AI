import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout
from src.ui.base_layout import style_background_home
from src.ui.base_layout import style_background_dashboard
def home_screen():

    header_home()
    style_base_layout()
    style_background_home()
    

    col1,col2=st.columns(2)

    with col1:
        st.markdown("""
        <h2 style='color: black;'>I'm Teacher</h2>
        
         """,unsafe_allow_html=True)
        if st.button("teacher portal",icon=':material/arrow_outward:',icon_position='right'):
            st.session_state['login_type']='teacher'
            st.rerun()

    with col2:
        st.markdown("""
        <h2 style='color: black;'>I'm Student</h2>
        
         """,unsafe_allow_html=True)
        if st.button("student portal",icon=':material/arrow_outward:',icon_position='right'):
            st.session_state['login_type']='student'
            st.rerun()
    footer_home()