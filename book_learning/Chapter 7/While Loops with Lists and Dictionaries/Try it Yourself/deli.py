# Try it Yourself | 7-8

sandwhich_orders = ["Tatnic Thriller", "Italian", "Ruben", "Hotdog"]
finished_sandwhich = []

while sandwhich_orders:
    current_order = sandwhich_orders.pop()

    print(f"I made ya {current_order}!")
    finished_sandwhich.append(current_order)

print("\nThe following sandwhiches have been made:")
for sandwhich in finished_sandwhich:
    print(sandwhich.title())