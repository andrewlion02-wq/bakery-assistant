recetas_por_nivel = {
    "Principiante": [
        {
            "nombre": "Focaccia",
            "ingredientes": ["Harina", "Agua", "Aceite de oliva", "Levadura","poolish", "Sal", "Azúcar"],
            "tiempo": "2 horas",
            "nivel": "Principiante"
        },
        {
            "nombre": "Pan integral",
            "ingredientes": ["Harina integral", "Agua", "masa madre", "Levadura", "Sal", "miel", "mix de semillas"],
            "tiempo": "2 horas",
            "nivel": "Principiante"
        }
    ],
    "Intermedio": [
        {
            "nombre": "Sourdough",
            "ingredientes": ["Harina", "Agua", "masa madre", "Levadura", "Sal"],
            "tiempo": "1 hora",
            "nivel": "Intermedio"
        },
        {
            "nombre": "Cinnamon roll",
            "ingredientes": ["Harina", "leche", "leche en polvo", "Levadura", "Sal", "azucar", "canela", "mantequilla", "huevos", "esencia de vainilla"],
            "tiempo": "1 hora",
            "nivel": "Intermedio"
        }
    ],
    "Avanzado": [
        {
            "nombre": "Pan de molde",
            "ingredientes": ["Harina", "Azucar", "leche en polvo", "agua", "Levadura", "Sal", "mantequilla"],
            "tiempo": "2 horas",
            "nivel": "Avanzado"
        },
        {
            "nombre": "Brioche",
            "ingredientes": ["Harina", "sal ", "Azucar", "Levadura", "Huevos","mantequilla",],
            "tiempo": "5 horas",
            "nivel": "Avanzado"
        }
    ]
}
print(recetas_por_nivel)
print(recetas_por_nivel.get("Principiante"))
print(recetas_por_nivel["Principiante"][0]["nombre"])


