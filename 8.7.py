favorite = ["sway", 
            "yuki",
            "sunflower",
            "baica",
            "shingun"]

print(favorite)

print(favorite[1])
print(favorite[2])

print(favorite[3])

print(favorite[4])

print(favorite[0])


favorite.append("pretender")

print(favorite)

num_songs=len(favorite)

print("there are " + str(num_songs) + " songs in the paylist")

favorite.pop(2)

print(favorite)

print(len(favorite))