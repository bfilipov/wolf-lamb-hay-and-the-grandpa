class Sprite:
    """
    Class representing game objects that will be manipulated in Game class
    Parameters:
        name [string] - name of the sprite that will be displayed in game
        id [int] - id of the sprite that will be used to identify the sprite in game
    """
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return self.name