from user_scanner.core.orchestrator import generic_validate, Result


def validate_archwiki(user):
    url = f"https://wiki.archlinux.org/api.php?action=query&format=json&list=users&ususers={user}&usprop=cancreate&formatversion=2"
    show_url = "https://wiki.archlinux.org"

    def process(response):
        if "\"userid\":" in response.text:
            return Result.taken()
        if "\"missing\":true" in response.text:
            return Result.available()
        return Result.error(f"Unexpected status: {response.status_code}")

    return generic_validate(url, process, show_url=show_url)


if __name__ == "__main__":
    user = input("Username?: ").strip()
    result = validate_archwiki(user)

    if result == 1:
        print("Available!")
    elif result == 0:
        print("Unavailable!")
    else:
        print("Error occurred!")
