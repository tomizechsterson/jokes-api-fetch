import requests
import html
import argparse

parser = argparse.ArgumentParser(description="Call the Chuck Norris joke API and return a joke")
parser.add_argument("-id", "--showid", action="store_true", help="Have the output include the joke id. Good for "
                                                                 "providing feedback, if necessary")
parser.add_argument("-i", "--include", choices=(["explicit", "nerdy"]), action="append", help="Choose a category to "
                                                                                              "include if you want to"
                                                                                              " only get jokes from "
                                                                                              "the provided category")
parser.add_argument("-e", "--exclude", choices=(["explicit", "nerdy"]), action="append", help="Choose a category to "
                                                                                              "exclude. Exactly the "
                                                                                              "opposite of the "
                                                                                              "include argument")
parser.add_argument("-f", "--firstName", help="The first name to use to replace Chuck in the returned joke")
parser.add_argument("-l", "--lastName", help="The last name to use to replace Norris in the returned joke")
args = parser.parse_args()

url = "https://api.icndb.com/jokes/random"
params = {}

for arg in vars(args):
    if getattr(args, arg) is not None and arg != "showid":
        params[arg] = getattr(args, arg)

if len(params) > 0:
    url += "?"

for p in params:
    if p == "exclude":
        url += p + "=[" + ",".join(params[p]) + "]&"
    elif p == "include":
        url += "limitTo=[" + ",".join(params[p]) + "]&"
    else:
        url += p + "=" + params[p] + "&"

response = requests.get(url)
if response.ok:
    json = response.json()
    if args.showid:
        print(html.unescape(json["value"]["joke"]) + " (Joke Id: " + str(json["value"]["id"]) + ")")
    else:
        print(html.unescape(json["value"]["joke"]))
else:
    response.raise_for_status()
