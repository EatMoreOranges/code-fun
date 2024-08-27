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
        # increase money -- increase 5022
        # update  hunger -- decrease hunger by 90
        pass

        





    def update_hunger(self, value):
        if self.hunger + value > 100:
            self.hunger = 100
        elif self.hunger + value < 0:
            self.hunger = 0

    def update_sleep(self, value):
        if self.sleep + value > 100:
            self.sleep = 100
        elif self.sleep + value < 0:
            self.sleep = 0        

    def update_hygiene(self, value):
        if self.hygiene + value > 100:
            self.hygiene = 100
        elif self.hygiene + value < 0:
            self.hygiene = 0 

    def update_blatter(self, value):
        if self.blatter + value > 100:
            self.blatter = 100
        elif self.blatter + value < 0:
            self.blatter = 0 

    def update_hygiene(self, value):
        self.hygiene = 0 if self.hygiene + value < 0 else self.hygiene + value
        self.hygiene = 100 if self.hygiene + value > 100 else self.hygiene + value

    def update_happiness(self, value):
        if self.happiness + value > 100:
            self.happiness = 100
        elif self.happiness + value < 0:
            self.happiness = 0

    def eat(self, food_item):
        if food_item == "apple":
            update_hunger(10)
        elif food_item == "burger":
            update_hunger(20)
        elif food_item == "pizza":
            update_hunger(30)
        elif food_item == "cake":
            update_hunger(40)
        elif food_item == "salad":
            update_hunger(50)
        else:
            update_hunger(25)



Avatar()