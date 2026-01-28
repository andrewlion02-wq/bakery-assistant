while True:
    option = input(
        "¿Dime que opcion deseas?\n "
        "1: Mostrar recetas\n "
        "2: Rercomendar recetas\n "
        "3: Salir\n "
        "Por favor elige una option valida (1, 2, 3): ").strip().lower()

    if option == "1":
        print(assistant.show_recipes())
    elif option == "2":
        print(assistant.recommend_recipes(level))
    elif option == "3":
        print("Saliendo del horno")
        break
    else:
        print("Por favor elige una option valida (1, 2, 3): ")

    

     



