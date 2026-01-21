class Flight:
    def __init__(self, seats):
        self.seats = seats

    def book_seat(self):
        if self.seats > 0:
            self.seats -= 1
            print("Seat booked")
        else:
            print("No seats available")


f = Flight(2)
f.book_seat()
f.book_seat()
f.book_seat()
