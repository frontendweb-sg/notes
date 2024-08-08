
class PizzaOrderSystem:
    tax = 18/100

    def size():
        size = input("Please select size, S, M or L : ")
        return size

    def menu():
        print("""Welcome to dominos:
              Would you like to order a pizza?
              Please select from the menu
              0: Peproni
              1: Peproni with cheeze loaded
              2. Paneer pizza loaded
              3. Paneer pizza veg loaded with cheez burst
              4. Chicken pizza""")
        return input()

    def peproni(size):
        if size == 's':
            return 100
        elif size == 'm':
            return 150
        else:
            return 200

    def peproniCheeze(size):
        if size == 's':
            return 150
        elif size == 'm':
            return 200
        else:
            return 250

    def paneerLoaded(size):
        p = 0
        if size == 's':
            p = 170
        elif size == 'm':
            p = 230
        else:
            p = 290
        print('p-{}'.format(p))
        return p

    def paneerVegLoaded(size):
        if size == 's':
            return 230
        elif size == 'm':
            return 280
        else:
            return 340

    def chicken(size):
        if size == 's':
            return 230
        elif size == 'm':
            return 340
        else:
            return 550

    @classmethod
    def init(cls):
        menu = int(cls.menu())
        size = cls.size().lower()
        size_price = 0
        match(menu):
            case 0:
                size_price = cls.peproni(size)
            case 1:
                size_price = cls.peproniCheeze(size)
            case 2:
                size_price = cls.paneerLoaded(size)
            case 3:
                size_price = cls.paneerVegLoaded(size)
            case 4:
                size_price = cls.chicken(size)
            case _:
                print("Thank you for visiting dominoz!")
                # exit()
        totalPrice = size_price + (size_price*cls.tax)
        print("Please pay Rs. {}".format(totalPrice))


PizzaOrderSystem.init()
