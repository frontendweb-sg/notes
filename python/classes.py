class University:
    university_name = "Delhi university"

    def __str__(self) -> str:
        return f"University(university_name:{self.university_name})"
    

class College(University):
    princial_name="PK"
    """College class"""
    def __init__(self,name,year) -> object:
        super().__init__();
        self.__name:str=name;
        self.year:int=year;

    def display_name(self):
        return self.__name;

    def __str__(self) -> str:
        return f"{self.__dict__}"


c = College('Rajdhani',1992)
print(c.university_name)
print(c)
print(vars(c))
print(College.__dict__)
print(c.__dict__)