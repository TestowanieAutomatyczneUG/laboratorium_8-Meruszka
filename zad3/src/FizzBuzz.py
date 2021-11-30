class FizzBuzz:
    def game(self, num):
        if isinstance(num, int):
            if (num % 5) == 0:
                if (num % 3) == 0:
                    return "FizzBuzz"
                else:
                    return "Buzz"
            elif (num % 3) == 0:
                return "Fizz"
            else:
                raise TypeError("Liczba nie dzieli sie")
        else:
            raise ValueError("Musi być intem")