class Avatar:
    def __init__(self):
        self.name = ""
        self.money = 0
        # avatar health values range between 0 and 100
        self.hunger = 100 # 100 = full, 0 = hungry
        self.blatter = 0
        self.sleep = 100
        self.hygiene = 100
        self.happiness = 100

    def go_to_work(self):
        # update sleep -- decrease sleep by 75
        self.sleep -= 75
        # increase money -- increase 5022
        self.money += 5022
        # update  hunger -- decrease hunger by 90
        self.hunger -= 90
    
    def go_to_party (self):
        # update happiness -- increase 1000
        self.happiness += 1000
        # update sleep -- decrease 50
        self.sleep -= 50
        # update hygiene -- decrease 100
        self.hygiene -= 100




desmen = Avatar()
desmen.go_to_work()
desmen.go_to_vacation()
desmen.go_to_party()
print(desmen.hunger)
print("money", desmen.money)
print("sleep", desmen.sleep)
print("happiness", desmen.happiness)
print("hygiene", desmen.hygiene)






# # print(Calculator().add(3, 2))
# x = Calculator()
# saving = x.add(1000,50)
# exp = x.sub(300, 1)

# print("Savings: " + str(saving))
# print("Expenses: " + str(exp))



