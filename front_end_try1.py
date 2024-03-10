# Libraries Imported
import streamlit as st
import io
import csv


# to disable warning by file_uploader going to convert into io.TextIOWrapper
st.set_option('deprecation.showfileUploaderEncoding', False)

# Sidebar and main screen text and title.
st.title("WhatsApp Chat Analyzer 😃")
st.markdown(
    "This app is used to analyze your WhatsApp Chat using the exported text file 📁.")
st.sidebar.image("./assets/images/banner.jpeg", use_column_width=True)
st.sidebar.title("Analyze:")
# ... (rest of the sidebar content)

# Upload feature for txt file and drop-down menu for date format selection
st.sidebar.markdown('**Upload your chat text file:**')
date_format = st.sidebar.selectbox('Please select the date format of your file:',
                                   ('mm/dd/yyyy', 'mm/dd/yy',
                                    'dd/mm/yyyy', 'dd/mm/yy',
                                    'yyyy/mm/dd', 'yy/mm/dd'), key='0')
filename = st.sidebar.file_uploader("", type=["txt"])
st.sidebar.markdown("**Don't worry your data is not stored!**")
st.sidebar.markdown("**Feel free to use 😊.**")

# Load data function
@st.cache_data
def load_data(date_format=date_format):
    # ... (rest of the function)

# Main Streamlit app logic
if filename is not None:
    try:
        contents, data = load_data()
        # ... (rest of the logic)
        
        

    except Exception as e:
        st.error("Error: {}".format(e))
        # ... (rest of the error handling)

