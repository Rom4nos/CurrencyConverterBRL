from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


import requests

API_KEY = "830428236c56527bc8643c95"

def click():
    global ed

    # Build API URL with ed notation and API key
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{ed.text}"

    try:
        # Make request to API
        response = requests.get(url)

        # Parse JSON response
        data = response.json()

        # Check if the ed notation is valid
        if ed.text not in data["conversion_rates"]:
            print(f"Invalid ed notation: {ed.text}")
        else:
            # Get exchange rate for the ed notation
            rate = data["conversion_rates"]["BRL"]

            # Display the result
            result_textinput.text = f"1 {ed.text} = {rate:.2f} BRL"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")

def build(): 
    layout = FloatLayout()

    
    title_label = Label(text="Currency Converter to BRL")
    title_label.size_hint = None, None
    title_label.height = 350
    title_label.width = 400
    title_label.y = 700
    title_label.x = 400


    global ed, result_textinput
    ed = TextInput(text="Enter Currency (e.g. EUR, GBP, JPY): ")
    ed.size_hint = None , None
    ed.height = 300
    ed.width = 400
    ed.y = 500
    ed.x = 400

    result_textinput = TextInput(multiline=False)
    result_textinput.size_hint = None, None
    result_textinput.height = 200
    result_textinput.width = 400
    result_textinput.y = 200
    result_textinput.x = 400

    bt = Button(text="Converter")
    bt.size_hint = None, None
    bt.height = 150
    bt.width = 200
    bt.y = 100
    bt.x = 500
    bt.on_press = click

    layout.add_widget(ed)
    layout.add_widget(bt)
    layout.add_widget(result_textinput)
    layout.add_widget(title_label)

    return layout

janela = App()
janela.build = build 
janela.run()
