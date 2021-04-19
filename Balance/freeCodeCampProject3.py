from Balance.conversor import converte_amount_str


class Category:

  ledger: list = []
  balance: float = 0

  def __init__(self, category: str):
    self.__category: str = category
    self.__balance: float = Category.balance
    self.__ledger: list = Category.ledger

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
      return True
    else:
      return False

  def get_balance(self) -> str:
    return f'O saldo é {self._Category__balance}'

  # Retira do saldo da categoria atual (self) e deposita em outra categoria (anotther_category)
  def transfer(self, amount, another_category):  
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
  
