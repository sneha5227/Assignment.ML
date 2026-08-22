city = " nEw dELhi "

city = city.strip()

if all(char.isalpha() or char == " " for char in city):
    print(city.title())
else:
    print("Invalid city")