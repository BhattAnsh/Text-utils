from django.http import HttpResponse
from django.shortcuts import render
import string

#text utils fucntions
def removepunctuation(text):
    text_without_punctuations = ''.join([char for char in text if char not in string.punctuation])
    return text_without_punctuations

def captialize(text):
    captialed = str(text).upper()
    return captialed

def removeNewLine(text):
    removed = str(text).replace("\n", "")
    return removed

#perfroming function according to user choice
def main_function(user_requests, user_text, functions):
    text = user_text
    for i in range(len(user_requests)):
        if user_requests[i] == 'on':
            text = str(functions[str(i)](text))
            print(text)
    return {'result': text}

#rendering the pages and giving the output on the web
def analyze(request):
    return render(request, ['index.html'])

def result(request):
    global user_text
    user_text =(request.POST.get('text', 'default'))
    removepunc = request.POST.get('removepunc', 'off')
    capital = request.POST.get('Capitalize', 'off')
    newline = request.POST.get('newlineremove', 'off')

    #this list will contain the user request
    user_requests = [removepunc, capital, newline]

    #this dict will contain the fuctions
    fucntions = {'0':removepunctuation, '1':captialize, '2':removeNewLine}

    params = main_function(user_requests, user_text, fucntions)

    return render(request, 'result.html', params)

