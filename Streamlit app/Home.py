import streamlit as st

# Function to set up the page configuration
def configure_page():
    st.set_page_config(
        page_title="Easy Bus", 
        page_icon="../images/logo.png", 
        layout='wide'
    )

# Function to display the logo and tagline
def display_home_page():
    col1, col2, col3 = st.columns([1, 2, 2])
    with col2:
        st.image("../images/logo.png", width=470)
    
    c1, c2, c3 = st.columns([1, 4, 1])
    with c2:
        st.write("##### Your Ultimate Bus Companion – Find the Perfect Ride, Effortlessly!")

# Main function to run the app
def main():
    configure_page()
    display_home_page()

# Run the app
if __name__ == "__main__":
    main()
