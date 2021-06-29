
letters = ["a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"]

word = input("Enter word: ")
word_numbers = []
cypher_numbers = []
precypher_numbers = []
cypher_text = []
shift = 12

letters = letters[0].split(",")

for i in range(0,len(word)):
    for j in range(0,len(letters)):
        
        if (word[i] == letters[j]):
            word_numbers.append(j)

for i in range(0,len(word_numbers)):
    precypher_numbers.append(word_numbers[i]+shift)
    cypher_numbers.append((word_numbers[i]+shift)%26)

print(f"Numbers of the word: {word_numbers}")
print(f"Precypher: {precypher_numbers}")
print(f"Cypher numbers: {cypher_numbers}")
            
cypher_text = [letters[i] for i in cypher_numbers]

print(f"Cypher text: {cypher_text}")
