from os import error
from flask import Flask, render_template, request,redirect,Flask, flash,url_for
import model as model
app = Flask(__name__)
app.secret_key = "don't tell HeeHee"
def checkString(input):
    try:
        # Convert it into integer
        val = int(input)
        return 0
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            return 0
        except ValueError:
            return 1
def check(age,name,lastname,income,balance):
    if age < 21:
        flash('Underage: อายุยังไม่ถึงเกณฑ์')
    elif 1 != checkString(name):
        flash('Name cannot be integer: ชื่อเป็นตัวเลขไม่ได้')
    elif 1 != checkString(lastname):
        flash('lastname cannot be integer: นามสกุลเป็นตัวเลขไม่ได้')
    elif 0 != checkString(income):
        flash('income must be number: รายได้ต้องเป็นตัวเลข')
    elif 0 != checkString(balance):
        flash('balance must be number: ยอดคงเหลือต้องเป็นตัวเลข')
    elif (0 == checkString(income)) or 0 == checkString(balance):
        if float(income) < 0:
            flash('income cannot be negative: รายได้ติดลบไม่ได้')
            return 1
        # if float(balance) < 0:
        #     flash('balance cannot be negative: ยอดคงเหลือติดลบไม่ได้')
        #     return 1
        return 0
    return 1
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/", methods = ["GET",'POST'])
def submit():
    if request.method == "POST":
        name = request.form['name']
        income = request.form['income']
        balance = request.form['balance']
        lastname = request.form['lastname']
        age =  model.calculateAge(request.form['age'])
        if(check(age,name,lastname,income,balance) == 1):
            return redirect(url_for('hello_world'))
        else:
            data = model.initial(request)
            result = model.prediction(data)
            if result[0] == 0:
                result = "เสียใจด้วยคุณมีโอกาสที่จะไม่ได้รับอนุมัติสินเชื่อส่วนบุคคล"
                m = " you have little or no chance of getting approved for a personal loan."
                he1 ="Unfortunately,"
            else:
                result = "ยินดีด้วยคุณมีโอกาสที่จะได้รับอนุมัติสินเชื่อส่วนบุคคล"
                m = " you have the opportunity to be approved for a personal loan."
                he1 ="Congratulations,"
            return render_template("result.html", resultmessage = result, name = request.form['name'], lastname = request.form['lastname'], m=m ,he1=he1)
    return redirect("index.html")



if __name__ == "__main__":
    app.run()