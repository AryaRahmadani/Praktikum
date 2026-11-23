nama_hero = "Arga"
level = 10
hp = 250.5
is_alive = True
inventory = ["Pedang", "Panah", "Belati", "Perisai"]
atribut = {"kekuatan": 80, "kelincahan": 65}

print("=== PROFIL KARAKTER ===")
print("Nama Hero :", nama_hero)
print("Level     :", level)
print("HP        :", hp)
print("Hidup     :", is_alive)
print("Inventory :", inventory)
print("Atribut   :", atribut)

print("\n=== TIPE DATA ===")
print("nama_hero :", type(nama_hero))
print("level     :", type(level))
print("hp        :", type(hp))
print("is_alive  :", type(is_alive))
print("inventory :", type(inventory))
print("atribut   :", type(atribut))


inventory.append("Ramuan HP")


level = float(level)
level = level + 0.5


print("\n=== PROFIL KARAKTER (TERBARU) ===")
print("Nama Hero :", nama_hero)
print("Level     :", level)
print("HP        :", hp)
print("Hidup     :", is_alive)
print("Inventory :", inventory)
print("Atribut   :", atribut)
print("Tipe data level sekarang:", type(level))