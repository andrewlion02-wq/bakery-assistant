from assistant import BakeryAssistant

assistant = BakeryAssistant()

name = input("Cual es tu nombre?: ").strip().lower()
years = int(input("Cuantos años de experiencia tienes haciendo pan? ").strip())
    
print(assistant.welcome(name))
level = assistant.bakery_level(years)
print(f" Tu nivel como panadero es {level}, como podria ayudarte? ")

