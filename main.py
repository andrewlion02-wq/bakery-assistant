from assistant import BakeryAssistant

def show_recommended_recipes_menu(assistant, level):
    recipes = assistant.get_recipes_for_level(level)
    
    if not recipes:
        print("Lo siento, no hay recetas para tu nivel actual.")
        return
    
    print("\nRecetas recomendadas para tu nivel:")
    for recipe_name in recipes:
        print(f"- {recipe_name}")

    recipe_name = input("Que receta te gustaria ver?: ").strip().lower()

    if recipe_name not in recipes:
        print("Receta no encontrada.")
        return
    
    while True:
        submenu = input(
            "\n1: Ver ingredientes\n "
            "2: Ver paso a paso\n "
            "3: Volver al menu principal\n "
            "Por favor elige una option para continuar (1, 2, 3): ").strip().lower()

        if submenu == "1":
            print(assistant.get_recipe_ingredients(level, recipe_name))
        elif submenu == "2":
            print(assistant.get_recipe_steps(level, recipe_name))
        elif submenu == "3":
            print("Volviendo al menu principal")
            break
        else:
            print("Por favor elige una opcion valida")

assistant = BakeryAssistant()

name = input("Cual es tu nombre?: ").strip().lower()
years = int(input("Cuantos años de experiencia tienes haciendo pan? ").strip())

level = assistant.bakery_level(years)

print(assistant.welcome(name))
print(f"Tu experiencia como panadero es: {level}")

while True:
    option = input(
        "¿Dime que opcion deseas?\n "
        "1: Mostrar recetas\n "
        "2: Recomendar recetas\n "
        "3: Salir\n "
        "Por favor elige una option para continuar (1, 2, 3): ").strip()

    if option == "1":
        print(assistant.show_recipes())
    elif option == "2":
        show_recommended_recipes_menu(assistant, level)
    elif option == "3":
        print("Saliendo del horno")
        break
    else:
        print("Por favor elige una opcion valida") 







