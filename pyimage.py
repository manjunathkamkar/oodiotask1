from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

import qrcode

def createQrCode(url):
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=5)
    qr.add_data(url)
    img = qr.make_image()
    img.save("qrcode.png")
    
def resizeImg(imgFile,height,width):
	imageOpen = Image.open(imgFile)
	return imageOpen.resize((height, width), Image.ANTIALIAS)

def drawImg(ImgDraw):
	draw = ImageDraw.Draw(ImgDraw)
	fontsize=40
	fontsize1=200
	f = open("Variable Data.txt", "r")
	searchlines = f.readlines()
	f.close()
	linkForQr =''
	for i, line in enumerate(searchlines):
	    if "Link" in line:
	    	link = line.split(':')
	    	linkForQr = link[1].replace('"', '')
	    	for l in searchlines:
	            mytext=l
	            print
	for j, line in enumerate(searchlines):
	            if "Link" in line:
	                for g in searchlines[j+2:j+3]:
	                    mytext2=g
	                    print

	font = ImageFont.truetype("font/Coval-Regular.ttf", fontsize)
	draw.text((3400,1200),linkForQr,('Black'),font=font)
	draw.text((3350,1250),mytext2,('Black'),font=font)
	createQrCode(linkForQr)

	ImgDraw.save('output/finalImage.png',dpi=(300, 300),quality=100)
	ImgDraw.show()
	

def main():

	new_im = Image.open("AP0578 Front Template (Input).jpg")
	# right bottom corner 3,3,1,1      
	new_im.paste(resizeImg("Kamal.png",450,450), (550,800)) #Paste in Main image
	new_im.paste(resizeImg("LogoWithName.png",1400,900), (2000,2500))
	new_im.paste(resizeImg("qrcode.png",420,420), (3350,800))
	drawImg(new_im)


main()








	

   
