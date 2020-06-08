# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
play_more = "YES"
while play_more == "YES":
    gameset = [["Rock", "Scissors"], ["Scissors", "Paper"], ["Paper", "Rock"]]
    player1 = input("P1 input (Rock-Paper-Scissors):")
    player2 = input("P2 input (Rock-Paper-Scissors):")
    if player1 == player2:
        print("Draw!")
    else:
        for game in gameset:
            if player1 == game[0] and player2 == game[1]:
                print("Player 1 wins")
            elif player1 == game[1] and player2 == game[0]:
                print("Player 2 wins")
    play_more = input("Play more? (YES\\NO): ")
