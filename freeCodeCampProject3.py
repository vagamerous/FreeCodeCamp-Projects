class Category:

  ledger = []
  balance = 0

  def __init__(self, category):
    self.__category = category
    self.__balance = Category.balance
    self.__ledger = Category.ledger

  def deposit(self, amount, description="None"):
    Category.ledger.append({'amount': amount, 'description': description})
    self.__balance = Category.balance + float(amount)

  def withdraw(self, amount, description='None'):
    if float(amount) < self.__balance:
      Category.ledger.append({'amount': amount, 'description': description})
      self.__balance =  float(amount)
      return True
    else:
      return False

  def get_balance(self):
    print(f'{self.__balance}')
    return self.__balance

  def transfer(self, amount, category):
    if float(amount) < self.__balance:
      Category.withdraw(self, amount, "Transfer to {category}")
      Category.deposit(category, amount, "Transfer from {self.__category}")
      return True
    else:
      return False
