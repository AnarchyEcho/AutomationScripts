import pyautogui, time, keyboard, win32gui

print('Press ctrl+c to quit.')
LINE_CLEAR = '\x1b[2K'

try:
  while 1:
    if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == 'NGU Idle':
      rect = win32gui.GetWindowRect(win32gui.FindWindow(None, 'NGU Idle'))
      try:
        if pyautogui.locateOnScreen('img/adventuretab.png', region=rect, confidence=0.8) is not None:
            try:
              if pyautogui.locateOnScreen('img/bossicon.png', region=rect, confidence=0.8) is not None:
                print(f'Killing boss.', end='\r', flush=True)
                time.sleep(0.5)
                print(end=LINE_CLEAR)
            except pyautogui.ImageNotFoundException:
              try:
                if pyautogui.locateOnScreen('img/noenemy.png', region=rect, confidence=0.8) is not None:
                  print(f'Waiting for enemy.', end='\r', flush=True)
                  time.sleep(0.5)
                  print(end=LINE_CLEAR)
              except pyautogui.ImageNotFoundException:
                print(f'Skipping normal mob.', end='\r', flush=True)
                keyboard.send('left')
                time.sleep(0.1)
                keyboard.send('right')
                time.sleep(0.5)
                print(end=LINE_CLEAR)
      except pyautogui.ImageNotFoundException:
        print(f'Waiting for adventure tab.', end='\r', flush=True)
        time.sleep(2)
        print(end=LINE_CLEAR)
except KeyboardInterrupt:
  print(f'Stopped boss sniping.', end='\r', flush=True)
