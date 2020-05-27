from flask import *  
from ISR.models import RDN
import numpy as np
from PIL import Image
#import re

app = Flask(__name__)  
 
#Homepage
@app.route('/')  
def upload():  
	return render_template("index.html")  
 
#Download Page
@app.route('/download', methods = ['POST'])  
def download():  
    if request.method == 'POST':  
        f = request.files['file']  
        
        img = Image.open(f)

        lr_img = np.array(img)
        model = RDN(weights='psnr-large')
        sr_img = model.predict(lr_img)
        out = Image.fromarray(sr_img)
        print("\nOutput resolution =",out.size,"\n")

        d=1
        while(out.size[1]/d>400):
        	d+=1

        out.save('images/HD_'+f.filename)		#Enhanced images are named HD_<filename>
        return render_template("download.html", name = '/images/HD_'+f.filename , y=out.size[0] , x=out.size[1], w=out.size[0]/d , h=out.size[1]/d)

#To GET image files
@app.route("/images/<string:str>")
def img(str):
	return send_file('images/'+str)

if __name__ == '__main__':  
    app.run()  