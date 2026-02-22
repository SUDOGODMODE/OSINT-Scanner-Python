from user_scanner.core.orchestrator import generic_validate, Result
from user_scanner.core.helpers import get_random_user_agent

def validate_albicla(user):
    url = f"https://albicla.com/{user}/post/1"
    show_url = f"https://albicla.com/{user}"

    headers = {
        'User-Agent': get_random_user_agent(),
    }

    def process(response):
        if response.status_code == 500 or "500 Post tymczasowo niedostępny" in response.text:
            return Result.taken()
        
        if "404 Nie znaleziono użytkownika" in response.text:
            return Result.available()

        return Result.error(f"Unexpected status: {response.status_code}")

    return generic_validate(url, process, show_url=show_url, headers=headers)


if __name__ == "__main__":
    user = input("Username?: ").strip()
    result = validate_albicla(user)

    if result == 1:
        print("Available!")
    elif result == 0:
        print("Unavailable!")
    else:
        print("Error occurred!")
