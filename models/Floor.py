from grpc import Status


class Floor:

    def __init__(self,no_of_slots):
        self.truck=False
        self.bike1=False
        self.bike2=False
        self.no_of_cars_occupied=0
        self.cars=[0 for x in range(no_of_slots-3)]
    
    def get_truck_status(self):
        return self.truck

    def get_bike1_status(self):
        return self.bike1
    
    def get_bike2_status(self):
        return self.bike2

    def set_truck_status(self,status):
        self.truck=status

    def set_bike1_status(self,status):
        self.bike1=status
    

    def get_car_slots(self):
        return self.cars
    
    def get_no_of_cars_occupied(self):
        return self.no_of_cars_occupied
    




