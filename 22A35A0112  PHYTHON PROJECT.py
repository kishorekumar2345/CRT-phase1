class car:
    def _init_(self):
        self.cgst=5555
        self.sgst=6478
        self.insurance=7567
    def company(self):
        while True:
            print("toyota,mercedes,mahendra")
            self.n=input("enter the car company")
            if self.n=="toyota":
                print("welcome to toyota")
                self.model()
                break
            elif self.n=="mercedes":
                print("welcome to mercedes")
                self.model()
                break
            elif self.n=="mahendra":
                print("welcome to mahendra")
                self.model()
                break
            else:
                print("enter valid company")
    def model(self):
        if self.n=="toyota":
            while True:
                print("select from fortuner and lc")
                self.choice=input("enter the car model")
                if self.choice=="fortuner":
                    self.price(self.choice)
                    break
                elif self.choice=="lc":
                    self.price(self.choice)
                    break
                else:
                    print("enter valid company")
    def model(self):
        if self.n=="mercedes":
            while True:
                print("select from glb and amg")
                self.choice=input("enter the car model")
                if self.choice=="glb":
                    self.price(self.choice)
                    break
                elif self.choice=="amg":
                    self.price(self.choice)
                    break
                else:
                    print("enter valid company")
    def model(self):
        if self.n=="mahendra":
            while True:
                print("select from thar and scorpio")
                self.choice=input("enter the car model")
                if self.choice=="thar":
                    self.price(self.choice)
                    break
                elif self.choice=="scorpio":
                    self.price(self.choice)
                    break
                else:
                    print("enter valid company")
    def price(self,choice):
        if choice=="fortuner":
            self.p = 4500000
        elif choice=="lc":
            self.p = 1000000
        elif choice=="glb":
            self.p = 6380000
        elif choice=="amg":
            self.p = 5800000
        elif choice=="thar":
            self.p = 1700000
        elif choice=="scorpio":
            self.p = 1800000
        tot_p = self.p + self.sgst + self.cgst +self.insurance
        print(tot_p)
        
c=car()
c.company()