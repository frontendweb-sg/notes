# What is request?

- A way to exchange data between a client and server.
- Client sends the request.
- Server responds to the request.
- Sent to a specific URL.
- Message returnd by server is called the response.

**`Request and Response Data:`**

- URL parameters.
- Form Data
- JSON
- Files
- XML

**`Request components:`**

- Method (GET,POST,PUT,DELETE,OPTIONS)
- Data
- Headers
- Authentication (can be included in data or headers)

**`Response components:`**

- Data
- Headers
- Status codes

**`Status code:`**

- 1xx: information
- 2xx: Sucess
- 3xx: Redirect
- 4xx: Client error
- 5xx: Server error

**`Installation:`**

```py
pip install requests
```

**`Write a program:`**

```py
# fetch data from (https://jsonplaceholder.typicode.com/posts)
import requests
def fetch_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # content data
    content_data = response.content
    print(content_data)

    # text data
    text_data = response.text
    print(text_data)

    # json data
    json_data = response.json()
    print(json_data)

    # status code
    print(response.status_code)

    # headers
    headers = response.headers
    print(headers)
```

**`Pass parameters:`**

```py
import requests
def fetch_posts():
    params = {'limit':10,'sort_by':'tittle'}
    response = requests.get('https://jsonplaceholder.typicode.com/posts',params)
```

**`Add headers:`**

```py
import requests

def fetch_posts():
    params = {'limit':10,'sort_by':'tittle'}
    headers={'my-auth': 'sdjfklsjfkldjflsdjflksdjflksdj'}
    response = requests.get('https://jsonplaceholder.typicode.com/posts',params,headers)
```

**`Send data:`**

```py
import requests

# post json data
def add_json_data():
    data = {'name':'pk','email':'abc@gamil.com'}
    response = requests.post('https://jsonplaceholder.typicode.com/posts',json=data)

# post files
def add_files():
    files = {'file': ('hero.jpg', open('hero.jpg','rb'),'images/jpeg')}
    response = requests.post('https://jsonplaceholder.typicode.com/posts',files=files)

# add data
def add_data():
    data = {'name':'pk','email':'abc@gamil.com'}
    response = requests.post('https://jsonplaceholder.typicode.com/posts',data=data)
```

**`Saving an image:`**

```py
import requests

def save_image():
    res = requests.get(
        "https://images.unsplash.com/photo-1533450718592-29d45635f0a9?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")

    print(res.headers)

    with open("lion.jpg", "wb") as f:
        for chunk in res.iter_content(chunk_size=500):
            f.write(chunk)

save_image()
```

**`Handle exception:`**

```py
import requests

res = requests.get("https://httpbisn.org/status/501")

try:
    res.raise_for_status()
except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
    print("ERROR!",e)

print(res)

# timeout error
res = requests.get("https://httpbisn.org/status/501",timeout=0.5)

try:
    res.raise_for_status()
except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError,requests.exceptions.ConnectTimeout) as e:
    print("ERROR!",e)
```

**`Authentication:`**

```py
def basic_auth():
    from requests.auth import HTTPBasicAuth
    try:
        res = requests.get("https://httpbin.org/basic-auth/user/passwd",
                           auth=HTTPBasicAuth('user', 'passwd'))
        print(res.status_code)
    except requests.exceptions.HTTPError as e:
        print("ERROR!", e)

basic_auth()
```
