
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.animation import Animation
from kivy.app import App
from kivymd.theming import ThemableBehavior
from kivymd.uix.expansionpanel import MDExpansionPanel,MDExpansionPanelOneLine




class MoreInformation(ThemableBehavior, BoxLayout):
    pass
    
class PaymentScreen(ThemableBehavior, Screen):

    has_already_opened = False

    mobile_btn = ObjectProperty(None)

    

    def on_enter(self):
        if self.has_already_opened:
            return
        else:
            self.has_already_opened = True

        content_for_panel = MoreInformation()
        md_expansion_panel = MDExpansionPanel(
            content=content_for_panel,
            icon="icons/add.png",
            #title = "More information",
            panel_cls=MDExpansionPanelOneLine(text="Cost breakdown")
        )
        
        #md_expansion_panel.bind(on_open=self.on_panel_open)
        #md_expansion_panel.bind(on_close=self.on_panel_close)
        #self.ids.expansion_panel_box.add_widget(md_expansion_panel)
        self.ids['expansion_panel_box'].add_widget(md_expansion_panel)


        # Remove the following widgets:1.Card input layout, 2.Change Payment method button, 3 New PaybyCard button

        # Link the screen
        self.app = App.get_running_app()
        self.screen_payment = self.app.root.ids['payment_screen']

        #Link the buttons and others to be named
        self.new_card_btn = self.screen_payment.ids['card_btn']       # New card button
        self.method_options = self.screen_payment.ids['method_button']# Change payment option button
        self.card_input = self.screen_payment.ids['card_layout']      # Card input layout

        self.CVV_input = self.screen_payment.ids['short_card_layout'] # Only CVV card input layout
        

        # REMOVE BUTTON PAY OPTIONS for new card, change payment method and card input layout widget when the function is called: 
        self.screen_payment.ids['out_method_layout'].remove_widget(self.new_card_btn)
        self.screen_payment.ids['out_method_layout'].remove_widget(self.method_options)
        self.screen_payment.ids['another_out_layout'].remove_widget(self.card_input)
        self.screen_payment.ids['another_out_layout'].remove_widget(self.CVV_input)




    def update_value(self):

        # Link the main screen
        self.app = App.get_running_app()
        
        screen_summary = self.app.root.ids['summary_screen']
        screen_payment = self.app.root.ids['payment_screen']

        # Update the total cost label top

        cost_total = screen_summary.ids['price_ticket']
        value = cost_total.text

        cost_label= screen_payment.ids['price_total']
        cost_label.text = value

        # Update the total cost label bottom
        cost_total = screen_summary.ids['price_ticket']
        value = cost_total.text

        cost_label= screen_payment.ids['price_total2']
        cost_label.text = value

        # Update the OUT label
        date = screen_summary.ids['date_departure']
        value = date.text

        date_label= screen_payment.ids['dep_date']
        date_label.text2 = value

        # Update the From label

        # Update the To label

    def pay_by_card(self):

        
        # CHECK IF CARD IS ALREADY ADDED TO THE SYSTEM OR NOT
        # IF ALREADY ADDED THEN THE "short_card_layout" IS ADDED
        # IF NOT ADDED THEN THE "card_layout" IS ADDED

        # Link the screen
        self.app = App.get_running_app()
        self.screen_payment = self.app.root.ids['payment_screen']
        #Link the buttons
        self.button_card = self.screen_payment.ids['card_button']
        self.button_mobile = self.screen_payment.ids['mobile_button']
        self.button_paypal = self.screen_payment.ids['paypal_button']

        #Link the buttons and others to be named
        self.new_card_btn = self.screen_payment.ids['card_btn']       # New card button
        self.method_options = self.screen_payment.ids['method_button']# Change payment option button
        self.card_input = self.screen_payment.ids['card_layout']      # Card input layout
        self.CVV_input = self.screen_payment.ids['short_card_layout'] # Only CVV card input layout
        
        # Check the database for the True OR False
        added_card = False

        if added_card == False:
            # REMOVING ALL BUTTON PAY OPTIONS widget when the function is called: 
            self.screen_payment.ids['options_method_layout'].remove_widget(self.button_mobile)
            self.screen_payment.ids['options_method_layout'].remove_widget(self.button_paypal)
            self.screen_payment.ids['options_method_layout'].remove_widget(self.button_card)


            # ADD THE NEW PAY BUTTON widget when the function is called:
            self.card_input.disabled = False 
            self.card_input.opacity = 1

            # ADD THE CARD INPUT LAYOUT  widget when the function is called:
            self.new_card_btn.disabled = False 
            self.new_card_btn.opacity = 1
           
            # ADD THE CHANGE PAYMENT METHOD BUTTON widget when the function is called:
            self.method_options.disabled = False 
            self.method_options.opacity = 1

            # ADD BUTTON PAY OPTIONS for new card, change payment method and card input layout widget when the function is called: 
            self.screen_payment.ids['another_out_layout'].add_widget(self.card_input)
            self.screen_payment.ids['out_method_layout'].add_widget(self.new_card_btn)
            self.screen_payment.ids['out_method_layout'].add_widget(self.method_options)
        
        else:
            print("At least one card is added on the system")

            # ADD ALL BUTTON PAY OPTIONS widget when the function is called: 
            self.screen_payment.ids['options_method_layout'].remove_widget(self.button_mobile)
            self.screen_payment.ids['options_method_layout'].remove_widget(self.button_paypal)
            self.screen_payment.ids['options_method_layout'].remove_widget(self.button_card)

            # ADD THE NEW PAY BUTTON widget when the function is called:
            self.CVV_input.disabled = False 
            self.CVV_input.opacity = 1

            # ADD THE CARD INPUT LAYOUT  widget when the function is called:
            self.new_card_btn.disabled = False 
            self.new_card_btn.opacity = 1
           
            # ADD THE CHANGE PAYMENT METHOD BUTTON widget when the function is called:
            self.method_options.disabled = False 
            self.method_options.opacity = 1

            # ADD BUTTON PAY OPTIONS for new card, change payment method and card input layout widget when the function is called: 
            self.screen_payment.ids['another_out_layout'].add_widget(self.CVV_input)
            self.screen_payment.ids['out_method_layout'].add_widget(self.new_card_btn)
            self.screen_payment.ids['out_method_layout'].add_widget(self.method_options)


        
    def pay_by_usaved_card(self):

        # When the button for unsaved card is pressed
        # Perfom the payment function by stripe move to the tictek screen
        pass 

    def pay_by_saved_card(self):
        #Check if the card is already added in the system then display the mini card input with CVV and last 4 digits
        pass

    def pay_by_paypal(self):

        # When the button is pressed these tasks are done:
        # Remove the other buttons and add the details for paying the cost
        # First if there's no card added then add the inputs 
        # If there's a card added to the system then move on to the option of adding the CVV and Paybutton

        # Link the screen
        self.app = App.get_running_app()
        self.screen_payment = self.app.root.ids['payment_screen']
        # ADDING and REMOVING the buttons and widgets

        # Remove all the buttons except pay by card button
        #Link the buttons
        self.button_card = self.screen_payment.ids['card_button']
        self.button_mobile = self.screen_payment.ids['mobile_button']
        self.button_paypal = self.screen_payment.ids['paypal_button']

        # ADD ALL BUTTON PAY OPTIONS widget when the function is called: 
        self.screen_payment.ids['options_method_layout'].remove_widget(self.button_mobile)
        self.screen_payment.ids['options_method_layout'].remove_widget(self.button_paypal)
        self.screen_payment.ids['options_method_layout'].remove_widget(self.button_card)

        #Link the buttons and others to be named
        self.new_card_btn = self.screen_payment.ids['card_btn']       # New card button
        self.method_options = self.screen_payment.ids['method_button']# Change payment option button
        #self.card_input = self.screen_payment.ids['card_layout']      # Card input layout
        self.CVV_input = self.screen_payment.ids['short_card_layout'] # Only CVV card input layout

        # ADD THE NEW PAY BUTTON widget when the function is called:
        self.CVV_input.disabled = False 
        self.CVV_input.opacity = 1

        # ADD THE CARD INPUT LAYOUT  widget when the function is called:
        self.new_card_btn.disabled = False 
        self.new_card_btn.opacity = 1
       
        # ADD THE CHANGE PAYMENT METHOD BUTTON widget when the function is called:
        self.method_options.disabled = False 
        self.method_options.opacity = 1


        # ADD BUTTON PAY OPTIONS for new card, change payment method and card input layout widget when the function is called: 
        self.screen_payment.ids['another_out_layout'].add_widget(self.CVV_input)
        self.screen_payment.ids['out_method_layout'].add_widget(self.new_card_btn)
        self.screen_payment.ids['out_method_layout'].add_widget(self.method_options)
       

    def change_pay_method(self):
        '''Called when the change payment button is pressed'''

        #Functions: 1. Return the payment options buttons(Paybycard,Paybymobile,PaybyPaypal)

        # Link the screen
        self.app = App.get_running_app()
        self.screen_payment = self.app.root.ids['payment_screen']

        #Link the buttons and others to be named
        self.button_card = self.screen_payment.ids['card_button']     # Card button
        self.button_mobile = self.screen_payment.ids['mobile_button'] # Mobile payment button
        self.button_paypal = self.screen_payment.ids['paypal_button'] # Paypal payment button

        # ADD BUTTON PAY OPTIONS for card, mobile and paypal widget when the function is called: 
        self.screen_payment.ids['options_method_layout'].add_widget(self.button_card)
        self.screen_payment.ids['options_method_layout'].add_widget(self.button_mobile)
        self.screen_payment.ids['options_method_layout'].add_widget(self.button_paypal)

        #Link the buttons and others to be named
        self.new_card_btn = self.screen_payment.ids['card_btn']       # New card button
        self.method_options = self.screen_payment.ids['method_button']# Change payment option button
        self.card_input = self.screen_payment.ids['card_layout']      # Card input layout
        self.CVV_input = self.screen_payment.ids['short_card_layout'] # Only CVV card input layout

        # REMOVE BUTTON PAY OPTIONS for new card, change payment method and card input layout widget when the function is called: 
        self.screen_payment.ids['out_method_layout'].remove_widget(self.new_card_btn)
        self.screen_payment.ids['out_method_layout'].remove_widget(self.method_options)
        self.screen_payment.ids['another_out_layout'].remove_widget(self.card_input)
        self.screen_payment.ids['another_out_layout'].remove_widget(self.CVV_input)





        


        
    









