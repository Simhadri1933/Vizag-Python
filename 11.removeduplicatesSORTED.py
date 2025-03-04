# def removedup(items):
#     list2 = []
#     for i in items:
#         if i not in list2:
#             list2.append(i)
#     return list2
# items = [0,4,6, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# print(removedup(items))
def removeDuplicate(items):
    list1 = []
    for i in items:
        if i not in list1:
            list1.append(i)
    return list1

items = [0, 0,8,1, 1,6, 1, 2, 2, 3, 3, 4]
print(removeDuplicate(items))