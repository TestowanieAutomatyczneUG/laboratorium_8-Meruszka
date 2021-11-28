class Pangram:
    def check(self, slowo):
        if isinstance(slowo, str):
            for i in 'abcdefghijklmnopqrstuvwxyz':
                if i not in slowo.lower():
                    return 'False'
            return 'True'
        else:
            raise Exception("Slowo musi byc stringiem")
