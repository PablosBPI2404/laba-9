name = input()
age = int(input())
def describe_person(name, age = 30):
    return f'My name is {name} i am {age}'
print(describe_person(name, age))
