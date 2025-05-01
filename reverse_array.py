#Array Reverse
#https://www.geeksforgeeks.org/program-to-reverse-an-array/
def b(arr):
  start=0
  end=len(arr)-1
  while start<end:
    arr[start],arr[end]=arr[end],arr[start]
    start += 1
    end -= 1
  return arr

a=[43,56,7,8,9065]
arr=b(a)
print(arr) 