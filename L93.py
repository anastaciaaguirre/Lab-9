#Abigail Lopez & Anastacia Aguirre

#Part C: CPSC List
cpsc_names= ["Abigail", "Lopez", "Anastacia", "Aguirre", "Emma", "Lombardo", "Allison", "Macrowski",
           "Sydney", "Eidelbes", "Therese", "Burns", "Mandy", "Guo", "Samantha", "Patin", 
           "Viviana", "Antimo", "Abigail", "Newton", "Elise", "Ward", "Leena", "Bradley"]

print(cpsc_names[::2])  #Even indices
print(cpsc_names[1::2])  ###Odd indices###

def first_letter(names):
    lasts= names[1::2]
    letters= dict()
    for index in lasts:
        if index[0] not in letters:
            letters[index[0]]=1
        else:
            letters[index[0]]+=1
    return letters


print(first_letter(cpsc_names))
