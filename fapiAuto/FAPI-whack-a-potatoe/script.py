import pyautogui, keyboard, win32gui, win32com.client

running, isHolding = False, False
startStopKey = "p"
gameTitle = 'Farmer Against Potatoes Idle'
activeWindow = win32gui.GetWindowText(win32gui.GetForegroundWindow())
gameWindow = win32gui.FindWindow(None, gameTitle)
rect = win32gui.GetWindowRect(gameWindow)

print("Starting WhackaMoler@1.0.1")
print(f"{startStopKey} - Start / Stop")
print("-" * 20)
print("🟩 Running" if running else "🛑 Stopped")

try:
  while True:
    activeWindow = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if keyboard.is_pressed(startStopKey) == True:
      if isHolding == False:
        isHolding = True
        print ("\033[A                             \033[A")
        print("🛑 Stopped" if running else "🟩 Running")
        running = not running
    else:
      isHolding = False

    if running and win32gui.GetWindowText(win32gui.GetForegroundWindow()) == gameTitle:
      location = pyautogui.locateOnScreen(
        image="img/eye.png",
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
  print(f'Stopped whack-a-moling')
