from math import sqrt
import csv

dataset = []


def distance(a, b):
    sum = 0

    print("Looking at {} and {}".format(a[1], b[1]))

    ava = a[7]/a[2]
    avb = b[7]/b[2]

    sum += (ava - avb)**2
    sum += (a[3] - b[3])**2
    sum += 10*(a[4]-b[4])**2
    sum += (a[5] - b[5])**2
    sum += (a[6] - b[6])**2

    return sqrt(sum)


def task1(compare):
    minimum = ['', 1000]
    for player in dataset[:15]:
        print(player)
        retr = distance(player, dataset[compare])
        if retr < minimum[1]:
            minimum[1] = retr
            minimum[0] = player[1]
            print("#"*30)
            print("New minimum: " + str(minimum))
            print("#"*30)
        print(retr)
        
    return minimum

        


def load_indian():
    global dataset
    dataset = []

    with open('data.csv') as csv_file:
        csvreader = csv.reader(csv_file, delimiter=',')
        line = 0

        for row in csvreader:
            row[0] = line-1
            if line == 0:
                line += 1
            else:
                nrow = [row[0], row[1]]
                for element in row[2:]:
                    if element != '-':
                        nrow.append(float(element))
                    else:
                        nrow.append(170.0)
                dataset.append(nrow)
                line += 1


load_indian()
print(dataset)

print("MIN: "*10 + str(task1(15)))
print("MIN: "*10 + str(task1(16)))
print("MIN: "*10 + str(task1(17)))

