from ParkingLotService import ParkingLotService

if __name__=='__main__':

    create=input()
    parking_lot_service=ParkingLotService(int(create.split(" ")[2]),int(create.split(" ")[3]),create.split(" ")[1])
    parking_lot_service.create_parking_lot()
    parking_lot_service.display_free_count('CAR')
    parking_lot_service.display_free_count('BIKE')
    parking_lot_service.display_free_count('TRUCK')
    parking_lot_service.display_free_slots('BIKE')
    parking_lot_service.display_free_slots('TRUCK')

    parking_lot_service.display_free_slots('CAR')
    
    parking_lot_service.display_occupied_slots('BIKE')
    parking_lot_service.display_occupied_slots('TRUCK')

    parking_lot_service.display_occupied_slots('CAR')