import requests


for i, server_url in enumerate(["http://0.0.0.0:5000/query_items/", "http://0.0.0.0:5000/add_items/"][::-1]):

    if i == 1:
        usernames.append("fuzzylogic12")
    # List of usernames to query
    usernames = ["stockfish", "komodo", "cheater"]

    # Send the POST request with JSON data
    response = requests.post(server_url, json=usernames)

    # Print the response content
    print(response.json())

