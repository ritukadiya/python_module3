#Write a Python program to map two lists into a dictionary
keys = ["name", "age", "city"]
values = ["Ritu", 24, "Ahmedabad"]

if len(keys) != len(values):
        print("Error : Lists must have the same length")
else:
    d = zip(keys,values)
    print("Dictionary :",dict(d))