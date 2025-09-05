from flask import Flask, render_template, request, redirect, url_for, flash
import os
import psycopg
from datetime import datetime
from urllib.parse import quote_plus

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Flash mesajları için

# -----------------------------
# Postgres Bağlantısı
# -----------------------------
DB_USER = "postgres"
DB_PASS = quote_plus("Nisa2025Secure")  # Şifre özel karakter içeriyorsa encode et
DB_HOST = "db.mjnpmjfuinztssstvqsu.supabase.co"
DB_NAME = "postgres"
DB_PORT = 5432

DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def get_connection():
    try:
        return psycopg.connect(DB_URL, autocommit=True)
    except Exception as e:
        print(f"DB bağlantısı kurulamadı: {e}")
        raise

# -----------------------------
# Ana Route
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        try:
            # Form verilerini al
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

            # Veritabanına kaydet
            with get_connection() as conn:
                with conn.cursor() as cur:
                    sql = """INSERT INTO arac_kayitlari
                             (tarih, iscikissaat, plaka, cikiskm, kumgirissaat, giriskm, kumcikissaat,
                              isletmegiriskm, isletmegirissaat, farkkm, uretici, ureticikm, tonaj)
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    cur.execute(sql, (tarih, iscikissaat, plaka, cikiskm, kumgirissaat, giriskm,
                                      kumcikissaat, isletmegiriskm, isletmegirissaat, farkkm,
                                      uretici, ureticikm, tonaj))

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
