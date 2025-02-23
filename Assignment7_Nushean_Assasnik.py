# homework7_Nushean_Assasnik.py

# Step 1: Create a list of pizza orders
pizza_orders = ["Pepperoni", "Margherita", "BBQ Chicken", "Veggie", "Hawaiian"]

# Step 2: Create an empty list for finished pizzas
finished_pizzas = []

# Step 3: Process each pizza order
while pizza_orders:
    current_pizza = pizza_orders.pop(0)  # Take the first pizza in the list
    print(f"Your {current_pizza} pizza pie is finished!")  # Print message
    finished_pizzas.append(current_pizza)  # Move it to finished pizzas

# Step 4: Print finished pizzas
print("\nAll pizzas are ready:")
for pizza in finished_pizzas:
    print(f"The pizza {pizza} was made.")
