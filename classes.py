# class MyClass:
#     a = 'b';
    
#     def dog(self):
#         print("Bark Bark")

# newClass = MyClass()
# print(newClass.dog())


class pagamento:
    def __init__(this,nome ,pagamento_status,quantidade) -> None:
        this.nome = nome
        this.pagamento_status = pagamento_status
        this.quantidade = quantidade

    def pago(this):
        this.pagamento_status = "sim"

    def status_pagamento(this):
        if this.pagamento_status == "sim":
            print(this.nome + " ja foi pago esse més, a quantidade de " + str(this.quantidade))
        else:
            print(this.nome + " ainda não foi pago esse més!")
        
def verify_pagamento():
    print("--------DIA DO PAGAMENTO----------")
    gui = pagamento("Guilherme", "no", 1200)
    alyfer = pagamento("Alyfer", "no", 1200)
    alyfer.pago()

    gui.status_pagamento()
    alyfer.status_pagamento()



class filmes:
    def __init__(this, filme,rate,genero) -> None:
        this.filme = filme
        this.genero = genero
        this.rate = rate

    def sobre(this):
        print("The " + this.filme + " has " + str(this.rate) + \
            " and is one of the best " + this.genero + " movie!")


def sobre_filme():
    print("______FILMES DO ANO________")
    black_adam = filmes("Black Adam", 9, "Action")
    print(black_adam.sobre())
    print("______________________________________________")
    
    eternals = filmes("Eternals", 8, "Action")
    print(eternals.sobre())
    print("______________________________________________")

    black_panter = filmes("Black Panter", 8, "Action")
    print(black_panter.sobre())
    print("______________________________________________")


calabresa = ["Queijo, Tomate, Calabreza, Azeitona"]
italiana = ["Molho de tomate", "Muçarela de búfala", "Manjericão"," Alcachofra", "Cogumelos"]
portuguesa = ["ovo cozido","presunto","queijo","azeitona", "orégano","tomate" ]

class Pizzaria:
    def __init__(self,pizza, items, time) -> None:
        self.pizza = pizza
        self.items = items
        self.time = time

    def sobre(self):
        print(self.pizza + " tem " + str(self.items)  \
            + " e leva " + str(self.time) + " para preparar." )



def display_pizzaria_menu():
    print("------- Menu -------")
    pizza_calabreza = Pizzaria("Pizza Calabresa", calabresa , 40)
    print("Pizza: ", pizza_calabreza.pizza)
    print("Tempo: ", pizza_calabreza.time)
    print("Acompanha: ",pizza_calabreza.items )
    print("____________________________________________________")

    pizza_italiana = Pizzaria("Pizza Italiana", italiana , 45)
    print("Pizza: ", pizza_italiana.pizza)
    print("Tempo: ", pizza_italiana.time)
    print("Acompanha: ",pizza_italiana.items )
    print("____________________________________________________")

    
    pizza_portuguesa = Pizzaria("Pizza Portuguesa", portuguesa, 45 )
    print("Pizza: ", pizza_portuguesa.pizza)
    print("Tempo: ", pizza_portuguesa.time)
    print("Acompanha: ",pizza_portuguesa.items )
    print("____________________________________________________")



def main():
    print("\n")
    verify_pagamento()
    print("\n")
    
    sobre_filme()
    print("\n")

    display_pizzaria_menu()
    print("\n")

if __name__ == "__main__":
    main()