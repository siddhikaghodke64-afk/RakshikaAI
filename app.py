import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

# ------------------ Database ------------------

def create_table():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sos_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        time TEXT,
        latitude TEXT,
        longitude TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    relation TEXT
    )
    """)
    conn.commit()
    conn.close()

# ------------------ Pages ------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/sos")
def sos():
    return render_template("sos.html")


# ------------------ Save SOS ------------------

@app.route("/save_sos", methods=["POST"])
def save_sos():

    data = request.json

    lat = data["latitude"]
    lon = data["longitude"]

    now = datetime.now()

    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M:%S")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO sos_history(date,time,latitude,longitude)
    VALUES(?,?,?,?)
    """, (date, time, lat, lon))

    conn.commit()
    conn.close()

    return jsonify({"status": "success"})

@app.route("/history")
def history():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT date,time,latitude,longitude
    FROM sos_history
    ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return render_template("history.html", data=data)

@app.route("/contacts")
def contacts():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, phone, relation FROM contacts")

    data = cursor.fetchall()

    conn.close()

    return render_template("contact.html", contacts=data)

@app.route("/save_contact", methods=["POST"])
def save_contact():

    name = request.form["name"]
    phone = request.form["phone"]
    relation = request.form["relation"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO contacts(name,phone,relation) VALUES(?,?,?)",
        (name, phone, relation)
    )

    conn.commit()
    conn.close()

    return redirect("/contacts")
@app.route("/alert")
def alert():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name, phone, relation
    FROM contacts
    """)

    contacts = cursor.fetchall()

    conn.close()

    return render_template("alert.html", contacts=contacts)

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/tips")
def tips():
    return render_template("tips.html")

@app.route("/nearby")
def nearby():
    return render_template("nearby.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")
# ------------------ Main ------------------

if __name__ == "__main__":
    create_table()
    app.run(debug=True)