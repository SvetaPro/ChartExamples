import math 
 
message = "10 лет вместе Поздравляю с твоим днем День программиста 256!" 
 
def draw_heart(message): 
    for y in range(-10, 10): 
        for x in range(-30, 30): 
            if ((x * 0.04)**2 + (y * 0.1)**2 - 1)**3 - (x * 0.04)**2 * (y * 0.1)**3 <= 0: 
                print(message[(x - y) % len(message)], end='') 
            else: 
                print(' ', end='') 
        print() 
 
draw_heart(message)
