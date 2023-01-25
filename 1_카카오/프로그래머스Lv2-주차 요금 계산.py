import math

def calculate_fee(fees, acc_minutes):
    base_time, base_fee, unit_time, unit_fee = fees
    if base_time >= acc_minutes:
        return base_fee
    return base_fee + math.ceil((acc_minutes - base_time) / unit_time) * unit_fee


def convert_time(time):
    return list(map(int, time.split(":")))


def time_for_minute(hour, minute):
    return hour * 60 + minute


def calculate_minute_interval(in_time, out_time):
    return time_for_minute(*convert_time(out_time)) - time_for_minute(*convert_time(in_time))


class Car:
    def __init__(self, in_time):
        self.__state = "IN"
        self.__last_in_time = in_time
        self.__acc_minutes = 0
        
    def get_state(self):
        return self.__state
    
    def get_acc_minutes(self):
        return self.__acc_minutes
    
    def update(self, state_type, time):
        if state_type == 'IN':
            self.__in__(time)
            return
        if state_type == 'OUT':
            self.__out__(time)
            return
        raise Exception(f"{state_type} is invalid..")
        
    def __in__(self, time):
        self.__state = "IN"
        self.__last_in_time = time
        
    def __out__(self, time):
        self.__state = 'OUT'
        self.__acc_minutes += calculate_minute_interval(self.__last_in_time, time)
        

class Time_Table:
    def __init__(self):
        self.__table = {}
    
    def get_table(self):
        return self.__table
    
    def get_car_ids(self):
        return sorted(self.__table.keys())
    
    def registry(self, registry_type, car_id, time):
        if registry_type == "IN":
            self.__in_car__(car_id, time)
            return
        if registry_type == "OUT":
            self.__out_car__(car_id, time)
            return
        raise Exception(f"{state_type} is invalid..")
        
    def get_rest_car_ids(self):
        return [car_id for car_id in self.__table.keys() if self.__table[car_id].get_state() == "IN"]
    
    def handle_rest(self):
        for car_id in self.get_rest_car_ids():
            self.registry("OUT", car_id, "23:59")
            
    def __in_car__(self, car_id, in_time):
        if car_id not in self.__table:
            self.__table[car_id] = Car(in_time)
            return
        car = self.__table[car_id]
        car.update("IN", in_time)
        
    def __out_car__(self, car_id, out_time):
        if car_id not in self.__table:
            raise Exception(f"{car_id} is not exist..")
        car = self.__table[car_id]
        car.update("OUT", out_time)


def solution(fees, records):
    time_table = Time_Table();
    
    for record in records:
        time, car_id, registry_type = record.split(" ")
        time_table.registry(registry_type, car_id, time)
    
    time_table.handle_rest()
    
    return [calculate_fee(fees, time_table.get_table()[car_id].get_acc_minutes()) for car_id in time_table.get_car_ids()]
"""
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.5MB)
테스트 2 〉	통과 (0.05ms, 10.5MB)
테스트 3 〉	통과 (0.08ms, 10.4MB)
테스트 4 〉	통과 (0.13ms, 10.4MB)
테스트 5 〉	통과 (0.37ms, 10.5MB)
테스트 6 〉	통과 (0.39ms, 10.4MB)
테스트 7 〉	통과 (2.72ms, 10.5MB)
테스트 8 〉	통과 (1.55ms, 10.5MB)
테스트 9 〉	통과 (0.58ms, 10.3MB)
테스트 10 〉	통과 (2.33ms, 10.6MB)
테스트 11 〉	통과 (3.54ms, 10.7MB)
테스트 12 〉	통과 (3.77ms, 10.6MB)
테스트 13 〉	통과 (0.06ms, 10.4MB)
테스트 14 〉	통과 (0.04ms, 10.5MB)
테스트 15 〉	통과 (0.04ms, 10.6MB)
테스트 16 〉	통과 (0.04ms, 10.5MB)
"""