from utils.utils import Utils
from ui.menu import Menu

mock_livros = [
    {"nome": "1984", "autor": "George Orwell", "ano": 1949, "preco": 45.90, "quantidade": 25},
    {"nome": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "preco": 32.50, "quantidade": 40},
    {"nome": "O Senhor dos Anéis: A Sociedade do Anel", "autor": "J.R.R. Tolkien", "ano": 1954, "preco": 65.00, "quantidade": 15},
    {"nome": "Harry Potter e a Pedra Filosofal", "autor": "J.K. Rowling", "ano": 1997, "preco": 49.90, "quantidade": 50},
    {"nome": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "ano": 1943, "preco": 24.90, "quantidade": 80},
    {"nome": "Cem Anos de Solidão", "autor": "Gabriel García Márquez", "ano": 1967, "preco": 55.00, "quantidade": 20},
    {"nome": "A Revolução dos Bichos", "autor": "George Orwell", "ano": 1945, "preco": 29.90, "quantidade": 35},
    {"nome": "Fahrenheit 451", "autor": "Ray Bradbury", "ano": 1953, "preco": 42.00, "quantidade": 18},
    {"nome": "O Alquimista", "autor": "Paulo Coelho", "ano": 1988, "preco": 39.90, "quantidade": 60},
    {"nome": "O Código Da Vinci", "autor": "Dan Brown", "ano": 2003, "preco": 34.50, "quantidade": 22}
]

stock_data = Utils.load_json_file('db/estoque.json', mock_livros)

sales_data = Utils.load_json_file('db/vendas.json', [])

app = Menu(stock_data, sales_data)

app.run()    
