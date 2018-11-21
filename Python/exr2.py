print("player 1 plz choose one of ,Rock,Paper,Scissors")
x=input()
print("plyer 2 plz choose one of ,Rock,Paper,Scissors")
y=input()

if x=='Rock' and y=='Scissors':
  print ("Player 1 wins,,Congratulations ")

elif x=='Scissors' and y=='paper':
   print ("Player 1 wins,,Congratulations")

elif x=='Paper' and y=='Rock':
   print ("Player 1 wins,,Congratulations")
elif x==y:
    print("Nothing")
else :
  print("Player 2 wins,, Congratulations")
