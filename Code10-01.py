from tkinter import *

##전역 변수 선언 부분##
window=None
canvas=None
XSIZE, YSIZE = 9999, 9999
inImage=[]
filename=''


## 함수 선언 부분 ##

## 파일 메뉴 아래 열기와 종료 하위 메뉴 함수 ##
def fileopen() :
    global filename

    filename = 'C:/Users/robot/OneDrive/바탕 화면/tree.fff'

    global inImage, XSIZE, YSIZE
    fp = open(filename, 'rb')

    for i in range(0, XSIZE) :
        tmpList = []
        for k in range(0, YSIZE) :
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)

    fp.close()
    displayImage(inImage)

def displayImage(image) :
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE) :
        tmpString = ""
        for k in range(0, YSIZE) :
            data = image[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data)
        rgbString += "{" + tmpString +  "} "
    paper.put(rgbString)

    canvas.pack()
    window.mainloop()

def exit() :
    window.quit()
    window.destroy()

## 사진 효과 메뉴 아래 밝게하기와 어둡게하기와 반전이미지 하위 메뉴 있는 코드 ##

def bright(image):
    global inImage, XSIZE, YSIZE

    for i in range(0, XSIZE):
        for k in range(0, YSIZE):
            data = inImage[i, k] + 100

    displayImage(inImage)

def dark(image):
    global inImage, XSIZE, YSIZE

    for i in range(0, XSIZE):
        for k in range(0, YSIZE):
            data = inImage[i, k] - 100

    displayImage(inImage)

def reverse(image):
    global inImage, XSIZE, YSIZE
    for i in range(0, XSIZE):
        for k in range(0, YSIZE):
            data = inImage[i][k]
            newdata = 255 - data
            inImage[i][k] = newdata

    displayImage(inImage)


## 메인 코드 부분 ##
window = Tk()
window.title("사진 보기")
canvas = Canvas(window, height = XSIZE, width = YSIZE)
paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image = paper, state = "normal")

## 파일 메뉴 아래 열기와 종료 하위 메뉴 있는 코드 ##

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=fileopen)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=quit)

## 사진 효과 메뉴 아래 밝게하기와 어둡게하기와 반전이미지 하위 메뉴 있는 코드 ##
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="사진효과", menu=fileMenu)
fileMenu.add_command(label="밝게하기", command=bright)
fileMenu.add_separator()
fileMenu.add_command(label="어둡게하기", command=dark)
fileMenu.add_separator()
fileMenu.add_command(label="반전 이미지", command=reverse)
