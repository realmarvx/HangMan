import getpass
# Initialize variables
word = ""
hint = ""
trial = 0 
count =1

# Display the game title
print ("                Hangman Game")

# Prompt the first player to enter the secret word
word = getpass.getpass("Secret word you want your friend to guess :").lower()
while word.isalpha() == False:
    word = getpass.getpass("Secret word must be Alphabets ONLY :").lower()

# Prompt the first player to enter the hint for the secret word
hint = getpass.getpass ("Give a hint of category this word falls under eg Fruits:")
while word.isalpha() == False:
    hint = getpass.getpass ("Hint must be Alphabets ONLY")
    
#Setting the Number of the trials (length of the word + 2)
trial = len(word)+2

#Outputing the Hint giving by Player 1
print ("Guess the word! Hint: word is a name of a {}. \nYou have {} Attepmts to win the game".format(hint,trial))

# Initialize the displayed word with underscores
length = len(word)
inputu =""
newstring = "_ " * length
newstring_Split = newstring.split() 
print (newstring)

# Prompt the second player to guess a letter
inputu = input ("Enter a letter to guess first: ").lower()
if inputu in word :
          for i in range(len(word)) :
              if word[i] == inputu:
                 newstring_Split[i] = inputu
          newstring = "".join(newstring_Split)  
    
# Main game loop

while newstring !=  word:
    print (newstring)
    
# Check if the player has run out of trials
   
    if count == trial: 
       print ( "Out of tries\nThe word was --> " + word)
       break
        
  # If the guessed letter is in the word    
    elif inputu  in word :
      count +=1
      inputu = input ("Enter a letter to guess: ").lower() 
      for i in range(len(word)):
              if word[i] == inputu:
                 newstring_Split[i] = inputu
      newstring = "".join(newstring_Split)
                
  # If the guessed letter is not in the word       
    elif inputu not in  word  :
       count +=1
       inputu = input ("Enter a letter to guess: ").lower()
       
       if inputu in word :
          for i in range(len(word)) :
              if word [i] == inputu:
                 newstring_Split [i] = inputu
          newstring = "".join(newstring_Split)  
             
# If the player has guessed the word correctly
if newstring ==  word:
   print (newstring +"\nCongratulations, You won!")

