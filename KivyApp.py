from kivy.app import App
from kivy.uix.gridlayout import GridLayout 
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest

class TrovaTemperatura(App):
    def build (self):
        self.window = GridLayout()
        self.window.cols = 1       #colonne
        self.window.size_hint = (0.8, 0.9)      #indichiamo i margini della finestra
        self.window.pos_hint = {"center_x" : 0.5, "center_y" : 0.5}  #centriamo gli elementi
        Window.size = (360, 640)   #dimensioni schermata
        
    
        self.window.add_widget(Image(source = "logo.png"))  #importiamo il logo 
        
        
        #creamo una variabile e gli associamo il metodo 
        
        self.input_testo = TextInput(          #text area input
            size_hint = (1, 0.2),              #dimensioni il primo dato della tupla orizzontale il secondo verticale
            font_size = '20sp',                #dimensione del font 20 dimensione "sp" relativa per renderlo responsive
            padding_y= '12sp',                 # padding
            halign= 'center'                   #allineamo il testo                   
            )                                  # 1 = 100% | 0.2 = 20%
    
        self.window.add_widget(self.input_testo)    #qua richiamiamo la funzione e la variabile
        
        #creamo una variabile e gli associamo le caratteristiche
        
        self.bottone = Button(         #bottone
            text = "VIA!",
            size_hint = (1, 0.2),
            bold = True,                       #testo in grassetto
            background_color='#0099ff'         #sfondo bottone
            )
        
        self.window.add_widget(self.bottone)   #qua richiamiamo la funzione e la variabile 
        self.bottone.bind(on_press= self.trova_temp)  #creamo il metodo azione al click e assiociamo il metodo trova_temp
        
        
        ##creamo una variabile e gli associamo le caratteristiche
        
        self.etichetta = Label(            #etichetta
            text = "cerca una città",
            font_size = '20sp',
            color = '007dd1'                  #colore font
            ) 
        self.window.add_widget(self.etichetta)
        
        return self.window
    
    def trova_temp(self, instance): #self, instance sono i parametri tipici quando associamo una
        def edit_label(request, result):
            temp = result['main']['temp']     #qui abbiamo estratto il risultato della temperatura generata all'API e salvata nella variabile
            self.etichetta.text = f"oggi a {self.input_testo.text} ci sono {temp} °C"  #funzione ad un metodo onpress
        link = f"https://api.openweathermap.org/data/2.5/weather?q={self.input_testo.text}&appid=81d10794b566f48bc76b8851e63d91e4&units=metric" #richiamiamo la API
        UrlRequest(link, edit_label)
        

TrovaTemperatura().run()
