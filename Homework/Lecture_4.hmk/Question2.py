VANILLA = 1
CHOCOLATE = 2
STRAWBERRY = 3
MANGO = 4

print("""flavours:
1. Vanilla
2. Chocolate
3. Strawberry
4. Mango""")

choice = int(input("Pick a flavour (1-4): "))

if choice == 1:
    flavour_name = "Vanilla"
elif choice == 2:
    flavour_name = "Chocolate"
elif choice == 3:
    flavour_name = "Strawberry"
elif choice == 4:
    flavour_name = "Mango"
else:
    print(f"{choice} is not on the menu. Serving Vanilla")
    flavour_name = "Vanilla"

print(f"You ordered: {flavour_name}")