import heapq

class Elevator:

    def __init__(self):
        self.current_floor=0
        self.direction='IDLE'
    
        self.up_requests=[]
        self.down_requests=[]
    def request(self,floor):
        if self.direction=='IDLE':
            if self.current_floor<floor:
                heapq.heappush(self.up_requests,floor)
            else:
                heapq.heappush(self.down_requests,-floor)
                
        if self.direction=='UP' and floor>self.current_floor:
            heapq.heappush(self.up_requests,floor)
            
        if self.direction=='DOWN' and floor<self.current_floor:
            heapq.heappush(self.down_requests,-floor)
        self.process_requests()


    def process_requests(self):
        while self.up_requests or self.down_requests:
            if self.up_requests:
                self.direction = "UP"
                while self.up_requests:
                    next_floor = heapq.heappop(self.up_requests)
                    self.move_to_floor(next_floor)
            
            if self.down_requests:
                self.direction = "DOWN"
                while self.down_requests:
                    next_floor = -heapq.heappop(self.down_requests)
                    self.move_to_floor(next_floor)

        self.direction = "IDLE"
        print("No more requests. Elevator is idle.")

    def move_to_floor(self,floor):
        print(f"Elevator moving from {self.current_floor} to {floor}")
        self.current_floor = floor

    

elevator = Elevator()
elevator.request(5)
elevator.request(2)
elevator.request(1)
elevator.request(25)
elevator.request(21)
elevator.request(18)





        
        




































