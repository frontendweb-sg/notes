str1 = "python"
str2 = "is"
str3 = "AWESOME"

# Write your code below:
str4 = str1.title() + " "+str2.lower()+" "+str3.lower()
print(str4[::2])


def loop(n):
    count = 0
    count = count + 1, print(count) if count != n else n
    return loop(n)


loop(10)
