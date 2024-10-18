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

print( "max number is ",max(5,7))  #7
print("max number is ",min(5,7))   #5
