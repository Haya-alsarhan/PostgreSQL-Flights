import os 

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getnv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


lef main();

# Lists all flights.

flights = db.execute("SELECT id, origin,destination, duration FROM flights").fetchall()

for flight in flights:
    print (f"{flight.origin} to {flight.destination} minutes.")

#Prompt user to choose a flight.

flight_id = int (input("\nFlight ID:"))

flight = db.execute("SELECT id, origin,destination, duration FROM flights WHERE id = :id ",

{"id": flight_id}).fetchone()

#Make sure flight is valid.

if flight is None:
    print("Error: No such flight.")

    return

#List passengers.

passengers = db.execute("SELECT id, origin,destination, duration FROM flights WHERE id = :id ",{"id": flight_id}).fetchone()

print ("/nPassengers:"))

for passenger in passengers:
    print(passenger.name)

    if len (passengers) ==0;
    print("No passengers.")

    if __name__ == "__main__";

    main()