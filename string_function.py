def reverse_word(word):
    return word[::-1]

def convert_latter(word):
    result =""
    for i in word :
        if ord(i) >=65 and ord(i)<=90 :
            result += chr(ord(i)+32)
        elif ord(i) >=97 and ord(i)<=122 :
            result += chr(ord(i)-32)
        else:
            result += i
    return result 
        
