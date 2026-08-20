def clean_sentence(text):
    words = text.split()
    text = " ".join(words)
    return text.capitalize()


text = " python is a very  powerful language "
print(clean_sentence(text))