print("------------------------------------------------------------------")
print("                            Multiplication Table")
print("———————————————————————————————————————————————————————————————————")

# Display the number title

for i in range(1, 13):
    print(format(i, "4d"), end=" ")
print(" ")
print("——————————————————————————————————————————————————————————————")

for j in range (1, 13):
    for k in range(1,14):
        print(format(j * k, "4d"), end =" ")
    print("  ")
