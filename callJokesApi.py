import requests
import html

response = requests.get('https://api.icndb.com/jokes/random')
# TODO: Add the ability to pass params for filter, exclude, first/last name and id
# TODO: Go TDD with this
if response.ok:
    json = response.json()
    print(html.unescape(json['value']['joke']))
else:
    response.raise_for_status()


class JokesApiCaller:

    def __init__(self):
        self.test = 'blah'
