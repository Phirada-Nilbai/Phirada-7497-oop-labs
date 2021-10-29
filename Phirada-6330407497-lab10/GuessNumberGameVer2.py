from GuessNumberGameVer1 import GuessNumberGameVer1
class GuessNumberGameVer2(GuessNumberGameVer1):
     def __init__(self, *args,**kwargs):
          super(GuessNumberGameVer2,self).__init__(*args,**kwargs)
          self._guesses = []
          self._numGuesses = 0

     def showSpecific(self):
         # self._guesses.append()
         pass

     def showGuesses(self):
          pass

     def promptGameMsg(self):
          return input(f"If you want to play again? type 'y' to continue or 'q' to quit.\n" +
                       f"Type 'a' to see all your guesses or 'g' to see a guess on a specific play:")


     def playGames(self):
          self.playGame()
          while True:
               answer = self.promptGameMsg()
               if answer == 'q':
                    break
               elif answer == 'y':
                    continue
               elif answer == 'a':
                    self.showGuesses()
               elif answer == 'g':
                    self.showSpecific()


if __name__ == "__main__":
    gng1 = GuessNumberGameVer2(5,8,4)
    gng1.playGames()
    print("Now let's play only one game")
    gng1.playGame()
