from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L")
print("Select your move (R, P or S)")
print()

player1_score = 0
player2_score = 0

while True:
  player_1 = input("Player 1 > ")
  print()
  player_2 = input("Player 2 > ")
  print()

  if (player_1 == "R"):
    if (player_2 == "R"):
      print("You both picked Rock, draw!")
    elif (player_2 == "S"):
      print("Player 1 smashed Player 2's Scissors into dust with their Rock")
      player1_score += 1
    elif (player_2 == "P"):
      print("Player 1's Rock is smothered by Player 2's Paper!")
      player2_score += 1
  elif (player_1 == "S"):
    if (player_2 == "S"):
      print("You both picked Scissors, draw!")
    elif (player_2 == "R"):
      print("player 2 smashed player 1's scissors into dust with their rock")
      player2_score += 1
    elif (player_2 == "P"):
      print("player 1 cut player 2's paper into pieces")
      player1_score += 1
  elif (player_1 == "P"):
    if (player_2 == "P"):
      print("You both picked Paper, draw!")
  elif (player_2 == "R"):
    print("player 1 smothered player 2's rock")
    player1_score += 1
  elif (player_2 == "S"):
    print("player 1's paper is cut into pieces")
    player2_score += 1

  print("Player 1 has", player1_score, "wins.")
  print("Player 2 has", player2_score, "wins.")

  if player1_score == 3 or player2_score == 3:
    print("Thanks for playing!")
    exit()
  else:
    continue
