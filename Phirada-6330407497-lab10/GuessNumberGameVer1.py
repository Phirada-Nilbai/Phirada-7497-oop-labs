from random import randint


class GuessNumberGameVer1:
    # class attribute
    _numOfGames = 0

    def __init__(self, minNum=1, maxNum=10, maxTries=3):
        self._minNum = minNum
        self._maxNum = maxNum
        self._maxTries = maxTries
        GuessNumberGameVer1.updateNumOfGames()

    @classmethod
    def updateNumOfGames(cls):
        cls._numOfGames = cls._numOfGames + 1

    @classmethod
    def getNumOfGames(cls):
        return cls._numOfGames

    def __str__(self):
        return f"Guess number game:({self._minNum}, {self._maxNum}, {self._maxTries})"


    def playGame(self):
        answer = randint(self._minNum, self._maxNum)
        print(f"GuessNumberGame with min number as {self._minNum}, max number as {self._maxNum}, max num of tries as {self._maxTries}")
        guess = input(f"Please enter a guess ({self._minNum}, {self._maxNum}):")
        numTries = self._maxTries
        while numTries > 0:
          numTries = numTries - 1
          if int(guess) == answer:
               print(f"Congratulations! That's correct")
               break
          elif int(guess) < answer :
               print(f"Please type a higher number! The number of remaining tries is {numTries}")
          else:
               print(f"Please type a lower number! The number of remaining tries is {numTries}")
          if numTries == 0 :
               print ("Sorry that you run out ot of the number of tries")
               break
          guess = input(f"Please enter a guess ({self._minNum}, {self._maxNum}):")

if __name__ == "__main__":
    gng1 = GuessNumberGameVer1(5,8,4)
    gng1.playGame()
