import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/Daddy_Finn_2022.jpg')

with col2:
    st.title('Dan Sanger')
    content = """
    Hi, I'm Dan! I am a freelance software developer based in Longmont, Colorado. I am a father, avid skier, hiker,
    and lover of all things outdoors. I have previously been the owner and co-founder of Wild Tree Naturals, LLC, 
    an organic bath and body care company. My goal is to find a software development position with a dynamic 
    organization where I can put my multiple tech skills, business experience, and soft skills to good use!
    """
    st.info(content)


content2 = """
Below you can find some of the apps that I have created! Feel free to contact me!
"""
st.write(content2)