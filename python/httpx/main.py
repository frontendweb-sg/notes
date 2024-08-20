import httpx


def fetch_post():
    headers = {'x-auth-token': "xcjlksfjioewojf"}
    data = httpx.get("http://localhost:3000/posts",
                     params={'title': "hello"}, headers=headers)
    print(data.headers['x-auth-token'])
    print("data", data.status_code)


def add_post(post: dict) -> None:
    data = httpx.post("http://localhost:3000/posts",
                      data=post, params={'isedit': True})

    print(data.status_code)
    print(data.json())


if __name__ == "__main__":
    fetch_post()
    # add_post({"title": "First posts", "body": "this is second posts"})
