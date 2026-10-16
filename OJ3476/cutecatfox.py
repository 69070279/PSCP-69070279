"""[LEARNING LOGS] CuteCat CuteFox"""

import json

def main():
    """Main Function"""
    cats = {}
    foxes = {}
    amount = int(input())

    for _ in range(amount):
        raw = input()
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            data = json.loads(raw.replace("'", '"'))

        for key, value in data.items():
            if "Cat" in value:
                cats[key] = value
            else:
                foxes[key] = value

    if "Garfield" not in foxes and "Cat01" not in cats.values():
        cats.setdefault("Garfield", "Cat01")
    if "Fubuki" not in cats and "Fox01" not in foxes.values():
        foxes.setdefault("Fubuki", "Fox01")

    print("Cat :", len(cats))
    print("Fox :", len(foxes))
    for key, value in sorted(cats.items(), key=lambda v: int(v[1][3:])):
        print(f"{key} : {value}")
    for key, value in sorted(foxes.items(), key=lambda v: int(v[1][3:])):
        print(f"{key} : {value}")

main()
