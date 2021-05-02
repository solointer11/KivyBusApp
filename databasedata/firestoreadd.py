import  firebase_admin
from firebase_admin import credentials,firestore,initialize_app,auth

# Use the application default credentials

cred = credentials.Certificate("/Users/solomongunda/Desktop/Draft2App/firestorekey/busappversion2-firebase-adminsdk-rsxy5-5c00535eb7.json")
firebase_admin.initialize_app(cred)

db = firestore.client()



doc_ref = db.collection('tickets')

from_city = 'Dar'
to_city = 'Mor'


route_ref = doc_ref.document(from_city+'-'+to_city)

company_ref = route_ref.collection('All_companies')

ticket_number_ref = company_ref.document('ticket_11')

ticket_number_ref.set({

	'from':from_city,
	'to': to_city,
	'Date' :'JULY 17',
	'Departure_time': '07:00',
	'Arrival_time': '12:00',
	'Bus_name': 'Bus C',
	'Ticket_price': '10,000',
	'id':'F1dR2857'

 })

print('ADDED TO DATABASE')





#route_ref = db.collection('tickets').document('Dar-Mor').collection('BUS A').stream()

#docs = route_ref.stream()  and "Arrival_time", "==", "12:00"

#docs = route_ref.where( "Date", "==", "10/07/2020").where("Arrival_time", "==", "12:00").stream()

#for doc in route_ref:
#	print(doc.to_dict())



def get_results(route,date):

	route_ref = db.collection('tickets').document(route).collection('All_companies')

	#docs = route_ref.stream()

	docs = route_ref.where( "Date", "==", date).stream()

	#for doc in docs:
		#print(doc.id, doc.to_dict())

	return docs


#route = 'Dar-Mor'
#date = '10/07/2020'

'''data = get_results(route,date)

my_dict = { el.id: el.to_dict() for el in data }

#print(my_dict.values())

info = my_dict.values()

for results in info:
	date = results['Date']
	name = results['Bus_name']

print(date,name)'''




#{'ticket_16': {'Date': '10/07/2020', 'Departure_time': '07:00', 'Bus_name': 'Bus C', 'Ticket_price': '10,000', 'Arrival_time': '12:00', 'id': 'FVD942857'}}
#dict_values([{'Ticket_price': '10,000', 'Arrival_time': '12:00', 'id': 'FVD942857', 'Departure_time': '07:00', 'Date': '10/07/2020', 'Bus_name': 'Bus C'}])


# Deleting documents 
#delete = db.collection(u'cities').document(u'DC').delete()














