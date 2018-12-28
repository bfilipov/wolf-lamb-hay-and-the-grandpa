from sprite.Sprite import Sprite

class Game:
    def __init__(self):

        self.first_brqg = []
        self.second_brqg = []
        self.sprites = []
        self.current_brqg = 0
        self.turns = 0
        self.game_over = False
        self.win = False

        for index, name in enumerate(["Дядо", "Вълк", "Агне", "Сено"]):
            sprite = Sprite(name, index)
            self.sprites.append(sprite)
            self.first_brqg.append(sprite)

    def move(self, value):
        value = int(value)
        if self.current_brqg == 0:
            coasts = [self.first_brqg,self.second_brqg]
        else:
            coasts = [self.second_brqg,self.first_brqg]
        try:
            if value != 0:
                coasts[0].remove(self.sprites[value])
                coasts[1].append(self.sprites[value])
            coasts[0].remove(self.sprites[0])
            coasts[1].append(self.sprites[0])
            self.current_brqg = 0 if self.current_brqg == 1 else 1
            self.turns += 1
        except ValueError:
            print("Обекта с номер{} не е на този бряг".format(value))

    def print_state(self):
        print(
            "|",
            *self.first_brqg,
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
            *self.second_brqg,
            "|",
            "\n_________________________________________________________"
        )

    def check_state(self):
        loose_type = 0
        for brqg in [self.first_brqg,self.second_brqg]:
            if all(sprite in brqg for sprite in [self.sprites[1], self.sprites[2]]) and not self.sprites[0] in brqg:
                loose_type = 1
            elif all(sprite in brqg for sprite in [self.sprites[3], self.sprites[2]]) and not self.sprites[0] in brqg:
                loose_type = 2

        if loose_type:
            loose_texts = {
                1: "За съжаление вълка изяде агнето.",
                2: "за съжаление агнето изяде сеното"
            }
            print(loose_texts[loose_type],"\nGame over")
            self.game_over = True

        if not self.first_brqg:
            self.win = True
            print("Поздравления! Вие решихте задачата с {} хода.".format(self.turns))
            self.game_over = True