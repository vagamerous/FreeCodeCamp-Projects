from Balance.conversor import converte_amount_str
from Balance.conversor import negative_amount
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
    self.__ledger: list = []
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
      Category.ledger.append({'amount': negative_amount(amount), 'description': description})
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
    for element in self.__ledger:
      print('{: <23}'.format(element['description']), '{: >6}'.format(converte_amount_str(element['amount'])))
    print('{: ^7} {: <23}'.format('Total: ', f'{self._Category__balance}'))
    return ''

  


def create_spend_chart():

  percentage0:float = 0
  percentage1:float = 0
  percentage2:float = 0
  percentage3:float = 0
  p0:str = ''
  p1:str = ''
  p2:str = ''
  p3:str = ''
  fin:str = '0|'  
  
  if len(Category.categories) == 1:
      percentage0 = 10*(Category.spentmap[Category.categories[0]] / Category.spent)
  if len(Category.categories) == 2:
      percentage0 = 10*(Category.spentmap[Category.categories[0]] / Category.spent)
      percentage1 = 10*(Category.spentmap[Category.categories[1]] / Category.spent)
  if len(Category.categories) == 3:
      percentage0 = 10*(Category.spentmap[Category.categories[0]] / Category.spent)
      percentage1 = 10*(Category.spentmap[Category.categories[1]] / Category.spent)
      percentage2 = 10*(Category.spentmap[Category.categories[2]] / Category.spent)
  if len(Category.categories) == 4:
      percentage0 = 10*(Category.spentmap[Category.categories[0]] / Category.spent)
      percentage1 = 10*(Category.spentmap[Category.categories[1]] / Category.spent)
      percentage2 = 10*(Category.spentmap[Category.categories[2]] / Category.spent)
      percentage3 = 10*(Category.spentmap[Category.categories[3]] / Category.spent)

  print('Percentage spent by category')
  
  for x in range(10, 0, -1):    

    if percentage0 >= x:
      p0 = 'o'
    else:
      p0 = ''
    
    if percentage1 >= x:
      p1 = 'o'
    else:
      p1 = ''

    if percentage2 >= x:
      p2 = 'o'
    else:
      p2 = ''

    if percentage3 >= x:
      p3 = 'o'
    else:
      p3 = ''
    
    print(f'{x: >2}{fin:^2}{p0: ^3}{p1: ^3}{p2: ^3}{p3: ^3}')
  
