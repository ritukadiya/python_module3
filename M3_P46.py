'''
Write a Python program to combine values in python list of dictionaries.

Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
300}, {'item': 'item1', 'amount': 750}]
'''

def values(list_of_dicts):
    dict = {}
    for d in list_of_dicts:
        key = d['item']
        if key in dict:
            dict[key] += d['amount']
        else:
            dict[key] = d['amount']
    return dict


data = [{'item': 'item1', 'amount': 400},{'item': 'item2', 'amount': 300},{'item': 'item1', 'amount': 750}]

dict=values(data)
print(dict)