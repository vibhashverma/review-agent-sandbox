def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error: Cannot divide by zero." if y == 0 else x / y

operations = {"1": ("+", add), "2": ("-", subtract), "3": ("*", multiply), "4": ("/", divide)}

while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = input("Enter choice (1/2/3/4) or 'q' to quit: ").strip().lower()
    if choice == 'q': print("Goodbye!"); break
    if choice in operations:
        try:
            n1, n2 = float(input("Enter first number: ")), float(input("Enter second number: "))
            sym, fn = operations[choice]
            print(f"Result: {n1} {sym} {n2} = {fn(n1, n2)}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    else:
        print("Invalid choice.")

