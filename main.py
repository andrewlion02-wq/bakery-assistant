from assistant import BakeryAssistant

assistant = BakeryAssistant()

name = input("Cual es tu nombre?: ").strip().lower()
years = int(input("Cuantos años de experiencia tienes haciendo pan? ").strip())
    
print(assistant.show_recipes())
level = assistant.bakery_level(years)
print(assistant.recommend_recipes(level))

