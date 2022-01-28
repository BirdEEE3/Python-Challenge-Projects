from zipfile import ZIP_BZIP2


i = 1 

#               Basic FizzBuzz(3 and 5)
# while i<=100:
#     if i%3 == 0 and i%5 == 0:
#         print("FizzBozz")
#     elif i%5 == 0:
#         print("Buzz")
#     elif i%3 == 0:
#         print("Fizz")
#     else:
#          print(i)
#     i+=1 

    
#              Complex FizzBuzz(any int)
#   getting values
x = int(input("enter an integer for Fizz: "))
z = int(input("Enter an integer for Buzz: "))

while i<=100:
     if i%x == 0 and i%z == 0:
         print("FizzBuzz")
     elif i%x == 0:
          print("Fizz")
     elif i%z == 0:
          print("Buzz")
     else:
          print(i)
     i+=1