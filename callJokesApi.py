import requests
import html
import argparse


def create_parser():
    result_parser = argparse.ArgumentParser(description="Call the Chuck Norris joke API and return a joke")
    result_parser.add_argument("-id", "--showid", action="store_true",
                               help="Have the output include the joke id. Good for "
                                    "providing feedback, if necessary")
    result_parser.add_argument("-i", "--include", choices=(["explicit", "nerdy"]), action="append",
                               help="Choose a category to "
                                    "include if you want to"
                                    " only get jokes from "
                                    "the provided category")
    result_parser.add_argument("-e", "--exclude", choices=(["explicit", "nerdy"]), action="append",
                               help="Choose a category to "
                                    "exclude. Exactly the "
                                    "opposite of the "
                                    "include argument")
    result_parser.add_argument("-f", "--firstName", help="The first name to use to replace Chuck in the returned joke")
    result_parser.add_argument("-l", "--lastName", help="The last name to use to replace Norris in the returned joke")
    return result_parser


def parse_args_for_query(arguments):
    result_params = {}
    for arg in vars(arguments):
        if getattr(arguments, arg) is not None and arg != "showid":
            result_params[arg] = getattr(arguments, arg)

    return result_params


def generate_url(parameters):
    result_url = "https://api.icndb.com/jokes/random"

    if url_requires_query_string(parameters):
        result_url += "?"

    for p in parameters:
        if p == "exclude":
            result_url += p + "=[" + ",".join(parameters[p]) + "]&"
        elif p == "include":
            result_url += "limitTo=[" + ",".join(parameters[p]) + "]&"
        else:
            result_url += p + "=" + parameters[p] + "&"

    return result_url.rstrip("&")


def url_requires_query_string(parameters):
    return len(parameters) > 0


def print_joke(r, arguments):
    json = r.json()
    if arguments.showid:
        print(html.unescape(json["value"]["joke"]) + " (Joke Id: " + str(json["value"]["id"]) + ")")
    else:
        print(html.unescape(json["value"]["joke"]))

parser = create_parser()
args = parser.parse_args()
params = parse_args_for_query(args)
url = generate_url(params)
response = requests.get(url)

if response.ok:
    print_joke(response, args)
else:
    response.raise_for_status()
