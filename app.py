from flask import Flask, render_template, request, redirect

import apiController
import mainman

app = Flask(__name__)

pageTitle = "PYGEO APP"

DEBUG = False


# Pages
@app.route('/', methods=['GET', 'POST'])
def home():
    print('Request Method: ' + request.method)
    data = apiController.get_data()
    if request.method == 'POST':
        if request.form.get('Run Map') == 'Run Map':
            # pass
            print("POST: Running map...")
            mailsys = mainman.mailman()
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
        print("No postback (GET REQ), rendering base....")

    # TODO - Consider better way to handle calls to apiController.get_data() given upstream API calls to IPStack.
    return render_template("home.html", data=data)  # apiController.get_data()
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
    if DEBUG:
        app.debug = True
        app.run(debug=True)
