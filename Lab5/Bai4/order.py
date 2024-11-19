from product import Product
from customer import Customer
class Order:
  def __init__(self, order_id, customer):
    self.order_id = order_id             
    self.customer = customer              
    self.products = []                    
    self.total_price = 0.0             
    
  #tổng tiền
  def calculate_total(self):
    self.total_price = sum(product.price * quantity for product, quantity in self.products)  
  
  #Thêm hàng vào hóa đơn với quantity - số lượng
  def add_product(self, product, quantity):
    if product.update_stock(quantity):
      self.products.append((product, quantity))
      return True
    return False 
    
  def __str__(self):
    self.calculate_total()
    products_info = "\n".join(f"- {product.product_name} (x{quantity}): {product.price * quantity:.2f}"for product, quantity in self.products)
    return (f"ID: {self.order_id}, Customer: {self.customer.name}, Total Price: {self.total_price:.2f}$\nProducts:\n{products_info}")