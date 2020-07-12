"""closure function: if we delete function then  clourse
function still hold the value of that function"""

def print__msg(msg):
    def printer():
        print(msg)
        return printer
    another=print__msg("hello")
    another()

        #printer()
        #print_msg("hello")




#def print_msg(msg):
 #   def printer():
  #      print(msg)

    #    printer()
     #   print_msg("hello")
