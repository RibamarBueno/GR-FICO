import matplotlib.pyplot as plt

def criar_grafico_barras():
    n_categorias = int(input("Digite o número de categorias : "))

    categorias = [] 
    valores = []

    for i in range (n_categorias):
        categoria = input("Digite o nome da categoria {i + 1} : ")
        valor = float("Digite o valor para a categoria {categoria} :")
        categorias.append(categoria)
        valores.append(valor)

    plt.bar(categorias, valores)

    plt.title('Gráfico de Barras')
    plt.xlabel('Categorias')
    plt.ylabel('Valores')

    plt.show()

if __name__ == "__main__":
    
    criar_grafico_barras()

