import pandas as pd
import time
import board
import neopixel
import time

time.sleep(30)

pixels = neopixel.NeoPixel(board.D21, 8, brightness=0.1, auto_write=False, pixel_order=neopixel.RGB)
df = pd.read_csv("https://api.covidtracking.com/v1/states/ny/daily.csv")
newcases_week = df.positiveIncrease[:8]
#print(newcases_week)
lednum = 0
for i in range(7,0,-1):
    if newcases_week[i] > newcases_week[i-1]:
        pixels[lednum] = (255, 0, 0)
    else:
        pixels[lednum] = (0, 255, 0)
    lednum+=1

    #while True:
        
pixels.show()
time.sleep(30)
pixels.fill((0,0,0))
pixels.show()

'''except KeyboardInterrupt:
    pixels.fill((0,0,0))
    pixels.show()
'''
