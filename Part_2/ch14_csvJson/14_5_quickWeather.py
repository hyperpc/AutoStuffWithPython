#! python3
import requests, json, sys, pprint

def LoadJsonWeather(appid, location):
    '''
    # compute location from command line arguments.
    if len(sys.argv) < 3:
        print('Usage: quickWeather.py location')
        sys.exit()
    appid = sys.argv[1]
    location = ' '.join(sys.argv[2:])
    '''

    # download the json data from OpenWeatherMap.org's API
    url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (location, appid) # to get current weather
    # url = 'https://pro.openweathermap.org/data/2.5/forecast/hourly?q=%s&appid=%s' % (location, appid) # to get weather forecast for 4 days by hour
    response = requests.get(url)
    response.raise_for_status()
    print('Raw data: ')
    pprint.pprint(response.text)

    # load json data into a python variable.
    weatherData = json.loads(response.text)
    print('Json data: ')
    print(weatherData)
    # print weather description
    w = weatherData['weather']
    print()
    print('Current weather in %s: ' % (location))
    print()
    print(w[0]['main'], '-', (w[0]['description']))

    '''
    w = weatherData['list']
    print('Current weather in %s: ' % (location))
    print(w[0]['weather'][0]['main'], '-', (w[0]['weather'][0]['description']))
    print()
    print('Tomorrow: ')
    print(w[1]['weather'][0]['main'], '-', (w[1]['weather'][0]['description']))
    print()
    print('Day after tomorrow: ')
    print(w[2]['weather'][0]['main'], '-', (w[2]['weather'][0]['description']))
    '''

def main():
    appid = 'my_api_id'  # obtain the appid from openWeatherMap.org after you registed as member
    location = 'San Francisco'
    LoadJsonWeather(appid, location)

if __name__ == '__main__':
    main()
