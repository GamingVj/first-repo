# Program 1 A: sum of element of array

# Program 1 A
# sum of elements in given array

def _sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return(sum)
arr = []
arr = [12,3,4,15,45,78,450]
n = len(arr)
ans = _sum(arr)
print("\nSum of the array is",ans,"\n")