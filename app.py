###where flask app will be generated


# -*- coding: utf-8 -*-


import os
from flask import Flask, render_template, request, redirect, session, url_for
import logging.config
from werkzeug import MultiDict
from flask_mail import Mail, Message
from form_contact import ContactForm #csrf
from flask_wtf.csrf import CSRFProtect

from flask_sslify import SSLify

app= Flask(__name__,static_url_path="",static_folder="static")

#app.config['SERVER_NAME'] = 'localhost:888'
sslify = SSLify(app, subdomains=True)

mail = Mail()
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
# csrf.init_app(app)
# csrf = CSRFProtect(app)
# csrf.init_app(app)
app.config['WTF_CSRF_ENABLED'] = False


#SESSION_COOKIE_SAMESITE = None # One of [None, 'Lax', 'Strict']
app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'aljazz.grachnar@gmail.com'
app.config['MAIL_PASSWORD'] = 'niffmkuyajczvipx'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] ='aljazz.grachnar@gmail.com'
# app.config.update( SESSION_COOKIE_NAME='MyApp-Session', )

mail.init_app(app)



@app.route('/', methods=['POST', 'GET'])

def index():
	
	title='Mlin Umetnin'

	######## portfolio pics selection ######
	path= "./static/images/home/portfolio"
	List_photo=[]
	path_list= "./static/images/gallery/"
	List_photo_names=[]
	desc_home_raw=[]
	desc_home=[]

	desc_path="./static/images/descriptions/home_pics_description.txt"


	file= open(desc_path,"r", encoding="utf-8")






##dont know yet if this is relevant to sort, if everything goes one after another
	for i in file:
		desc_home_raw.append(i)

	desc_home_raw.sort()

	for i in desc_home_raw:
		row=[]

		row.append(i.split(",")[1])
		row.append(i.split(",")[2])
		desc_home.append(row)
	# print(desc_home)



	for name in os.listdir(path_list):
		

		if os.path.isdir(os.path.join(path_list, name)):

			List_photo_names.append(name)
		else:
			pass

	List_photo_names.sort()






	for image in os.listdir(path):

		List_photo.append("/images/home/portfolio/"+image)


	List_photo.sort()
	
	# print('#######################################')
	# print(List_photo)
	# print('#######################################')



	######## contact form ############
	form = ContactForm()

	formdata = session.get('formdata', None)
	# print('#######################################')
	# print('#######################################')

	# print(session.get('csrf_token'))



	if formdata:
		form = ContactForm(MultiDict(formdata))
		form.validate()
		session.pop('formdata')

	if form.validate_on_submit() == True:
		print('-------------------------')
		print(request.form['name'])
		print(request.form['email'])
		print(request.form['message'])
		print('-------------------------')
		send_message(request.form)

		# return redirect(url_for('index', success=True))
		return redirect('/success')

	if form.is_submitted() and not form.validate():
		print('-------------------------')
		print('validate wrong')
		print('-------------------------')
		session['formdata'] = request.form
		return redirect('#contact')




	return render_template('main/home.html', title=title, form=form,List_photo=List_photo,desc_home=desc_home, List_photo_names=List_photo_names)





@app.route('/gallery/', methods=['POST', 'GET'])
def gallery():
	
	title='Mlin Umetnin-gallery'

	form = ContactForm()





	desc_gallery=description()


	# print(desc_gallery)




	######## gallery pics selection ######
	List_photo,Cov_photo,List_photo_names=gallery_pic_finder()
	#List_photo=gallery_pic_finder()
	
	# print('#######################################')
	# print(Cov_photo)
	# print('#######################################')
	# print(List_photo)
	# print('#######################################')



	return render_template('main/gallery.html', title=title, form=form, List_photo=List_photo, Cov_photo=Cov_photo,desc_gallery=desc_gallery, List_photo_names=List_photo_names)

@app.route('/about/', methods=['POST', 'GET'])

def about():
	title='Mlin Umetnin-about'
	form = ContactForm()


	return render_template('main/about.html', title=title, form=form)









