

first_word = input("Enter The First Word: ")
second_word = input("Enter The Second Word: ")

print(f"Before Swap: {first_word}, {second_word}")

first_word, second_word = second_word, first_word
print(f"After Swap: {first_word}, {second_word}")
