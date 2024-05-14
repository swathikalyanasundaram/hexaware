# task 1: Conditional Statements 

# def book_tickets(available_ticket,no_of_booking_ticket):
#     if available_ticket >= no_of_booking_ticket:
#         remaining_ticket=available_ticket-no_of_booking_ticket
#         print (f"tickets booked successfully,remaining tickets:{remaining_ticket}")
#     else:
#         print("ticket unavailable")

# available_ticket=int(input("enter the available ticket"))
# no_of_booking_ticket=int(input("enter the number of booking ticket"))

# book_tickets(available_ticket,no_of_booking_ticket)

# task 2:Nested Conditional Statements 
# Create a program that simulates a Ticket booking and calculating cost of tickets. Display tickets options 
# such as "Silver", "Gold", "Dimond". Based on ticket category fix the base ticket price and get the user input 
# for ticket type and no of tickets need and calculate the total cost of tickets booked. 

# def ticket_booking(ticket_type,no_of_ticket):
#     if ticket_type=="silver":
#         base_price=50
#     elif ticket_type == "gold":
#         base_price=100
#     elif ticket_type =="diamond":
#         base_price=200
#     else:
#         print("invalid ticket type")
#         return None
#     total_cost=base_price*no_of_ticket
#     return total_cost

# ticket_type=input("enter ticket type silver(50)/gold(100)/diamond(200):")

# no_of_ticket=int(input("enter the number of tickets:"))

# total_cost=ticket_booking(ticket_type,no_of_ticket)

# print(f"total cost:{total_cost}")

# Task 3: Looping 
# From the above task book the tickets for repeatedly until user type "Exit"
    


# def ticket_booking(ticket_type,no_of_ticket):
#     if ticket_type=="silver":
#         base_price=50
#     elif ticket_type == "gold":
#         base_price=100
#     elif ticket_type =="diamond":
#         base_price=200
#     else:
#         print("invalid ticket type")
#         return None
#     total_cost=base_price*no_of_ticket
#     return total_cost

# while True:

#     ticket_type=input("enter ticket type silver(50)/gold(100)/diamond(200)/exit:")

#     if ticket_type=="exit":
#         print("exiting.....")
#         break

#     no_of_ticket=int(input("enter the number of tickets:"))

#     total_cost=ticket_booking(ticket_type,no_of_ticket)

#     print(f"total cost:{total_cost}")   
    

# Task 4: Class & Object 
# Create a Following classes with the following attributes and methods: 
# 1. Event Class: 
# • Attributes: 
# o event_name, 
# o event_date DATE, 
# o event_time TIME, 
# o venue_name, 
# o total_seats, 
# o available_seats, 
# o ticket_price DECIMAL, 
# o event_type ENUM('Movie', 'Sports', 'Concert') 
# • Methods and Constuctors: 
# o Implement default constructors and overload the constructor with Customer 
# attributes, generate getter and setter, (print all information of attribute) methods for 
# the attributes. 
# o calculate_total_revenue(): Calculate and return the total revenue based on the 
# number of tickets sold. 
# o getBookedNoOfTickets(): return the total booked tickets 
# o book_tickets(num_tickets): Book a specified number of tickets for an event. Initially 
# available seats are equal to the total seats when tickets are booked available seats 
# number should be reduced. 
# o cancel_booking(num_tickets): Cancel the booking and update the available seats. 
# o display_event_details(): Display event details, including event name, date time seat 
# availability.


from enum import Enum

class EventType(Enum):
    movie=1
    sports=2
    concert=3

class Event:
    def __init__(self,event_name,event_date,event_time,venue_name,total_seats,available_seats,ticket_price,event_type) -> None:
        self.event_name=event_name
        self.event_date=event_date
        self.event_time=event_time
        self.venue_name=venue_name
        self.total_seats=total_seats
        self.available_seats=available_seats
        self.ticket_price=ticket_price
        self.event_type=event_type

    def get_event_name(self):
        return self.event_name
    def set_event_name(self,event_name):
        return self.event_name == event_name
    def get_event_date(self):
        return self.event_date
    def set_event_date(self,event_date):
        return self.event_date == event_date
    def get_event_time(self):
        return self.event_time
    def set_event_time(self,event_time):
        return self.event_time==event_time
    
