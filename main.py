# Qsetion #1
same_value_and_id_1 = 1
same_value_and_id_2 = 1
same_value_and_id_3 = 1
is_value_eqv = same_value_and_id_1 == same_value_and_id_2 == same_value_and_id_3
is_id_eqv = same_value_and_id_1 is same_value_and_id_2 is same_value_and_id_3

print(id(same_value_and_id_1),id(same_value_and_id_2),id(same_value_and_id_3))
print(is_value_eqv)
print(is_id_eqv)

# Qestion #2
changeble_1 = 255
changeble_2 = 255.0

print(changeble_1 == changeble_2)
print(changeble_1 is changeble_2)

# Qestion #3
same_value_and_id_1 = 1
same_value_and_id_2 = 1
same_value_and_id_3 = 1

changeble_1 = 255
changeble_2 = 255.0

print(int(same_value_and_id_1) is float(same_value_and_id_2) is str(same_value_and_id_3))
print(int(changeble_1) is int(changeble_2))
