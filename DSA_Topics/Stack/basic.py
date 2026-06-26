class Stack:
    def is_valid(self, strings):
        abc = ["]", "}", ")"]
        xyz = []

        count = len(strings)

        if count%2 != 0:
            return False

        for i in range(len(strings)):
            if strings[i] not in abc:
                xyz.append(strings[i])

            elif len(xyz) == 0:
                return False
 
            else:
                a = xyz[-1] + strings[i]
                if a == "{}" or a == "[]" or a == "()":
                    xyz.pop()
                else:
                    return False

        return len(xyz) == 0


strings = "([}}])"

obj = Stack()
print(obj.is_valid(strings))