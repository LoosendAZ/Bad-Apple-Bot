import cv2 
  
def FrameCapture(path): 
    
    vidObj = cv2.VideoCapture(path) 
    
    count = 0
    
    success = 1
  
 while success: 
        if count % 3 == 0:
            success, image = vidObj.read() 
            cv2.imwrite("C:\\Users\\aiden\\Downloads\\bad-apple-bot-main\\bad-apple-bot-main\\frames\\frame%d.png" % count, image)
            
if __name__ == '__main__': 

    FrameCapture('C:\\Users\\aiden\\Downloads\\bad-apple-bot-main\\bad-apple-bot-main\\frames\\bad_apple.mp4')
