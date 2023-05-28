import streamlit as st

def generate_sitemap(blog_name):

    sitemap_url = f"https://{blog_name}.blogspot.com/atom.xml?redirect=false&start-index=1&max-results=500"

    return sitemap_url

# Streamlit application

st.title("Blogger Sitemap Generator")

# Input form

blog_name = st.text_input("Enter the name of your Blogger website (without 'blogspot.com')")

# Generate sitemap

if st.button("Generate Sitemap"):

    if blog_name:

        sitemap_url = generate_sitemap(blog_name)

        st.write("Sitemap:", sitemap_url)

    else:

        st.warning("Please enter the name of your Blogger website.")

