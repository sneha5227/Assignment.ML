def validate_sku(sku):
    sku = sku.strip().upper()

    if (len(sku) == 8 and
        sku[:3].isalpha() and
        sku[3] == "-" and
        sku[4:].isdigit()):

        return "Valid: " + sku

    return "Invalid SKU"


sku = " xYz-9876 "

print(validate_sku(sku))