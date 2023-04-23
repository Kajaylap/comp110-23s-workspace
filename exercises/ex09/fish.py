"""File to define Fish class."""


class Fish:
    """Fish class."""
    age: int

    def __init__(self):
        """Fish ages."""
        self.age = 0
        return None
    
    def one_day(self):
        """Age increases per day."""
        self.age += 1
        return None