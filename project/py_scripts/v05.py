import v04_Led_Light
import v05_Pedestrian_Button
import time

# Abstraction as simple interface hides (farcarde design pattern)
# the complexity of the implementation of the class 'Led_Light' in the module 'v04_Led_Light'

red_light = v04_Led_Light.Led_Light(3, False)
ped_button = v05_Pedestrian_Button.Pedestrian_Button(22, True)

while True:
    time.sleep(1)
    red_light.led_light_state = ped_button.button_state
