def check_palindrome_num(nums):

    s_num = str(nums)

    l = 0
    r = len(s_num)-1
    
    while l<r:
        if s_num[l] != s_num[r]:
            return False
        l += 1
        r -= 1
        
    return True

num = 1221
print(check_palindrome_num(num))




