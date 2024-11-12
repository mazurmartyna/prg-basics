# 5x5 cinema seating
# A = Available, B = Booked

cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]



def seats_total(seats):
   total_seat = 0
   for row in cinema_seats:
      for item in row:
         total_seat += 1
   return total_seat

def seats_available(seats):
   available_seats = 0 
   for row in cinema_seats:
      for item in row:
         if item == 'A':
            available_seats += 1
   return available_seats

def seats_booked(seats):
   booked_seats = 0
   for row in cinema_seats:
      for item in row:
         if item == 'B':
            booked_seats += 1
   return booked_seats

def seat_status(cinema_seats, row, place):
   if cinema_seats[row][place] == 'A':
        return 'Available'
   else:
        return 'Booked'

print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1-1, 1-1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5-1, 5-1))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3-1, 5-1))