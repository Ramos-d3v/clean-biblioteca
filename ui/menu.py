from utils.utils import Utils
from services.services import Services

class Menu:
    def __init__(self, data_stock:list, data_sales:list) -> None:
        self.data_stock = data_stock
        self.data_sales = data_sales

        self.caixa = Utils.sum_caixa(self.data_sales)
    
    def display_init(self):
        print("\n" + "=" * 60)
        print(" " * 20 + "Livraria Ramos")
        print(f" " * 16 + f"Caixa acumulado: R${self.caixa:.2f}")
        print("=" * 60)
        print("Acervo disponível:")
        for id_livro, livro in enumerate(self.data_stock):
            print(f" {id_livro + 1}. Nome: {livro['nome']} - Autor: {livro['autor']} - Ano: {livro['ano']} - R${livro['preco']:.2f} - Quantidade: {livro['quantidade']}")
        print("=" * 60)
    def run(self):
        while True:
            self.display_init()
            print("""
            ================MENU================
            1 - Registarr venda de livro
            2 - Cadastrar  novo livro
            3 - Alterar preço de um livro
            4 - Repor estoque de um livro
            5 - Pesquisar por Nome/Autor
            6 - Promoções
            7 - Nota fiscal (vendas da Sessão)
            8 - Painel de estatísticas e balanço
            9 - Sair
            """)

            comand = Utils.input_force_int("Digite o número do comando que deseja fazer: ")

            match comand:
                case 9:
                    print("Saindo do programa...")
                    break
                case 1:
                    id_book = Utils.input_force_int("Digite o ID do livro que deseja vender: ")
                    quantity = Utils.input_force_int("Digite a quantidade que deseja vender: ")
                    valor_faturado = Services.sell_register(self.data_stock, self.data_sales, id_book, quantity)
                    self.caixa += valor_faturado
                    if valor_faturado > 0:
                        print(f"Valor faturado nessa venda: R${valor_faturado:.2f}")
                case 2:
                    nome = Utils.input_non_empty_string("Digite o nome do livro: ")
                    autor = Utils.input_non_empty_string("Digite o nome do autor: ")
                    ano = Utils.input_force_int("Digite o ano de publicação: ")
                    preco = Utils.input_force_float("Digite o preço do livro: ")
                    quantidade = Utils.input_force_int("Digite a quantidade em estoque: ")
                    
                    Services.register_new_book(self.data_stock, nome, autor, ano, preco, quantidade)

                case 3:
                    id_book = Utils.input_force_int("Digite o ID do livro que deseja alterar o preço: ")
                    new_price = Utils.input_force_float("Digite o novo preço do livro: ")
                    updated_price = Services.change_book_price(self.data_stock, id_book, new_price)
                    if updated_price > 0:
                        print(f"Preço do livro atualizado para: R${updated_price:.2f}")
                        
                case 4:
                    id_book = Utils.input_force_int("Digite o ID do livro que deseja repor o estoque: ")
                    quantity = Utils.input_force_int("Digite a quantidade que deseja adicionar ao estoque: ")
                    Services.restock_book(self.data_stock, id_book, quantity)
                    print("Estoque atualizado com sucesso!")
                case 5:
                    search_query = Utils.input_non_empty_string("Digite o nome ou autor do livro que deseja pesquisar: ")
                    results = Services.search_book(self.data_stock, search_query)
                    print(f"Resultados da pesquisa para '{search_query}':")
                    if results:
                        for livro in results:
                            print(f"Nome: {livro['nome']} - Autor: {livro['autor']} - Ano: {livro['ano']} - R${livro['preco']:.2f} - Quantidade: {livro['quantidade']}")
                    else:
                        print("Nenhum livro encontrado com esse nome ou autor.")

                case 6:

                    aplicacao_desconto = Utils.input_force_int("Coloque 1 para aplicar desconto geral, e 0 para aplicar apenas em um livro: ")
                    porcentagem = Utils.input_force_float("Digite a porcentagem de desconto: ")
                    if aplicacao_desconto == 0:
                        id_book = Utils.input_force_int("Digite o ID do livro que deseja aplicar o desconto: ")
                        Services.make_promotions(self.data_stock, porcentagem, id_book)
                    else:
                        Services.make_promotions(self.data_stock, porcentagem)
                case 7:
                    Services.generate_invoice(self.data_sales)
                case 8:
                    print("Painel de estatísticas e balanço")
                
                case _:
                    print("Comando inválido. Por favor, tente novamente.")
            