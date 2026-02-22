from user_scanner.core.orchestrator import generic_validate, Result


def validate_anilist(user):
    url = "https://graphql.anilist.co"
    show_url = f"https://anilist.co/user/{user}"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {"query": "query{User(name:\"" + user + "\"){id name}}"}

    def process(response):
        if response.status_code == 200 and "\"id\":" in response.text:
            return Result.taken()

        if response.status_code == 404 or "Not Found" in response.text:
            return Result.available()

        return Result.error(f"Unexpected status: {response.status_code}")

    return generic_validate(url, process, show_url=show_url, method="POST", json=payload, headers=headers)


if __name__ == "__main__":
    user = input("Username?: ").strip()
    result = validate_anilist(user)

    if result == 1:
        print("Available!")
    elif result == 0:
        print("Unavailable!")
    else:
        print("Error occurred!")
