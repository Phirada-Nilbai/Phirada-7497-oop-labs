#Phirada Nilbai
#633040749-7
#Lab9 P2

from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def load_image(self, filename):
        pass

    @abstractmethod
    def save_image(self, filename):
        pass


class Bitmap(Image):
     def load_image(self,filename):
          self.filename = filename
          print(f"loading bitmap {self.filename}")

     def save_image(self,filename):
          self.filename = filename
          print(f"save bitmap {self.filename}")

class Jpeg(Image):
     def load_image(self,filename):
          self.filename = filename
          print(f"loading jpeg {self.filename}")

     def save_image(self,filename):
          self.filename = filename
          print(f"saving jpeg {self.filename}")

if __name__ == "__main__":
     bitmap1 = Bitmap()
     bitmap1.save_image("kku.bmp")
     bitmap1.load_image("kku.bmp")
     jpeg1 = Jpeg()
     jpeg1.save_image("en.jpg")
     jpeg1.load_image("en.jpg")


