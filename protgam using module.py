#program using os module
#from os import* its for all
#import os
#listdir
#os.listdir(r"F:\videos") //it is use for find the list of give derctory datas
#os.path.join()
#os.remove("file path which u want to delete")

import os
names  = os.listdir(r"F:\videos") #where r is for becz here \ char is use
                                  #python may be confuse so using r char we say to the programm given in given path string is constant

print(names)


