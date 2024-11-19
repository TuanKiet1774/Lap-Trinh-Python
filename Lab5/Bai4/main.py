from product import Product
from customer import Customer
from order import Order


# Tạo khách hàng
customer1 = Customer(customer_id=64131060, name="Phạm Tuấn Kiệt", email = "kiet.pt.64cntt@ntu.edu.vn")
customer2 = Customer(customer_id=64131061, name="Huỳnh Minh Bảo", email= "bao.hm.64cntt@ntu.edu.vn")

# Tạo sản phẩm
bread = Product(product_id="SP001", product_name="Bánh mì", price=1.50, stock=100)
milk = Product(product_id="SP002", product_name="Sữa", price=2.00, stock=50)
noodle = Product(product_id="SP003", product_name="Mì gói", price=3.00, stock= 30)

# Tạo đơn hàng
order1 = Order(order_id="DH001", customer=customer1)
order2 = Order(order_id="DH002", customer=customer2)

# Thêm sản phẩm vào đơn hàng
order1.add_product(bread, 2)  # Thêm 2 bánh mì
order1.add_product(noodle, 3)  # Thêm 3 mì gói
order2.add_product(noodle, 3)  # Thêm 3 mì gói

#Thông tin các đơn hàng
print(order1)
print(order2)

print(noodle)