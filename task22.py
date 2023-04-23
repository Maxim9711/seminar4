# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input())
list_1=[]
for i in range(n):
    num = int(input())
    list_1.append(num)
print(list_1)

m = int(input())
list_2 = []
for i in range(m):
    num = int(input())
    list_2.append(num)
print(list_2)

generalNum = list_1 + list_2
generalNum.sort()
print(generalNum)

print("Общие числа: ")

buff = []
for i in generalNum:
    if generalNum.count(i) > 1 and i not in buff:
        print(i)
        buff.append(i)