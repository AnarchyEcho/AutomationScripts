import pyautogui, win32gui

gameTitle = 'Farmer Against Potatoes Idle'
gameWindow = win32gui.FindWindow(None, gameTitle)
rect = win32gui.GetWindowRect(gameWindow)

pyautogui.screenshot(
    imageFilename="img/region_test.png",
    region=rect
)
