
"""sentence=input("Enter in a sentence...")
vowels={"a":0, "e":0, "i":0, "o":0, "u":0}
for letter in sentence:
    if letter in vowels:
        vowels[letter]+=1

print(vowels)"""

# most frequently used word
sentence=input("Enter in a sentence..").lower()

#converting string to list
list=sentence.split()
count={}.fromkeys(list,0)
 
for i in list:
    if i in count:
        count[i]+=1
m=max(count.values())
for key,value in count.items():
    if value==m:
        k=key
print(count)
print(f"The most frequently used word is {k}")