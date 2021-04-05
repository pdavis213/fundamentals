import random

owners_and_pets = {
    'Preston': "Shepherd/mix",
    'Harleigh': "Sedimentary rock",
    'Austin': "Coon hound",
    'Chris': "Husky/Shepherd",
    'Adrien': ["Invisible Horse", "gandalf", "pikachu"]
}

# print(owners_and_pets['Preston'])

# for k in owners_and_pets.items():
#    print(k)

# for key, val in owners_and_pets.items():
#    print(key, val)


# def findValues(str):
#    for key, val in owners_and_pets.items():
#       if key ==str:
#            return val

# print(findValues("Harleigh"))


#h = random.randint(0,10)

def randomPetFinder(str):
    adriensPets = owners_and_pets[str]
    randnum = random.randint(0, len(adriensPets))
    print(adriensPets[randnum])


randomPetFinder('Adrien')
