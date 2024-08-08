class Calc:
    result = 0

    def add(x, y):
        print(f"{x} + {y} = {(x+y)}")
        return x+y

    def sub(x, y):
        print(f"{x} - {y} = {(x-y)}")
        return x-y

    def mul(x, y):
        print(f"{x} * {y} = {(x*y)}")
        return x*y

    def div(x, y):
        print(f"{x} / {y} = {(x/y)}")
        return x/y

    def operator():
        return input("""
                     Choose from the list: \n
                     + : Addition
                     - : Subtraction
                     * : Multiplication
                     / : Division
                     """)

    def selection(self, op, x, y):
        match(op):
            case "+":
                self.result = self.add(x, y)
            case "-":
                self.result = self.sub(x, y)
            case "*":
                self.result = self.mul(x, y)
            case "/":
                self.result = self.div(x, y)
            case _:
                print("exit")

    @classmethod
    def calc(cls):
        print("""Calculator:""")
        x = float(input("What's the first number? "))
        op = cls.operator()
        y = float(input("What's the second number? "))
        cls.selection(cls, op, x, y)

    @ classmethod
    def init(cls):
        cls.calc()
        print("calculated result is: {}".format(cls.result))
        current_s = True
        while current_s:
            print("Type 'y' to continue calculating with {}, or type 'n' to start a new calculation and 'e' for exit: ".format(
                cls.result))
            more = input()
            if more == 'n':
                cls.calc()
            elif more == 'y':
                op = cls.operator()
                y = float(input("What's the second number? "))
                cls.selection(cls, op, cls.result, y)
            else:
                current_s = False
                print("Thank you")


if __name__ == "__main__":
    Calc.init()
