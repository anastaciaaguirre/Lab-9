#Abigail Lopez & Anastacia Aguirre


#Part C: Cake Recipes
#I found my own recipes sorry!
velvet= ["coffee", "water", "cocoa powder", "flour", "baking powder", "baking soda",
         "sea salt", "cinnamon", "sugar", "vegetable oil", "unsalted butter", "eggs", "buttermilk",
         "vanilla extract", "red food coloring", "distilled white vinegar"]
lemon= ["unsalted butter", "sugar", "eggs", "lemon zest", "flour", "baking powder", "baking soda",
        "kosher salt", "fresh lemon juice", "buttermilk", "vanilla extract"]


def same_ingr(recipe_1, recipe_2):
    all_ingr= dict()
    repeated= []
    for item in recipe_1:
        if item not in all_ingr:
            all_ingr[item]=1
        else:
            all_ingr[item]+=1
    for item in recipe_2:
        if item not in all_ingr:
            all_ingr[item]=1
        else:
            all_ingr[item]+=1
    for item in all_ingr:
        if all_ingr[item]>1:
            repeated.append(item)
    print("Repeated ingredients:", repeated)

same_ingr(velvet, lemon)
