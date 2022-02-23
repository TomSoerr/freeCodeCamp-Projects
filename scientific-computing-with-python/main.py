from arithmetic_arranger import arithmetic_arranger
from time_calculator import add_time
import budget
from budget import create_spend_chart
import shape_calculator
import prob_calculator

print('\ntesting arithmetic arranger...\n')
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

print('\ntesting add time...\n')
print(add_time("11:06 PM", "2:02"))

print('\ntesting budget app...\n')
food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

print('\ntesting shape calculator...\n')
rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)

print('\ntesting prob calculator...\n')
prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)