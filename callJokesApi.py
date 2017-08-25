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
parser.add_argument("-f", "--firstname", help="The first name to use to replace Chuck in the returned joke")
parser.add_argument("-l", "--lastname", help="The last name to use to replace Norris in the returned joke")
args = parser.parse_args()
for arg in vars(args):
    print(arg, getattr(args, arg))

response = requests.get('https://api.icndb.com/jokes/random')
# TODO: Make use of the rest of the above arguments
# firstname: firstName
# lastname: lastName
# include: limitTo (array)
# exclude: exclude (array)
if response.ok:
    json = response.json()
    if args.showid:
        print(html.unescape(json['value']['joke']) + " (Joke Id: " + str(json['value']['id']) + ")")
    else:
        print(html.unescape(json['value']['joke']))
else:
    response.raise_for_status()
