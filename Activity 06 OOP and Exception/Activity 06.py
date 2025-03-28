class Item:
    def __init__(self, item_id, name, description, price):
        self.id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Price: ${self.price:.2f}\nDescription: {self.description}"


class ItemManager:
    def __init__(self):
        self.items = {}  # Dictionary to store items with id as key

    def create_item(self):
        try:
            item_id = input("Enter Item ID: ").strip()
            if item_id in self.items:
                print("Error: Item ID already exists.")
                return

            name = input("Enter Item Name: ").strip()
            description = input("Enter Item Description: ").strip()
            price = float(input("Enter Item Price: ").strip())

            if price < 0:
                print("Error: Price must be a positive value.")
                return

            self.items[item_id] = Item(item_id, name, description, price)
            print("✅ Item added successfully!")

        except ValueError:
            print("Error: Price must be a valid number.")

    def read_items(self):
        if not self.items:
            print("No items found.")
        else:
            print("\n📋 Item List:")
            for item in self.items.values():
                print(item, "\n" + "-"*40)

    def update_item(self):
        item_id = input("Enter Item ID to update: ").strip()
        if item_id not in self.items:
            print("Error: Item not found.")
            return

        name = input("Enter new name (leave blank to keep current): ").strip()
        description = input("Enter new description (leave blank to keep current): ").strip()
        try:
            price_input = input("Enter new price (leave blank to keep current): ").strip()
            price = float(price_input) if price_input else self.items[item_id].price

            if price < 0:
                print("Error: Price must be a positive value.")
                return

            if name:
                self.items[item_id].name = name
            if description:
                self.items[item_id].description = description
            self.items[item_id].price = price

            print("✅ Item updated successfully!")

        except ValueError:
            print("Error: Price must be a valid number.")

    def delete_item(self):
        item_id = input("Enter Item ID to delete: ").strip()
        if item_id in self.items:
            del self.items[item_id]
            print("✅ Item deleted successfully!")
        else:
            print("Error: Item not found.")

    def menu(self):
        while True:
            print("\n📦 Item Management Menu:")
            print("[C] - Create Item")
            print("[R] - Read Items")
            print("[U] - Update Item")
            print("[D] - Delete Item")
            print("[X] - Exit")

            choice = input("Enter your choice: ").strip().upper()

            if choice == 'C':
                self.create_item()
            elif choice == 'R':
                self.read_items()
            elif choice == 'U':
                self.update_item()
            elif choice == 'D':
                self.delete_item()
            elif choice == 'X':
                print("Exiting... Have a great day! 🚀")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = ItemManager()
    manager.menu()
