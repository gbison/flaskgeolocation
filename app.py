import urllib

from flask import Flask, render_template, request, jsonify, redirect

from api.apiController import get_data

from models.mainman import mailman

app = Flask(__name__)

pageTitle = "GEOLOC APP"


# Pages
@app.route('/', methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Run Map') == 'Run Map':
            # pass
            print("POST: Running map...")
            data = get_data()
            mailsys = mailman()
            mailsys.mail_setup()
            if mailsys.mail_login():
                mymsg = mailsys.build_mail()
                mymsg.set_from('hennesygts@gmail.com')
                mymsg.set_to('hennesygts@gmail.com')
                mymsg.set_subject('JSON Payload Data')
                mymsg.set_msg(str(data))
                mailsys.mail_send(mymsg.msg)
                mailsys.smtp.close()
            return redirect(data[1].mapURL)
    elif request.method == 'GET':
        print("No postback, rendering base....")
    return render_template("home.html", data=get_data())
    # return render_template("home.html", data=get_my_ip())


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


# Endpoints
# app.add_url_rule('/get_my_ip', 'getIP', get_data)

if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True)


