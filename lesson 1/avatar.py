class Avatar:
    def __init__(self):
        self.name = ""
        self.money = 0
        # avatar health values range between 0 and 100
        self.hunger = 100
        self.blatter = 0
        self.sleep = 100
        self.hygiene = 100
        self.happiness = 100

    def go_to_work(self):
        # update sleep -- decrease sleep by 75
        self.sleep -= 75
        # increase money -- increase 5022
        self.money += 5022
        # update hunger -- decrease hunger by 90
        self.hunger -= 90
    def go_to_vacation(self):
        # update happiness to 1000
        self.happiness += 1000
        # decrease sleep by 50
        self.sleep -= 50
        # decrease money by 1000
        self.money -= 1000

desmen = Avatar()
desmen.go_to_work()
desmen.go_to_vacation()
print(desmen.hunger)
print("money",desmen.money)
print("sleep",desmen.sleep)
print("happiness",desmen.happiness)