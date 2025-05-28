import requests

# response = requests.get("https://jsonplaceholder.typicode.com/users")
# print(response.status_code)          # 200
# print(response.json()[0]["name"])    # First user's name

# data ={"name": "Harsh Pratap Singh",
#        "email": "harsh@13gmail.com"
#       }

# response = requests.post("https://jsonplaceholder.typicode.com/users", json=data)
# print(response.status_code)
# print(response.json())

#Print the title of the first post:

# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(response.status_code)
# print(response.json()[0]["title"])

#Print all userIds (use a loop):

# posts = response.json()

# for post in posts:
#   print(post['userId'])

#Make a POST request to:

# data = {
#   "title": "My First API Post",
#   "body": "Learning APIs with Python",
#   "userId": 101
# }
# response = requests.post("https://jsonplaceholder.typicode.com/posts",json = data)

# response2 = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId": 1})


