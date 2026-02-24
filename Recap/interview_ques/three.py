def mainFunc(str1, str2):

    result = ""
    min_len = min(len(str1), len(str2))

    for i in range(1, min_len + 1):
        if str1[:i] == str2[-i:]:
            result = str1[:i]
    return result if len(result) > 0 else -1

str1 = "programming"
str2 = "startpro"

print(mainFunc(str1, str2))


    




