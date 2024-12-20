print("Choose a formula to calculate:")
print("1. Perimeter of a square")
print("2. Area of a triangle")
print("3. Diameter of a circle")
print("4. Force")
print("5. Speed")

choice = int(input("Enter the number corresponding to your choice (1-5): "))

if choice == 1:
    print("Formula for the perimeter of a square is P = 4a")
    a = float(input("Enter the length of a side of the square: "))
    print(f"The perimeter of the square is: {4 * a}")

elif choice == 2:
    print("Formula for the area of a triangle is A = 0.5 * base * height")
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print(f"The area of the triangle is: {0.5 * base * height}")

elif choice == 3:
    print("Formula for the diameter of a circle is d = 2r")
    r = float(input("Enter the radius of the circle: "))
    print(f"The diameter of the circle is: {2 * r}")

elif choice == 4:
    print("Formula for force is F = mass * acceleration")
    mass = float(input("Enter the mass of the object: "))
    acceleration = float(input("Enter the acceleration: "))
    print(f"The force is: {mass * acceleration}")

elif choice == 5:
    print("Formula for speed is S = distance / time")
    distance = float(input("Enter the distance: "))
    time = float(input("Enter the time: "))
    if time != 0:
        print(f"The speed is: {distance / time}")
    else:
        print("Time cannot be zero. Division by zero is undefined.")

else:
    print("Invalid choice! Please select a number between 1 and 5.")