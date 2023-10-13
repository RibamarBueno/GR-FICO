import matplotlib.pyplot as plt 

def criar_grafico_barras():
    titulo = input("Digite o titulo do gráfico: ")
    titulo_eixo_x = input("Digite o titulo do eixo X (Linha vertical): ")
    titulo_eixo_y = input("Digite o titulo do eixo Y (Linha horizontal): ")

    n_categorias  int(input("Digite o numero de categorias: "))

    categorias = []
    valores = [] 

    for i in range (n_categorias):
        categoria = input("Digite o nome da categoria :")
        valor = float(input("Digite o valor para a categoria :"))
        categorias.append(categoria)
        valores.append(valor)

    plt.bar(categorias,valores)

    plt.title(titulo)
    plt.xlabel(titulo_eixo_x)
    plt.ylabel(titulo_eixo_y)

    plt.show

if __name__ == "__main__":
    criar_grafico_barras()

