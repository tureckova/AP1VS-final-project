"""Basic converter from decimal numeral system."""

dest_base = int(input("Zadej číslem číselnou soustavu, "
                      "do které chceš číslo převést: "))
num = int(input(f"Zadej číslo v desítkové soustavě,"
                f"které chceš převést do {dest_base} soustavy: "))
num_copy = num
mod_list = []

while num > 0:
    mod_list.append(num % dest_base)
    num //= dest_base

mod_list.reverse()
mod_list = [str(i) for i in mod_list]
result = "".join(mod_list)

print()
print(f"Vámi zadané číslo {num_copy} z desítkové "
      f"soustavy se v {dest_base} soustavě zapisuje jako {result}.")
