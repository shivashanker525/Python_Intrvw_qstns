list1= [1,2,3,4,5,5,6,6,6,6,6,6,7,7,8,8,8,86,8,9,999,25,5,8,9,6,8,4,6,6,4,6,8,7]
list2 = [4,5,6,7,8]
# HEre we are checking whethere a list consisting all unique numbers r not
def unique_list(list1):
    for i in range(len(list1)):
        if len(list1) == len(set(list1)):
            print("unique")
            break
    else:
        print("Not unique")

unique_list(list1)
unique_list(list2)