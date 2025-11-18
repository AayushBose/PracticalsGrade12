file = open(r"C:\Users\aayus\OneDrive\Documents\GitHub\PRACTICALS\Python\File7.txt",'r')
#frequency of vowels
content = file.readlines()
print(content)
def freq():
    countA=countE=countI=countO=countU=0
    for i in content:
        for j in range(len(i)):
            if i[j].upper()=='A':
                countA = countA+1
            elif i[j].upper()=='E':
                countE = countE+1
            elif i[j].upper()=='I':
                countI = countI+1
            elif i[j].upper()=='O':
                countO = countO+1
            elif i[j].upper()=='U':
                countU = countU+1
    print('A =',countA,'E =',countE,'I =',countI,'O =',countO,'U =',countU)

def case():
    countl=countu=0
    for i in content:
        for j in range(len(i)):
            if i[j].isupper():
                countu = countu+1
            elif i[j].islower():
                countl = countl+1
    print('Total lower case =',countl)
    print('Total upper case =',countu)

print("Counts are:")
freq()
case()
