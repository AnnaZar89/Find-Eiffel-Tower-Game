print('''
+--------------------------------------------------------------------------------------------------------------+
          !                                                                                                              !
          !                                                                                                              !
          !                                                                                 X                            !
          !                                                                            LE SACRE-COEUR                    !
          !                                                                                                              !
          !                                                                                                              !
          !                                                                                                              !
          !                                                                                                              !
          !           X   L'ARC DE TRIOMPHE                                                                              !
          !                                                                                                              !
          !                                                                                                              !
          !                                                                X                                             !
          !                                                                  L'OPERA                                     !
          !                                                                                                              !
          !                                                                                                              !                                                                                                                                                                                                            
          !                    .- - - - - - - - - - - - -.                                                               !
          !                .--'      LA SEINE             `--..                                                          !
          !             .-'    .- - - - - - - - - - - - -.     `-.                                                       !
          !           .'   ..-'                           `-.     `--..                                                  !
          !         .'   .'                                  `..       `..                                               !
          !        .   .'                                       `--.      `--.                                           !
          !       .   .                                             `-.       `-.                                        !
          !      .   .                                                 `--.      `-.                                     !
          !     .   .                                                      `-.      `---.                                !
          !    .   .                                                          `--.       `--.                            !
          !   .   .                                                               `-.        `-.                         !
          !  .   .                                                                   `.         `.                       !
          !     .    X                                                                 .          `.                     !
          !    .                                                                        `. ..       -                    !
          !      LA TOUR EIFFEL                                                           : :`-.     `.                  !
          !                                                                                : :  `-.    `.                !
          !                                                                                .  `.   `--.  `.              !
          !                                                                                 :   \      `.  `.            !
          !                                                                                  `.  `.     `.   `           !
          !                                                                                    `-.`.   X :   NOTRE-DAME  !
          !                                                                                       -.`-...:.              !
          !                                                                                         `-..                 !
          !                                                                                             `--              !
          !                                                                                                              !                                                                                                             
          +--------------------------------------------------------------------------------------------------------------+
''')
print("Welcome to Paris.\nYour mission is to find the Eiffel Tower.\nYou're at a cross road. ")
query_1 = input('Where would you like to go? Type "left" or "right."\n').lower()
if query_1 == "left":
    query_2 = input("metro or RER B? \n").lower()
    if query_2 == "rer b":
        query_3 = input("swim or wait? \n").lower()
        if query_3 == "wait":
            print("You got on a bateau-mouche that took you near the Eiffel Tower. "
                  "Congratulations, you win!")
        elif query_3 == "swim":
            print("E. coli bacteria has invaded your body. Game over!")
        else:
            print("You chose different option than proposed. Game over!")
    elif query_2 == "metro":
        print("Unfortunately, the metro doors slammed shut on your jacket. "
              "The metro started moving with you. You died instantly. You were buried at Père Lachaise Cemetery."
              "Game over!")
        print('''
                 __)(__
           _____/      \\_____
          |                  ||
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
        ''')

    else:
        print("You chose different transport than proposed. Game over!")

elif query_1 == "right":
    print("You got lost in the Paris catacombs. Game over!")
else:
    print("You chose different direction than proposed. Game over!")