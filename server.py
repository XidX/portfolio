from flask import Flask, render_template, request, redirect
import csv

# from app import app
# to activate the virutal inviroment you shoud use this command
# .\\"web server"\Scripts\activate.ps1
# $env:FLASK_APP = "server.py"
# $env:FLASK_DEBUG=1


app = Flask(__name__)
print(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open("C:\\Users\ibr-s\PycharmProjects\web devolepment\web server\database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')
        # -------------------------------
# with open('database.csv', 'w', newline='') as csvfile:
#     fieldnames = ['email', 'subject', 'message']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'email': 'email1', 'subject': 'subject1', 'message': 'message1'})

def write_to_csv(data):
    with open("C:\\Users\ibr-s\PycharmProjects\web devolepment\web server\database.csv", mode="a") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
             # ---------------------------------
        # this method will repeat a headres for every row!!!
        # fieldnames = ['email', 'subject', 'message']
        # header_writer = csv.DictWriter(database2, fieldnames=fieldnames)
        # header = header_writer.writeheader()
        # header.writerow({'email': 'email1', 'subject': 'subject1', 'message': 'message1'})

        # ---------------------------------
        csv_writer = csv.writer(database2, delimiter=",", quotechar=";", quoting=csv.QUOTE_MINIMAL)

        # header_writer.writeheader()
        # csv_writer.writerow(data)

        csv_writer.writerow([email, subject, message])


# ----------------------------------------------------------------


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # return "testing"
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            print(data)
            # write_to_file(data)
            write_to_csv(data)
            return redirect("thankyou.html")
        except:
            return ("did not svae to data base")
    # else:
    #     return 'something went wrong. Try again'

# @app.route("/index.html")
# def my_home():
#     return render_template("index.html")

# @app.route('/about.html')
# def about():
#     return render_template("about.html")
#
# @app.route('/components.html')
# def components():
#     return render_template("components.html")
#
# @app.route('/contact.html')
# def contact():
#     return render_template("contact.html")
#
# @app.route('/work.html')
# def work():
#     return render_template("work.html")
#
# @app.route('/works.html')
# def works():
#     return render_template("works.html")
#
# @app.route('/blogs')
# def blog():
#     return 'this is the blogs page'


# using render
# @app.route('/')
# def hello_world():
#     print(url_for('static', filename='programming.png'))
#     return render_template("index.html")


# @app.route('/blogs')
# def blog():
#     return 'this is the blogs page'


# @app.route('/<username>')
# def username(username=None):
#     return render_template("index.html", name=username)


# @app.route('/<username>/<int:post_id>')
# def username(username=None, post_id=None):
#     return render_template("index.html", name=username, post_id=post_id)

# @app.route('/favicon')
# def blog2():
#     return 'this is the blogs page'
# name = input(f"Who are you?, pleas enter your name here:  ")
# print("hello %s" % (f"nice to meat you {name}",))
