import pandas as pd
import time
import board
import neopixel
import time

time.sleep(20) #wait for system to start up

pixels = neopixel.NeoPixel(board.D21, 8, brightness=0.1, auto_write=False, pixel_order=neopixel.RGB)

df = pd.read_csv("https://api.covidtracking.com/v1/states/ny/daily.csv")
newcases_week = df.positiveIncrease[:8]

lednum = 0
for i in range(7,0,-1):
    if newcases_week[i] > newcases_week[i-1]:
        pixels[lednum] = (255, 0, 0)  #glow red
    else:
        pixels[lednum] = (0, 255, 0)  #glow green
    lednum+=1
        
pixels.show()
time.sleep(60)  #added this line so that the leds turn off after 60s b/c I didn't want them to keep running; can be altered or removed
pixels.fill((0,0,0))
pixels.show()

