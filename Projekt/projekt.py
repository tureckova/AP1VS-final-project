"""Basic converter from decimal numeral system."""

# Dictionary with values for hexadecimal numeral system
dict_with_letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

# Ask the user from which numeral system to which
# numeral system they want the number to be converted.
dest_base = int(input("Zadej číslem číselnou soustavu, "
                      "do které chceš číslo převést: "))
# Ask user what the number they want to convert is.
num = int(input(f"Zadej číslo v desítkové soustavě,"
                f"které chceš převést do {dest_base} soustavy: "))
num_copy = num
mod_list = []

while num > 0:
    mod_list.append(num % dest_base)
    num //= dest_base

# If the destination numeral system is hexadecimal,
# we need to cover the letter usage in this numeral system

if dest_base == 16:
    for i in range(len(mod_list)):
        if mod_list[i] > 9:
            mod_list[i] = dict_with_letters[mod_list[i]]

mod_list.reverse()
mod_list = [str(i) for i in mod_list]
result = "".join(mod_list)

print()
print(f"Vámi zadané číslo {num_copy} z desítkové "
      f"soustavy se v {dest_base} soustavě zapisuje jako {result}.")
