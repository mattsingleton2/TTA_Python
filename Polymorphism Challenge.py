# Challenge: 
# Create a parent class and 2 children classes that inherit from the parent.
# These child classes should display polymorphism on the parent class method(s).

class Hero: 
    Name = "Unknown"
    Level = None
    Experience = None
    Primary_Weapon = "Unknown"
    Inventory = []
    Alive = True
    
    def stats(self):
        msg = "\nName: {}\nLevel: {}\nExperience: {}\nPrimary Weapon: {}\nInventory: {}\nAlive: {}".format(self.Name,self.Level,self.Experience,self.Primary_Weapon,self.Inventory,self.Alive)
        return msg
    
    def levelUp(self):
        self.level += 1
        return self.level
    
    def heroAttack(self):
        msg = "\n{} swings his {} with an untrained eye...".format(self.Name, self.Primary_Weapon)
        return msg
    
    def getItem(self, item):
        self.Inventory.append(item)
        return self.Inventory
    
    
class Merchant(Hero):
    Name = "Karn"
    Level = 1
    Experience = 0
    Primary_Weapon = "Spear"
    Inventory = ['scales', 'pouch', 'bag', 'spear', 'a small silvery brooch']
    Alive = True
    
    # We'll display polymorphism by saying Merchant classes
    # Always find a little extra gold when picking up items.
    def getItem(self, item):
        self.Inventory.append(item)
        self.Inventory.append('3 gold')
        return self.Inventory
    
class RedMage(Hero):
    Name = "Koyo"
    Level = 18
    Experience = 19092
    Primary_Weapon = "Rapier and Focus"
    Inventory = ['Rapier', 'Focus', 'Red Mage Garb', 'Pointy Hat', '388 gold', 'a monster trophy head']
    Alive = True
    
    # Here, we'll change the message return for the Hero Attack method
    # Since this hero is a little more experienced.
    def heroAttack(self):
        msg = "\n{} swings his {} with an expert precision, channeling arcane might into the thrust.".format(self.Name, self.Primary_Weapon)
        return msg
        


if __name__ == "__main__":
    Karn = Merchant()
    print(Karn.stats())
    Karn.getItem('A new book on Python3!')
    print("{} is carrying:\n{}".format(Karn.Name,Karn.Inventory))