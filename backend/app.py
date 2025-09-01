from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Flash mesajları için

# Veritabanı bağlantı bilgileri (Heroku Postgres veya Supabase)
DB_HOST = "your_db_host"
DB_NAME = "your_db_name"
DB_USER = "your_db_user"
DB_PASS = "your_db_password"
DB_PORT = "5432"

def get_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )
    return conn

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        try:
            tarih = request.form.get("tarih") or datetime.now().strftime("%Y-%m-%d")
            iscikissaat = request.form.get("iscikissaat") or "00:00"
            plaka = request.form.get("plaka")
            cikiskm = float(request.form.get("cikiskm") or 0)
            kumgirissaat = request.form.get("kumgirissaat") or "00:00"
            giriskm = float(request.form.get("giriskm") or 0)
            kumcikissaat = request.form.get("kumcikissaat") or "00:00"
            isletmegiriskm = float(request.form.get("isletmegiriskm") or 0)
            isletmegirissaat = request.form.get("isletmegirissaat") or "00:00"
            farkkm = giriskm - cikiskm
            uretici = request.form.get("uretici")
            ureticikm = float(request.form.get("ureticikm") or 0)
            tonaj = int(request.form.get("tonaj") or 0)

            conn = get_connection()
            cur = conn.cursor()
            sql = """INSERT INTO arac_kayitlari
                     (tarih, iscikissaat, plaka, cikiskm, kumgirissaat, giriskm, kumcikissaat,
                      isletmegiriskm, isletmegirissaat, farkkm, uretici, ureticikm, tonaj)
                     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cur.execute(sql, (tarih, iscikissaat, plaka, cikiskm, kumgirissaat, giriskm,
                              kumcikissaat, isletmegiriskm, isletmegirissaat, farkkm,
                              uretici, ureticikm, tonaj))
            conn.commit()
            cur.close()
            conn.close()

            flash("Kayıt başarıyla eklendi!", "success")
            return redirect(url_for("form"))
        except Exception as e:
            flash(f"Hata oluştu: {e}", "danger")
            return redirect(url_for("form"))

    return render_template("form.html")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render PORT'u kullan
    app.run(host="0.0.0.0", port=port)
