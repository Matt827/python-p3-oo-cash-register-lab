#!/usr/bin/env python3
import ipdb
class CashRegister:
  
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []
  
  def add_item(self, title, price, quantity = 1):
    self.total = self.total + (price * quantity)
    for item in range(quantity):
      self.items.append(title)
    self.previous_transactions.append(
      {
        'title': title,
        'price': price, 
        'quantity': quantity
      }
    )
    
  def apply_discount(self):
    if self.discount > 0:
      self.total = self.total - (self.total * (self.discount / 100))
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    last_transaction = self.previous_transactions.pop()
    self.total = self.total - (last_transaction["price"] * last_transaction["quantity"])
  
  
# cash = CashRegister()
# ipdb.set_trace()