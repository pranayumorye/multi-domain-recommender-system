import requests
import pandas as pd

# list_of_searches = ["animal farm", "hunger games"]
list_of_searches = pd.read_csv("../datasets/books10k.csv")["title"].str.replace(r"\(.*\)","")
list_of_searches = list_of_searches[:300]

list_of_wikiids = pd.read_csv("../datasets/booksummaries.csv", delimiter="\t")["Wiki_id"]

base_url = "https://en.wikipedia.org/w/api.php"
headers = {"user-agent": "WikiTitleScraper/1.0"}

parameters = {"action": "query"}
parameters["list"] = "search"
parameters["format"] = "json"
parameters["srlimit"] = "1"
parameters["srprop"] = "size|wordcount|timestamp"

count = 0

for title in list_of_searches:
    parameters["srsearch"] = title + " book novel"
    res = requests.get(base_url, headers=headers, params=parameters)
    res_json = res.json()["query"]["search"][0]
    print(title)
    print(res_json["title"], str(res_json["pageid"]))
    try:
        print(list_of_wikiids[list_of_wikiids == res_json["pageid"]].index[0])
    except:
        print("Not Found in booksummaries.csv")
        count += 1
    print()

print(count)
