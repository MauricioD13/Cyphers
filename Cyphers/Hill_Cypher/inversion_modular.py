def module_invert(determinant):
    for i in range(0,abs(determinant)+1):
        if (determinant*i)%26==1:
            return i
    else:
            print("No tiene inverso modular")