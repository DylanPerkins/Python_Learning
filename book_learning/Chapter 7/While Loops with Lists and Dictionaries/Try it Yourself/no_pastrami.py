# Try it Yourself | 7-9

sandwhich_orders = ["Pastrami", "Tatnic Thriller", "Pastrami", "Italian", "Ruben", "Hotdog", "Pastrami"]
finished_sandwhich = []

print("Unfortunatley we're out'a Pastrami!")
while 'Pastrami' in sandwhich_orders:
    sandwhich_orders.remove('Pastrami')


while sandwhich_orders:
    current_order = sandwhich_orders.pop()

    print(f"I made ya {current_order}!")
    finished_sandwhich.append(current_order)

print("\nThe following sandwhiches have been made:")
for sandwhich in finished_sandwhich:
    print(sandwhich.title())