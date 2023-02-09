function deleteBook(id, token, url){
    $.ajax({
        url: url,
        type: "post",
        data: {"lstusu":id},
        beforeSend: function(){
            $("#response").html("<img src='images/1488.gif' alt='Espere...'>");
        },
        success: function(datos){
           $("#divres").html(datos);
        },
        error: function(controlador, mensaje){
            $("#divres").html("Error<br>Petición no procesada<br>" + mensaje);
        }
    });

}