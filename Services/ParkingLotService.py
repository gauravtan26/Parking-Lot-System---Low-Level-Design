from Floor import Floor
from parking_lot import ParkingLot
from Floor import Floor

class ParkingLotService:

    def __init__(self,n_of_floors,no_of_slots,id):
        self.parking_lot=ParkingLot(n_of_floors,no_of_slots,id)

    
    def add_floors(self):
        for i in range(self.parking_lot.no_of_floors):
            self.parking_lot.add_floor(Floor(self.parking_lot.no_of_slot_floors))
    
    def create_parking_lot(self):
        self.add_floors()
        print("Created parking lot with {} floors and {} slots per floor".format(self.parking_lot.get_no_of_floors(),self.parking_lot.get_n_slots_on_floors()))

    def get_empty_bike_slots(self,floor:Floor):
        if floor.bike1 is False and floor.bike2 is False:
            return 2
        elif floor.bike1 and floor.bike2:
            return 0
        else:
            return 1
    
    def get_empty_truck_slots(self,floor:Floor):
        if floor.truck:
            return 0
        else:
            return 1
        
    def get_empty_car_slots(self,floor:Floor):
        return self.parking_lot.get_n_slots_on_floors()-3-floor.get_no_of_cars_occupied()

    def display_free_count(self,vehicle_type):
        empty=0
        for i in range(self.parking_lot.get_no_of_floors()): 
            if vehicle_type=='BIKE':
                empty=self.get_empty_bike_slots(self.parking_lot.get_floors()[i])
            elif vehicle_type=='TRUCK':
                empty=self.get_empty_truck_slots(self.parking_lot.get_floors()[i])
            else:
                empty=self.get_empty_car_slots(self.parking_lot.get_floors()[i])
            print("No. of free slots for {} on Floor {}: {}".format(vehicle_type,i+1,empty))

    def get_free_bike_slots_bike(self,floor:Floor):
        free_slots=[]
        if floor.get_bike1_status() is False:
            free_slots.append(2)
        if floor.get_bike2_status() is False:
            free_slots.append(3)
        return free_slots
    
    def get_free_truck_slots(self,floor:Floor):
        if floor.get_truck_status():
            return [0]
        else:
            return [1]
    
    def get_free_slots_car(self,floor:Floor):
        empty=[]

        for i in range(len(floor.cars)):
            if floor.cars[i]==0:
                empty.append(i+4)
        return empty
    def display_free_slots(self,vehicle_type):
        for i in range(self.parking_lot.get_no_of_floors()): 
            if vehicle_type=='BIKE':
                empty=self.get_free_bike_slots_bike(self.parking_lot.get_floors()[i])
                
                print("Free slots for {} on Floor {}: {}".format(vehicle_type,i+1,str(empty)[1:-1]))
            elif vehicle_type=='TRUCK':
                empty=self.get_free_truck_slots(self.parking_lot.get_floors()[i])
                print("Free slots for {} on Floor {}: {}".format(vehicle_type,i+1,str(empty)[1:-1]))
            else:
                empty=self.get_free_slots_car(self.parking_lot.get_floors()[i])
                print("Free slots for {} on Floor {}: {}".format(vehicle_type,i+1,str(empty)[1:-1]))
            # print("No. of free slots for {} on Floor {}: {}".format(vehicle_type,i+1,empty))


    def get_occupied_slots_bike(self,floor:Floor):
        occupied=[]

        if floor.get_bike1_status():
            occupied.append(2)
        if floor.get_bike2_status():
            occupied.append(3)
        return occupied
    def get_occupied_slots_truck(self,floor:Floor):
        occupied=[]
        if floor.get_truck_status():
            return [1]
        else:
            return [0]

    def get_occupied_slots_car(self,floor:Floor):
        occupied=[]

        for i in range(len(floor.cars)):
            if floor.cars[i]==1:
                occupied.append(i+4)
        return occupied
    def display_occupied_slots(self,vehicle_type):
        for i in range(self.parking_lot.get_no_of_floors()): 
            if vehicle_type=='BIKE':
                empty=self.get_occupied_slots_bike(self.parking_lot.get_floors()[i])
            elif vehicle_type=='TRUCK':
                empty=self.get_occupied_slots_truck(self.parking_lot.get_floors()[i])
            else:
                empty=self.get_occupied_slots_bike(self.parking_lot.get_floors()[i])
            # print(empty)
            print("Occupied slots for {} on Floor {}: {}".format(vehicle_type,i+1,str(empty)[1:-1]))