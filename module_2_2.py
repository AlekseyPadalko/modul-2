first = int(input("Введите число: "))
second = int(input("Введите еще число: "))
third = int(input("Введите третье число: "))

if first == second and second == third:
    print(3)
elif first == second or first == third:
    print(2)
else:
    print(0)






