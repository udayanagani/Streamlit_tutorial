import streamlit as st
st.sidebar.title("This is written inside the sidebar")
st.sidebar.button("Button")
st.sidebar.radio("Pick your gender",["Male","Female"] )

container = st.container()
container.write("This is written inside the container")
st.write("This is written outside the container")
