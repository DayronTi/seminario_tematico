#classe
#sintaxe
#características: Marca, Memória Ram, Placa vídeo

#init: 
#self: Serve para acessar as propriedades e métodos de uma instancia
#ñ podemos criar propriedades estáticas para todos os objetos
#esses são os atributos: 

#   class Computador:
#          def __init__(self, marca, memoria_ram,placa_de_video) -> None:
#             self.marca = marca
#            self.memoria_ram = memoria_ram
#            self.placa_de_video = placa_de_video
#        pass
#
#    computador1 = Computador('Lenovo','16gb','Nvidia')
#    computador2 = Computador('Asus', '8gb', 'Snorlax')
#    computador3 = Computador('Sansung', '12gb', 'Porra')
#    print(computador1.marca,computador1.memoria_ram,computador1.placa_de_video)
#    print(computador2.marca,computador2.memoria_ram,computador2.placa_de_video)
#    print(computador3.marca,computador3.memoria_ram,computador3.placa_de_video)

#Ligar, Desligar, Exibir configurações

class Computador: 
    def __init__(self, marca, memoria_ram, placa_de_video) -> None:
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def Ligar(self):
            print('Estou ligando')
        
    def Desligar(self):
            print('Estou desligando')

    def ExibirInformacoesDesteComputador(self):
            print(self.marca, self.memoria_ram, self.placa_de_video)

computador1 = Computador('asus', '18gb', 'Nvidia')
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformacoesDesteComputador()


#É útil ver o self como parâmetro dos seus métodos, pois desssa forma todas propriedades atribuidas para dentro do 'self' podem ser atribuidas ou acessadas em qualquer outro lugar, dentro da sua clase