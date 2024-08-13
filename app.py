from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Riya@2003'
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def Home():
    if request.method == 'POST':
        # Retrieve form data
        seat = request.form.get('seat')
        food = request.form.get('food')
        name = request.form.get('name')
        age = request.form.get('age')
        sex = request.form.get('sex')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user (seat, food, name, age, sex) VALUES (%s, %s, %s, %s, %s)", (seat, food, name, age, sex))
        mysql.connection.commit()  # Commit the transaction to the database
        cur.close()

        # Redirect back to the form page with an empty form
        return redirect(url_for('Home'))

    return render_template('new4.html')

if __name__ == "__main__":
    app.run(debug=True)
