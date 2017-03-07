import numpy as np
import cv2
from PIL import Image
import pytesseract
import re
from difflib import SequenceMatcher


def enhanceImg(cv_img):
	
	# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# orig_img = cv2.equalizeHist(orig_img)

	# orig_img = cv2.cvtColor(orig_img,cv2.COLOR_GRAY2RGB)

	# orig_img = cv2.fastNlMeansDenoisingColored(orig_img,None,10,10,7,21)

	kernel = np.ones((5,5),np.uint8)
	# orig_img = cv2.erode(orig_img,kernel,iterations = 1)
	cv_img[cv_img<=200]=0
	cv_img[cv_img>200]=255
	print(cv_img.shape)
	(thresh, bw_img) = cv2.threshold(cv_img, 128, 255, cv2.THRESH_BINARY)
	cv2.imwrite('res.png',cv_img)
	return bw_img


def parseText(img):
	img = Image.fromarray(img)
	txt = pytesseract.image_to_string(img,lang='eng')
	# print(txt)
	return txt

def getTotalBill(text):
	# lineList = re.sub("[^\w]", "\n",  text).split()
	lineList = text.split("\n")
	# print(lineList)
	max_ratio=0.0
	billLine=""
	billWord=""
	for line in lineList:
		# wordList=re.sub("[^\w]", " ",  line).split()
		wordList=line.split(" ")
		for word in wordList:
			m = SequenceMatcher(None, word.lower(), "total")
			if m.ratio()>max_ratio:
				max_ratio=m.ratio()
				billLine=line
				billWord=word
	billLineList=billLine.split(billWord)
	billAmountStr=billLineList[len(billLineList)-1]
	return billAmountStr


def getBillInfo(inpImgPath):
	# print(inpImgPath)
	orig_img=cv2.imread(inpImgPath,0)
	bw_img=enhanceImg(orig_img)
	imgText=parseText(bw_img)
	totalBill=getTotalBill(imgText)
	return totalBill



if __name__=="__main__" :
	# print("kuch")
	imgname="sampleImages/sidecar-restaurant-e28093-018-restaurant-bill.jpg"
	totalBill=getBillInfo(imgname)
	print(totalBill)
