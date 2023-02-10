function deleteBook(id, url, token){
    let data = new FormData();
    data.append('id', id);
    $.ajax({
        url: url,
        type: "post",
        headers: { 
            contentType: "application/json",
            'X-CSRFToken': token
        },
        data: {
            'id': id
        },
        beforeSend: function(){
            $("#response").html("<img src='images/1488.gif' alt='Waiting...'>");
        },
        success: function(datos){
            console.log(datos)
           $("#response").html(datos);
        },
        error: function(controlador, mensaje){
            $("#response").html("Error<br>Petición no procesada<br>" + mensaje);
        }
    });

}