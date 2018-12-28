import os
from game.Game import Game


g = Game()
while True:
    os.system('cls')
    g.print_state()
    g.check_state()
    if not g.game_over:
        help_str = ""
        for element in [g.first_brqg, g.second_brqg][g.current_brqg]:
            help_str += "{} - {}\n".format(element.id, element.name)

        print("В момента сме на бряг номер {}. \n Можем да преместим:\n{}".
              format(g.current_brqg+1, help_str)
              )
        while True:
            user_input = input()
            if user_input in ["0", "1", "2", "3"]:
                break
            else:
                print('Моля проверете въведената стойност')
        g.move(user_input)
    else:
        break
