place=["","ten","hundred","thousand","ten thousand","hundred thousand","million","ten million","hundred million","billion","ten billion","hundred billion","trillion","ten trillion","hundred trillion","quadrillion"]
#ADD hundred Thusands
numbers=["","one","two","three","four","five","six","seven","eight","nine"]

outliers_tens=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
outliers_teens=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]


def int_to_str(int_var):
    str_var = ""
    if int_var < 0:
        str_var += "minus "
        int_var *= -1
    for i in range(len(str(int_var))):
        #checks if 2nd last digit
        if i == len(str(int_var))-2:
            if len(str(int_var)) != 2:
                    str_var += "& "
            if int(str(int_var)[i]) == 1:
                str_var += outliers_teens[int(str(int_var)[i+1])]
                int_var -= int(str(int_var)[i+1]) 
            else:    
                str_var += outliers_tens[int(str(int_var)[i])]
            str_var += " "
        elif int(str(int_var)[i]) != 0:
            str_var += numbers[int(str(int_var)[i])]
            str_var += " "
            str_var += place[len(str(int_var))-1-i]
            str_var += " "
    return str_var




while True:
    print()
    while True:
        try:
            nbr = int(input("Enter number in integer format [max 16 digits]:"))      
        except ValueError:
            print("Make sure input is in integer format.")
            continue
        else:
            print(int_to_str(nbr))
            break
    

    