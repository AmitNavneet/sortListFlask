from flask import Flask,request,render_template
from flask import jsonify
app=Flask(__name__)

numberList=[]

@app.route('/',methods=['POST','GET'])
def index():
    return render_template('index.html')


@app.route('/insertNumber',methods=['POST'])
def insertNumber():
    
    num=request.form.get('num')

    if num=='':
        return render_template('index.html')
    num=int(num)
    numberList.append(num)
    
    return render_template('index.html',numbers=numberList)
    #return jsonify(numberList)

@app.route('/ascending',methods=['POST'])
def ascending():
    ascList=numberList.copy()
    ascList.sort()
    return render_template('index.html',ascList=ascList,originalList=numberList)
    

@app.route('/clearList',methods=['POST'])
def clearList():
    if len(numberList)>0:
        numberList.clear()
    
    return render_template('index.html')

@app.route('/descending',methods=['POST'])
def descending():
    descList=numberList.copy()
    descList.sort(reverse=True)
    return render_template('index.html',descList=descList,originalList=numberList)

if __name__=='__main__':
    app.run(debug=True)