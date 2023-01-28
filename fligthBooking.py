class Flight:
    def __init__(self, flight_number, departure_city, arrival_city, departure_time, arrival_time, price, seats):
        self.flight_number = flight_number
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        self.seats = seats
        self.booked_seats = []

    def __str__(self):
        return f"Flight Number: {self.flight_number}\nDeparture: {self.departure_city} at {self.departure_time}\nArrival: {self.arrival_city} at {self.arrival_time}\nPrice: {self.price}\nSeats: {self.seats}\nBooked Seats: {', '.join(self.booked_seats)}"

    def book_seat(self, seat_number):
        if seat_number in self.seats and seat_number not in self.booked_seats:
            self.booked_seats.append(seat_number)
            return f"Seat {seat_number} booked successfully."
        return "Seat not available."

    def cancel_booking(self, seat_number):
        if seat_number in self.booked_seats:
            self.booked_seats.remove(seat_number)
            return f"Booking for seat {seat_number} cancelled successfully."
        return "Booking not found."

    def set_price(self, price):
        self.price = price
        return f"Price set to {price}."

class Airline:
    def __init__(self, name, flights):
        self.name = name
        self.flights = flights

    def __str__(self):
        return f"Airline: {self.name}\nFlights: {', '.join([flight.flight_number for flight in self.flights])}"

    def check_flight(self, flight_number):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                return flight
        return "Flight not found."

    def book_seat(self, flight_number, seat_number):
        flight = self.check_flight(flight_number)
        if flight:
            return flight.book_seat(seat_number)
        return "Flight not found."

    def cancel_booking(self, flight_number, seat_number):
        flight = self.check_flight(flight_number)
        if flight:
            return flight.cancel_booking(seat_number)
        return "Flight not found."
