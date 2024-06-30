import streamlit as st
from llm import GPT_content_generator

# Defining a class for managing session state
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# Main function to run the blog generator app
def My_Blog():
    # Checking if session state is initialized
    if 'session_state' not in st.session_state:
        st.session_state.session_state = SessionState(chat_history=[], chat_count=0)

    # Setting up the Streamlit page configuration
    st.set_page_config(
        page_title='Blog Generator',
        page_icon='🤖'
    )

    # Displaying the subheader and header for the app
    st.subheader('My Custom Blog Generator')
    st.header("Blog's Generator using OpenAI API 🤖")

    # Creating an input field for the user to enter the blog topic
    user_topic = st.text_input("Enter the Blog Topic")

    # Creating two columns for input fields
    col1, col2 = st.columns([6, 6])

    with col1:
        # Creating an input field for the number of words with limits and step size
        no_words = st.number_input('No of Words', min_value=50, max_value=4000, step=50)

    with col2:
        # Creating a dropdown menu for selecting the blog style
        blog_style = st.selectbox("Select Blog Style", [
            "professional", "teenager", "child", "author", "lifestyle", "tech_enthusiast", 
            "niche_hobbyist", "activist", "educator", "entrepreneur", "health_and_fitness_enthusiast"
        ])

    # Creating a button to submit and generate the blog
    submit = st.button("Generate Blog")

    if submit:
        # Generating blog content when the button is clicked
        with st.spinner('Crafting your content, please wait...'):
            generated_blog = GPT_content_generator(blog_style, user_topic, no_words)
            # Incrementing chat count and appending the generated blog to chat history
            st.session_state.session_state.chat_count += 1
            numbered_blog = f"{st.session_state.session_state.chat_count}. {generated_blog}"
            st.session_state.session_state.chat_history.append(numbered_blog)
            # Displaying the generated blog content
            st.write(f'Generated Blog:\n {generated_blog}')
    
    # Creating a button to display chat history
    if st.button("Chat History"):
        for i, chat in enumerate(st.session_state.session_state.chat_history):
            st.text_area(f"Chat {i+1}", value=chat, height=200, disabled=False)

# Running the blog generator app
if __name__ == "__main__":
    My_Blog()
