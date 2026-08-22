def are_anagrams(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    return sorted(str1) == sorted(str2)


str1 = "Dormitory"
str2 = "Dirty room"

print(are_anagrams(str1, str2)) 