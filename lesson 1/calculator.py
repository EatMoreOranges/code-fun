class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, num1):
        self.value = num1 

    def sub(self, num1):
        self.value = self.value - num1 

    # def div(self, num1, num2):
    #     ans = num1 / num2


# print(Calculator().add(3, 2))
x = Calculator()
saving = x.add(1000,50)
exp = x.sub(300, 1)

print("Savings: " + str(saving))
print("Expenses: " + str(exp))