def swapPosition(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


List = [23, 65, 19, 90]
pos1, pos2 = 2, 4

print(swapPosition(List, pos1-2, pos2-1))

# functions to find the sum of all items in dictionary
def sum_of_values(dictionary):
    return sum(dictionary.values())