import json
import datetime
class Utils:
    
    @staticmethod
    def verify_id(book_id: int, stock_data: list) -> bool:
        if book_id < 1 or book_id > len(stock_data):
            print("ERRO: Id do livro invalido")
            return False
        return True
    

    @staticmethod
    def sum_caixa(sales_data: list) -> float:
        caixa = sum(sale['valor'] for sale in sales_data)
        return caixa
    @staticmethod
    def load_json_file(filename:str, default_data:list = None) -> list:  
        try:
            if default_data is None:
                default_data = []
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except FileNotFoundError as e:
            print(f"File not found: {e}")
            return default_data
        except Exception as e:
            print(f"An error occurred while loading the file(Returning default data): {e}")
            return default_data
    
    @staticmethod
    def input_force_int(message:str) -> int:
        while True:
            try:
                value = int(input(message))
                return value
            except ValueError:
                print("Invalid input. Please enter an integer.")

    @staticmethod
    def input_force_float(message:str) -> float:
        while True:
            try:
                value = float(input(message))
                return value
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    @staticmethod
    def input_non_empty_string(message:str) -> str:
        while True:
            value = input(message).strip()
            if value:
                return value
            else:
                print("Input cannot be empty. Please enter a valid string.")

    @staticmethod
    def get_current_datetime() -> str:
        now = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
        return now 
    
    @staticmethod
    def save_json_file(filename:str, data:list) -> list:
        try:
            with open(filename, 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")