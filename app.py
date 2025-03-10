from flask import Flask, render_template,request
from prediction import prediction
import pandas as pd
df=pd.read_csv("artifacts\\merged_titanic.csv")

data=df.drop(["PassengerId","Name","Ticket","Cabin"],axis=1)
col=data.head(1).columns
print(len(col))




app =Flask(__name__)
@app.route("/",methods=['GET','POST'])
def Home():
    if request.method == 'POST':
        Pclass =float (request.form.get("Pclass"))
        Sex =float (request.form.get("Sex"))
        Age =float (request.form.get("Age"))
        SibSp =float (request.form.get("SibSp"))
        Parch =float (request.form.get("Parch"))
        Fare =float (request.form.get("Fare"))
        Embarked =float(request.form.get("Embarked"))
        total=[[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]]
        a = prediction(data=total)
        if a[0] == 1:
            a = "Maligant"
        else:
            a = "Benign"

        
        return render_template("index.html",name =a, columns=col)

    return render_template("index.html",coulmns=col)    

if __name__ == "__main__":
    app.run(debug=True)    
