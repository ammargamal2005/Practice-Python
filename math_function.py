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
    return int(num)
def my_ciel (num):
    return int(num)+1



