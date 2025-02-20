from flask import Flask, render_template,request




app =Flask(__name__)
@app.route("/",methods=['GET','POST'])
def Home():
    if request.method == 'POST':
        Pclass=request.form['Pclass']
        Sex=request.form['Sex']
        Age=request.form['Age']
        SibSp=request.form['SibSp']
        Parch=request.form['Parch']
        Fare=request.form['Fare']
        Embarked=request.form['Embarked']
        total=[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]
        

        
        return render_template("index.html",name = total)

    return render_template("index.html",name='ikram')    
if __name__ == "__main__":
    app.run(debug=True)    
