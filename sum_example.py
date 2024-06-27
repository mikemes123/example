#The function takes an input of a number and uses that input as a loop, constantly adding the i to the inputted number. 
#Finally printing the answer#
def sum(int):
    for i in range(int):
        int = i + int
    print(int)
sum(5)
sum(10)