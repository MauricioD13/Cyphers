import Binary   
def ip_finder(x,y):
    IP=[]
    IP=x.split(".")
    Mask=int(y)
    bits=[]
    for i in range(7,-1,-1):
        bits.append(2**i)
    mask_decimal=[]
    number=0
    cont=Mask
    for i in range(0,4):
        for i in range(0,cont):
            number=bits[i]+number
            #print("Number {}, i {}".format(number,i))
            if i>=7:
                break
        mask_decimal.append(number)
        cont=cont-8
        number=0
    mask_binary=[]
    for i in range(4):
        mask_binary.append(Binary.decimal_to_binary(mask_decimal[i]))
    wildcard_decimal=[]
    # Saber en que posicion comienzan los ceros

    Wildcard=32-Mask
    # Wildcard
    cont=Wildcard
    wildcard_bits=bits[::-1]
    for i in range(0,4):
        for i in range(0,cont):
            number=wildcard_bits[i]+number
            #print("Number {}, i {}".format(number,i))
            if i>=7:
                break
        wildcard_decimal.append(number)
        cont=cont-8
        number=0
    wildcard_decimal=wildcard_decimal[::-1]

    #User per net
    flag=0
    user_available=0
    for i in range(4):
        if (wildcard_decimal[i]!=0 and flag==0):
            #print(wildcard_decimal[i],flag)
            user_available=wildcard_decimal[i]+1
            flag=1
        else:
            user_available=user_available*(wildcard_decimal[i]+1)
    user_available=user_available-2
    
    #Net Address
    net_address=[0,0,0,0]
    net_address_binary=[]
    byte=int(Mask/8)
    position=Mask-(byte*8)
    IP_binary=Binary.decimal_to_binary(int(IP[byte]))
    net_address_binary=IP_binary
    for i in range(8):
        if i>=position:
            net_address_binary[i]=0
    net_address=IP
    net_address[byte]=str(Binary.binary_to_decimal(net_address_binary))
    for i in range(byte+1,4):
        net_address[i]=0
    mask_complete=" "
    wildcard_complete=" "
    net_address_complete=" "
    mask_complete=str(mask_decimal[0])+"."+str(mask_decimal[1])+"."+str(mask_decimal[2])+"."+str(mask_decimal[3])
    wildcard_complete=str(wildcard_decimal[0])+"."+str(wildcard_decimal[1])+"."+str(wildcard_decimal[2])+"."+str(wildcard_decimal[3])
    net_address_complete=str(net_address[0])+"."+str(net_address[1])+"."+str(net_address[2])+"."+str(net_address[3])
    ip_info=[]
    ip_info.append(mask_complete)
    ip_info.append(wildcard_complete)
    ip_info.append(net_address_complete)
    ip_info.append(user_available)
    return ip_info
   # print("Mascara de red \t {} \n Wildcard \t {} \n Net Address \t {} \n".format(mask_complete,wildcard_complete,net_address_complete))