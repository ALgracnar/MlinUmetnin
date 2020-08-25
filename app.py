###where flask app will be generated

from flask import Flask, render_template
import logging.config
import smtplib



app= Flask(__name__,static_url_path="",static_folder="static")
#app.config['SERVER_NAME'] = 'localhost:888'

@app.route('/')
def index():

    title='Mlin Umetnin'
    return render_template('index.html', title=title)

#@app.route('/contact')
#def contact():
#    title = 'Mlin Umetnin-Contact'
#    return render_template('contact.html', title=title)


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

if __name__ == '__main__':
    app.run()