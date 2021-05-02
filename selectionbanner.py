from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle
from functools import partial
from kivy.app import App
import kivy.utils
from kivymd.uix.card import MDSeparator
from summaryscreen import MyClass



class SelectionBanner(GridLayout):

    def __init__(self, **kwargs):
        self.cols = 1
        
        
        super(SelectionBanner,self).__init__()
        # Bus company data
        company = str(kwargs['bus_company'])

        # Ticket data
        price = str(kwargs['ticket_price'])

        # Departure data
        dep_city =str(kwargs['city_departure'])
        dep_date =str(kwargs['date'])
        dep_time =str(kwargs['time_departure'])
        
        # Arrival data
        arr_date = str(kwargs['date'])
        arr_time = str(kwargs['time_arrival'])
        arr_city = str(kwargs['city_arrival'])
        
        #data = company,price,dep_city,dep_time,dep_date,arr_city,arr_time,arr_date
        #travel_data = []
        #travel_data.append(data)
        #print(travel_data)  

        travel_data = {"company": ''+company+'',"price":''+price+'','dep_city': ''+dep_city+'',"dep_time":''+dep_time+'',
                    "dep_date": ''+dep_time+'', "arr_city" : ''+arr_city+'',"arr_time": ''+arr_time+'',"arr_date":''+arr_date+''}
        # Need left FloatLayout fro adding the widgets 

        mainlayout = FloatLayout()

        # Creating the company label
        company_label = MDLabel(text=company, size_hint=(.20 , .10), pos_hint={'center_x': .25, 'top': .85})
        mainlayout.add_widget(company_label)


        # Create a left background layout

        left_box = BoxLayout(orientation = 'horizontal',size_hint=(0.2 , 0.85),  pos_hint={'center_x': .23, 'top': .63})
        left_background = Image(source="icons/roundcorner.png", allow_stretch = True, keep_ratio = False)

        # Initialising widgets for bacground
        left_box.add_widget(left_background)
        mainlayout.add_widget(left_box)

        # Create a left background layout

        right_box = BoxLayout(orientation = 'horizontal',size_hint=(0.2 , 0.85),  pos_hint={'center_x': .76, 'top': .63})
        right_background = Image(source="icons/roundcorner.png", allow_stretch = True, keep_ratio = False)

        # Initialising widgets for bacground
        right_box.add_widget(right_background)
        mainlayout.add_widget(right_box)

    
    
        # Departure info obtained from main app root
        # Creating the time,date and city label postioned in a rounded box
        time_departure_label = MDLabel(text=dep_time, size_hint=(.20 , .10), pos_hint={'center_x': .28, 'top': .45})
        date_departure_label = MDLabel(text=dep_date, size_hint=(.20 , .10), pos_hint={'center_x': .28, 'top': .25})
        city_departure_label = MDLabel(text=dep_city, size_hint=(.20 , .10), pos_hint={'center_x': .28, 'top': .08})
        
        # widgets added to floatlayout
        mainlayout.add_widget(time_departure_label)
        mainlayout.add_widget(date_departure_label)
        mainlayout.add_widget(city_departure_label)
        
        # Arrival info obtained from main app root
        # Creating the time,date and city label postioned in a rounded box
        time_arrival_label = MDLabel(text=arr_time, size_hint=(.20 , .10), pos_hint={'center_x': .80, 'top': .45})
        date_arrival_label = MDLabel(text=arr_date, size_hint=(.20 , .10), pos_hint={'center_x': .80, 'top': .25})
        city_arrival_label = MDLabel(text=arr_city, size_hint=(.20 , .10), pos_hint={'center_x': .80, 'top': .08})

        
        # widgets added to floatlayout
        mainlayout.add_widget(time_arrival_label)
        mainlayout.add_widget(date_arrival_label)
        mainlayout.add_widget(city_arrival_label)

        

        # Inserting button
        button = MDFillRoundFlatButton(text = 'Book', pos_hint={'center_x': .25, 'top': -0.3})
                                       #on_release= partial(SummaryScreen().get_values))
                                       #partial(App.get_running_app().next_screen))
        button.bind(on_release= partial(MyClass().get_values,str(travel_data)))
        button.bind(on_release= partial(App.get_running_app().next_screen),)
        
        # widgets added to floatlayout
        mainlayout.add_widget(button)

        # Adding the price Label
        price_label = MDLabel(text=price, size_hint=(.40 , .10), pos_hint={'center_x': .70, 'top': -0.4})        

        # widgets added to floatlayout
        mainlayout.add_widget(price_label)


        separator = MDSeparator(pos_hint={'center_x': .58, 'top': -0.75}, size=(0.9, 0.9))
        mainlayout.add_widget(separator)


        # ADD ALL THE WIDGET TO THE FLOATLAYOUT
        
        self.add_widget(mainlayout)
        

       
