
from sympy import re


class ParkingLot:
    def __init__(self,n:int,no_of_slot_floors,id):
        self.no_of_floors=n
        self.floors=[]
        self.no_of_slot_floors=no_of_slot_floors
        self.id=id


    def get_no_of_floors(self):
        return self.no_of_floors
    
    def set_no_of_floors(self,n):
        self.no_of_floors=n

    def set_floors(self,floors):
        self.floors=floors
    
    def get_floors(self):
        return self.floors

    def add_floor(self,floor):
        self.floors.append(floor)


    def get_n_slots_on_floors(self):
        return self.no_of_slot_floors