from msvcrt import kbhit, getch
import pyautogui, keyboard, win32gui, win32com.client, pathlib

def whacker():
  LINE_CLEAR = '\x1b[2K'
  running, isHolding = False, False
  startStopKey = "p"
  gameTitle = 'Farmer Against Potatoes Idle'
  activeWindow = win32gui.GetWindowText(win32gui.GetForegroundWindow())
  gameWindow = win32gui.FindWindow(None, gameTitle)
  rect = win32gui.GetWindowRect(gameWindow)
  basePath = 'F:/Code_projects/pyScripts/farmersAgainstPotatoes/whacker/'

  print(f'{LINE_CLEAR}Press {startStopKey} to {"PAUSE" if running else "START"}', end='\r')

  try:
    while True:
      if kbhit():
        key = ord(getch())
        if key == 113:
          break

      activeWindow = win32gui.GetWindowText(win32gui.GetForegroundWindow())
      if keyboard.is_pressed(startStopKey) == True:
        print(f'{LINE_CLEAR}Press {startStopKey} to {"PAUSE" if running else "START"}', end='\r')
        if isHolding == False:
          isHolding = True
          running = not running
      else:
        isHolding = False

      if running and win32gui.GetWindowText(win32gui.GetForegroundWindow()) == gameTitle:
        location = pyautogui.locateOnScreen(
          image=f"{basePath}img/eye.png",
          confidence=0.8,
          region=rect,
          grayscale=True
        )

        if location:
          pyautogui.click(location)
      if running and activeWindow != gameTitle:
        win32com.client.Dispatch("WScript.Shell").SendKeys('%')
        win32gui.SetForegroundWindow(gameWindow)
  except KeyboardInterrupt:
    print(f'{LINE_CLEAR}', end='\r')

if __name__ == '__main__':
  whacker()
