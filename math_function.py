#math founction
#max function
def max(num1,num2):
    if num1>num2:
        return num1
    elif num2>num1 :
        return num2 
    else :
        return None 
#min function
def min(num1,num2):
    if num1<num2:
        return num1
    elif num2<num1 :
        return num2   
    else :
        return None 
def abs(num):
    if num>=0  :
        return num
    return -num


        
def our_max(num1,num2):
   num1=abs(num1)
   num2=abs(num2)
   
   if num1>num2:
        return num1
    
   elif num1<num2:
        return num2
    
   else :
        return None 

def my_floar (num):
    num = abs(num)
    return int(num)

def my_ciel (num):
    num = abs(num)
    return int(num)+1

def my_exp (x):
    return 2.718282**x


def my_factorial(x):
    factor = 1
    for x in range(1,x+1):
        factor *=x
    return factor    

# The perimeter of any equilateral shape
def Perimeter_of_shape (length,numOfShape):
    return length*numOfShape   
    
    
def circle (rad):
    print( "Area of circle is", 3.14*(rad**2))
    print ("Perimeter of circle is",2*3.1415*rad)
    

def mean(my_data :list):
    sum = 0
    for i in my_data :
        sum += i         
    return (sum/len(my_data))
