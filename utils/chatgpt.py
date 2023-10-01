import openai
from config import GetOpenAIKey

def CallChatGPTAI(input_text):
    # Use OpenAI GPT API to get the response
    # Make sure to replace 'your_openai_api_key' with your actual OpenAI API key
    openai_api_key = GetOpenAIKey()
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
        apiKey=openai_api_key,
    )
    return response.choices[0].text.strip()