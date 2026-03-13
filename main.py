from flask import Flask, render_template

app = Flask(__name__)

students = [
"구승윤","김규민","김남현","김동진","김민재","김용찬","김윤기","김은총","박시온",
"박하진","심재한","양준호","이승준","이지오","이태빈","장민경","장준혁",
"장지한","장하균","정승민","정지훈","정현준","조석열","주하준","최재률",
"홍예권","홍준민"
]

@app.route("/")
def home():
    return render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)