# list datastucture
# list are mutable(changeable)
# list are ordered
# list have indexes
from datatypes import student

fruits=['apple','banana','mango','pineapple','orange','pear']
print(fruits)
fruits[2]="Watermelon"
print(fruits)
print(f"I love Eating {fruits[2]}")

numbers=[1,2,3,4,5,6,7,8]
numbers.append(9)

print(numbers[4:])

# tuple data structure
# tuple are immutable
# tuple are ordered
# tuple have indexes
cars=('BMW','AUDI','Subaru','Mercedes','Toyota','Nissan')
print(cars[4])

      # set data strctutrese
      # set are non ordered
      # set don't have index

days={'monday','tuesday','wednesday','thursday','friday','saturday',
      'sunday'}
print(days)

# dictionaries datastructures
students={"Name":"John","Age":45 ,"Gender":"M","School":"eMobilis"}
print(students)
print(students["Name"])
print("The age of",students["Name"],"is",students["Age"])