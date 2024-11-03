from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from dotenv import load_dotenv, find_dotenv

# Function that generates blog content using OpenAI's language model
def GPT_content_generator(blog_style, user_topic, no_words):
    # Load the API key from environment variables
    load_dotenv(find_dotenv(), override=True)
    
    # Initializing the language model with specified parameters
    llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.1)

    # Definining the prompt template to structure the blog content
    template = f"""
        Write a comprehensive blog on the topic "{user_topic}" in the style of {blog_style}. Limit the blog to {no_words} words.
        
        Ensure the content is engaging and informative. Include practical examples or insights related to the topic.
        
        Title: 
        Conclusion: 
    """

    # Creating a chat prompt template
    prompt_template = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template("You are a helpful AI writing assistant."),
            HumanMessagePromptTemplate.from_template(template)
        ]
    )

    # Creating a chain that links the prompt template to the language model
    chain = prompt_template | llm

    # Invoke the model with the provided parameters and get the response
    response = chain.invoke({
        'blog_style': blog_style,
        'user_topic': user_topic,
        'no_words': no_words
    })

    # Returning the generated blog content
    return f'\n\n\n{response.content}'
