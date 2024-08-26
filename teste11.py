class Contato: 
 def __init__(self, nome, endereco, email): 
  self.nome = nome 
  self.endereco = endereco 
  self.email = email 
  #aqui ele cria as variaveis
class Agenda: 
 def __init__(self): 
  self.contatos = []
 def adicionar_contato(self, contato): 
  self.contatos.append(contato) 
 def remover_contato(self, contato): 
  self.contatos.remove(contato)
 def listar_contatos(self): 
  for contato in self.contatos:

#gerencia uma lista de contatos, permitindo adicionar, remover e listar contatos armazenados.
   print("nome", contato.nome)
   print("Endereço:", contato.endereco) 
   print("email", contato.email) 

agenda = Agenda()
contato1 = Contato("João", "Rua A, 123", "joao@example.com")
contato2 = Contato("Maria", "Rua B, 456", "maria@example.com")

agenda.adicionar_contato(contato1) 
agenda.adicionar_contato(contato2) 
agenda.listar_contatos() 
agenda.remover_contato(contato1) 
agenda.listar_contatos()
#aqui ele meio que seta os atributos das variaveis 