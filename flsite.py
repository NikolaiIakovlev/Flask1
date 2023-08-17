from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'

menu = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]

@app.route("/index")
@app.route("/")
def index():
    print( url_for('index'))
    return render_template('index.html', menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"

@app.route("/about")
def about():
    print( url_for('about'))
    return render_template('about.html', title="О сайте", menu=menu)

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if len(request.form['username']) > 2:
        flash('Сообщение отправлено', category='success')
    else:
        flash('Ошибка отправки', category='error')
        # print(request.form["username"])
    return render_template('contact.html', title="Обратная связь", menu=menu)


# with app.test_request_context():
#     print(url_for('about'))
#     print(url_for("profile", username="ypoura"))

if __name__ == "__main__":
    app.run(debug=True)
