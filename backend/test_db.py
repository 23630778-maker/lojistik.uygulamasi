import psycopg2

DB_HOST = "db.mjnpmjfuinztssstvqsu.supabase.co"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "Nisa2025Secure"  # yeni şifren
DB_PORT = 5432

def test_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT,
            options="-c client_encoding=UTF8"
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO arac_kayitlari (plaka) VALUES (%s) RETURNING id;", ("TEST123",))
        inserted_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        print(f"Başarılı! Test kaydı eklendi, ID: {inserted_id}")
    except Exception as e:
        print(f"HATA: {e}")

if __name__ == "__main__":
    test_connection()
