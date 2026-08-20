def is_palindrome(sentence):
    cleaned = ""

    for char in sentence:
        if char.isalnum():
            cleaned += char.lower()

    return cleaned == cleaned[::-1]


sentence = "Was it a car or a cat I saw?"
print(is_palindrome(sentence))