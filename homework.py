places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

print(list(filter(lambda name: name != " " and name != "" and name != "  ", places)))

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

author.sort(key=(lambda name: name.lower().split()[-1]))
print(author)

# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

names = []
degree = []

for place in places:
    names.append(place[0])
    degree.append(place[-1])   


finished = list(map((lambda name, degree: (name, degree*(9/5)+32)), names, degree))

print(finished)

def fib(i, current_num = 1, prev_num = 0):
    if i > 0:
        print(f"iteration {i}: {current_num}")
        new_num = current_num + prev_num
        return fib(i-1, new_num, current_num)
    else:
        print(f"iteration {i}: {current_num}")


fib(5)