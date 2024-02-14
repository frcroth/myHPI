import os

import requests


def main():
    api_key = os.environ["API_KEY"]
    title = os.environ["RELEASE_TITLE"]
    body = os.environ["RELEASE_BODY"]
    host = "localhost:8000"

    response = requests.post(
        f"http://{host}/post",
        json={
            "title": title,
            "body": body,
        },
        headers={"X-API-KEY": api_key},
    )
    if response.status_code == 200:
        print("Post successful")
        exit(0)
    else:
        print("Post failed")
        exit(1)


if __name__ == "__main__":
    main()
