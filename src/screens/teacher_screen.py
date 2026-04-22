import streamlit as st
from src.ui.base_layout import style_background_dashboard,style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
def teacher_screen():
    header_dashboard()
    style_background_dashboard()
    style_base_layout()
    
    
    
    
    if 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type=="register":
        teacher_screen_register()
        
     

def teacher_screen_login():
   c1,c2=st.columns(2,vertical_alignment='center',gap='xxlarge')

   with c1:
        header_dashboard()
   with c2:
        if st.button("Go back to Home",type="secondary",key='loginbackbtn',shortcut="control+backspace"):
            st.session_state['login_type']=None
            st.rerun()
        

   st.header("Login using password",text_alignment="center")
   st.space()

   teacher_username=st.text_input("Enter username",placeholder="ananyaroy")

   

   teacher_pass=st.text_input("Enter password",type="password",placeholder="Enter password")

   

   st.divider()

   bt1,bt2=st.columns(2)

   with bt1:
       st.button("Login",icon=':material/passkey:',shortcut='control+enter',width='stretch')
   with bt2:
       if st.button("Register",type="primary",icon=':material/passkey:',width='stretch'):
           st.session_state.teacher_login_type='register'

   footer_dashboard()




def teacher_screen_register():
   
   c1,c2=st.columns(2,vertical_alignment='center',gap='xxlarge')

   with c1:
        header_dashboard()
   with c2:
        if st.button("Go back to Home",type="secondary",key="loginbackbtn",shortcut='control+backspace'):
           st.session_state['login_type']=None
           st.rerun()
   st.header("register teacher profile")
        
   st.space()
   teacher_username=st.text_input("Enter username",placeholder="ananyaroy")

   teacher_name=st.text_input("Enter name",placeholder="Ananya Roy")
   
   teacher_pass=st.text_input("Enter password",type="password",placeholder="Enter password")

   teacher_confirm_password=st.text_input("confirm your password",type="password",placeholder="enter password")
   
   st.divider()

   bt1,bt2=st.columns(2)

   with bt1:
       st.button("Register now",icon=':material/passkey:',shortcut='control+enter',width='stretch')
   with bt2:
       if st.button("Login instead",type="primary",icon=':material/passkey:',shortcut='control+enter',width='stretch'):
           st.session_state.teacher_login_type='login'
           st.rerun()

   footer_dashboard()

   