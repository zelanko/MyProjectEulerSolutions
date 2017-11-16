import csv

letters = dict()

for i,l in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", start=1):
    letters[l] = i

with open("p022_names.txt") as file:
    for list in csv.reader(file):
        name_list = sorted(list)

sum_of_name_scores = sum(
    [place * sum([letters[letter] for letter in name])
        for place, name in enumerate(name_list, start=1)]
)

print(sum_of_name_scores)
    
