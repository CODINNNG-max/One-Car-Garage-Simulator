class Car:
    def __init__(self,make,model,year):
        self.make= make
        self.model=model
        self.year=year
        self.turned_on=False
        
    def display_info(self):
        print(f"You currently own a {self.year} {self.make} {self.model}")
        
    def turn_on(self):
        if not self.turned_on:
            print('__TURNING ON......__')
            print(f'Your {self.make} {self.model} is now ready to run')
            self.turned_on= True
        else:
            print(f'Your {self.make} {self.model} is already up and running')
            
    def turn_off(self):
        if self.turned_on:
            print('__TURNING OFF....__')
            print(f'Your {self.make} {self.model} is now turned off')
            self.turned_on=False
        else:
            print(f'Your {self.make} {self.model} is already turned off')

    def status(self):
        if self.turned_on:
            print('CHECKNG CAR STATUS.....')
            print('Your car is running and ready to go !')
        else:
            print('Your car is currently off')
            
class Electric(Car):
    def __init__(self,make,model,year,battery):
        super().__init__(make,model,year)
        self.battery=battery
    
    def charge(self):
        print(f'Charging the {self.battery} battery')
        
    def display_info(self):
        print(f"You currently own a {self.year} {self.make} {self.model} with a {self.battery}KWh battery")

class Garage:
    def __init__(self):
        self.car=[]
        
    def add_car(self,mycar):
        print(f'__ADDING the {mycar.year} {mycar.make} {mycar.model} to garage__')
        self.car.append(mycar)
        print(f'Your {mycar.year} {mycar.make} {mycar.model} is now in your garage')
        
    def show_garage(self):
        print('__DISPLAYING GARAGE___')
        for i, item in enumerate(self.car,1):
            print(f'{i}.',end='')
            item.display_info()
            
def choice():
    while True:
        ch=input("Would you like to make : \n1. A Gas powered car \n2. An Electric car\n3. Exit\n")
        if ch =="1":
            while True:
                inv=['lamborghini','ferrari','mercedes','audi','bugatti','alfa romeo','aston martin','mclaren','bentley','fiat','gmc','hyundai','koenigsegg','skoda','porsche','renault','volkswagen','toyota','nissan']
                umake=input("Enter a car brand :").strip().lower()
                if umake in inv:
                    break
                else:
                    print('We currently do not have this brand...')
            umodel=input("Enter a  model :").strip()
            while True:
                try:
                    uyear=int(input("Enter a year model was made : "))
                    if uyear <1900 or uyear>2027:
                        print('Enter a valid year')
                        continue
                    break
                except ValueError:
                    print('Enter a four digit year e.g. 2013')
                    continue
            return Car(umake,umodel,uyear)

        elif ch =="2":
            while True:
                inv2=['tesla','byd','hyundai','porsche','polestar']
                umake=input("Enter a car brand :").strip().lower()
                if umake in inv2:
                    break
                else:
                    print('We currently do not have this brand...')
            umodel=input("Enter a  model :")
            while True:
                try:
                    uyear=int(input("Enter a year model was made : "))
                    if uyear <1900 or uyear>2027:
                        print('Enter a valid year')
                    else:
                        break
                except ValueError:
                    print('Enter valid input e.g. 2013')
            while True:
                try:
                    ubattery=int(input('Enter battery size in Kw : '))
                    if ubattery <10 or ubattery>250:
                        print('Enter a valid battery size')
                    else:
                        break
                except ValueError:
                    print('Enter valid input')
            return Electric(umake,umodel,uyear,ubattery)
        elif ch=="3":
            print('Exited successfully')
            exit()
        else:
            print('Please enter 1, 2, or 3')
            continue

    
def interact():
    global mycar
    while True:
        try:
            rt=int(input("Would you like to : \n1.Turn on your car \n2.Turn off your car \n3.Display car info \n4.Display car staus\n5.Create another car \n6.View Garage \n7.Charge Electric car\n8.Exit\n"))
            if rt ==1:
                mycar.turn_on()
            elif rt ==2:
                mycar.turn_off()
            elif rt==3:
                mycar.display_info()
            elif rt==4:
                mycar.status()
            elif rt==5:
                newcar=choice()
                mycar=newcar
                mygarage.car=[newcar]
            elif rt==6:
                mygarage.show_garage()
            elif rt ==7:
               if isinstance(mycar,Electric):
                   mycar.charge()
               else:
                   print(f'Your {mycar.year} {mycar.make} {mycar.model} is not electric')
            elif rt==8:
                return print('Exited successfully')
        except ValueError:
            print('Please enter a number from the ones listed above')
        

mygarage=Garage()
mycar=choice()
mygarage.add_car(mycar)
interact()

