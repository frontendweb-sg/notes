import requests


# fetch posts
def get_all_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # you can also get "text" or "content"
    content_data = response.content
    print(content_data)

    text_data = response.text
    print(text_data)

    # status code
    print(response.status_code)

    # headers
    print(response.headers)

    # return json data
    return response.json()


# fetch posts by id and prams
def get_post_by_id(id: int = 1):
    params = {'is_ok': True}
    res = requests.get(
        f"https://jsonplaceholder.typicode.com/posts/{id}", params)
    return res.json()


# add token in headers
def get_users_post(id: int = 1):
    params = {'sort_by': 'title'}
    headers = {'my-token': "jdsfklsjklfjsdkfjslkfjdkl"}
    res = requests.get(
        "https://jsonplaceholder.typicode.com/posts/", params=params, headers=headers)
    return res.json()


# add new data
def add_post():
    data = {'name': 'pk', 'age': 12}
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts", params={'one': 1}, json=data)

    # status code
    print(response.status_code)  # 201

    # return added data
    return response.json()


# upload files
def upload_file():
    files = {'file': ('file.jpg', open('file.jpg', 'rb'), 'images/jpg')}
    res = requests.post(
        "https://jsonplaceholder.typicode.com/posts", files=files)
    return res


# save image from server
def save_image():
    res = requests.get(
        "https://images.unsplash.com/photo-1533450718592-29d45635f0a9?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")

    print(res.headers)

    with open("lion.jpg", "wb") as f:
        for chunk in res.iter_content(chunk_size=500):
            f.write(chunk)


def exception_handle():
    res = requests.get("https://httpbin.org/status/501")
    try:
        res.raise_for_status()
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
        print("ERROR!", e)
    print(res)


def timeout_error():
    res = requests.get("https://httpbin.org/status/501", timeout=0.5)
    try:
        res.raise_for_status()
    except requests.exceptions.ConnectTimeout as e:
        print("ERROR!", e)
    print(res)


def basic_auth():
    from requests.auth import HTTPBasicAuth
    try:
        res = requests.get("https://httpbin.org/basic-auth/user/passwd",
                           auth=HTTPBasicAuth('user', 'passwd'))
        print(res.status_code)
    except requests.exceptions.HTTPError as e:
        print("ERROR!", e)


basic_auth()
