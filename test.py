import time
import requests


# for i, server_url in enumerate(["https://54.176.0.0:5000/query_items/", "http://54.176.0.0:5000/add_items/"][::-1]):
i = 1
# server_url = "http://54.176.0.0:5000/query_items/"
# server_url = "http://54.176.0.0:5000/add_cheaters/"
server_url = "http://localhost:5000/query_items/"
if i == 1:
    # List of usernames to query
    usernames = [ "muncher", "dragondeeznuts", "testnutsack"]
    usernames.append("fuzzylogic12")

    t1 = time.time()
    # Send the POST request with JSON data
    response = requests.post(server_url, json=usernames)

    # Print the response content
    print(response.json())
    print(time.time() - t1)

