def permutations(word):
    if len(word) <= 1:
        return [word]
    else:
        all_permutations = []
        for i in range(len(word)):
            first_char = word[i]
            remaining = word[:i] + word[i + 1:]
            
            remaining_perms = permutations(remaining)
            
            for perm in remaining_perms:
                all_permutations.append(first_char + perm)
        return all_permutations

input_word = input("Enter a word: ")
permutations_list = set(permutations(input_word))

print("All permutations of "+ input_word+" :")
print(permutations_list)
