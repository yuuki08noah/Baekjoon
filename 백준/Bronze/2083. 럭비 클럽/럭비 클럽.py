while True:
    name, age, weight = input().strip().split()
    if name == '#': break
    age, weight = int(age), int(weight)
    print(name, "Junior" if age <= 17 and weight < 80 else "Senior")