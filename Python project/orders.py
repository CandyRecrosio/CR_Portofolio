

from databasemenu import books, cakes, coffees




order = []




def find_item_by_id(item_id):
    for item in coffees + cakes + books:
        if item["id"] == item_id:
            return item
    return None




def add_item_to_order(item_id):
    item = find_item_by_id(item_id)


    if not item:
        print("Item not found.")
        return False


    for order_item in order:
        if order_item["id"] == item_id:
            order_item["quantity"] += 1
            print(
                f"Added another {item['name']} to your order (quantity: {order_item['quantity']})"
            )
            return True


    order_item = {
        "id": item["id"],
        "name": item["name"],
        "price": item["price"],
        "quantity": 1,
    }


    order.append(order_item)
    print(f"{item['name']} added to your order!")
    return True




def view_order():
    if not order:
        print("\nYour order is empty.")
        return


    print("\nYOUR ORDER:")
    total = 0.0


    for item in order:
        item_total = item["price"] * item["quantity"]
        total += item_total
        print(f"  - {item['name']} x{item['quantity']} = £{item_total:.2f}")


    print(f"\nTOTAL: £{total:.2f}")


