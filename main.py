from msvcrt import kbhit, getch
import sys

# nguIdle scripts
from nguIdle.bossSniper.bossSniper import bossSniper

# fapi scripts
from farmersAgainstPotatoes.whacker.whacker import whacker

LINE_CLEAR = '\x1b[2K'
pauseKey = 'p'
scriptDict = {
  'nguIdle': ['bossSniper', 'test'],
  'farmersAgainstPotatoes': ['whacker']
}
scriptDict_i = list(scriptDict.keys())

def main():
  print('Select category then script to run.', end='\n\r')
  print('Press Q to exit, or go back to menu from category.', end='\n\n\r')

  curText = ''
  level = 0
  def newText(arr):
    match level:
      case 0:
        curText = '> ' + f''.join(f'{f"[ {key} ]" if i == selected else key} ' for i, key in enumerate(arr))
        print(f'{LINE_CLEAR}{curText}', end='\r', flush=True)
      case 1:
        curText = '>> ' + f''.join(f'{f"[ {key} ]" if i == selected else key} ' for i, key in enumerate(arr))
        print(f'{LINE_CLEAR}{curText}', end='\r', flush=True)

  selected = 0
  prevSelected = selected
  newText(scriptDict.keys())

  while True:
    if kbhit():
      key = ord(getch())

      match key:
        case 13:
          '''Enter'''
          match level:
            case 0:
              level = level + 1 if level == 0 else level
              prevSelected = selected
              selected = 0
              newText(scriptDict[scriptDict_i[prevSelected]])
            case 1:
              print(f'{LINE_CLEAR}{scriptDict[scriptDict_i[prevSelected]][selected]}', end='\r')

        case 75:
          '''Left arrow'''
          match level:
            case 0:
              selected = selected - 1 if selected != 0 else 0
              newText(scriptDict)
            case 1:
              selected = selected - 1 if selected != 0 else 0
              newText(scriptDict[scriptDict_i[prevSelected]])
        case 77:
          '''Right arrow'''
          match level:
            case 0:
              selected = selected + 1 if selected != (len(scriptDict) - 1) else selected
              newText(scriptDict.keys())
            case 1:
              selected = selected + 1 if selected != (len(scriptDict[scriptDict_i[prevSelected]]) - 1) else selected
              newText(scriptDict[scriptDict_i[prevSelected]])

        case 113:
          '''Q'''
          match level:
            case 0:
              print(f'\nExited script menu.', end='\r')
              sys.exit()
            case 1:
              level = 0
              selected = prevSelected
              newText(scriptDict.keys())

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print(f'\nInterrupted PyScripts.', end='\r')
