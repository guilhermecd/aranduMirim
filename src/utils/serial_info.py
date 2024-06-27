import pygame as pg
import threading
import queue
import serial
import time

class SerialInfo(threading.Thread):
    def __init__(self, data_queue):
        super().__init__()
        self.serial_port = '/dev/ttyUSB0'  # ou 'COM3' dependendo do sistema operacional
        self.baud_rate = 9600
        self.data_queue = data_queue
        self.my_serial = self.init_serial()
        self.slots_plataforma = {
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        }
        self.stop_thread = threading.Event()

    def init_serial(self):
        try:
            ser = serial.Serial(self.serial_port, self.baud_rate)
            return ser
        except serial.SerialException as e:
            print(f"Erro ao inicializar a porta serial: {e}")
            return None

    def run(self):
        while not self.stop_thread.is_set():
            if self.my_serial and self.my_serial.is_open:
                try:
                    line = self.my_serial.readline().decode().strip()
                    if line:
                        try:
                            _, plataforma, _, caractere, code = line.split(" ")
                            plataforma = plataforma.replace(':', '')
                            self.slots_plataforma[plataforma] = caractere
                            self.data_queue.put(self.slots_plataforma.copy())
                        except Exception as e:
                            print(f"Erro ao processar a linha: {line}, Erro: {e}")
                except serial.SerialException as e:
                    print(f"Erro na comunicação serial: {e}")
                    self.reset_serial()
                except Exception as e:
                    print(f"Erro desconhecido: {e}")
            time.sleep(0.1)  # Pequena pausa para evitar uso intensivo de CPU

    def reset_serial(self):
        if self.my_serial and self.my_serial.is_open:
            self.my_serial.close()
        self.my_serial = self.init_serial()

    def stop(self):
        self.stop_thread.set()
        if self.my_serial and self.my_serial.is_open:
            self.my_serial.close()

    def clean_slots (self):
        self.slots_plataforma = {
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        }
