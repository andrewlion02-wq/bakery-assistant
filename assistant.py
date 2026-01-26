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

    def show_reciopes(self):
        pass

    


