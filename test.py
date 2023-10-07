list1 = ['bobby', 'hadz', 'com']

# for item1, item2, item3 in zip(list1, list1[1:0], list1[3:0]):
#     # bobby 1 a
#     # hadz 2 b
#     # com 3 c
#     print(item1, item2, item3)


for item1, item2, item3 in zip(list1, list1, list1):
    # bobby 1 a
    # hadz 2 b
    # com 3 c
    print(item1, item2, item3)