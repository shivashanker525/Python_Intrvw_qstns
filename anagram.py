def anagram(string1,string2):
    string1 = string1.replace(" ","").lower()
    string2 = string2.replace(" ","").lower()
    new_string = {}
    for i in string1:
        if i in new_string:
            new_string[i] += 1
        else:
            new_string[i] = 1
    for i in string2:
        if i in new_string:
            new_string[i] -= 1
        else:
            new_string[i] = 1

    for i in new_string:
        if new_string[i] != 0:
            return False
    return True
        
print(anagram("pop","  pop    "))