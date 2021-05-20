### Thread
###### 패키지 이름은 threading인데 일정 시간마다 (00초, 00분) 함수를 실행하여 반복 동작이 이뤄짐. 패키지는 pip로 다운로드 받아야한다.

	import time
    import threading
    
    def printHello():
    	print("Hello")
        threading.Timer(5, printHello).start()
        
	printHello
    
    
### Schedule
###### 패키지 이름이 schedule이다. 특정 날짜에 실행되게끔 할 수 있다. 패키지는 pip로 다운로드 받아야한다.

	import time
    import schedule
    
    def printHello():
    	print("Hello")
        
	schedule.every(30).minutes.do(printHello) #매30분마다 
    schedule.every().monday.at('00:10').do(printHello) #월요일 00시10분
    schedule.every().day.at('10:30').do(job) #매일 10시30분
    
	while True:
    	schedule.run_pending()
        time.sleep(1)