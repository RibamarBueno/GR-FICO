import matplotlib.pyplot as plt 

def criar_grafico_barras():
    categorias = ['a','b','c','d']
    valores = [20,35,30,15]

    plt.bar(categorias, valores)

    plt.title('Grafico de barras')
    plt.xlabel('Categorias')
    plt.ylabel('Valores')

    plt.show()

if __name__ ++ "__main__":
    criar_grafico_barras()   


