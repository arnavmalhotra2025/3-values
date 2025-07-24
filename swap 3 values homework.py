# Input three values
a = input("Enter value for a: ")
b = input("Enter value for b: ")
c = input("Enter value for c: ")

print("\nBefore swapping:")
print(f"a = {a}, b = {b}, c = {c}")

# Swapping logic
# a -> b, b -> c, c -> a
a, b, c = c, a, b

print("\nAfter swapping:")
print(f"a = {a}, b = {b}, c = {c}")