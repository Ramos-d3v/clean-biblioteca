import pandas as pd
from utils.utils import Utils

class Services:

    @staticmethod
    def sell_register(stock_data: list, sales_data: list, book_id: int, quantity: int) -> float:
        
        # verifica se o id é maior que 0 ou esta disponivel
        if not Utils.verify_id(book_id, stock_data):
            print("ERRO: Id do livro invalido")
            return 0
        
        quantity_data = stock_data[book_id - 1]['quantidade']

        #verify if the user pass a negative number.
        if quantity < 1:
            print("ERRO: Quantidade deve ser maior que 0")
            return 0
        
        #verify if the quantity is available in stock
        elif quantity > quantity_data:
            print(f"ERRO: Quantidade indisponível no estoque, restam apenas {quantity_data} unidades")
            return 0
        
        #atualiza o estoque do livro
        quantity_data -= quantity
        stock_data[book_id - 1]['quantidade'] = quantity_data
        
        # Calcula o valor total faturado
        valor_venda = stock_data[book_id - 1]['preco'] * quantity
        
 
        sales_data.append({
            "horario": Utils.get_current_datetime(),
            "item": stock_data[book_id - 1]['nome'],
            "quantidade": quantity,
            "valor": valor_venda  
        })
        print(f"Venda registrada: {sales_data[-1]}")

        Utils.save_json_file("db/estoque.json", stock_data)
        Utils.save_json_file("db/vendas.json", sales_data)

        return valor_venda

    @staticmethod  
    def register_new_book(stock_data: list, nome: str, autor: str, ano: int, preco: float, quantidade: int) -> None:
        new_book = {
            "nome": nome,
            "autor": autor,
            "ano": ano,
            "preco": preco,
            "quantidade": quantidade
        }
        stock_data.append(new_book)

        Utils.save_json_file("db/estoque.json", stock_data)

    @staticmethod
    def change_book_price(stock_data: list, book_id: int, new_price: float) -> float:
        if not Utils.verify_id(book_id, stock_data):
            print("ERRO: Id do livro invalido")
            return 0

        stock_data[book_id - 1]['preco'] = new_price
        Utils.save_json_file("db/estoque.json", stock_data)
        return new_price
    
    @staticmethod
    def restock_book(stock_data: list, book_id: int, quantity: int) -> None:
        if not Utils.verify_id(book_id, stock_data):
            print("ERRO: Id do livro invalido")
            return
        
        if quantity < 1:
            print("ERRO: Quantidade deve ser maior que 0")
            return
        
        stock_data[book_id - 1]['quantidade'] += quantity
        Utils.save_json_file("db/estoque.json", stock_data)

    @staticmethod
    def search_book(stock_data:list, search_term:str) -> list:
        search_term_lower = search_term.lower().strip()
        results = []
        for book in stock_data:
            if search_term_lower in book['nome'].lower() or search_term_lower in book['autor'].lower():
                results.append(book)
        return results
    
    @staticmethod
    def make_promotions(stock_data:list, discount_percentage: float, book_id:int = None ) -> None:
        if book_id is not None:
            
            if not Utils.verify_id(book_id, stock_data):
                print("ERRO: Id do livro invalido")
                return
            
            preco_atual = stock_data[book_id - 1]['preco']
            stock_data[book_id - 1]['preco'] = round(preco_atual * (100 - 
            discount_percentage) / 100, 2)
            
            print("Promoção aplicada com sucesso!") 
            Utils.save_json_file("db/estoque.json", stock_data)
        else:
            for book in stock_data:
                round(book['preco'] * (100 - discount_percentage) / 100, 2)
            print("Promoção aplicada com sucesso!")
            
        Utils.save_json_file("db/estoque.json", stock_data)

    @staticmethod
    def generate_invoice(sales_data:list) -> None:
        print("Nota fiscal (vendas da Sessão)")
        for sale in sales_data:
            print(f"Horario: {sale['horario']} - Item: {sale['item']} - Quantidade: {sale['quantidade']} - Valor: R${sale['valor']:.2f}")
    
    @staticmethod
    def generate_balance(stock_data:list, sales_data:list) -> str:
        if not sales_data:
            print("Nenhuma venda registrada.")
            return
        
        df_sales = pd.DataFrame(sales_data)
        df_stock = pd.DataFrame(stock_data)

        total_balance = df_sales['valor'].sum()
        mean_sells = df_sales['valor'].mean()
        max_sell = df_sales['valor'].max()
        min_sell = df_sales['valor'].min()

        ranking_livros = df_sales.groupby('item')['valor'].sum().sort_values(ascending=False)

        total_patrimonio = (df_stock['preco'] * df_stock['quantidade']).sum()

        report = f"""
        ======================= PAINEL DE BALANÇO =======================
        - TOTAL DE VENDAS REALIZADAS: R${total_balance:.2f}
        - MÉDIA DE VENDAS REALIZADAS: R${mean_sells:.2f}    
        - MAIOR VENDA REALIZADA: R${max_sell:.2f}
        - MENOR VENDA REALIZADA: R${min_sell:.2f}
        - PATRIMÔNIO TOTAL: R${total_patrimonio:.2f}

        --- RANKING DE LIVROS MAIS VENDIDOS (QTD) ---
        {ranking_livros.to_string()}
        =================================================================
        """
        return report





