import requests
while True:
    api_key = '97864f740b9244528821765942dfbe91'
    base_url = 'http://api.weatherbit.io/v2.0/current'
    city_name = input("enter you city here:")
    url = f"{base_url}?city={city_name}&key={api_key}"
    response = requests.get(url)
    #print(response)
    posts = response.json()
    #print(posts)
    if response.status_code == 200:
        city = (posts['data'][0]['city_name'])
        country = (posts['data'][0]['country_code'])
        temp = (posts['data'][0]['app_temp'])
        fahrenheit = temp* 9/5 + 32
        datetime = (posts['data'][0]['datetime'])
        cloud = (posts['data'][0]['clouds'])
        latitude = (posts['data'][0]['lat'])
        longitude = (posts['data'][0]['lon'])
        sunset = (posts['data'][0]['sunset'])
        weather_description = (posts['data'][0]['weather']['description'])
        print(f"city_name: {city}")
        print(f"country: {country}")
        print(f"temprature: {temp}°C")
        print(f"date: {datetime}")
        print(f"temp_fahernheit: {int(fahrenheit)}f")
        print(f"latitude: {latitude}")
        print(f"longitude: {longitude}")
        print(f"clouds: {cloud}")
        print(f"sunset: {sunset}")
        print(f"weather_description: {weather_description}")
    else:
        print("your api is invalid!")
        break
    choice = ("y/n")
    choice = input("enter your choice y/n:")
    if choice == 'y':
        print("My weather App is ready for you....")
    elif choice == 'n':
        print('Thanks for using our services....\n'
              'Close the Weather App....')
        break
    else:
        print("Thanks for using my services....")
        break
input("press enter to exit ......")
