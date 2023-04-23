"""File to define River class."""

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

__author__ = "730418782"


class River:
    """River class."""
    day: int
    bear: list()
    fish: list()
    
    def __init__(self, num_fish: int, num_bears: int): 
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self): 
        """Determines the age for both fish and bears."""
        update_fish_list: list() = []
        update_bear_list: list[Bear] = []
        for fish in self.fish:
            if fish.age <= int(3):
                update_fish_list.append(fish)
        for bears in self.bears:
            if bears.age <= int(5):
                update_bear_list.append(bears)
        self.fish = update_fish_list
        self.bears = update_bear_list
        return None
    
    def remove_fish(self, amount: int): 
        """Removing fish method."""
        for x in range(amount):
            if self.fish:
                self.fish.pop(0)
        return None

    def bears_eating(self): 
        """Simulates each bear eating fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
                bear.hunger_score += 3
        return None
    
    def check_hunger(self): 
        """Checks hunger score of each bear to determine survival."""
        new_bears_list: list() = []
        for bear in self.bears:
            if bear.hunger_score < 0:
                new_bears_list.append(bear)
        self.bears = new_bears_list
        return None
        
    def repopulate_fish(self): 
        """Adding fish offsprings."""
        fish_offspring = (len(self.fish) // 2) * 4
        for x in range(fish_offspring):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self): 
        """Adding bear offspring."""
        bear_offspring = len(self.bears) // 2 
        for x in range(bear_offspring):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Prints river population."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Simulates a week."""
        for x in range(7):
            self.one_river_day()
        return None
            
