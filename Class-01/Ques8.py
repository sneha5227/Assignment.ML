def extract_domain(email):

    if "@" not in email:
        return "Invalid"

    domain = email.split("@")[1].split(".")[0]

    return domain.title()


email = "developer_99@microsoft.com"

print(extract_domain(email))