from GuessNumberGameVer2 import GuessNumberGameVer2
class GuessNumberGameVer3(GuessNumberGameVer2):
     def guessAverage(self):
          pass
     def guessMin(self):
          pass
     def guessMax(self):
          pass

     def promptGameMsg(self):
          return input(f"If you want to play again? type 'y' to continue or 'q' to quit.\n" +
                       f"Type 'a' to see all your guesses or 'g' to see a guess on a specific play:\n" +
                       f"Type 'v' to see average or 'm' to see minimum or 'x' to see maximum of your guesses:")

     def playGames(self):
          self.playGame()
          while True:
               answer = self.promptGameMsg()
               if answer == 'v':
                    self.guessAverage()
               elif answer == 'm':
                    self.guessMin()
               elif answer == 'x':
                    self.guessMax()

if __name__ == "__main__":
    gng1 = GuessNumberGameVer3(5,8,4)
    gng1.playGames()
    print("Now let's play only one game")
    gng1.playGame()
