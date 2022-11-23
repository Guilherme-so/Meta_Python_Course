my_dictionary = {1: "coofe", 2: "tea", 3: "milk", "for": "cake", "five": "pancake"}

my_dictionary[1] = "bread"
my_dictionary[2] = "cracker"
my_dictionary[3] = "cookie"

# print(my_dictionary)

for idx, breakfast in my_dictionary.items():
    print("Today the brakfast is: " + breakfast)
