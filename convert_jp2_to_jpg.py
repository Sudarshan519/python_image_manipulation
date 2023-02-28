import os
import cv2
# Folder Path
path = "/Users/user/Downloads/Cards-2/Residence Card/" #"/Users/user/Downloads/Cards-2/MyNumberCard/" #"/Users/user/Downloads/Cards-2/Driving License/" 

# 
path_to_converted= path+"converted/"
# Change the directory
os.chdir(path)
  
# Read text File

if not os.path.exists(path_to_converted):
    os.makedirs(path_to_converted)

for file in os.listdir():

    if file.endswith(".jp2"):
        
        data=(file.split('.')[0])
        # Convert
        image = cv2.imread(file)
        cv2.imwrite(path_to_converted+data+'.jpg', image)


tilted=path_to_converted+"tilted/"
front=path_to_converted+"front/"
back=path_to_converted+"back/"
folders=[tilted,front,back]

for a in folders:
    if not os.path.exists(a):
        os.makedirs(a)

 
 
# Change the directory
os.chdir(path_to_converted)
for file in os.listdir():
     
    if os.path.isfile(path_to_converted+file):
        data=list(file.split(".")[0])
        if(data!=[]):
            
            check=(data.pop())
            if check=='a':
                os.replace(path_to_converted+file,front+file)
            elif check=='b':
                os.replace(path_to_converted+file,back+file)
            else:
                os.replace(path_to_converted+file,tilted+file)

    # if(data[1]=='a'):
    #     print("front")
    # elif data[1]=='b':
    #     print("back")
    # else :
    #     print("tilted")
 