bits=[]
for i in range(7,-1,-1):
        bits.append(2**i)
def decimal_to_binary(number):
    binary=[]
    counter=number
    for i in range(8):
        if bits[i]<=counter:
            binary.append(1)
            counter=counter-bits[i]
        else:
            binary.append(0)
    return binary
def binary_to_decimal(binary):
    number=0
    for i in range(8):
        if binary[i]==1:
            number=bits[i]+number
    return number
