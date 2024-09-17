f = open("csv/employees.csv", "r")

for l in f.readline():
    print(l)
# line = f.readline()
f.close()
