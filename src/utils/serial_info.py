import serial

class SerialInfo():
    def __init__(self):
        # self.my_serial = serial.Serial('/dev/ttyUSB0', 9600)
        self.my_serial = serial.Serial('COM3', 9600)

        self.slots_plataforma = {
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        }

    def get_slots (self):
        # Lê uma linha da porta serial
        # line = self.my_serial.readline().decode().strip()
        line = self.my_serial.read(self.my_serial.in_waiting)
        print( self.my_serial.readline().decode())
        # Verifica se há dados
        if line:
            try:
                _, plataforma, _, caractere, code = line.split(" ")
                plataforma = plataforma.replace(':', '')
                self.slots_plataforma[plataforma] = caractere
                return self.slots_plataforma
            except Exception as e:
                print(f"Erro ao processar a linha: {line}, Erro: {e}")
                return {'1': '', '2': '', '3': '','4': ''}
    
    def clean_slots (self):
        self.slots_plataforma = {
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        }
