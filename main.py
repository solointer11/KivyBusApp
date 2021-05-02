import sys
sys.path.append("/".join(x for x in __file__.split("/")[:-1]))
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.theming import ThemeManager
from selectionbanner import SelectionBanner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from summaryscreen import SummaryScreen
from paymentscreen import PaymentScreen
from addcardscreen import AddCardScreen
from kivy.clock import Clock
from kivy.animation import Animation
from changecardscreen import CardInfo
from FirebaseLoginScreen.firebaseloginscreen import FirebaseLoginScreen
import requests
import traceback
import os.path
from json import dumps
from kivy.network.urlrequest import UrlRequest
import json
import os
import google.cloud
import firebase_admin
from firebase_admin import credentials,auth
from firebase_admin import firestore

#from google.oauth2.credentials import Credentials
#from google.cloud import storage
#from google.cloud import firestore
#import google.cloud.firestore

#from google.cloud.firestore import Client

from requests.exceptions import HTTPError
from google.oauth2.credentials import Credentials


# Formatting the window to simulate a phone 
from kivy.utils import platform
from kivy.config import Config
from kivy.core.window import Window

# Fixing the screen size for mobile app
if platform not in ('android', 'ios'):
    #Approximate dimensions of mobile phone.
    Config.set('graphics', 'resizable', '0')
    Window.size = (375, 667)

# Use the application default credentials

cred = credentials.Certificate("busappversion2-firebase-adminsdk-rsxy5-5c00535eb7.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


# Declare all screens
class HomeScreen(Screen):
    pass

class BusSelectionScreen(Screen):
    pass

class SelectTicketScreen(Screen):
    pass

class TicketScreen(Screen):
    pass   

class CardScreen(Screen):
    pass

class AccountScreen(Screen):
    pass

class ChangeCardScreen(Screen):
    pass



class MainApp(MDApp):
    #refresh_token_file = "refresh_token.txt" 
    #web_api_key = "AIzaSyBT7sEo7tWB_rYnYkbrgSePgLfEHiK_otY"
    debug = False
    localId = ""
    idToken = ""
    refresh_token_file = "refresh_token.txt" 
    web_api_key = "AIzaSyBT7sEo7tWB_rYnYkbrgSePgLfEHiK_otY"
        
   
    def build(self):
        self.fire = FirebaseLoginScreen()
        app_user = self.current_user()

         

    def current_user(self):
        if self.debug:
            print("Attempting to log in a user automatically using a refresh token.")
        token = self.fire.load_refresh_token()
        self.refresh_token = token
        refresh_url = "https://securetoken.googleapis.com/v1/token?key=" + self.web_api_key
        refresh_payload = dumps({"grant_type": "refresh_token", "refresh_token": self.refresh_token})
        res = UrlRequest(refresh_url, req_body=refresh_payload,
                   on_success=self.load_user,
                   on_failure=self.fire.failed_account_load,
                   on_error=self.fire.failed_account_load)


    def load_user(self,urlrequest, data):
        if self.debug:
            print("Successfully logged a user in automatically using the refresh token")
        self.idToken = data['id_token']
        self.localId = data['user_id']
        return self.localId, self.idToken


    def change_card(self):
        grid = self.root.ids['change_card_screen'].ids['card_info']

        card_name = ['Micheal Jackson','Micheal Jackson','Micheal Jackson']
        last_card_numbers = ['2134','2342','3231']
        expiry_date = ['08/20','04,22','09/21']
        
        for i in card_name:
            pass
        for g in last_card_numbers:
            pass
        for h in expiry_date:
            pass

            task = CardInfo(name_passenger = i,last_card_numbers = g, expiry_date = h ) 

            grid.add_widget(task)


    def test_function(self):

        # Link the API firestore
        FIRESTORE_REST_API = "https://firestore.googleapis.com/v1/"

        # Authenticate users
        id_token = self.idToken   # Already singed in user from the current_user() function

        
        # Link to firesore specific poject
        YOUR_PROJECT_ID = "busappversion2"

        # TESTING AND DEBUGGING hardcording email and password
        #email = "example@test.com"
        #password = "coolpassword123"
        #response = self.sign_in_with_email_and_password(self.web_api_key, email, password)
        #token = response['idToken']

        # Sending the request to the API
        request_url = "https://firestore.googleapis.com/v1/projects/%s/databases/(default)/documents/users?key=%s" %(YOUR_PROJECT_ID,self.web_api_key)
        headers = {"content-type": "application/json; charset=UTF-8","Authorization": "Bearer %s"% (id_token)}
        result = requests.get(request_url, headers = headers).json()
        print(result)
        
        return result
        


    def sign_in_with_email_and_password(self,api_key, email, password):
        FIREBASE_REST_API = "https://identitytoolkit.googleapis.com/v1/accounts"
        request_ref = "%s:signInWithPassword?key=%s" % (FIREBASE_REST_API, api_key)
        headers = {"content-type": "application/json; charset=UTF-8"}
        data = json.dumps({"email": email, "password": password, "returnSecureToken": True})
        req = requests.post(request_ref, headers=headers, data=data)
        try:
            req.raise_for_status()
        except HTTPError as e:
            raise HTTPError(e,request_object.text)

        return req.json()


    def search_responce(self):  

        route = 'Dar-Mor'
        date = 'JULY 17'
        route_ref = db.collection('tickets').document(route).collection('All_companies').where( "Date", "==", date).stream()
                    
        data = route_ref

        for doc in data:
            #print(doc.to_dict())
            results = doc.to_dict()
            date = results['Date']
            name = results['Bus_name']
            depart = results['Departure_time']
            arrives = results['Arrival_time']
            price = results['Ticket_price']
            from_city = results['from']
            to_city = results['to']
        
            banner_grid = self.root.ids['bus_selection_screen'].ids['banner_grid']
          

            w = SelectionBanner(bus_company = name,ticket_price =  price ,time_departure = depart ,
                                time_arrival = arrives, date = date, city_departure = from_city, city_arrival = to_city) 

           
            banner_grid.add_widget(w)

    def next_screen(self,widget):
        #Used to change the screen after the price button is selected
        
        #card_input = self.root.ids['card_screen'].ids['card_id']
        #card_input.text = sources
        print('changed to summaryscreen')
        # FURTHER CHANGES TO BE MADE
        self.change_screen("summary_screen")

    def change_screen(self,screen_name):
        # Get the screen manger from the kiv file
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name
        #screen_manager = self.root.ids

MainApp().run()

