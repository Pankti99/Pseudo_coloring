

import cv2


def read_img_medical(sn):

        s = cv2.imread('E:/msc AI/pseudocoloring/source/Medical/'+str(sn)+".jpg")
        return s
    
def read_img_satellite(sn):

        s = cv2.imread('E:/msc AI/pseudocoloring/source/Satellite/'+str(sn)+".jpg")
        return s
    
    
    
def color():
    countm=0
    counts=0
#    sources_med = ['s1','s2','s3','s4','s5','s6']
#    sources_set =  ['s1','s2','s3','s4','s5']
    sources_med = ['s1']
    sources_set =  ['s4']
    
    for i in range(0,len(sources_med)):
        print("Medical Converting picture"+str(i+1)+"...")
        m = read_img_medical(sources_med[i])
        cv2.imshow("Gray Image",m)
        cv2.waitKey(0)
        im_color1 = cv2.applyColorMap(m, cv2.COLORMAP_JET)
        im_color2 = cv2.applyColorMap(m, cv2.COLORMAP_PARULA)
        im_color3 = cv2.applyColorMap(m, cv2.COLORMAP_PLASMA)
        countm+=1
        cv2.imwrite('E:/msc AI/pseudocoloring/output/Medical/j'+str(countm)+'.jpg',im_color1)
        cv2.imwrite('E:/msc AI/pseudocoloring/output/Medical/p'+str(countm)+'.jpg',im_color2)
        cv2.imwrite('E:/msc AI/pseudocoloring/output/Medical/o'+str(countm)+'.jpg',im_color3)
        cv2.imshow("color",im_color2)
        cv2.waitKey(0)
        
        cv2.imshow("color",im_color1)
        cv2.waitKey(0)
  
        cv2.imshow("color",im_color3)
        cv2.waitKey(0)
      
        
        
    for i in range(0,len(sources_set)):
        print("Satellite Converting picture"+str(i+1)+"...")
        s = read_img_satellite(sources_set[i])
        cv2.imshow("Gray Image",s)
        cv2.waitKey(0)
        im_color1 = cv2.applyColorMap(s, cv2.COLORMAP_VIRIDIS)
        im_color2 = cv2.applyColorMap(s, cv2.COLORMAP_TWILIGHT_SHIFTED)
        im_color3 = cv2.applyColorMap(s, cv2.COLORMAP_TURBO)
        counts+=1
        cv2.imwrite('E:/msc AI/pseudocoloring/output/Satellite/j'+str(counts)+'.jpg',im_color1)
        cv2.imwrite('E:/msc AI/pseudocoloring/output/Satellite/p'+str(counts)+'.jpg',im_color2)
        cv2.imwrite('E:/msc AI/pseudocoloring/output/Satellite/r'+str(counts)+'.jpg',im_color3)
        
        
        cv2.waitKey(0)
        cv2.imshow("color",im_color2)
        cv2.waitKey(0)
        cv2.imshow("color",im_color1)
        cv2.waitKey(0)
        cv2.imshow("color",im_color3)
        cv2.waitKey(0)
        cv2.destoryAllWindows()

color()
























