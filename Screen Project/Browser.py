import time,webbrowser, pyautogui
count=0
while 1:
	search=input("Search String: ")
	webbrowser.open("https://www.google.co.in/search?q="+search)
	count=count+1
	time.sleep(1)
	spyautogui.hotkey('ctrl','num1')
		
	print("tab closed")

print(count)
