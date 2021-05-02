APP:


Database:
-The database should contain the user tickets.
-It should retrieve the available buses that still contain the tickets on the database
-So far the database only shows the tickets from similar bus companies

GOAL:
The goal is to display only the bus companies with available tickets. If the tickets are all finished with a respective bus company then the bus company will not be shown in the 'Select Bus' screen.

SOLUTION:

1. Display only the tickets that are available on the 'Select Bus' screen. This will produce a situation duplicates when a same company will have multiple tickets.

2. Display all available buses for that route but once the user select a particular bus company. The user can advance to the 'Summay' screen if that  bus company have the ticket available in the database. If not then instead of a summary screen a different screen that tells the user that there are no available tickets. This is not an ideal case since the users won't be sure what they see on 'Select Bus' screen is actually available or not. It's much more efficient to display only the available tickets.








