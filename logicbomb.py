from datetime import date

today = date.today()
target = date(2024, 8, 15)  
def show_message():
    diamond_shape = [
        1, 3, 5, 7, 9, 11
    ]

    for row in diamond_shape:
        gap_size = int((14 - (0.5 * (row + 1))))
        print(" " * gap_size + "*" * row)
    print(">>>>> LOGIC BOMB <<<<<")
    print(" ")
    exit()

def bomb():
    if today == target:
        show_message()

print("Running program ")
bomb()
print("Nothing to see here...")
