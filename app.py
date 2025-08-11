import streamlit as st

def main():
    with st.sidebar:
        st.title("Main menu ")
        st.write("Home")
        st.write("Dashboard")
        st.write("Update")
    

if __name__=='__main__':
    main()