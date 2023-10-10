class Product:
    def __init__(self, name: str, price: int, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity


class Shope:
    prdct_list = []

    def __init__(self, name: str, location: str) -> None:
        self.name = name
        self.location = location

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self.prdct_list.append(product)
        else:
            print("Invalid Product")

    def buy_product(self, productName: str, quantity: int) -> None:
        for product in self.prdct_list:
            if product.name == productName:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    print(
                        f'Congratulations! You bought {productName} quantity is {quantity}')
                else:
                    print(
                        f'We have the quanity of the product is {product.quantity} and you enter {quantity}')
            else:
                print(f'Sorry {productName} not found in the shop')


menaBazar = Shope("Mina Bazar","Mirpur")
prdct1 = Product("Laptop",3000, 2)
menaBazar.add_product(prdct1)
menaBazar.buy_product("Mobile",1)