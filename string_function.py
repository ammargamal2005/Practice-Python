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
        
def my_count (text, word ):
    listText= text.split(" ")
    count = 0 
    for i in listText :
        if i == word :
            count +=1 
            return count 
        else :
            count +=1

def my_remove(txt , word):
      listText = txt.split(" ")
      new_txt = []
      
      for i in listText:
          if i != word :
             new_txt.append(i) 
      return ' '.join(new_txt)

def isُexisting (txt, word):
    listText = txt.split(" ")
    for i in listText :
         if i == word :
             return True
         else:
            return False
        
def my_replace(txt, new_word ,old_word ):
      listText = txt.split(" ")
      new_txt = []
      for i in listText:
           if i!= old_word:
              new_txt.append(i)
           else:
               new_txt.append(new_word)
      return ' '.join(new_txt)
  
