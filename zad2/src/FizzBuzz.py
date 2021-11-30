class FizzBuzz:
    def game(self, num):
        if (num % 5) == 0:
            if (num % 3) == 0:
                return "FizzBuzz"
            else:
                return "Buzz"
        elif (num % 3) == 0:
            return "Fizz"
        else:
            raise Exception("Error in FizzBuzz")