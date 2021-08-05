import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
# app.config["TEMPLATES_AUTO_RELOAD"] = True

# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///fotki.db'
# db = SQLAlchemy(app)

# Configure CS50 Library to use SQLite database
# db = SQL("sqlite:///fotki.db")
db = SQL(os.getenv("DATABASE_URL"))

@app.route("/ph_rez", methods=["GET", "POST"])
def ph_rez():
    if request.method == "POST":
        # Get area
        area = request.form.get("area")
        if area == "Весь мир":
            deals = db.execute("SELECT * FROM fotos GROUP BY Country")
        else:
            deals = db.execute("SELECT * FROM fotos WHERE Area = ? GROUP BY Country", area)
        return render_template("ph_filtered.html", deals=deals, area=area)
    else:
        areas = db.execute("SELECT * FROM fotos GROUP BY Area")
        return render_template("ph_rez.html", areas=areas)


@app.route("/", methods=["GET", "POST"])
def phe_rez():
    if request.method == "POST":
        # Get area
        area = request.form.get("area")
        if area == "The World":
            deals = db.execute("SELECT * FROM fotos GROUP BY fotos.CountryEng")
        else:
            deals = db.execute("SELECT * FROM fotos WHERE fotos.AreaEng = ? GROUP BY fotos.CountryEng", area)
        return render_template("phe_filtered.html", deals=deals, area=area)
    else:
        areas = db.execute("SELECT * FROM fotos GROUP BY fotos.AreaEng")
        return render_template("phe_rez.html", areas=areas)


@app.route("/ph_filtered", methods=["GET", "POST"])
def ph_filtered():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        country = request.form.get("country")
        if country == "Все страны":
            deals1 = db.execute("SELECT City, HrefRus, Visit FROM fotos GROUP BY Country")
        else:
            deals1 = db.execute("SELECT City, HrefRus, Visit FROM fotos WHERE Country = ? ORDER BY City", country)
        return render_template("ph_final.html", deals1=deals1, country=country)
    # else:
        # area=ph_rez(area)
        # areas = db.execute("SELECT * FROM fotos GROUP BY Сountry")
        # return render_template("ph_filtered.html", areas=areas, area=area, country=country)


@app.route("/phe_filtered", methods=["GET", "POST"])
def phe_filtered():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        country = request.form.get("country")
        if country == "All countries":
            deals1 = db.execute("SELECT CityEng, HrefEng, Visit FROM fotos GROUP BY CountryEng")
        else:
            deals1 = db.execute("SELECT CityEng, HrefEng, Visit FROM fotos WHERE CountryEng = ? ORDER BY CityEng", country)
        return render_template("phe_final.html", deals1=deals1, country=country)
    # else:
        # area=ph_rez(area)
        # areas = db.execute("SELECT * FROM fotos GROUP BY Сountry")
        # return render_template("ph_filtered.html", areas=areas, area=area, country=country)


@app.route("/ph_final", methods=["GET", "POST"])
def ph_final():

    if request.method == "POST":
        return redirect('/ph_rez')
    else:
        return redirect('/p')


@app.route("/phe_final", methods=["GET", "POST"])
def phe_final():

    if request.method == "POST":
        return redirect('/')


@app.route("/izm", methods=["GET", "POST"])
def izm():
    if request.method == "POST":
        earea = request.form.get("area")
        arii = db.execute("SELECT Area FROM fotos WHERE AreaEng = ?", earea)
        area = arii[0]['Area']
        country = request.form.get("country")
        ecountry = request.form.get("ecountry")
        terr = request.form.get("terr")
        eterr = request.form.get("eterr")
        city = request.form.get("city")
        ecity = request.form.get("ecity")
        visdate = request.form.get("visdate")
        visyear = request.form.get("visyear")
        pagename = request.form.get("pagename")

        try:
            db.execute("INSERT INTO fotos VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", area, earea, country, ecountry,
                       terr, eterr, city + ' ', ecity + ' ', pagename + '.html', pagename + 'e.html', visdate,  visyear)
            # flash("Chosen city was successfully added to database!")
        except:
            return("It was error while adding...")

        goroda = db.execute("SELECT CityEng, Visit, God FROM fotos WHERE CityEng IS NOT NULL ORDER BY CityEng")
        return render_template("izm.html", goroda=goroda)

    else:
        areas = db.execute("SELECT AreaEng FROM fotos GROUP BY AreaEng ORDER BY AreaEng")
        goroda = db.execute("SELECT CityEng, Visit, God FROM fotos WHERE CityEng IS NOT NULL ORDER BY CityEng")
        return render_template("izm.html", areas=areas, goroda=goroda)


@app.route("/update", methods=["GET", "POST"])
def update():
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        oldcity = request.form.get("oldcity")
        try:
            db.execute("DELETE FROM fotos WHERE CityEng = ?", oldcity)
            # flash("{{ city }} was successfully deleted from database!")
        except:
            return("It was error while deleting...")

        areas = db.execute("SELECT AreaEng FROM fotos GROUP BY AreaEng ORDER BY AreaEng")
        goroda = db.execute("SELECT CityEng, Visit, God FROM fotos WHERE CityEng IS NOT NULL ORDER BY CityEng")
        return render_template("izm.html", areas=areas, goroda=goroda)
    else:
        areas = db.execute("SELECT AreaEng FROM fotos GROUP BY AreaEng ORDER BY AreaEng")
        goroda = db.execute("SELECT CityEng, Visit, God FROM fotos WHERE CityEng IS NOT NULL ORDER BY CityEng")
        return render_template("izm.html", areas=areas, goroda=goroda)

