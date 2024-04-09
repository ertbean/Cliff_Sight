def cavemod():
      print('darkness covers the cave in a menasing way')
      print('you walk in sowly fearing for the worst')
      print('Bleep!')
      print('you hear a voice yelling at you' )
      print('"Welcome to Gobcave"')
      print('"Please choose a class"')
      print('"what race ...."')
      print('"Your a blobur!"')
      i = "I ma what!"
      e = "Of course i am"
      no_speak = "that is not a speak option"
      speak = input('press enter for options to speak')
      w = 2
      a = 2
      while w == 2 :
            speak1 = input('choose a speak option 1 "i ma what" 2 of course i am')
            if speak1.lower()== '1':
             print(i)
             w += 1 
             break
            else:
             if speak1.lower()== '2':
                  print(e)
                  a += 1
                  break
      if a == 3:
            print('I have just never seen one before')
            print('Wow!')
            print('you say"yes i am so list what a blobur is" ')
            print('" a blobur is very powerful creature because of its magical ability"') 
            print('"and its telekenesis up to a small range"')
            print('"And its amazing sight in battle"')
           
      else:
            if w == 3:
                  print('"your a blobur a very powerful creature because of its magical ability"')
                  print('"and its telekenesis up to a small range"')
                  print('"And its amzaing sight in battle"')
      print('as you hear the word sight you remember something')  
      print('like a vision')  
      print('you are in a room, where someones holding you')  
      print(' what will you call him') 
      name = input('it sounds like there going to call him')
      print('"so',name,'is my name" you say to your self') 
      wait = input('continue press y or enter to continue daydreaming')
      i = 1 
      while not wait.lower()== 'y':
           i += 1
           wait = input('continue press y or enter to continue daydreaming')
      while not wait.lower()== 'y':
       if wait.lower()== 'y': 
            break
       else:
            if i == 6:
                print('ert')
                
