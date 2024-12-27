import getpass

word = ""
hint = ""
trial = 0 
count =1
print ("                Hangman Game")
word = getpass.getpass("Secret word you want your friend to guess :").lower()
while word.isalpha() == False:
    word = getpass.getpass("Secret word must be Alphabets ONLY :").lower()


hint = getpass.getpass ("Give a hint of category this word falls under eg Fruits:")
while word.isalpha() == False:
    hint = getpass.getpass ("Hint must be Alphabets ONLY")

trial = len(word)+2
print ("Guess the word! Hint: word is a name of a {}. \nYou have {} Attepmts to win the game".format(hint,trial))

length = len(word)
inputu =""
newstring = "_ " * length
newstring_Split = newstring.split() 
print (newstring)
inputu = input ("Enter a letter to guess first: ").lower()
if inputu in word :
          for i in range(len(word)) :
              if word[i] == inputu:
                 newstring_Split[i] = inputu
          newstring = "".join(newstring_Split)  

while newstring !=  word:
    print (newstring)
   
    if count == trial: 
       print ( "Out of tries\nThe word was --> " + word)
       break
    
    elif inputu  in word :
      count +=1
      inputu = input ("Enter a letter to guess: ").lower() 
      for i in range(len(word)):
              if word[i] == inputu:
                 newstring_Split[i] = inputu
      newstring = "".join(newstring_Split)
                
       
    elif inputu not in  word  :
       count +=1
       inputu = input ("Enter a letter to guess: ").lower()
       
       if inputu in word :
          for i in range(len(word)) :
              if word [i] == inputu:
                 newstring_Split [i] = inputu
          newstring = "".join(newstring_Split)  
             

if newstring ==  word:
   print (newstring +"\nCongratulations, You won!")

