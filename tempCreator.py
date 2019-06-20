from PIL import Image,ImageFont,ImageDraw

import qrcode


class CreateTemplate(object):
	def __init__(self):
		super(CreateTemplate, self).__init__()

	def resizeImg(self,imgFile,height,width):
		self.imageOpen = Image.open(imgFile)
		return self.imageOpen.resize((height, width), Image.ANTIALIAS)
#get all files required to generate output
	def getFiles(self):
		self.template_in = Image.open("inputs/AP0578 Front Template (Input).jpg")
		#'resizeImg' used to resize images before placing into template
		self.template_in.paste(self.resizeImg("inputs/Kamal.png",505,380), (510,850)) #Paste in Main image
		self.template_in.paste(self.resizeImg("inputs/Kamal.png",536,400), (2430,2630))
		self.template_in.paste(self.resizeImg("inputs/qrcode.png",410,410), (3380,760))
		#'generateImg used to fetch text file data and place in the template'
		return self.generateImg(self.template_in)

	def generateImg(self,template_in):
		draw = ImageDraw.Draw(self.template_in)
		fontsize=50
		fontsize1=145
		f = open("inputs/Variable Data.txt", "r")
		data_set = f.readlines() 
		f.close()
		for i, line in enumerate(data_set):
			if "Link" in line:
				link= line.split(':')
				self.linkForQr = link[1].replace('"', '')
				for j in data_set[i+2:i+3]:
					self.password=j

			if "Title" in line:
				link= line.split(':')
				self.title = link[1]			

		font = ImageFont.truetype("inputs/font/Coval-Regular.ttf", fontsize)
		font1 = ImageFont.truetype("inputs/font/tagetts2_U.ttf", fontsize1)
		draw.text((3400,1180),self.linkForQr,('Black'),font=font)
		draw.text((3350,1230),self.password,('Black'),font=font)
		draw.text((2000,3130),self.title,('Black'),font=font1)
		#calls 'createQrCode' to geneate QRcode with given link from text file.
		self.createQrCode(self.linkForQr)
		self.template_in.save('output/finalImage.png',dpi=(300, 300),quality=100)

	def createQrCode(self, linkForQr):
	    self.qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=5)
	    self.qr.add_data(self.linkForQr)
	    self.img = self.qr.make_image()
	    self.img.save("inputs/qrcode.png")


if __name__ == '__main__':
	T  = CreateTemplate()
	Files = T.getFiles()





	

   
