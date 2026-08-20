def validate_username(username):
    username = username.strip()
    if len(username) >= 5 and username.isalnum():
        return username.lower()
    return "Invalid"

   