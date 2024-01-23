print("*** Welcome to the multiplication table ***")
number=int(input("Enter a number:"))
print(f"Multiplication table for {number}:")
for aze in range (1,11):
  result = aze * number
  print(f" {number} × {aze} = {result}")
