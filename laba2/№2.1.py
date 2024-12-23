def greet(name):
    return('Приветствую, ' + name)
print(greet('Максимов Павел'))




def square(number):
    return number * number
print(square(5))




x = int(input('Введите число '))
y = int(input('Введите число '))
def max_of_two(x, y):
    if x > y:
        return x
    elif x == y:
        return('Нету среди них максимального')
    return y
print('Максимальное число:', max_of_two(x, y))



