#Import streamlit library
from ast import arg
import streamlit as st
import gpt_2_simple as gpt2

#Function to run model and generate new text

def render_page():
    st.title("Kat AI")
    st.image("kat.png")
    st.text("Click the button below to have Kat AI write you a blog post!")
    st.button(label="Generate blog post", on_click = write_blog_post)

def generate():
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess)
    text = gpt2.generate(sess, return_as_list=True)[0]
    return text

def write_blog_post():
    post_copy = generate()
    st.session_state['post_copy'] = post_copy


render_page()
st.header("Blog post" if 'post_copy' in st.session_state else "")
st.write(st.session_state['post_copy'] if 'post_copy' in st.session_state else "")
