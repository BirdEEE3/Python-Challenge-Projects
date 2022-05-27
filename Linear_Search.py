
#           Basic consecutive numbers

arr = [1,2,3,4,5,6,7,8,9,10]
n = int(input("Input the number you need to find: "))

for x in range(len(arr)):
    if n == arr[x]:
        print("The number", n,"is at index ",x)
    elif n not in arr:
        print("Number not available")
        break


#           Letters

arr2 = ["a","b","c","d","f","g","h","i","j","k","l","o"]
n2 = str(input("Input the letter you need to find: "))

for let in range(len(arr2)):
    if n2 == arr2[let]:
        print("The letter", n2, "is at the index", let)
    elif n2 not in arr2:
        print("The letter is not available")
        break
