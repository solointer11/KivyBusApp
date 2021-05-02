from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
import ast
from kivy.app import App
from kivy.factory import Factory
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.expansionpanel import MDExpansionPanel





class SummaryScreen(Screen):

	

	def callback_for_menu_items(self, *args):
		pass
		#toast(args[0])

	def show_example_bottom_sheet(self):
		booking_fees = "TZS 1,000"
		offer = "TZS 2,000"
		ticket_cost = "TZS 10,000"

		bs_menu = MDListBottomSheet()
		

		bs_menu.add_item(
		"Breakdown",
		lambda x: self.callback_for_menu_items(
		""
		),
		)

		bs_menu.add_item(              					
		" Booking fees  " +booking_fees+"" ,
		lambda x: self.callback_for_menu_items(
		""
		),
		icon="clipboard-account",
		)

		bs_menu.add_item(
		" Discounts       " +offer+" ",
		lambda x: self.callback_for_menu_items(""),
		icon="nfc",
		)

		bs_menu.add_item(
		" Ticket costs    " +ticket_cost+"" ,
		lambda x: self.callback_for_menu_items(""),
		icon="ticket-account",
		)

		bs_menu.open()
            
             
            


class MyClass():

	def get_values(self,data,widget):


		# Get the values after clicking the price button
		# Ditribute the values the appropriate sections in the summary screen kv
		
		info_data = ast.literal_eval(data)

		arrival_city = info_data['arr_city']

		#print(bus_name,arrival_city)

		self.app = App.get_running_app()
		screen = self.app.root.ids['summary_screen']

		# Update the bus name  label 
		bus_name = info_data['company']
		bus_name_label = screen.ids['bus_name_label']
		bus_name_label.text = bus_name

		# Update the ticket price label 
		ticket_price = info_data['price']
		ticket_price_label = screen.ids['price_ticket']
		ticket_price_label.text = ticket_price

		# Update the departure and arrival info label 
		#Departure
		departure_city = info_data['dep_city']
		departure_time = info_data['dep_time']
		departure_date = info_data['dep_date']

		dep_city_label = screen.ids['from_city']
		dep_city_label.text = departure_city

		dep_time_label = screen.ids['from_time']
		dep_time_label.text = departure_time

		#dep_date_label = screen.ids['']
		#dep_date_label.text = departure_date

		# Arrival
		arrival_city = info_data['arr_city']
		arrival_time = info_data['arr_time']
		arrival_date = info_data['arr_date']

		arr_city_label = screen.ids['to_city']
		arr_city_label.text = arrival_city


		arr_time_label = screen.ids['to_time']
		arr_time_label.text =arrival_time


	
	    









	

	   






								
							