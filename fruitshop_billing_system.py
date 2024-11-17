import tkinter as tk
from tkinter import messagebox

class SupermarketManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Fruits Store")
        self.root.geometry("1024x600")  # Adjusted for a wider window
        self.root.configure(bg="#F0F8FF")  # Light blue background

        self.items = {
            "Fruits": {
                "Apples": 100,
                "Bananas": 50,
                "Cherries": 150,
                "Dates": 200,
                "Grapes": 120,
                "Oranges": 30,
                "Guava": 120,
                "Kiwi": 250,
                "Mango": 100,
                "Pineapple": 80,
                "Watermelon": 100
            }
        }
        self.cart = {}

        self.create_widgets()

    def create_widgets(self):
        # Title Frame
        title_frame = tk.Frame(self.root, bg="#F0F8FF")
        title_frame.pack(fill=tk.X, pady=10)

        # Main Frame
        main_frame = tk.Frame(self.root, bg="#F0F8FF")
        main_frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

        # Items Frame (for displaying items)
        items_frame = tk.Frame(main_frame, bg="#F0F8FF")
        items_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Form Frame (for input fields)
        form_frame = tk.Frame(main_frame, bg="#F0F8FF")
        form_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Buttons Frame (for action buttons)
        buttons_frame = tk.Frame(main_frame, bg="#F0F8FF")
        buttons_frame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=10, pady=10)

        # Grid Configurations
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Title Label
        tk.Label(title_frame, text="Fruits store", font=("Arial", 24, "bold"), bg="#F0F8FF", fg="#00008B").pack()

        # Display Items (Fruit list)
        for category, items in self.items.items():
            tk.Label(items_frame, text=category, font=("Arial", 18, "bold"), bg="#F0F8FF", fg="#8B0000").pack(anchor="w")
            for item, price in items.items():
                tk.Label(items_frame, text=f"{item}: Rs. {price}", font=("Arial", 14), bg="#F0F8FF", fg="#4682B4").pack(anchor="w")

        # Form Frame for input fields
        form_inner_frame = tk.Frame(form_frame, bg="#F0F8FF")
        form_inner_frame.pack(pady=20)

        # Item Name Label and Entry
        tk.Label(form_inner_frame, text="Enter item name:", font=("Arial", 14), bg="#F0F8FF").grid(row=0, column=0, pady=5, padx=10, sticky="e")
        self.item_entry = tk.Entry(form_inner_frame, font=("Arial", 14), width=20)
        self.item_entry.grid(row=0, column=1, pady=5, padx=10)

        # Quantity Label and Entry
        tk.Label(form_inner_frame, text="Enter quantity:", font=("Arial", 14), bg="#F0F8FF").grid(row=1, column=0, pady=5, padx=10, sticky="e")
        self.quantity_entry = tk.Entry(form_inner_frame, font=("Arial", 14), width=20)
        self.quantity_entry.grid(row=1, column=1, pady=5, padx=10)

        # Add to Cart Button
        tk.Button(buttons_frame, text="Add to Cart", font=("Arial", 14), bg="#32CD32", fg="white", command=self.add_to_cart).pack(pady=10, fill=tk.X)

        # Show Bill Button
        tk.Button(buttons_frame, text="Show Total Bill", font=("Arial", 14), bg="#4682B4", fg="white", command=self.show_bill).pack(pady=10, fill=tk.X)

        # Exit Button
        tk.Button(buttons_frame, text="Exit", font=("Arial", 14), bg="#DC143C", fg="white", command=self.root.quit).pack(pady=10, fill=tk.X)

    def add_to_cart(self):
        item = self.item_entry.get().strip()
        quantity = self.quantity_entry.get().strip()
        found = False

        try:
            quantity = int(quantity)
            if quantity <= 0:
                messagebox.showerror("Error", "Please enter a valid quantity.")
                return

            # Search for item in the store
            for category in self.items.values():
                if item in category:
                    if item in self.cart:
                        self.cart[item] += quantity
                    else:
                        self.cart[item] = quantity
                    found = True
                    messagebox.showinfo("Cart Update", f"Added {quantity} {item}(s) to your cart.")
                    break

            if not found:
                messagebox.showerror("Error", "Item not available in store.")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid quantity.")

    def show_bill(self):
        if not self.cart:
            messagebox.showinfo("Total Bill", "No items in the cart.")
            return

        bill = 0
        bill_details = "Your Cart:\n"
        for item, quantity in self.cart.items():
            for category in self.items.values():
                if item in category:
                    price = category[item] * quantity
                    bill += price
                    bill_details += f"{item} x {quantity}: Rs. {price}\n"
                    break
        bill_details += f"\nTotal Bill: Rs. {bill}"

        messagebox.showinfo("Total Bill", bill_details)

if __name__ == "__main__":
    root = tk.Tk()
    app = SupermarketManagement(root)
    root.mainloop()
