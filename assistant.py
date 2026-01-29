class BakeryAssistant:
    def __init__ (self):
        self.recipes_by_level = {
            "Principiante": {
                "focaccia": {
                    "ingredientes": ["harina de trigo 1000g", "agua 350ml", "poolish 1200g (harina de trigo 600g + agua 600ml + azucar 2g + levadura 2g)", "sal 10g", "azucar 20g", "levadura 10g", "aceite de oliva 150ml"],
                    "pasos": [ 
                        "Paso 1: mezclar todos los ingredientes en un bol grande ecepto el poolish",
                        "Paso 2: amasar por 15 minutos y formar una masa homogenea y lisa",
                        "Paso 3: agregar el poolish y amasar nuevamente hasta optener una masa lisa",
                        "Paso 4: dejar reposar la masa por 1 hora y media y dar pliegues cada 30 minutos ",
                        "Paso 5: precalienta el horo 200 grados y hornear a 175 grados por 20 minutos",
                    ]
                }, 
                "pan integral": {
                    "ingredientes": ["harina integral 1000g", "agua 650ml", "levadura 10g", "sal 10g", "miel 120g", "mix de semillas de tu eleccion previamente hidratadas", "masa madre 200g"],
                    "pasos": [
                        "Paso 1: mezcla todos los ingredientes en un bol grande ecepto las semillas hasta obtener una masa homogenea y lisa",
                        "Paso 2: agrega las semillas y mezcla",
                        "Paso 3: deja reposar la masa por 1 hora",
                        "Paso 4: hornea la masa por 20 minutos a 180 grados"
                    ]
                }
            },
            "Intermedio": {
                "sourdough": {
                    "ingredientes": ["harina 1000g", "agua 650ml", "levadura 3g", "sal 20g", "masa madre 200g"],
                    "pasos": [
                        "Paso 1: mezcla todos los ingredientes en un bol grande ecepto la masa madre",
                        "Paso 2: agrega la masa madre y mezcla",
                        "Paso 3: deja reposar la masa por 1 hora",
                        "Paso 4: hornea la masa por 20 minutos a 250 grados"
                    ]
                }, 
                "pan de zanahoria": {
                    "ingredientes": ["harina 1000g", "agua 600ml", "levadura 20g", "sal 20g", "zanahoria 350g", "panela 80g", "mantequilla vegetal 50g","amapola 90g", "ralladura de 2 naranjas "],
                    "pasos": [
                        "Paso 1: mezcla todos los ingredientes en un bol grande ecepto la zanahoria",
                        "Paso 2: agrega la zanahoria y mezcla",
                        "Paso 3: deja reposar la masa por 1 hora",
                        "Paso 4: hornea a 180 grados por 20 minutos"
                    ]
                }
            },
            "Avanzado": {
             "pan de molde": {
                    "ingredientes": ["harina 1000g", "leche 600ml", "levadura 20g", "sal 20g", "azucar 80g", "mantequilla 100g"],
                    "pasos": [
                        "Paso 1: mezcla todos los ingredientes en un bol grande ecepto la mantequilla",
                        "Paso 2: agrega la mantequilla y mezcla",
                        "Paso 3: deja reposar la masa",
                        "Paso 4: hornea a 180 grados por 20 minutos"
                    ]
                }, 
                "brioche": {
                    "ingredientes": ["harina 1000g", "leche 350ml", "levadura 30g", "azucar 160g", "sal 10g", "huevos 5", "mantequilla 300g"],
                    "pasos": [
                        "Paso 1: mezcla todos los ingredientes en un bol grande ecepto la mantequilla",
                        "Paso 2: agrega la mantequilla previamenete cortada en cubo y fria, mezclar hasta obtener una masa homogenea y lisa",
                        "Paso 3: deja reposar la masa por 24 horas",
                        "Paso 4: hornea a 170 grados por 20 minutos"
                    ]
                }
            }
        }

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
        result = "Recetas disponibles:\n"
        for level, recipes in self.recipes_by_level.items():
            result += f"nivel {level}:\n"
            for recipe_name in recipes:
                result += f"- {recipe_name}\n"
        
        return result
        
    def recommend_recipes(self, level):
        recipes = self.recipes_by_level.get(level)
            
        if recipes is None:
            return "Lo siento, no hay recetas para tu nivel actual."

        result = f"Recetas recomendadas para tu nivel {level}:\n"
        for recipe in recipes:
            result += f"- {recipe}\n"
        
        return result
        
    def get_recipes_for_level(self, level):
        return self.recipes_by_level.get(level, {})

    def get_recipe_ingredients(self, level, recipe_name):
        recipe = self.recipes_by_level.get(level, {}).get(recipe_name.lower())
        if not recipe:
            return "Lo siento receta no encontrada"
        
        result = "ingredientes:\n"
        for ingredient in recipe["ingredientes"]:
            result += f"- {ingredient}\n"
        
        return result   

    def get_steps(self, level, recipe_name):
        recipe = self.recipes_by_level.get(level, {}).get(recipe_name.lower())
        if not recipe:
            return "Lo siento receta no encontrada"
        
        result = "paso a paso:\n"
        for step in recipe["pasos"]:
            result += f"- {step}\n"
        
        return result
        
  



    


