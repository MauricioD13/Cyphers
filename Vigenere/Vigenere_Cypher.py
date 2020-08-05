
def preparation(key,plaintext):
    aux=key
    while len(key)<len(plaintext):
            key=key+aux
    return key

def Encrypt(key,plaintext):
    key=key[0:len(plaintext)]
    key_numbers=[]
    plaintext_numbers=[]
    cyphertext_list=[]
    lenght_key=len(key)
    cyphertext=""
    for i in range(0,lenght_key):
        key_numbers.append(ord(key[i]))
        plaintext_numbers.append(ord(plaintext[i]))
    for i in range(0,lenght_key):
        cyphertext_list.append(chr(key_numbers[i]+plaintext_numbers[i]%127))
        cyphertext=cyphertext+cyphertext_list[i]
    print(cyphertext)
    return cyphertext 
def Decrypt(key,cyphertext):
    key=list(key)
    key_numbers=[]
    cyphertext_numbers=[]
    plaintext_list=[]
    plaintext=""
    lenght_key=len(key)
    for i in range(0,lenght_key):
        key_numbers.append(ord(key[i]))
        cyphertext_numbers.append(ord(cyphertext[i]))
    for i in range(0,lenght_key):
        plaintext_list.append(chr(cyphertext_numbers[i]-key_numbers[i]%127))
        plaintext=plaintext+plaintext_list[i]
    return plaintext

        
key="hola"
plaintext="quiero que esto funcione"
key=preparation(key,plaintext)
message=Encrypt(key,plaintext)
message=Decrypt(key,message)
print(message)