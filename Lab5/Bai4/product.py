class Product:
  def __init__(self, product_id, product_name, price, stock):
    self.product_id = product_id
    self.product_name = product_name
    self.price = price
    self.stock = stock
    
  def update_stock(self, quantity):
    if quantity > 0 and quantity <= self.stock:
      self.stock -= quantity
      return True
    return False
    
  def __str__(self):
    return (f"Product[ID: {self.product_id}, Name: {self.product_name}, Price: {self.price}, Stock: {self.stock}]")