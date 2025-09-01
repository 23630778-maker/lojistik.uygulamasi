Imports System.Data
Imports System.Data.SqlClient

Public Class WebForm1
    Inherits System.Web.UI.Page

    Protected Sub Page_Load(ByVal sender As Object, ByVal e As EventArgs) Handles Me.Load

    End Sub

    Protected Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        ' Değişkenleri tanımla
        Dim tarih As DateTime
        Dim iscikissaat As TimeSpan
        Dim plaka As String
        Dim cikiskm As Decimal
        Dim kumgirissaat As TimeSpan
        Dim giriskm As Decimal
        Dim kumcikissaat As TimeSpan
        Dim isletmegiriskm As Decimal
        Dim isletmegirissaat As TimeSpan
        Dim farkkm As Decimal
        Dim uretici As String
        Dim ureticikm As Decimal
        Dim tonaj As Integer

        ' TextBox'lardan değerleri al ve dönüştür
        If Not DateTime.TryParse(TextBox14.Text, tarih) Then
            tarih = DateTime.Now ' veya varsayılan değer
        End If

        If Not TimeSpan.TryParse(TextBox2.Text, iscikissaat) Then
            iscikissaat = TimeSpan.Zero
        End If

        plaka = If(String.IsNullOrWhiteSpace(TextBox3.Text), "", TextBox3.Text)

        If Not Decimal.TryParse(TextBox4.Text, cikiskm) Then cikiskm = 0
        If Not TimeSpan.TryParse(TextBox5.Text, kumgirissaat) Then kumgirissaat = TimeSpan.Zero
        If Not Decimal.TryParse(TextBox6.Text, giriskm) Then giriskm = 0
        If Not TimeSpan.TryParse(TextBox8.Text, kumcikissaat) Then kumcikissaat = TimeSpan.Zero
        If Not Decimal.TryParse(TextBox7.Text, isletmegiriskm) Then isletmegiriskm = 0
        If Not TimeSpan.TryParse(TextBox9.Text, isletmegirissaat) Then isletmegirissaat = TimeSpan.Zero

        ' Fark KM otomatik hesapla
        farkkm = giriskm - cikiskm

        uretici = If(String.IsNullOrWhiteSpace(TextBox11.Text), "", TextBox11.Text)
        If Not Decimal.TryParse(TextBox12.Text, ureticikm) Then ureticikm = 0
        If Not Integer.TryParse(TextBox13.Text, tonaj) Then tonaj = 0

        ' SQL bağlantısı ve parametreli sorgu
        Dim connectionString As String = "Data Source=NISA\SQLEXPRESS05;Initial Catalog=lojistik;Integrated Security=True"
        Using baglanti As New SqlConnection(connectionString)
            Dim sql As String = "INSERT INTO AracKayitlari " &
                                "(tarih, iscikissaat, plaka, cikiskm, kumgirissaat, giriskm, kumcikissaat, isletmegiriskm, isletmegirissaat, farkkm, uretici, ureticikm, tonaj) " &
                                "VALUES (@tarih, @iscikissaat, @plaka, @cikiskm, @kumgirissaat, @giriskm, @kumcikissaat, @isletmegiriskm, @isletmegirissaat, @farkkm, @uretici, @ureticikm, @tonaj)"

            Using komut As New SqlCommand(sql, baglanti)
                ' Parametreleri ekle
                komut.Parameters.AddWithValue("@tarih", tarih)
                komut.Parameters.AddWithValue("@iscikissaat", iscikissaat)
                komut.Parameters.AddWithValue("@plaka", plaka)
                komut.Parameters.AddWithValue("@cikiskm", cikiskm)
                komut.Parameters.AddWithValue("@kumgirissaat", kumgirissaat)
                komut.Parameters.AddWithValue("@giriskm", giriskm)
                komut.Parameters.AddWithValue("@kumcikissaat", kumcikissaat)
                komut.Parameters.AddWithValue("@isletmegiriskm", isletmegiriskm)
                komut.Parameters.AddWithValue("@isletmegirissaat", isletmegirissaat)
                komut.Parameters.AddWithValue("@farkkm", farkkm)
                komut.Parameters.AddWithValue("@uretici", uretici)
                komut.Parameters.AddWithValue("@ureticikm", ureticikm)
                komut.Parameters.AddWithValue("@tonaj", tonaj)

                ' Bağlantıyı aç ve sorguyu çalıştır
                baglanti.Open()
                komut.ExecuteNonQuery()
                baglanti.Close()
            End Using
        End Using

        ' Başarı mesajı
        ClientScript.RegisterStartupScript(Me.GetType(), "alert", "alert('Kayıt başarıyla eklendi!');", True)
    End Sub
End Class
