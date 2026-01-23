'''
SD-GAL-05 SD-TA-007 Exercise 005
Author: Mary Ronan
Last Modified: 22/01/2026
OOP Python - Stock Control System
'''
from abc import ABC, abstractmethod

# Class
class Product:

    # Class Instance
    def __init__(self, prodCode, prodName, prodDescription, prodPrice):
        self.prodCode = prodCode
        self.prodName = prodName
        self.prodDescription = prodDescription
        self.prodPrice = prodPrice

# Abstract Class
class Goods(Product, ABC):

    # Class Instance
    def __init__(self, prodCode, prodName, prodDescription, prodPrice, quantity):
        super().__init__(prodCode, prodName, prodDescription, prodPrice)
        self.quantity = quantity

    # Get Product Quantity
    def getQuantity(self):
        return self.quantity

    # Display Product Information
    @abstractmethod
    def getProductDetails(self):
        pass

# Class 
class GoodsIn(Goods):

    # Class Variables
    storageCharge = 5.00

    # Class Instance
    def __init__(self, prodCode, prodName, prodDescription, prodPrice, quantity, supplierCode):
        super().__init__(prodCode, prodName, prodDescription, prodPrice, quantity)
        self.supplierCode = supplierCode

    # Display Product Information
    def getProductDetails(self):
        print("Product: ", self.prodCode, "-", self.prodName, "-", self.prodDescription)
    
    # Calculate Storage Charge
    def calcStorageCharge(self):
        return self.storageCharge * self.quantity

# Class 
class GoodsOut(Goods):

    # Class Instance
    def __init__(self, prodCode, prodName, prodDescription, prodPrice, quantity, customerName, deliveryRegNumber):
        super().__init__(prodCode, prodName, prodDescription, prodPrice, quantity)
        self.customerName = customerName
        self.deliveryRegNumber = deliveryRegNumber

    # Display Product Information
    def getProductDetails(self):
        print("Product: ", self.prodCode, "-", self.prodName)

    # Get Delivery Registration Number
    def getRegNumber(self):
        return self.deliveryRegNumber

# Main Program
def main():

    # Get User Input
    print("=".ljust(50, "="))
    print("Welcome to the Stock Management System".center(50))
    print("=".ljust(50, "="))
    goodsType = input("Goods Inbound or Outbound [I/O]: ")
    prodCode = input("Enter Product Code: ")
    prodName = input("Enter Product Name: ")
    prodDescription = input("Enter Product Description: ")
    prodPrice = float(input("Enter Product Price: €"))
    quantity = int(input("Enter Quantity: "))

    # Create Goods Instance
    if goodsType.upper() == "I":
        supplierCode = input("Enter Supplier Code: ")
        goods = GoodsIn(prodCode, prodName, prodDescription, prodPrice, quantity, supplierCode)
    else:
        customerName = input("Enter Customer Name: ")
        deliveryRegNumber = input("Enter Delivery Van Registration Number: ")
        goods = GoodsOut(prodCode, prodName, prodDescription, prodPrice, quantity, customerName, deliveryRegNumber)
        
    # Process Goods Inbound
    if isinstance(goods, GoodsIn):
        print("-".ljust(50, "-"))
        print("Goods Inbound".center(50))
        print("-".ljust(50, "-"))
        print("Product: ", goods.getProductDetails())
        print("Quantity: ",goods.getQuantity())
        print("Supplier Code: ", goods.supplierCode)
        print("Storage Charge: €", goods.calcStorageCharge())
        print("-".ljust(50, "-"))

    # Process Goods Outbound
    if isinstance(goods, GoodsOut):
        print("-".ljust(50, "-"))
        print("Goods Outbound".center(50))
        print("-".ljust(50, "-"))
        print("Product: ", goods.getProductDetails())
        print("Quantity: ",goods.getQuantity())
        print("Customer: ",goods.customerName)
        print("Delivery Registration No.: ", goods.getRegNumber())
        print("-".ljust(50, "-"))
    
main()
    

            
        
    

