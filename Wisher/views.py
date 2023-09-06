from django.shortcuts import render,redirect
import requests,json

def page(request):
    category = "happiness"
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'Vp71qvPyFEpWhQXVFTWQCg==MTaAUVNU6tFV0V9m'})
    jsondata = json.loads(response.text)
    data = jsondata[0]
    quote = data['quote']
    author = data["author"]
    context = {'quote':quote,'author':author}
    return render(request,'page.html',context)