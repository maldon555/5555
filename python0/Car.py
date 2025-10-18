class Car:
    @classmethod
    def a(cls):
        print("hello")
    
    def __init__(self,model,price:float,color,user=None):
        self.model=model
        self.price=price
        self.color=color
        self.user=user if user is not None else "Unknown"
        self.__a=1000 # private attribute
    def get_a(self,*args):
            self.a=args
            #b=""
            #for i in range(len(self.a)):   
                #print(self.a[i])
                #b+=str(self.a[i])
            b = "  ".join(str(x) for x in self.a)
            #print(b)
            return f"the private method is: \n{self.__a}\n{b}"
            
        
    def print(self):
        print(f"Car model: {self.model}\nCar price: {self.price}\nCar color: {self.color}\nuser name: {self.user}\n ","#"*10)


b=Car("Kia","3000","blue")
c=Car("Toyota",5000,"white","Ahmed")
c.print()
b.print()


