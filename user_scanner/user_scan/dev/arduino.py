from user_scanner.core.orchestrator import status_validate

def validate_arduino(user):
    url = f"https://forum.arduino.cc/u/{user}.json"
    show_url = "https://arduino.cc"

    return status_validate(url, 404, 200, show_url=show_url)
