from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from dotenv import load_dotenv, find_dotenv

def GPT_content_generator(blog_style, user_topic, no_words):
    # Load the API key
    load_dotenv(find_dotenv(), override=True)

    llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.1)

    # Define the prompt template
    template = f"""
        Write a comprehensive blog on the topic "{user_topic}" in the style of {blog_style}. Limit the blog to {no_words} words.

        Ensure the content is engaging and informative. Include practical examples or insights related to the topic.

        Title: 
        Conclusion: 
    """

    prompt_template = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template("You are a helpful AI writing assistant."),
            HumanMessagePromptTemplate.from_template(template)
        ]
    )

    # Use RunnableSequence 
    chain = prompt_template | llm

    response = chain.invoke({
        'blog_style': blog_style,
        'user_topic': user_topic,
        'no_words': no_words
    })

    return f'\n \n \n{response.content}'
