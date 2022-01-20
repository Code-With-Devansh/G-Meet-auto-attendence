from PyPDF2 import PdfFileWriter, PdfFileReader
import webbrowser
import pyautogui
import time
import keyboard
import threading
import os
from PIL import ImageGrab, Image
def keyCheck():
    keyboard.wait("ctrl+c")
    pyautogui.alert("Program terminated!")
    os._exit(1)
meetingID = open(r'F:\Visual Studio\Python\BotToAttendGmeet\meetlink.txt').read() 
if meetingID == '':
    meetingID = pyautogui.prompt(text='Enter your meeting link', title='Meeting link', default='')
link = "<liNk>?authuser=1"
meetingID = link.replace('<liNk>', meetingID)
chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chromePath))
webbrowser.get('chrome').open_new_tab(meetingID)
keycheck = threading.Thread(target=keyCheck, name="KeyCheck")
keycheck.daemon = True
keycheck.start()
def isLoaded():
    while True:
        time.sleep(1)
        img = ImageGrab.grab()
        if img.getpixel((948, 412)) == (26, 115, 232):
            return
time.sleep(1)
isLoaded()
time.sleep(2)
pyautogui.hotkey('ctrl', 'd')
pyautogui.hotkey('ctrl', 'e')
pyautogui.click(946, 396)
def checkJoined():
    while True:
        time.sleep(1)
        img = ImageGrab.grab().convert('L')
        dat = img.load()
        if dat[740, 695] < 150:
            return True
checkJoined()
time.sleep(3)
pyautogui.hotkey('ctrl', 'alt', 'p')
time.sleep(1.5)
pyautogui.hotkey('ctrl', 'p')
time.sleep(4)
for i in range(5):
    pyautogui.press('tab')
    time.sleep(0.1)
pyautogui.press('enter')
time.sleep(0.5)
img = ImageGrab.grab().convert('L')
dat = img.load()
if dat[1071, 194] > 200:
    pyautogui.click(1071, 194)
pyautogui.click(935, 335)
time.sleep(0.2)
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.click(973, 429)
pyautogui.click(1010, 672)
time.sleep(4)
pyautogui.click(330, 53)
time.sleep(0.3)
pyautogui.typewrite(r"F:\Visual Studio\Python\BotToAttendGmeet")
pyautogui.press('enter')
time.sleep(0.3)
pyautogui.click(369, 374)
run = ""
pyautogui.typewrite(f"BOT")
time.sleep(0.3)
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(740, 682)
pyautogui.hotkey('ctrl', 'f4')
printtedfilePath = os.path.join(r'F:\Visual Studio\Python\BotToAttendGmeet',f"BOT.pdf")
pdf = PdfFileReader(printtedfilePath)
page = pdf.getPage(0)
page.mediaBox.lowerRight = (2350, 70)
page.mediaBox.upperLeft = (2050, 3350)
output = PdfFileWriter()
output.addPage(page)
fileName = 'Att.pdf'
open(fileName, 'w').close()
with open(fileName, 'wb') as f:
    output.write(f) 
os.rename('F:\Visual Studio\Python\BotToAttendGmeet\Att.pdf', f'F:\Visual Studio\Python\BotToAttendGmeet\Attendence_Log\Att_{time.strftime("%d%m_%H%M")}.pdf')
fileNam = f'Att_{time.strftime("%d%m_%H%M")}.pdf'
urL = f'file:///F:/Visual%20Studio/Python/BotToAttendGmeet/Attendence_Log/{fileNam}'
chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chromePath))
webbrowser.get('chrome').open_new_tab(urL)
exit()