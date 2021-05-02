from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.label import MDIcon
from kivymd.uix.card import MDSeparator
from kivy.metrics import dp
from kivy.app import App


class CardInfo(FloatLayout):
	"""docstring for CardInfo"""
	def __init__(self, **kwargs):
		self.height = dp(80)
		self.size_hint_y = None

		super(CardInfo, self).__init__()


		# Creating the variables
		name_passenger = kwargs['name_passenger']
		last_card_numbers = kwargs['last_card_numbers']
		expiry_date = kwargs['expiry_date']


		# Creating the widgets

		icon_left = MDIcon(halign = ('left'),icon =  ('credit-card-outline'), size_hint = (0.5,0.2), pos_hint= {"center_x":0.3, "center_y": 0.5})
		
		name_label = MDLabel( text = (name_passenger), pos_hint = {"center_x":0.65, "center_y": 0.7})

		dot_icons = MDIcon( icon = ('dots-horizontal'), size_hint_y = None, pos_hint= {"center_x":0.65, "center_y": 0.4})

		last_4_numbers = MDLabel(text = (last_card_numbers),pos_hint=  {"center_x":0.73, "center_y": 0.4})

		expiry_date = MDLabel(text = ('Expiry ' +expiry_date+''), pos_hint = {"center_x":0.88, "center_y": 0.4})

		separator = MDSeparator(pos_hint =  {'center_x': .5, 'top': 0.1})

		# Adding the widgets to the floatlayout

		self.add_widget(icon_left)
		self.add_widget(name_label)
		self.add_widget(dot_icons)
		self.add_widget(last_4_numbers)
		self.add_widget(expiry_date)
		self.add_widget(separator)
