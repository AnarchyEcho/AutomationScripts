import pyautogui, time, keyboard, win32gui, pathlib

def bossSniper():
  print('Press ctrl+c to quit.')
  LINE_CLEAR = '\x1b[2K'
  boss = False
  basePath = 'F:/Code_projects/pyScripts/nguIdle/bossSniper/'
  print(f'Awaiting game.', end='\r', flush=True)

  try:
    while True:
      if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == 'NGU Idle':
        rect = win32gui.GetWindowRect(win32gui.FindWindow(None, 'NGU Idle'))
        if pyautogui.locateOnScreen(f'{basePath}img/adventuretab.png', region=rect, confidence=0.8, grayscale=True):

          try:
            if pyautogui.locateOnScreen(f'{basePath}img/bossicon.png', region=rect, confidence=0.8) != None:
              boss = True
              print(f'Killing boss.', end='\r', flush=True)
              print(end=LINE_CLEAR)
          except:
            continue

          try:
            if pyautogui.locateOnScreen(f'{basePath}img/noenemy.png', region=rect, confidence=0.8) != None:
              boss = False
              print(f'Waiting for enemy.', end='\r', flush=True)
              print(end=LINE_CLEAR)
          except:
            continue

          try:
            if pyautogui.locateOnScreen(f'{basePath}img/noenemy.png', region=rect, confidence=0.8) == None and not boss:
              print(f'Skipping normal mob.', end='\r', flush=True)
              keyboard.send('left')
              time.sleep(0.1)
              keyboard.send('right')
              time.sleep(0.1)
              print(end=LINE_CLEAR)
          except:
            continue

        else:
          print(f'Waiting for adventure tab.', end='\r', flush=True)
          print(end=LINE_CLEAR)
      else:
        boss = False
  except KeyboardInterrupt:
    print(f'Stopped boss sniping.', end='\n', flush=True)

if __name__ == '__main__':
  bossSniper()
