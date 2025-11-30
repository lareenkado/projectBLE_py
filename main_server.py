from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
@app.route("/")
def home():
    return render_template("page_home.html")

@app.route("/auth")
def auth():
    return render_template("page_auth.html")

@app.route("/checkin")
def checkin():
    return render_template("page_checkin.html")

@app.route("/dashboard")
def dashboard():
    return render_template("page_dashboard.html")
if __name__ == "__main__":
    app.run(debug=True)