@app.route('/gallery/<collection>/<image_no>', methods=['POST', 'GET'])
def single_photo(image_no, collection):
	title='Atelje Mlin Umetnin'
	form = ContactForm()



	desc_gallery= description()


	path_img= "/images/gallery/"+collection+"/"+image_no+".jpg"

		


	List_photo,Cov_photo,List_photo_names=gallery_pic_finder()
	# print(List_photo_names)
	# print(collection)


	colection_index = List_photo_names.index(collection)
	pic_index= List_photo[colection_index].index(path_img)

	no_colections=len(List_photo_names)
	no_pic=len(List_photo[colection_index])
	print('§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')
	# print(no_colections)
	# print(no_pic)
	# print(colection_index)
	# print(pic_index)
	# print('§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')
	# print(desc_gallery)
	# print('§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')
	# print(desc_gallery[colection_index][pic_index][3])
	# print('§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')


	exit_path="/gallery/#"+collection

	if pic_index==0:
		# print('blah 210')
		pic_pre= List_photo[colection_index-1][len(List_photo[colection_index-1])-1]
	else:
		pic_pre= List_photo[colection_index][pic_index-1]



	try:

		pic_after= List_photo[colection_index][pic_index+1]
	except:
		if (colection_index+1)==no_colections:
			pic_after= List_photo[0][0]
			# print('blah 216')

		else:
			# print('blah 219')

			pic_after= List_photo[colection_index+1][0]










	return render_template('main/gallery_view.html', title=title, form=form, path_img=path_img, pic_pre=pic_pre,pic_after=pic_after,desc_gallery=desc_gallery, pic_index=pic_index, colection_index=colection_index, exit_path=exit_path)


@app.route('/success', methods=['GET'])
def success():

	return render_template('main/send_success.html')




@app.errorhandler(404) 
def not_found(e):
  
	return redirect('/')

@app.errorhandler(500) 
def not_found(e):
  
	return redirect('/')



def description():

	desc_files=[]

	desc_gallery=[]

	desc_path="./static/images/descriptions/gallery/"

	coll_inex_desc=0
	for name_ in os.listdir(desc_path):
		desc_files.append(name_)
	desc_files.sort()

	for name in desc_files:
		desc_gallery_raw=[]

		desc_gallery.append([])

		path= desc_path+name

		# print(path)
		file= open(path, "r" , encoding="utf-8")
		

####################################################

	#dont know yet if this is relevant to sort, if everything goes one after another
		for i in file:
			# print('§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')
			# print('§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')
			# print(i)
			# print('§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')
			# print('§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')
			desc_gallery_raw.append(i)
		# print(desc_gallery)
		# print("dreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeekkkkkk")

		# desc_gallery_raw.sort()
		# print(desc_gallery)

		for j in desc_gallery_raw:
			row=[]

			for  k in j.split(";"):

			
				row.append(k)

			desc_gallery[coll_inex_desc].append(row)
		# desc_gallery[coll_inex_desc].sort()

		coll_inex_desc=coll_inex_desc+1

	# desc_gallery.sort()


	return desc_gallery





def gallery_pic_finder():


	path= "./static/images/gallery/"
	List_photo=[]
	List_photo_names=[]
	Cov_photo=[]
	
	a=0
	
	for name in os.listdir(path):
		

		if os.path.isdir(os.path.join(path, name)):

			List_photo.append([])
			List_photo_names.append(name)

			for image in os.listdir(os.path.join(path, name)):

				List_photo[a].append("/images/gallery/"+name+"/"+image)

			List_photo[a].sort()

			a=a+1
		else:
			Cov_photo.append("/images/gallery/"+name)

	List_photo.sort()
	List_photo_names.sort()
	Cov_photo.sort()

	return List_photo, Cov_photo,List_photo_names





def send_message(message):
    name = message.get('name')
    email =message.get('email')
    text = message.get('message')

    msg = Message(subject=message.get('email'),
    		recipients = ['mlinumetnin@gmail.com'],
            body= "You have received a new feedback from {} <{}>.\n \n Sporočilo: {}".format(name, email, text)        
            
    )  
    mail.send(msg)





logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

if __name__ == '__main__':
    app.run(debug=True)