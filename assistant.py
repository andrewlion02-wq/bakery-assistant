class BakeryAssistant:
    def welcome(self, name):
        return f"Hola {name}, Mi nombre es Eurísaco, y seré tu asistente virtual en panadería. "

    def bakery_level(self, years):
        if years < 1:   
            return "Principiante"
        elif years <= 3:
            return "Intermedio"
        else:
            return "Avanzado"

    def show_recipes(self):
        products = ["Focaccia", "Pan integral", "Sourdough", "Cinnamon roll", "Pan de molde", "Brioche"]
        result = ""
        for index, product in enumerate(products, start=1):
            result += f"producto {index}: {product}\n"
        
        return result
        
    def recommend_recipes(self, level):
        recipes_by_level = {
            "Principiante": ["focaccia", "pan integral"],
            "Intermedio": ["sourdough", "cinnamon roll"],
            "Avanzado": ["pan de molde", "brioche"]
        }

        recipes = recipes_by_level.get(level)
        if recipes is None:
            return "Lo siento, no hay recetas para tu nivel actual."

        result = f"Recetas recomendadas para tu nivel {level}:\n"
        for recipe in recipes:
            result += f"- {recipe}\n"
        
        return result
        

        

    


