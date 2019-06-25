from flask import Flask
app = Flask(__name__)
c = ""
@app.route("/bmi/<int:weight>/<int:hight>")
def bmi(weight,hight):
    b = hight / weight
    
    if b < 16:
        c = "Severely underweight"
    elif 16 <= b <18.5:
        c = "Underweight"
    elif 18.5 <= b <25:
        c = "Normal"
    elif 25 <= b < 30:
        c = "Overweight"
    else:
        c = "Obese"
    return "your BMI: {0}".format(b), c
if __name__ == "__main__":
    app.run(debug = True)
    
