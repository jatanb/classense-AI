import streamlit as st


def style_background_home():
    st.markdown("""
       <style>
                .stApp{
                background: #1f2939 !important;
                }

                .stApp div[data-testid="stColumn"]{
                background-color:#ffe2c6 !important;
                padding:1.5rem !important;
                border-radius:3rem !important
                }
                
       </style>

                """
            ,unsafe_allow_html=True)

def style_background_dashboard():
    st.markdown("""
       <style>
                .stApp{
                background: ##2563eb !important;
                }
                
       </style>

                """
            ,unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
       <style>
            @import url('https://fonts.googleapis.com/css2?family=Abel&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Abel&family=Outfit:wght@100..900&display=swap');
            /*hide top bar of streamlit*/

            #MainMenu,footer,header{
                 visibility:hidden;
                }

            .block-container{
                 padding-top:1.5rem !important;
                }
            h1{
                 font-family: 'Climate Crisis',sans-serif !important;
                 font-size: 3.5rem !important;
                 line-height:1.1 !important;
                 margin-bottom:0rem !important;
                }
            h2{
                 font-family: 'Climate Crisis',sans-serif !important;
                 font-size: 3.5rem !important;
                 line-height:1.1 !important;
                 margin-bottom:0rem !important;
                }
            h3,h4,p,span{
                 font-family: 'outfit', sans-serif ;
                }

            button{
                 border-radius: 1.1rem !important;
                 background: #3b82f6 !important;
                 color: white !important;
                 padding: 10px 20px !important;
                 border: none !important;
                 transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                 border-radius: 1.1rem !important;
                 background: #2563eb !important;
                 color: white !important;
                 padding: 10px 20px !important;
                 border: none !important;
                 transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                 border-radius: 1.1rem !important;
                 background: #4b5563 !important;
                 color: white !important;
                 padding: 10px 20px !important;
                 border: none !important;
                 transition: transform 0.25s ease-in-out !important;
                }
                
                
                
       </style>

                """
            ,unsafe_allow_html=True)