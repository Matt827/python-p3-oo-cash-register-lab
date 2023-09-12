#!/usr/bin/env python3
import ipdb
class CashRegister:
  
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transaction = []
    
  def add_item(self, title, price, quantity = 1):
    self.total += price * quantity
    for n in range(quantity):
        self.items.append(title)
    self.previous_transaction.append(
      {"item": title, "price": price, "quantity": quantity}
    )
    
  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:  
      discount_total = self.total * (self.discount / 100)
      self.total -= discount_total
      print(f"After the discount, the total comes to ${int(self.total)}.")
      
  def void_last_transaction(self):
    last_transaction = self.previous_transaction.pop()
    self.total -= last_transaction["price"] * last_transaction["quantity"]
    for n in range(last_transaction["quantity"]):
      self.items.pop()
    if not self.items:
      self.total = 0