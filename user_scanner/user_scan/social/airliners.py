from user_scanner.core.orchestrator import status_validate

def validate_airliners(user):
    url = f"https://www.airliners.net/user/{user}/profile"
    show_url = "https://www.airliners.net"

    return status_validate(url, 404, 200, show_url=show_url)


if __name__ == "__main__":
    user = input("Username?: ").strip()
    result = validate_airliners(user)

    if result == 1:
        print("Available!")
    elif result == 0:
        print("Unavailable!")
    else:
        print("Error occurred!")

