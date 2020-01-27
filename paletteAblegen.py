''' Code für das Fahrzeug mit der Palette

    Der Code für das Fahrzeug dass anfangs die Palette trägt, das zweite, entgegenkommende
    Fahrzeug erkennt. Dann die Palette abstellt, sich umdreht, wegfährt und das zweite
    Fahrzeug informiert, dass es loslegen kann.

'''

from botlib.bot import Bot
import time

bot = None
    
def initialisiereRoboter():
    global bot
    bot = Bot()
    bot.calibrate()

def scanNachEntgegenkommendemFahrzeug():
    #TODO realisieren der kompletten Funktion. Eventuell aufnehmen in die Botlib
    pass

def entgegenkommendesFahrzeugOhnePaletteErkannt():
    #TODO testen der Funktion
    paletteAbsetzen()
    #TODO weit genug zurückfahren
    umdrehen()
    nachrichtAnFahrzeugZwei()
    pass

def paletteAbsetzen():
    #TODO realisieren der kompletten Funktion, oder einbinden von der Botlib
    pass

def umdrehen():
    #TODO realisieren der kompletten Funktion, oder einbinden von der Botlib
    '''
bp.set_motor_position(bp.PORT_D, 70)
time.sleep(1)
bp.set_motor_power(bp.PORT_B, -30)
time.sleep(4)
bp.set_motor_power(bp.PORT_B, 0)
time.sleep(1)
bp.set_motor_position(bp.PORT_D, 0)
time.sleep(1)
bp.set_motor_position(bp.PORT_D, -60)
bp.set_motor_power(bp.PORT_B, 30)
time.sleep(4)
bp.set_motor_power(bp.PORT_B, 0)
bp.set_motor_position(bp.PORT_D, 0)
time.sleep(1)
bp.set_motor_power(bp.PORT_B, 20)
time.sleep(1)
bp.set_motor_power(bp.PORT_B, 0)'''
    bot.drive_steer(1)
    time.sleep(1)
    bot.drive_power(-30)
    time.sleep(3.52)
    bot.drive_power(0)
    time.sleep(1)
    bot.drive_steer(0)
    time.sleep(1)
    bot.drive_steer(-1)
    bot.drive_power(30)
    time.sleep(3.52)
    bot.drive_power(0)
    bot.drive_steer(0)
    time.sleep(1)
    bot.drive_power(20)
    time.sleep(1)
    bot.drive_power(0)

def nachrichtAnFahrzeugZwei():
    #TODO realisieren der kompletten Funktion
    #TODO Gedanken über implementation mit MQTT machen
    #Nachfrage möglich bei: Mercedes, Kris
    pass

def test():
    initialisiereRoboter()
    umdrehen()
test()