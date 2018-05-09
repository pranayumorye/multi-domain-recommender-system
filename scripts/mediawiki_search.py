import requests
import pandas as pd
import re

# list_of_searches = ["animal farm", "hunger games"]
list_of_searches = pd.read_csv("../datasets/books10k.csv", usecols=["title"])
regex = re.compile(r"\(.*\)")
list_of_searches = list_of_searches[3002:4001]
list_of_pageids = pd.read_csv("../datasets/booksummaries.csv", delimiter="\t")["Wiki_id"]
normalised_df = pd.read_csv("../datasets/titles_and_pageids.csv", delimiter="\t")

base_url = "https://en.wikipedia.org/w/api.php"
headers = {"user-agent": "WikiTitleScraper/1.0"}

parameters = {"action": "query"}
parameters["list"] = "search"
parameters["format"] = "json"
parameters["srlimit"] = "1"
parameters["srprop"] = "size|wordcount|timestamp"
count = 0

for idx, title in list_of_searches.itertuples():
    if normalised_df.iloc[idx]["wiki_id"] != -1:
        continue
    title = regex.sub("", title)
    parameters["srsearch"] = title + " book novel"
    res = requests.get(base_url, headers=headers, params=parameters)
    try:
        res_json = res.json()["query"]["search"][0]
    except:
        print("No search results returned")
    print(title)
    print(res_json["title"], str(res_json["pageid"]))
    try:
        booksummaries_index = list_of_pageids[list_of_pageids == res_json["pageid"]].index[0] 
        print(booksummaries_index)
        normalised_df.set_value(idx, "booksummaries_index", booksummaries_index)
        normalised_df.set_value(idx, "wiki_id", res_json["pageid"])
    except:
        print("Not Found in booksummaries.csv")
        count += 1
    print()

print(count)
normalised_df.to_csv("../datasets/titles_and_pageids.csv", sep="\t", index=False)
