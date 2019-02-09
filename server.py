from flask import Flask, render_template, request

import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/checkout', methods=['post'])
def checkout():  
    straw_qty = request.form['straw_quantity']
    rasp_qty = request.form['raspberry_quantity']
    apple_qty =request.form['apple_quantity']
    stud_name =request.form['student_name']
    stud_id =request.form['student_id']
    time_stamp=datetime.datetime.now()
    total_items = int(straw_qty)+int(rasp_qty)+int(apple_qty)
    print('*'*10,'Charging:',request.form['student_name'],'for',total_items,'items', '*'*10)
    return render_template('checkout.html',straw = straw_qty, rasp = rasp_qty, apple = apple_qty, name = stud_name, s_id = stud_id, total_items = total_items ,time_stamp=time_stamp.strftime("%B %m, %Y %X"))



if __name__=='__main__':
    app.run(debug=True)

