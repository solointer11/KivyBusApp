from kivy.uix.screenmanager import Screen
from kivy.app import App


class AddCardScreen(Screen):
    
    def card_number_input(self):

    	# Link the main screen
        self.app = App.get_running_app()

        # Link the specific screen
        self.screen = self.app.root.ids['add_card_screen']

        #Link the label
        self.card_number = self.screen.ids['number']


        a = self.card_number.text 
    
        first = a[0:4]
        second = a[4:8]
        third = a[8:12]
        fourth = a[12:16]
        #print(len(a))
        #print(first + " " + second + " " + third + " " + fourth)
        new = first + "   " + second + "   " + third + "   " + fourth

        # Link the screen
        self.screen = self.app.root.ids['add_card_screen']

        #Link the label
        self.card_number = self.screen.ids['updated_number']

        self.card_number.text = new


    def card_month_input(self):

        # Link the main screen
        self.app = App.get_running_app()

        # Link the specific screen
        self.screen = self.app.root.ids['add_card_screen']

        #Link the label
        self.card_number = self.screen.ids['month']


        a = self.card_number.text 
    
        first = a[0:2]
        
        #print(len(a))
        #print(first + " " + second + " " + third + " " + fourth)
        new = first+"/"

        # Link the screen
        self.screen = self.app.root.ids['add_card_screen']

        #Link the label
        self.card_number = self.screen.ids['updated_month']

        self.card_number.text = new




