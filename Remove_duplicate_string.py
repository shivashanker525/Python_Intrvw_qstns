str1 = "GeeksforGeeks"

def remove_duplicate_without_order(str1):
    return "".join(set(str1))


print(remove_duplicate_without_order(str1))


from collections import OrderedDict
def remove_duplicate_with_order(str1):
    return "".join(OrderedDict.fromkeys(str1))


print(remove_duplicate_with_order(str1))