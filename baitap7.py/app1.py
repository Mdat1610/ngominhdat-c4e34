from flask import Flask, render_template, redirect
app = Flask(__name__)
prof = {
    "name": "Ngô Minh Đạt",
    "age": 19,
    "work": "Barista",
    "school": "Đại học LĐ-XH",
    "Hobbies": "Xem Stream, Chơi Game, Lướt Facebook",
    "sport": "E-sport, Bóng Rổ"
}
@app.route("/about-me")
def home():
    return render_template("my_profiles.html", PROF = prof)

@app.route("/school")
def school():
    return redirect('http://techkids.vn ')
if __name__ == "__main__":
    app.run(debug=True)