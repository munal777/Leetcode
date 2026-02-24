def mainFunc(sentences):

    count = 0

    for s in sentences:
        s_arr = s.lower().split()
        curr_count = len(set(s_arr))

        if curr_count > count:
            count = curr_count
    
    return count




sen = ["The quick brown fox", "the fox fox quick quick"]
print(mainFunc(sen))

