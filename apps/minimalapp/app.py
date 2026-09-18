from flask import Flask, render_template, url_for, request, redirect, flash

app = Flask(__name__)

# SECRET_KEYを設定する
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"


@app.route("/")
def index():
    return "Hello, Flaskbook!"


@app.route("/hello/<string:name>", methods=["GET", "POST"], endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}!"


@app.route("/name/<string:name>", methods=["GET", "POST"])
def show_name(name):
    return render_template("index.html", name=name)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # form 属性を使ってフォームの値を取得する
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        # 入力チェック
        is_Valid = True

        if not username:
            flash("ユーザーネームは必須です")

        # メールを送る

        # contactエンドポイントへリダイレクトする
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")
