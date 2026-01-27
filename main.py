from assistant import BakeryAssistant

assistant = BakeryAssistant()

name = input("Cual es tu nombre?: ").strip().lower()
years = int(input("Cuantos años de experiencia tienes haciendo pan? ").strip())

level = assistant.bakery_level(years)

print(assistant.welcome(name))
print(f"Tu experiencia como panadero es: {level}")

def advice (option, assistant, level):
    if option == "1":
        return assistant.show_recipes()
    elif option == "2":
        return assistant.recommend_recipes(level)
    elif option == "3":
        return "El pan esta listo saliendo del horno"
    else:
        return "Opcion no valida, por favor elije 1, 2 o 3"

print("\n¿Que deseas hacer?")
print("1. Ver todas las recetas")
print("2. Ver recetas recomendadas. segun mim nivel")
print("3. Salir")

option = input("Elige una opcion (1, 2, 3): ").strip().lower()

print(advice(option, assistant, level))



