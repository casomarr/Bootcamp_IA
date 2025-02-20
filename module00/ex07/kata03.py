kata = "The right format"

nb_of_lines = 42 - len(kata) - 1
lines = '-' * nb_of_lines
print(f"{lines}{kata}") # and not print(lines, kata) because it will add a space in between