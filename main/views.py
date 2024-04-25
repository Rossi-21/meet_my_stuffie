from django.shortcuts import render
from django.conf import settings
import requests

api_key = settings.API_KEY

def dashboard(request):
    URL = "https://api.openai.com/v1/chat/completions"
    
    stuffie_name = request.GET.get('stuffie-name')
    animal = request.GET.get('animal-type')
    color = request.GET.get('color')
    personality = request.GET.get('personality')
    child_name = request.GET.get('child-name')
    # ChatGPT Configuration
    payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{
        "role": "user", 
        # ChatGPT Prompt
        "content": f"""You are a child's stuffed animal. You are embued with all the magical qualities of 
                    a stuffed imaginary friend. You are {stuffie_name} the stuffed {animal}. 
                    Your personality is {personality}. Your color is {color}.
                    you have unconditional love for your owner who is named {child_name}. 
                    Your should always respond with the voice of {stuffie_name}.
                    """
        }],
    "temperature" : 1.0,
    "top_p":1.0,
    "n" : 1,
    "stream": False,
    "presence_penalty":0,
    "frequency_penalty":0,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    # Get the response from the ChatGPT API
    response = requests.post(URL, headers=headers, json=payload, stream=False)
    # Save the json response as a veriable called data
    data = response.json()
    
    context = {
        'data' : data,
    }
    return render(request, "index.html", context)
