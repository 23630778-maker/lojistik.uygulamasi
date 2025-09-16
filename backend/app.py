from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Flash mesajları için

# Burada tam yolunu yazıyoruz
EXCEL_FILE = r"C:\Users\nisak\OneDrive\lojistik.xlsx"

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

            # Verileri sözlük olarak hazırla
            data = {
                "tarih": tarih,
                "iscikissaat": iscikissaat,
                "plaka": plaka,
                "cikiskm": cikiskm,
                "kumgirissaat": kumgirissaat,
                "giriskm": giriskm,
                "kumcikissaat": kumcikissaat,
                "isletmegiriskm": isletmegiriskm,
                "isletmegirissaat": isletmegirissaat,
                "farkkm": farkkm,
                "uretici": uretici,
                "ureticikm": ureticikm,
                "tonaj": tonaj
            }

            # Excel dosyası var mı kontrol et
            if os.path.exists(EXCEL_FILE):
                df = pd.read_excel(EXCEL_FILE)
                df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
            else:
                df = pd.DataFrame([data])

            # Excel'e kaydet
            df.to_excel(EXCEL_FILE, index=False)

            flash("Kayıt başarıyla eklendi!", "success")
            return redirect(url_for("form"))

        except Exception as e:
            flash(f"Hata oluştu: {e}", "danger")
            return redirect(url_for("form"))

    return render_template("form.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
