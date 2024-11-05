class Order:
  def __init__(self, order_id, customer):
    self.order_id = order_id             
    self.customer = customer              
    self.products = []                    
    self.total_price = 0.0             
    
  def calculate_total(self):
    self.total_price = sum(product.price * quantity for product, quantity in self.products)  
  
  def add_product(self, product, quantity):
    self.products.append((product, quantity))
    self.calculate_total()  
    
  def __str__(self):
    products_info = "\n".join(f"- {product.product_name} (x{quantity}): {product.price * quantity:.2f}"for product, quantity in self.products)
    return (f"Order[ID: {self.order_id}, Customer: {self.customer.name}, Total Price: {self.total_price:.2f}$]\nProducts:\n{products_info}")