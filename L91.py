#Abigail Lopez & Anastacia Aguirre

#Part A: Write the get method yourself
def my_get_method(dictionary, key):
    print(dictionary[key])

dict= {"one":"uno", "two":"dos", "three":"tres"}
my_get_method(dict, "one")

dict= {1:"one", 2:"two", 3:"three"}
my_get_method(dict, 1)

dict= {True:"sky is blue", False:"sky is green"}
my_get_method(dict, True)
