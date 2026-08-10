import math

data = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue")
]

x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))

distances = []

for point, px, py, label in data:
    d = math.sqrt((x - px) ** 2 + (y - py) ** 2)
    distances.append((d, point, label))

distances.sort()

k = 3
nearest = distances[:k]

print("\nNearest Neighbors:")
for d, point, label in nearest:
    print(point, "- Distance:", round(d, 2))

red = 0
blue = 0

for d, point, label in nearest:
    if label == "Red":
        red += 1
    else:
        blue += 1

if red > blue:
    result = "Red"
else:
    result = "Blue"

print("\nPredicted Class:", result)