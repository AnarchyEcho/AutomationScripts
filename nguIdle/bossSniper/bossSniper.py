from msvcrt import getch, kbhit
from os.path import dirname, join, abspath
from dotenv import dotenv_values
import pyautogui, time, keyboard, win32gui

def bossSniper():
  LINE_CLEAR = '\x1b[2K'
  boss = False
  absoPath = dirname(dirname(dirname(abspath(__file__))))
  basePath = f'{dotenv_values(join(absoPath, ".env"))["NGUPATH"]}/bossSniper/'
  print(f'{LINE_CLEAR}Awaiting game.', end='\r', flush=True)

  try:
    while True:
      if kbhit():
        key = ord(getch())
        if key == 113:
          break

      if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == 'NGU Idle':
        rect = win32gui.GetWindowRect(win32gui.FindWindow(None, 'NGU Idle'))
        if pyautogui.locateOnScreen(f'{basePath}img/adventuretab.png', region=rect, confidence=0.8, grayscale=True):

          try:
            if pyautogui.locateOnScreen(f'{basePath}img/bossicon.png', region=rect, confidence=0.8) != None:
              boss = True
              print(f'{LINE_CLEAR}Killing boss.', end='\r', flush=True)
          except:
            continue

          try:
            if pyautogui.locateOnScreen(f'{basePath}img/noenemy.png', region=rect, confidence=0.8) != None:
              boss = False
              print(f'{LINE_CLEAR}Waiting for enemy.', end='\r', flush=True)
          except:
            continue

          try:
            if pyautogui.locateOnScreen(f'{basePath}img/noenemy.png', region=rect, confidence=0.8) == None and not boss:
              print(f'{LINE_CLEAR}Skipping normal mob.', end='\r', flush=True)
              keyboard.send('left')
              time.sleep(0.1)
              keyboard.send('right')
              time.sleep(0.1)
          except:
            continue

        else:
          print(f'{LINE_CLEAR}Waiting for adventure tab.', end='\r', flush=True)
      else:
        boss = False
  except KeyboardInterrupt:
    print(f'{LINE_CLEAR}', end='\r')

if __name__ == '__main__':
  bossSniper()
