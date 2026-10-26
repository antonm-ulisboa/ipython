MENU ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def get_price(item):
    # Normalize the input before looking up the price.
    return MENU.get(item.strip().title())


def main():
    total = 0

    while True:
        try:
            item = input("Item: ")
        except EOFError:
            # Ctrl+D ends the order.
            print()
            break

        price = get_price(item)

        if price is not None:
            total += price
            print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()
