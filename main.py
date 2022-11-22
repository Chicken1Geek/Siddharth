global queryArray

queryArray = ['n - Create new Ticket',
              'r - View Tickets',
              'g - Get ticket',
              'd - Delete Ticket',
              'p - Purge Tickets']

def loadFile():
    with open('tickets.txt','rt') as file:
        ticketsRaw = file.read().split('\n')
        ticketsDb = []
        for ticketStr in ticketsRaw:
            ticketsDb.append(ticketStr.split(','))
        ticketsDb.remove([""])
    return ticketsDb

def writeFile(ticketsDb):
    with open('tickets.txt','wt') as file:
        data = ''
        for i in ticketsDb:
            ticketStr = ''
            for j in i:
                ticketStr += j + ','
            data += ticketStr.rstrip(',') + '\n'
        file.write(data)
            

def createTicket(name,movie,seat):
    db = loadFile()
    db.append([name,movie,seat])
    writeFile(db)

def readTickets():
    db = loadFile()
    if db == []:
        print('No records found')
    for i in db:
        print(f'''\nName: {i[0]}\nMovie: {i[1]}\nSeat: {i[2]}''')

def getTicket(seatNo):
    for i in loadFile():
        if i[2] == seatNo:
            return i
    raise ValueError

def deleteTicket(seatNo):
    db = loadFile()
    db.remove(getTicket(seatNo))
    writeFile(db)

def purgeTickets():
    writeFile([])

def menu():
    for i in queryArray:
        print(i)

def main():
    print('\nKnox Theaters')
    menu()
    query = input('>>> ').lower()

    if query == 'n':
        print('\nCreating new ticket')
        name = input('Enter name: ')
        movie = input('Enter movie: ')
        seat = input('Seat number: ')
        createTicket(name,movie,seat)
        print('Create ticket')
    elif query == 'r':
        readTickets()
    elif query == 'g':
        try:
         print(getTicket(input('Enter Seat Number: ')))
        except ValueError:
            print('\nSeat number not found')
    elif query == 'p':
        purgeTickets()
        print('All tickets deleted')
    elif query == 'd':
        try:
            deleteTicket(input('Enter Seat no: '))
            print('Deleted ticket')
        except ValueError:
            print('No ticket with seatno')
    else:
        print('Wrong query')

while True:
    main()
