import numpy as np
import math
import inversion_modular

#This function complete the message to be a multiple of the square of the lenght key
def text_issue(text,square):
    i=1
    while square*i<len(text):
        i=i+1
        if i*square==len(plaintext):
            break
    res=i*square
    diff=res-len(plaintext)
    for i in range(0,diff):
        text.append("z")
        print(text)
    return res


#Preparation for Encription 
def preparation(key,text,option):
    key_numbers=[]
    text_numbers=[]
    text=list(text)
    key=list(key)
    lenght_text=len(text)
    information=[]
    for j in range(len(key)): 
        for i in Letters.items():           
            if i[0]==key[j]:
                key_numbers.append(i[1])
    information.append(int(math.sqrt(len(key_numbers)))) #square 0
    if option=="encrypt":
        information.append(text_issue(text,information[0])) #lenght_plaintext 1
    else:
        information.append(len(text))
    for j in range(len(text)):
        for i in Letters.items():
         if i[0]==text[j]:
              text_numbers.append(i[1])
    information.append(text_numbers) # text_numbers 2
    information.append(np.array(key_numbers).reshape(information[0],information[0])) #key_matrix 3
    det_key_matrix=int(np.linalg.det(information[3]))
    #print(information[3])
    #print(det_key_matrix)
    invert_number=inversion_modular.module_invert(det_key_matrix-1)
    #print(invert_number)
    information.append(invert_number)
    information.append(det_key_matrix-1)
    # Contain of the array information: 
    # square            0
    # lenght_plaintext  1
    # text_numbers      2
    # key_matrix        3
    # invert_number     4
    # determinant       5
    # lenght_text       6
    return information

#Encryption
def Encryption(information):
    square=information[0]
    lenght_plaintext=information[1]
    plaintext_numbers=information[2]
    key_matrix=information[3]
    words=int(lenght_plaintext/square)
    array_plaintext=[]
    for i in range(0,words):
        array_plaintext.append(np.array(plaintext_numbers[i*square:(i*square)+square]))
    result=[]
    res=[]
    for p in range(0,words):
        result=np.dot(array_plaintext[p],key_matrix)
        result=result%26
        for j in range(0,3):
            for i in Letters.items():
                    if i[1]==result[j]:
                        res.append(i[0])
    encript_message=""
    for i in range(0,lenght_plaintext):
        encript_message=encript_message+res[i]
    return encript_message

#Decryption 
def Decryption(information):
    # Varible name change
    square=information[0]
    lenght_plaintext=information[1]
    plaintext_numbers=information[2]
    print(plaintext_numbers)
    key_matrix=information[3]
    inverse_number=information[4]
    det_key_matrix=information[5]
    
    #Process of decryption
    inverse=np.linalg.inv(key_matrix)
    inverse_key_matrix=np.round(inverse,1)
    adj_key_matrix=inverse_key_matrix * det_key_matrix
    mod_inverse_matrix=adj_key_matrix * inverse_number
    mod_inverse_matrix=mod_inverse_matrix%26
    #print(mod_inverse_matrix)
    words=int(lenght_plaintext/square)
    array_plaintext=[]
    for i in range(0,words):
        array_plaintext.append(np.array(plaintext_numbers[i*square:(i*square)+square]))
        #print(array_plaintext)
    result=[]
    res=[]
    for p in range(0,words):
        result=np.dot(array_plaintext[p],mod_inverse_matrix)
        result=result%26
        for j in range(0,3):
            for i in Letters.items():
                    if i[1]==result[j]:
                        res.append(i[0])
    decrypt_message=" "
    for i in range(0,lenght_plaintext):
        decrypt_message=decrypt_message+res[i]
    print(decrypt_message)

    
    
Letters={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
#plaintext=input("Palabra a cifrar:")
plaintext="teamomucho"
text_numbers=[]
key_numbers=[]
#Key=input("Palabra llave:")
key="ebdacbfbd"
information=[]
information=preparation(key,plaintext,"encrypt")
encript_message=Encryption(information)
key_decrypt="ebdacbfbd"
information=preparation(key_decrypt,encript_message,"decrypt")
Decryption(information)