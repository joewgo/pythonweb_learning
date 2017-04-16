import random
try:

 you_choice = int(input('是否開始猜拳？0.不想玩，離開 or 1. 開始猜拳 '))
#剪刀:0 石頭:1 布:2
 while you_choice == 1:
  computer_choice = random.randint(0,2)
  the_choice = int(input('請問要出？0.剪刀 1.石頭 2.布'))
    
  if the_choice == 0:
      print('你出的是「剪刀」！')
      if computer_choice == 0:
        print('電腦也出「剪刀」！，平手')
      elif computer_choice == 1:
        print('電腦出「石頭」！，你輸了！')
      elif computer_choice == 2:
        print('電腦出「布」！，太棒了，你勝利了！')
        
        
  if the_choice == 1:
      print('你出的是「石頭」！')
      if computer_choice == 0:
        print('電腦出「剪刀」！，太棒了，你勝利了！')
      elif computer_choice == 1:
        print('電腦也出「石頭」！，平手！')
      elif computer_choice == 2:
        print('電腦出「布」！，你輸了！')
        
        
  if the_choice == 2:
      print('你出的是「布」！')
      if computer_choice == 0:
        print('電腦出「剪刀」！，你輸了！')
      elif computer_choice == 1:
        print('電腦出「石頭」！，太棒了，你勝利了！')
      elif computer_choice == 2:
        print('電腦也出「布」！，平手！')
  

 print('剪刀、石頭、布，程式結束')

except ValueError:
  print("請輸入數字")

  