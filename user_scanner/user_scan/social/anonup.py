from user_scanner.core.orchestrator import status_validate

def validate_anonup(user):
    url = f"https://anonup.com/@{user}"
    show_url = "https://anonup.com"

    return status_validate(url, 302, 200, show_url=show_url)


if __name__ == "__main__":
    user = input("Username?: ").strip()
    result = validate_anonup(user)

    if result == 1:
        print("Available!")
    elif result == 0:
        print("Unavailable!")
    else:
        print("Error occurred!")
