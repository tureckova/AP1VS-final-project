"""Basic converter from decimal numeral system."""
# Converter for numeral systems starting from unary numeral system
# and ending at the hexatridecimal numeral system.
#
# Other numeral systems are basically useless because there is no
# usage for them and there is not enough letters in
# the latin alphabet for them to use.

# Create a dictionary of the latin alphabet for numeral systems
# that have the base bigger than 10 -> 10: 'A', 11: 'B' .....,  35: 'Z'
keys = range(10, 36)
values = [chr(i) for i in range(65, 91)]
letters_dict = dict(zip(keys, values))

# Ask the user to which numeral system they want the number to be converted.
dest_base = int(input("Zadej číslem číselnou soustavu, "
                      "do které chceš číslo převést: "))

# This Converter can only covert numbers if the destination base is higher
# than 0 or lower than 37.
if 0 < dest_base < 37:
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

    if dest_base > 10:
        for i in range(len(mod_list)):
            if mod_list[i] > 9:
                mod_list[i] = letters_dict[mod_list[i]]

    mod_list.reverse()
    mod_list = [str(i) for i in mod_list]
    result = "".join(mod_list)

    print()
    print(f"Vámi zadané číslo {num_copy} z desítkové "
          f"soustavy se v {dest_base} soustavě zapisuje jako {result}.")
else:
    print()
    print("Převodce soustav nedokáže číslo převést mezi "
          "Vámi zadanými soustavami, prosím zkuste to "
          "znovu s jinými soustavami.")
