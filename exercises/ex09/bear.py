"""File to define Bear class."""


class Bear:
    """Bear class."""
    age: int
    hunger_score: int
    
    def __init__(self):
        """Age and hunger."""
        self.age = 0
        self.hunger_score = 0
        """Initial hunger amount."""
        return None
    
    def one_day(self):
        """Increase day by one."""
        self.age += 1
        self.hunger_score -= 1 
        """Decrease hunger number."""
        return None
    
    def eat(self, num_fish: int):
        """Changes hunger score for bears."""
        self.hunger_score += num_fish
        return None
    
