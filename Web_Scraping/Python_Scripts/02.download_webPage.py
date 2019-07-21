import requests as re

response_obj = re.get('https://automatetheboringstuff.com/files/rj.txt')

try:
    response_obj.raise_for_status()
    playFile = open('RomeoAndJuliet.txt', 'wb')
    for chunk in response_obj.iter_content(100000):
        playFile.write(chunk)
except Exception as exc:
    print('There was a problem: %s' % (exc))

