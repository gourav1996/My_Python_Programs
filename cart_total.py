lower_range=0
upper_range=99
cart_item=[]
cart_quantity=[]
cart = []
name=input('HELLO,"PLEASE ENTER YOUR NAME"::')
print(f'"Welcome {name},Start Adding Names and Prices of Item From Your Cart to Get Total bill"')
while upper_range>lower_range:
    lower_range=lower_range+1
    item_in=input("Enter The Name Of Item::")
    price=int(input("Enter the price of Item:: "))
    quantity=int(input("Enter The quantiy of Item::"))
    price_total=price*quantity
    cart.append(price_total)
    cart_item.append(item_in)
    cart_quantity.append(quantity)
    opt=int(input("Enter '0' if u want to Continue adding Items in Cart::\nEnter '1' If You Dont want to add item in Cart Further:: \n "))
    if opt==1:
       lower_range=99
    else :
        print("Keep Adding::")
#TO PRINT LIST SIDE BY SIDE
total_cart=(sum(cart))
print("Bill Over View")
for cart_item,cart_quantity,cart in zip(cart_item,cart_quantity,cart):
    print(f"{cart_item} {cart_quantity} {cart}")
print(f"TOTAL BILL={total_cart}")

print(f'{name},"THANKS FOR SHOPPING WITH US"')

