from cmd import Cmd

# nguIdle scripts
from nguIdle.bossSniper.bossSniper import bossSniper

# fapi scripts
from farmersAgainstPotatoes.whacker.whacker import whacker

pauseKey = 'p'
scriptList = {
  'nguIdle': ['bossSniper'],
  'farmersAgainstPotatoes': ['whacker']
}

class SubMenu(Cmd):
  prompt = '>> '

  def do_back(self, inp):
    '''Go back to previous menu'''
    return True

  def default(self, inp):
    if inp == 'q' or 'quit' or 'exit':
      return self.do_back(inp)

class NguMenu(SubMenu):
  def do_snipe(self, inp):
    '''Start sniping bosses in adventure mode'''
    bossSniper()

class FapiMenu(SubMenu):
  def do_whack(self, inp):
    '''Start whack-a-moling'''
    whacker()

nguMenu = NguMenu()
fapiMenu = FapiMenu()

class ScriptMenu(Cmd):
  prompt = '> '
  intro = f'Select category then script to run\n'

  def do_ngu(self, inp):
    '''Menu for NGUIdle scripts'''
    nguMenu.cmdloop(intro='Select ngu script')

  def do_fapi(self, inp):
    '''Menu for Farmers Against Potatoes Idle scripts'''
    fapiMenu.cmdloop(intro='Select fapi script')

  def do_exit(self, inp):
    '''Exit PyScripts, shortcut: q'''
    print(f'Exited script menu.', end='\r')
    return True

  def default(self, inp):
    if inp == 'q' or 'quit':
      return self.do_exit(inp)

scriptMenu = ScriptMenu()

if __name__ == '__main__':
  try:
    scriptMenu.cmdloop()
  except KeyboardInterrupt:
    print(f'\nInterrupted PyScripts.', end='\r')
