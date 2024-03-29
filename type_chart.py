type_chart = (
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,1,1,1,1,1,1,1,1,1,1,1,1,0.5,0,1,1,0.5),
    (0,1,0.5,0.5,1,2,2,1,1,1,1,1,2,0.5,1,0.5,1,2),
    (0,1,2,0.5,1,0.5,1,1,1,2,1,1,1,2,1,0.5,1,1),
    (0,1,1,2,0.5,0.5,1,1,1,0,2,1,1,1,1,0.5,1,1),
    (0,1,0.5,2,1,0.5,1,1,0.5,2,0.5,1,0.5,2,1,0.5,1,0.5),
    (0,1,0.5,0.5,1,2,0.5,1,1,2,2,1,1,1,1,2,1,0.5),
    (0,2,1,1,1,1,2,1,0.5,1,0.5,0.5,0.5,2,0,1,2,2),
    (0,1,1,1,1,2,1,1,0.5,0.5,1,1,1,0.5,0.5,1,1,0),
    (0,1,2,1,2,0.5,1,1,2,1,0,1,0.5,2,1,1,1,2),
    (0,1,1,1,0.5,2,1,2,1,1,1,1,2,0.5,1,1,1,0.5),
    (0,1,1,1,1,1,1,2,2,1,1,0.5,1,1,1,1,0,0.5),
    (0,1,0.5,1,1,2,1,0.5,0.5,1,0.5,2,1,1,0.5,1,2,0.5),
    (0,1,2,1,1,1,2,0.5,1,0.5,2,1,2,1,1,1,1,0.5),
    (0,0,1,1,1,1,1,1,1,1,1,2,1,1,2,1,0.5,0.5),
    (0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,0.5),
    (0,1,1,1,1,1,1,0.5,1,1,1,2,1,1,2,1,0.5,0.5),
    (0,1,0.5,0.5,0.5,1,2,1,1,1,1,1,1,2,1,1,1,0.5)
)

type_name = {
    0: "Null",
    1: "Normal",
    2: "Fire",
    3: "Water",
    4: "Electric",
    5: "Grass",
    6: "Ice",
    7: "Fighting",
    8: "Poison",
    9: "Ground",
    10: "Flying",
    11: "Psychic",
    12: "Bug",
    13: "Rock",
    14: "Ghost",
    15: "Dragon",
    16: "Dark",
    17: "Steel"
}

if __name__ == "__main__":
    for y, i in enumerate(type_chart):
        print(f"Type {type_name[y]}")
        for x, n in enumerate(type_chart):
          print(f"Against {type_name[x]}: {type_chart[y][x]}")
        print("")