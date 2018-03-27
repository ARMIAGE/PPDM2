  function validateForm()
    {
        var a=document.forms["FilesSelection"]["file"].value;

        if (a==null || a=="")
        {
            alert("Veuillez selectioner un fichier");
            return false;
        }
    }