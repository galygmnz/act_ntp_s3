import time  


minuto = 0
segundo = 0

while segundo < 60:
    print(f"{minuto:02d}:{segundo:02d}")
    
    time.sleep(1) 
    segundo += 1
