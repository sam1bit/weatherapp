from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    data={}
    if request.method=='POST':
        city=request.POST['city']
        source=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=06907b5faf6f34aff939387ea34a21f6').read()
        list_of_data=json.loads(source)
        print(list_of_data)
        data={
            'Country_code':list_of_data['sys']['country'],
            'Coordinate':list_of_data['coord']['lon'],
            'Weather':list_of_data['weather'][0]['description'],
            'Temperature':str(list_of_data['main']['temp'])+'k',
            'Humidity':list_of_data['main']['humidity']
            }
    print(data)
    return render(request,'index.htm',data)