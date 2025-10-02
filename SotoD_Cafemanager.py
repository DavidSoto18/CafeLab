
cafe_name = "Soto Cafe"
tax_rate = 0.07

item_names = []
item_prices = []
item_quantities = []

discount_used = False

def show_banner():
    print("=" * 50)
    print(f"Welcome to {cafe_name} -- Tax Rate: {tax_rate * 100:.2f}%")
    print("=" * 50)

def add_item(name: str, price: float, qty: int):
    item_names.append(name)
    item_prices.append(price)
    item_quantities.append(qty)
    print(f"Added {qty} x {name} at ${price:.2f} each.")

def view_cart():
    if not item_names:
        print("Your cart is empty.")
        return

    print("\nCurrent Cart:")
    subtotal = 0
    for i in range(len(item_names)):
        line_total = item_prices[i] * item_quantities[i]
        subtotal += line_total
        print(f"{i+1}. {item_quantities[i]} x {item_names[i]} @ ${item_prices[i]:.2f} = ${line_total:.2f}")

    print(f"Subtotal: ${subtotal:.2f}")

    max_price = max(item_prices)
    max_index = item_prices.index(max_price)
    print(f"Most expensive item: {item_names[max_index]} @ ${max_price:.2f}")

    avg_line_total = subtotal / len(item_names)
    print(f"Average line total: ${avg_line_total:.2f}")

def remove_item(index: int):
    if 1 <= index <= len(item_names):
        removed_name = item_names.pop(index - 1)
        item_prices.pop(index - 1)
        item_quantities.pop(index - 1)
        print(f"Removed item: {removed_name}")
    else:
        print("Invalid item number.")

def compute_subtotal() -> float:
    return sum(price * qty for price, qty in zip(item_prices, item_quantities))

def compute_tax(subtotal: float, tax_rate: float) -> float:
    return subtotal * tax_rate

def apply_discount(subtotal: float, code: str) -> float:
    if code == "STUDENT10":
        return subtotal * 0.10
    return 0.0

def checkout():
    global discount_used

    if not item_names:
        print("Your cart is empty.")
        return

    subtotal = compute_subtotal()
    print(f"Cart subtotal: ${subtotal:.2f}")
    code = input("Enter discount code (or press Enter): ").strip()

    discount = 0.0
    if code == "STUDENT10":
        if not discount_used:
            discount = apply_discount(subtotal, code)
            discount_used = True
        else:
            print("Discount code already used.")
    elif code:
        print("Invalid discount code.")

    tax = compute_tax(subtotal - discount, tax_rate)
    total = subtotal - discount + tax

    print("\n--- RECEIPT ---")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"TOTAL: ${total:.2f}")
    print(f"\nThank you for visiting {cafe_name}!")

    item_names.clear()
    item_prices.clear()
    item_quantities.clear()

def main_menu():
    show_banner()

    while True:
        print("\n1) Add item")
        print("2) View cart")
        print("3) Remove item")
        print("4) Checkout")
        print("5) Quit")

        choice = input("Choose: ").strip()

        if choice == '1':
            name = input("Item name: ").strip()
            if not name:
                print("Item name cannot be empty.")
                continue
            try:
                price = float(input("Item price: "))
                qty = int(input("Quantity: "))
                if price < 0 or qty < 0:
                    print("Price and quantity must be non-negative.")
                    continue
                add_item(name, price, qty)
            except ValueError:
                print("Invalid input. Price must be a number, quantity must be an integer.")

        elif choice == '2':
            view_cart()

        elif choice == '3':
            try:
                index = int(input("Enter item number to remove: "))
                remove_item(index)
            except ValueError:
                print("Invalid input. Please enter a valid item number.")

        elif choice == '4':
            checkout()

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main_menu()