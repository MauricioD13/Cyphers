import numpy as np
import math
import inversion_modular

#This function complete the message to be a multiple of the square of the lenght key
def plaintext_issue(plaintext,square):
    i=1
    while square*i<len(plaintext):
        i=i+1
    res=i*square
    diff=res-len(plaintext)
    for i in range(0,diff):
        plaintext.append("z")
    return res

Letters={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
#plaintext=input("Palabra a cifrar:")
plaintext="teamomucho"
plaintext=list(plaintext)
plaintext_numbers=[]
key_numbers=[]
#Key=input("Palabra llave:")
key="ebdacbfbd"
key=list(key)
#Preparation for Encription 
def preparation(key,plaintext):
    information=[]
    for j in range(len(key)): 
        for i in Letters.items():           
            if i[0]==key[j]:
                key_numbers.append(i[1])
    information.append(int(math.sqrt(len(key_numbers)))) #square 0
    information.append(plaintext_issue(plaintext,information[0])) #lenght_plaintext 1
    for j in range(len(plaintext)):
        for i in Letters.items():
         if i[0]==plaintext[j]:
              plaintext_numbers.append(i[1])
    information.append(plaintext_numbers) # plaintext_numbers 2
    information.append(np.array(key_numbers).reshape(information[0],information[0])) #key_matrix 3
    det_key_matrix=int(np.linalg.det(information[3]))
    invert_number=inversion_modular.module_invert(det_key_matrix)
    # Contain of the array information: 
    # square            0
    # lenght_plaintext  1
    # plaintext_numbers 2
    # key_matrix        3
    return information

#Encription
def Encryption(square,lenght_plaintext,plaintext_numbers,key_matrix):
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
    encript_message=" "
    for i in range(0,lenght_plaintext):
        encript_message=encript_message+res[i]
    print(encript_message)

information=[]
information=preparation(key,plaintext)
square=information[0]
lenght_plaintext=information[1]
plaintext_numbers=information[2]
key_matrix=information[3]

Encryption(square,lenght_plaintext,plaintext_numbers,key_matrix)