
letters = ["a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"]

word = input("Ingresar palabra: ")
word_numbers = []
cypher_numbers = []
cypher_text = []
shift = 12

letters = letters[0].split(",")

for i in range(0,len(word)):
    for j in range(0,len(letters)):
        
        if (word[i] == letters[j]):
            word_numbers.append(j)

for i in range(0,len(word_numbers)):
    cypher_numbers.append((word_numbers[i]+shift)%26)

print(word_numbers)
print(cypher_numbers)
            
cypher_text = [letters[i] for i in cypher_numbers]

print(cypher_text)
