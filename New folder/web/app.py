from flask import Flask
#1.Creat app/sever
app = Flask(__name__)
#2. biulding route

# function binding
@app.route("/")
def home():
    return "c4e34"
@app.route("/say-hi")
def say_hi():
    return "Hi everyone"
@app.route("/say-hi/<name>/<age>")
def say_hi_everyone(name, age):
    return "Hi {0}, {1}".format(name, age)
@app.route("/add/<int:x>/<int:y>")
def add(x,y):
    
    c = x + y
    # return "{0}".format(c)
    return str(c)
    



#3. run sever
if __name__ == "__main__":
    app.run(debug = True)
