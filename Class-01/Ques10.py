def clean_phone(raw_num):
    digits = ""

    for char in raw_num:
        if char.isdigit():
            digits += char

    if len(digits) != 10:
        return "Invalid Number"

    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"


raw_num = "555-987-6543"

print(clean_phone(raw_num))