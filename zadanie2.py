import matplotlib.pyplot as plt

class Pacjent:
    liczba_pacjentow = 0 
    
    def __init__(self):
        self.imie = []
        self.wiek = []
        self.liczba_wizyt = []

        
    #wprowadzamy dane pacjentow    
    def get_data(self):
        while Pacjent.liczba_pacjentow < 3:
            try:
                a = (str(input("Wprowadź imię pacjenta: ")))
            except ValueError:
                print("Wprowadź poprawną wartość.")     
            try:    
                b = int(input("Wprowadź wiek pacjenta: "))
            except ValueError:
                print("Wprowadź poprawną wartość.")    
            try:
                c = int(input("Wprowadź liczbę wizyt u lekarza w roku: "))
            except ValueError:
                print("Wprowadź poprawną wartość.")
            self.imie.append(a)
            self.wiek.append(b)
            self.liczba_wizyt.append(c)    
            
            Pacjent.liczba_pacjentow += 1    



class DataProcessor:
    def __init__(self, dane_pacjenta):
        self.imie = dane_pacjenta.imie 
        self.wiek = dane_pacjenta.wiek
        self.liczba_wizyt = dane_pacjenta.liczba_wizyt
        self.liczba_pacjentow = Pacjent.liczba_pacjentow 
        self.processed_data = None
    
    #liczymy srednia liczbe wizyt na pacjenta
    def process_data(self):
        self.processed_data = print("Średnia liczba wizyt u lekarza w roku to " + round(sum(self.liczba_wizyt)/self.liczba_pacjentow, 2))
    
    def get_processed_data(self):
        return self.processed_data
    
    def display_data(self):
        print(self.processed_data)

class DataVisualizer:
    def __init__(self, data_processor):
        self.data_processor = data_processor
    
    def show_data_in_chart(self):
        self.wiek = data_processor.wiek
        self.liczba_wizyt = data_processor.liczba_wizyt

        plt.bar(self.wiek, self.liczba_wizyt)
        plt.title("Liczba wizyt u lekarza w ciągu roku przez róznych pacjentów")
        plt.xlabel("Pacjent")
        plt.ylabel("Liczba wizyt")
        plt.show()

dane_pacjenta = Pacjent()
dane_pacjenta.get_data()
data_processor = DataProcessor(dane_pacjenta)
data_processor.process_data()
data_processor.display_data()
data_visualizer = DataVisualizer(data_processor)
data_visualizer.show_data_in_chart()
