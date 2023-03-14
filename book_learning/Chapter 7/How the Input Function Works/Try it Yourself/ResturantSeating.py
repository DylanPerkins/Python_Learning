# Try it Yourself | 7-2

guests = input("How many seats will you need for dinner tonight? ")
guests = int(guests)

if guests > 8:
    print(f"Unfortunately you'll have to wait a little bit for a table of {guests} people.")
else:
    print(f"A table for {guests} is ready, please follow me!")