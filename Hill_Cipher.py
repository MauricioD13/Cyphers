import numpy as np
import math
import inversion_modular
def plaintext_issue(plaintext):
    
Letters={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
#plaintext=input("Palabra a cifrar:")
plaintext="hola"
plaintext=list(plaintext)
plaintext_numbers=[]
key_numbers=[]
#Key=input("Palabra llave:")
key="cehbcbdbf"
key=list(key)
for j in range(len(plaintext)):
    for i in Letters.items():
        if i[0]==plaintext[j]:
            plaintext_numbers.append(i[1])
for j in range(len(key)): 
    for i in Letters.items():           
        if i[0]==key[j]:
            key_numbers.append(i[1])
square=int(math.sqrt(len(key_numbers)))
key_matrix=np.array(key_numbers).reshape(square,square)
message=np.array(plaintext_numbers.reshape(square,square))
print(key_matrix)
det_key_matrix=int(np.linalg.det(key_matrix))
invert_number=inversion_modular.module_invert(det_key_matrix)
