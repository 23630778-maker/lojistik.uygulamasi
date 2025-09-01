<%@ Page Language="vb" AutoEventWireup="false" CodeBehind="WebForm1.aspx.vb" Inherits="WebApplication16.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:TextBox ID="TextBox14" runat="server"></asp:TextBox>
            <asp:Label ID="Label1" runat="server" Text="Tarih:"></asp:Label>
        </div>
        <p>
            <asp:TextBox ID="TextBox2" runat="server"></asp:TextBox>
            <asp:Label ID="Label2" runat="server" Text="İşlem Çıkış Saati:"></asp:Label>
        </p>
        <p>
            <asp:TextBox ID="TextBox3" runat="server"></asp:TextBox>
            <asp:Label ID="Label3" runat="server" Text="Plaka:"></asp:Label>
        </p>
        <p>
            <asp:TextBox ID="TextBox4" runat="server"></asp:TextBox>
            <asp:Label ID="Label4" runat="server" Text="Çıkış KM:"></asp:Label>
        </p>
        <p>
            <asp:TextBox ID="TextBox5" runat="server"></asp:TextBox>
            <asp:Label ID="Label5" runat="server" Text="Kümes Giriş Saati:"></asp:Label>
        </p>
        <p>
            <asp:TextBox ID="TextBox6" runat="server"></asp:TextBox>
            <asp:Label ID="Label6" runat="server" Text="Giriş KM:"></asp:Label>
        </p>
        <p>
            <asp:TextBox ID="TextBox8" runat="server"></asp:TextBox>
            <asp:Label ID="Label7" runat="server" Text="Kümes Çıkış Saat:"></asp:Label>
        </p>
        <p>
            <asp:TextBox ID="TextBox7" runat="server" style="margin-bottom: 0px"></asp:TextBox>
            <asp:Label ID="Label8" runat="server" Text="İşletme Giriş KM:"></asp:Label>
        </p>
        <p>
            <asp:TextBox ID="TextBox9" runat="server"></asp:TextBox>
            <asp:Label ID="Label9" runat="server" Text="İşletme Giriş Saat:"></asp:Label>
        </p>
        <p>
            <asp:TextBox ID="TextBox10" runat="server" Width="158px"></asp:TextBox>
            <asp:Label ID="Label10" runat="server" Text="Fark KM:"></asp:Label>
        </p>
        <p>
            <asp:TextBox ID="TextBox11" runat="server" Height="16px"></asp:TextBox>
            <asp:Label ID="Label11" runat="server" Text="Üretici:"></asp:Label>
        </p>
        <p>
            <asp:TextBox ID="TextBox12" runat="server"></asp:TextBox>
            <asp:Label ID="Label12" runat="server" Text="Üretici KM:"></asp:Label>
        </p>
        <p>
            <asp:TextBox ID="TextBox13" runat="server"></asp:TextBox>
            <asp:Label ID="Label13" runat="server" Text="Tonaj:"></asp:Label>
        </p>
        <p>
            &nbsp;</p>
        <p>
            <asp:Button ID="Button1" runat="server" Text="KAYDET" />
            <asp:Label ID="Label14" runat="server" Text="Label"></asp:Label>
        </p>
    </form>
</body>
</html>
