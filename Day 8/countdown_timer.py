import time  
  
def countdown(c):      
    while c:  
        m, s = divmod(c, 60)  
        timer = '{:02d}:{:02d}'.format(m, s)  
        print(timer, end="\r")  
        time.sleep(1)  
        c -= 1       
    print('Fire in the hole!!')  

c = input("Enter the time value in seconds: ")  

countdown(int(c))  