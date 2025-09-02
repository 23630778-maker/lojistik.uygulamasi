from flask import Flask, render_template, request, redirect, url_for, flash
import pyodbc
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Flash mesajları için

# -----------------------------
# SQL Server Bağlantısı
# -----------------------------
DB_SERVER = r"NISA\SQLEXPRESS05"  # SQL Server instance adı
DB_NAME = "lojistik"               # Veritabanı adı
DB_TRUSTED_CONNECTION = True       # Şifre yoksa True, varsa False yapıp DB_USER ve DB_PASS ekle

def get_connection():
    if DB_TRUSTED_CONNECTION:
        conn_str = (
            f'DRIVER={{ODBC Driver 18 for SQL Server}};'
            f'SERVER={DB_SERVER};'
            f'DATABASE={DB_NAME};'
            f'Trusted_Connection=yes;'
        )
    else:
        DB_USER = "kullanici_adi"
        DB_PASS = "sifre"
        conn_str = (
            f'DRIVER={{ODBC Driver 18 for SQL Server}};'
            f'SERVER={DB_SERVER};'
            f'DATABASE={DB_NAME};'
            f'UID={DB_USER};'
            f'PWD={DB_PASS};'
        )
    return pyodbc.connect(conn_str)

# -----------------------------
# Ana Route
# -----------------------------
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
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
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

# -----------------------------
# Uygulamayı Başlat
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
