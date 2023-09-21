import requests
apiKey = 'b4985c8f2ee03926a7990747891137ee'
cityName = input('Enter the name of your city: ')
url = f'http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}'
response = requests.get(url)

if response .status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        ftemp = (temp - 273.15) * 9/5 + 32
        ftemp = round(ftemp, 2)
        print('Temperature of {}: {} F'.format(cityName, ftemp))
        print(f'Description of {cityName}: {desc}')
else:
       print("We couldn't fetch the data for this area!")

