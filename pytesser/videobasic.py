import cv2 as cv
import pytesseract as tess
import numpy as np
import re
tess.pytesseract.tesseract_cmd=r"C:/Program Files/Tesseract-OCR/tesseract.exe"

cap=cv.VideoCapture("C:/Users/Turing/Downloads/ipl Basics.mp4")

def find_score(img):
    score_position=img[635:675,385:492]
    score_position = np.pad(score_position, ((5, 5), (5, 5)), "constant", constant_values=255)
    _, score_thresh = cv.threshold(score_position, 20, 255, cv.THRESH_BINARY)
    score_final=tess.image_to_string(score_thresh)

    score_f=re.search("[0-9]*[-]",score_final)
    if(score_f):
        runs=score_final[score_f.span()[0]:score_f.span()[1]-1]
        wicket=score_final[score_f.span()[1]:score_f.span()[1]+1]
        return runs,wicket
    return -1,-1

def find_over(img):
    over_position=img[666:690,240:360]
    over_position=255-over_position
    overs_position = np.pad(over_position, ((5, 5), (5, 5)), "constant", constant_values=255)
    _, over_thresh = cv.threshold(overs_position, 30, 255, cv.THRESH_BINARY)
    overs=tess.image_to_string(over_thresh)
    over=re.search("[0-9]*[.,]",overs)

    if(over):
        overs_com=overs[over.span()[0]:over.span()[1]-1]
        balls=overs[over.span()[1]:over.span()[1]+1]
        return overs_com,balls
    return -1,-1

def get_batsmen(img):
    player1 = img[629:652, 529:640]
    player2 = img[666:686, 529:640]

    player1 = np.pad(player1, ((7, 7), (7, 7)), "constant", constant_values=255)
    player2 = np.pad(player2, ((7, 7), (7, 7)), "constant", constant_values=255)

    _, player1 = cv.threshold(player1, 60, 255, cv.THRESH_BINARY)
    _, player2 = cv.threshold(player2, 60, 255, cv.THRESH_BINARY)

    player1=tess.image_to_string(player1)
    player2=tess.image_to_string(player2)

    if(player1[-1]=='*' or player1[-1]=='"'):
        on_strike=player1[:-1]
        other_side=player2
    else:
        on_strike=player2[:-1]
        other_side=player1
    return on_strike,other_side


prev_score=-1

while(cap.isOpened()):
    _,frame=cap.read()
    cv.imshow("Video Stream", frame)
    frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    score,wicket=find_score(frame)
    overs,balls=find_over(frame)
    on_strike,other_side=get_batsmen(frame)

    if(cv.waitKey(1) ==ord('q')):
        break
    if(prev_score!=score and score!="-1"):
        print("The Score is {} for {} wickets".format(score, wicket))
        print("The Number of Overs is {} and {} balls is completed".format(overs, balls))
        print("{} is on the strike".format(on_strike))
        prev_score = score
    else:
     continue
cap.release()
cv.destroyAllWindows()