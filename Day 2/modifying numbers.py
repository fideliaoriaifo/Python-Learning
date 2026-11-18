print (8/3) #this will return 2.6666666666666665, because division always returns a float
#to convert to an interger
print (int(8/3)) #this will return 2, because we are converting the float to an integer
print (round(8/3)) #this will return 3, because we are rounding the float to the nearest whole number
#specify the number of decimal places to round to
print (round(8/3, 2)) #this will return 2.67

#floor division - returns the largest integer less than or equal to the result of the division
print (8//3) #this will return 2, because floor division returns the largest integer less than 
#or equal to the result of the division

result = 4/2
result /= 2 #this is the same as result = result / 2
print (result)