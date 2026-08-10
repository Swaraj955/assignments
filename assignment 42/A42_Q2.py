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

print("\nPrediction Results")

for k in [1, 3, 5]:
    if k <= len(data):
        nearest = distances[:k]
    else:
        nearest = distances

    red = 0
    blue = 0

    for d, point, label in nearest:
        if label == "Red":
            red += 1
        else:
            blue += 1

    if red > blue:
        result = "Red"
    elif blue > red:
        result = "Blue"
    else:
        result = "Blue"

    print("K =", k, "->", result)

print("\nAs K increases, more nearby data points are considered.")