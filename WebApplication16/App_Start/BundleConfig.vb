Imports System.Collections.Generic
Imports System.Linq
Imports System.Web
Imports System.Web.Optimization

Public Class BundleConfig
    ' Paketleme hakkında daha fazla bilgi için lütfen https://go.microsoft.com/fwlink/?LinkId=303951 adresini ziyaret edin.
    Public Shared Sub RegisterBundles(ByVal bundles As BundleCollection)
        RegisterJQueryScriptManager()

        bundles.Add(New ScriptBundle("~/bundles/WebFormsJs").Include(
                        "~/Scripts/WebForms/WebForms.js",
                        "~/Scripts/WebForms/WebUIValidation.js",
                        "~/Scripts/WebForms/MenuStandards.js",
                        "~/Scripts/WebForms/Focus.js",
                        "~/Scripts/WebForms/GridView.js",
                        "~/Scripts/WebForms/DetailsView.js",
                        "~/Scripts/WebForms/TreeView.js",
                        "~/Scripts/WebForms/WebParts.js"))

        ' Bu dosyaların çalışması için sıra çok önemlidir; belirli bağımlılıkları vardır
        bundles.Add(New ScriptBundle("~/bundles/MsAjaxJs").Include(
                "~/Scripts/WebForms/MsAjax/MicrosoftAjax.js",
                "~/Scripts/WebForms/MsAjax/MicrosoftAjaxApplicationServices.js",
                "~/Scripts/WebForms/MsAjax/MicrosoftAjaxTimer.js",
                "~/Scripts/WebForms/MsAjax/MicrosoftAjaxWebForms.js"))

        ' Gelişmek ve öğrenmek için Modernizr'\in Geliştirme sürümünü kullanın. Üretime
        ' üretim için hazır. https://modernizr.com adresinde derleme aracını kullanarak yalnızca ihtiyacınız olan sınamaları seçin.
        bundles.Add(New ScriptBundle("~/bundles/modernizr").Include(
                        "~/Scripts/modernizr-*"))
    End Sub

    Public Shared Sub RegisterJQueryScriptManager()
        Dim jQueryScriptResourceDefinition As New ScriptResourceDefinition
        With jQueryScriptResourceDefinition
            .Path = "~/scripts/jquery-3.7.0.min.js"
            .DebugPath = "~/scripts/jquery-3.7.0.js"
            .CdnPath = "http://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.7.0.min.js"
            .CdnDebugPath = "http://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.7.0.js"
        End With

        ScriptManager.ScriptResourceMapping.AddDefinition("jquery", jQueryScriptResourceDefinition)
    End Sub
End Class
