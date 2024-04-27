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
    prompt = request.GET.get('prompt')
    # ChatGPT Configuration
    
    messages =  [{
        "role": "system", 
        # ChatGPT Prompt
        "content": f"""You are a child's stuffed animal. You are embued with all the magical qualities of 
                    a stuffed imaginary friend. You are {stuffie_name} the stuffed {animal}. 
                    Your personality is {personality}. Your color is {color}.
                    you have unconditional love for your owner who is named {child_name}. 
                    Your should always respond with the voice of {stuffie_name}.
                    """
        }]
        
    messages.append({
        "role": "user",
        "content": f"{prompt}"
    })
    
    payload =  {
        "model": "gpt-3.5-turbo",
        "messages" : messages,    
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
    try:
        # Get the response from the ChatGPT API
        response = requests.post(URL, headers=headers, json=payload, stream=False)
        # Save the json response as a variable called data
        data = response.json()
        print("Response from OpenAI API:", data)  # Print the response for debugging
        
        # Check if the response contains 'choices' key
        if 'choices' in data:
            bot_response = data["choices"][0]["message"]["content"]
        else:
            bot_response = "Error: No bot response found"
    except Exception as e:
        print("Error processing response:", e)
        bot_response = "Error: Unable to process bot response"
    
    
    
    
    # Save the json response as a veriable called data
    data = response.json()
    
    messages.append({
        "role": "assistant",
        "content": bot_response
    })
    
    context = {
        'data' : data,
    }
    return render(request, "index.html", context)
