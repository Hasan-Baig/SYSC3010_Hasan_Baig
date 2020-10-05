from sense_hat import SenseHat
import time

sense = SenseHat()
  
sense.clear()

#selection helps switch between letters every loop
selection = False     

while True: 
  events = sense.stick.get_events()
  for event in events:
    if event.action == "pressed":
      if selection == False:
        # Show first intial 
        sense.show_letter("A")
        selection = True
      else:
        # Show last intial
        sense.show_letter("B")
        selection = False