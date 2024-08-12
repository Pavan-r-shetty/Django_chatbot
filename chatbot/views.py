from django.shortcuts import render
from django.http import JsonResponse
import openai

openai_api_key = 'your key'
openai.api_key = openai_api_key


def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    return answer

# Create your views here.
def chatbot(request):

    if request.method == 'POST':

       message = request.POST.get('message')
    #    response = 'Hi this is my response' 
       response = ask_openai(message)
       return JsonResponse({'message': message,'response': response})
    
    return render(request, 'chatbot.html')