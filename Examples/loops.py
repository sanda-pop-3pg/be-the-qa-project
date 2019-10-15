# def loops():
#     numbers = [2,3,5,7]
#     for number in numbers:
#         print(number)

# def loops():
#     for x in range(5):
#         print(x)

# def loops():
#     count = 0
#     while count < 5:
#         print(count)
#         count = count + 1

# loops()

# output = ""
# for i in ["a", "b", "c", "d", "e"]:
#     if i == "d":
#         continue
#     output = output + " " + i

output = ""
for i in ["a", "b", "c", "d", "e"]:
    if i == "c":
        break
    output = output + " " + i

print(output)
