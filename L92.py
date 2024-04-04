#Abigail Lopez & Anastacia Aguirre

#Part B: CPSC dictionary
students= {"Lopez":"Abigail", "Aguirre":"Anastacia", "Lombardo":"Emma", "Macrowski":"Allison",
           "Eidelbes":"Sydney", "Burns":"Therese", "Guo":"Mandy", "Patin":"Samantha", 
           "Antimo":"Viviana", "Newton":"Abigail", "Ward":"Elise", "Bradley":"Leena"}


#I thought you asked to return the repeated names and I didn't want to delete it
def repeatednames(dictionary):
    repeats=dict()
    lists=[]
    first_name= dictionary.values()
    for name in first_name:
        if name not in repeats:
            repeats[name]=1
        else:
            repeats[name]+=1
    for name in repeats:
        if repeats[name]>1:
            lists.append(name)
    return lists

print(repeatednames(students))

#This is the correct code!
def name_freq(dictionary):
    repeats=dict()
    first_name= dictionary.values()
    for name in first_name:
        if name not in repeats:
            repeats[name]=1
        else:
            repeats[name]+=1
    return repeats

print(name_freq(students))
