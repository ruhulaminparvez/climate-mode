from django.shortcuts import render
import json
import urllib.request


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=46c96491f6195b98e6f035f167d4a040').read()
        json_data = json.loads(res)
        data = {
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon']) + ',' + str(json_data['coord']['lat']),
            'weather': str(json_data['weather'][0]['description']),
            'temp': str(json_data['main']['temp']) + 'k',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
        }
    else:
        city=''
        data = {}

    return render(request, 'index.html', {'city': city, 'data': data})
