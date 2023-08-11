katz_deli = []

def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        positions = [f"{i+1}. {name}" for i, name in enumerate(katz_deli)]
        print("The line is currently:", " ".join(positions))

line(katz_deli)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")


def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        del katz_deli[0]    



