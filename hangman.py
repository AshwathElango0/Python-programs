wordlist=['ardvark', 'baboon', 'camel']
import random
word=random.choice(wordlist)

lifecount=5
x=len(word)
for i in range(x):
    print("_", end=' ')
print()

count=[]
for i in range(x):
   count+='_'
while '_' in count and lifecount>0:
 guess=input("Guess a letter : ")
 guess.lower()
 for i in range(x):
    if word[i]==guess:
        count[i]=guess
 if guess not in word:
       lifecount-=1
 print(count)
        
 
