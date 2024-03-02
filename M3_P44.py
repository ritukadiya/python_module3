'''
Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}
'''
def generate_combinations(data, prefix='', level=0):
    if level == len(data):
        print(prefix)
        return

    current_key = list(data.keys())[level]
    for letter in data[current_key]:
        generate_combinations(data, prefix + letter, level + 1)

data = {'1': ['a', 'b'], '2': ['c', 'd']}

generate_combinations(data)