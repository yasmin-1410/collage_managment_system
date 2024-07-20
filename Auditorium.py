class Auditorium():
    __EventList=[]
    __Date=None
    __Time=None
    __TotalSeats=0
    __DepartmentId=0
    
    def BookEvents(self, eventName, Date, Time, TotalSeats):
        try:
            with open("BookEvents.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 5:
                        event_id = int(parts[0])
                        booked_event_name = parts[1]
                        booked_date = parts[2]
                        booked_time = parts[3]
                        booked_total_seats = int(parts[4])
                        
                        if booked_event_name == eventName and booked_date == Date and booked_time == Time:
                            print("The auditorium is already booked for this event at the same date and time.")
                            return
        except FileNotFoundError:
            pass
        try:
            with open("Auditorium.txt", 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        event_id = int(parts[0])
                        auditorium_event_name = parts[1]
                        auditorium_total_seats = int(parts[2])
                        
                        if auditorium_event_name == eventName:
                            if auditorium_total_seats >= TotalSeats:
                                with open("BookEvents.txt", "a") as file:
                                    file.write(f"{event_id},{eventName},{Date},{Time},{TotalSeats}\n")
                                print(f"Event '{eventName}' booked for {Date} at {Time}.")
                                return
                            else:
                                print("Total seats not enough.")
                                return
        except FileNotFoundError:
            print("Error: The Auditorium.txt file was not found.")
            return

        print("Error: Event not found in the auditorium list.")

# auditorium = Auditorium()
# auditorium.BookEvents("Cairo Opera House", "2023-08-15", "18:00", 500)


        