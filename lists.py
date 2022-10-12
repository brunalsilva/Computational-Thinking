def test() : # do not change this line!
    values = [4, 7, 8, 9, -5] # do not change this line!
# write your code here so that it modifies values
# be sure to indent your code!
    if values[-1] < 0:
        values.pop(-1)
    
    average = (values[0]+values[1])/2
    values.insert(1, average)
    
    first = values[0]
    last = values[-1]
    
    values[0] = last
    values[-1] = first
    
    print(values)
    return values # do not change this line!
# do not write any code below here
test() # do not change this line!
# do not remove this line!
