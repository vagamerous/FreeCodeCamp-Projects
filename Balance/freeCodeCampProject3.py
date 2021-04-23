from Balance.conversor import converte_amount_str
"""arquivo que contem uma unica funcao que converte o valor inserido em string para ser retornado no final"""

class Category:

  ledger: list = []  # e o extrato, aquilo q e mostrado quando damos print no objeto
  balance: float = 0
  categories: list = [] # usada no gráfico
  spent: float = 0
  spentmap: dict = {} # dicionario dos valores gastos, tendo como chave o nome da categoria. Usado no gráfico de gastos; 

  def __init__(self, category: str):
    self.__category: str = category
    self.__balance: float = Category.balance
    self.__ledger: list = Category.ledger
    Category.categories.append(self.__category)
    self.__spent: float = Category.spent
    self.__spentmap = Category.spentmap
    

  def check_funds(self, amount):
    if float(amount) > self.__balance:
      return False
    else:
      return True

  def deposit(self: object, amount: float, description: str ="None"):
    Category.ledger.append({'amount': amount, 'description': description})
    self.__balance: float = Category.balance + float(amount)

  def withdraw(self, amount, description: str ='None'):
    x = Category.check_funds(self, amount)
    if x == True:
      Category.ledger.append({'amount': amount, 'description': description})
      self.__balance = self.__balance - float(amount)
      Category.spent =  Category.spent + float(amount)
      found = False
      for chave in Category.spentmap.keys():
        if chave == f'{self.__category}':
          Category.spentmap[f'{self.__category}'] = Category.spentmap[f'{self.__category}'] + float(amount)
          found = True
      if found == False:
        Category.spentmap[f'{self.__category}'] = float(amount)
        
      return True
    else:
      return False

  def get_balance(self) -> str:
    return f'O saldo é {self._Category__balance}'

  
  def transfer(self, amount, another_category):
    """# Retira do saldo da categoria atual (self) e deposita em outra categoria (anotther_category)"""
    if Category.check_funds(self, amount) == True:
      Category.withdraw(self, amount, "Transfer to f'{another_category}'")
      Category.deposit(another_category, amount, "Transfer from {self.__category}")
      return True
    else:
      return False

  def __str__(self: object) -> str:
    """É o que aparece na tela quando o usa-se o comando print no objeto -> print(objeto)"""
    return f'{self.formatacao()}'

  def formatacao(self: object) -> str:
    """Formata o  ledger quando faz o print do objeto"""
    print(f'{self.__category:*^30}') 
    for element in self.ledger:
      print('{: <23}'.format(element['description']), '{: >6}'.format(converte_amount_str(element['amount'])))
    print('{: ^7} {: <23}'.format('Total: ', f'{self._Category__balance}'))
    return ''

  


def create_spend_chart():

    percentage = 0
  
  print('Percentage spent by category')
  for x in range(10, 0, -1):
    print('{: >4}'.format(f'{x}0|', end=''))
    for element in Category.categories:
      percentage = 10*(Category.spentmap[element] / Category.spent)
      if percentage >= (x):
        print('{: ^3}'.format('o', end=''))
      else:
        print('{: ^3}'.format('', end=''))
  
