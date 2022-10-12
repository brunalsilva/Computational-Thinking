def verify(number) : # do not change this line!

  # write your code here so that it verifies the card number
    if number[0] != '4':
        return 1
    
    fourth = int(number[3])
    fifth = int(number[5])
    
    if fourth <= fifth:
        return 2
    
    soma = 0
    
    for item in number:
        if item != '-':
            soma += int(item)
    
    if soma % 4 != 0:
        return 3
    
    firsttwo = int(number[0]+number[1])
    seventheight = int(number[7]+number[8])
    
    if firsttwo + seventheight != 100:
        return 4
    
    return True # modify this line as needed

input = "4094-3460-2754" # change this as you test your function
output = verify(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!
