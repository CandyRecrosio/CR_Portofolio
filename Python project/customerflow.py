from databasemenu import  books, cakes, coffees


from orders import (
    find_item_by_id,
    add_item_to_order,
    view_order,
    order,
)




def show_welcome_message():
    print("=" * 60)
    print("📚☕ Welcome to Brewed & Booked Bookshop & Café!")
    print("Your favourite place for books, coffees, and cakes. ☕️📚🍰")
    print("=" * 60)




def show_main_menu():
    print("\nMain Menu")
    print("\t1. 🚻 Customer\t2. Employee\t3. Exit")




def show_customer_menu():
    print("\n--- 🛒 Customer Menu ---")
    print("\t1. View & Add to Order")
    print("\t2. Search Product Details")
    print("\t3. Review yor order")
    print("\t4. Checkout and Pay")
    print("\t5. Return to Main Menu")




# ---------- MENU DISPLAY FUNCTIONS ----------




def display_coffees():
    print("\n☕ Coffees")
    for coffee in coffees:
        print(f"\t{coffee['id']} - {coffee['name']} (£{coffee['price']})")




def display_cakes():
    print("\n🍰 Cakes")
    for cake in cakes:
        print(f"\t{cake['id']} - {cake['name']} (£{cake['price']})")




def display_books():
    print("\n📚 Books")
    for book in books:
        print(f"\t{book['id']} - {book['name']} (£{book['price']})")




def display_full_menu():
    print("\n--- 📋 Brewed & Booked Menu ---")
    display_coffees()
    display_cakes()
    display_books()




def take_card_payment_for_order():
    # UPDATED: Uses global order from orders.py
    if not order:
        print("❌ Your order is empty. Cannot process payment.")
        return False


    # Calculate total from order items (uses quantity from orders)
    total_amount = sum(item["price"] * item["quantity"] for item in order)
    print(f"\n💳 Your total amount is £{total_amount:.2f}")
    input("Press Enter to simulate card payment...")
    confirm = input("Confirm payment? (y/n): ").strip().lower()
    if confirm == "y":
        print("✅ Payment successful!")
        return True
    else:
        print("❌ Payment cancelled.")
        return False




def get_item_by_user_input():
    try:
        item_id = int(input("\nEnter the item ID: "))
        item = find_item_by_id(item_id)
        if item:
            print(f"\n🔍 Product Details")
            print(f"\tName: {item['name']}")
            print(f"\tPrice: £{item['price']:.2f}")
            print(f"\tDescription: {item['description']}")
            return item
        else:
            print("❌ Item not found.")
            return None
    except ValueError:
        print("❌ Please enter a numeric ID.")
        return None




# ---------- CUSTOMER FLOW ----------




def customer_flow():
    # USES GLOBAL: order from orders.py (not local variable)
    while True:
        show_customer_menu()
        choice = input("Please select (1-5): ")


        if choice == "1":
            display_full_menu()
            item = get_item_by_user_input()
            if item:
                confirm = input(
                    f"Do you want {item['name']} added to order? (y/n): "
                ).lower()
                if confirm == "y":
                    # REPLACED: Now uses add_item_to_order() from orders.py
                    add_item_to_order(item["id"])


        elif choice == "2":
            display_full_menu()
            get_item_by_user_input()
            input("\nPress Enter to return...")


        elif choice == "3":
            # REPLACED: Now uses view_order() from orders.py
            view_order()


        elif choice == "4":
            # UPDATED: Uses global order from orders.py
            payment_success = take_card_payment_for_order()


            if payment_success:
                print("\n" + "✨" * 25)
                print("Thank you for your order at Brewed & Booked!")
                print("Your treats and books will be ready shortly.")
                print("✨" * 25)
                # REPLACED: Now uses order.clear()




                order.clear()
                break


        elif choice == "5":
            print("\nReturning to Main Menu...")
            break
        else:
            print("❌ Invalid choice. Please try again.")




# ---------- MAIN APP ----------




def main():
    show_welcome_message()


    while True:
        show_main_menu()
        choice = input("Please select an option (1–3): ")


        if choice == "1":
            customer_flow()


        elif choice == "2":
            print("\n🔐 Employee access coming soon...")
            # placeholder – Connect the employee flow


        elif choice == "3":
            print("\n👋 Thank you for visiting Brewed & Booked. Goodbye!")
            break


        else:
            print("❌ Invalid choice. Please try again.")




if __name__ == "__main__":
    main()






