#import app #import the module
#app.hello()
#app.bye()

#import app as msg #name the module that you imported
#msg.bye()
#msg.bye()

#from app import hello, bye #import the functions that you NEEDED from module
#hello()
#bye()

from app import * #import ALL the functions from the module
hello()
bye()

help("modules") #prints all the built-in module