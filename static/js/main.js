
// function deleteBook(id, url, token){
//     console.log(url)
//     let data = new FormData();
//     data.append('id', id);
//     $.ajax({
//         url: url,
//         type: "post",
//         headers: { 
//             contentType: "application/json",
//             'X-CSRFToken': token
//         },
//         data: {
//             'id': id
//         },
//         beforeSend: function(){
//             $("#response").html("<img src=\"{% static 'media/icons/1488.gif' %}\" alt='Waiting...'  width='30px'>");
//         },
//         success: function(datos){
//             console.log(datos)
//            $("#response").html(datos);
//         },
//         error: function(controlador, mensaje){
//             $("#response").html("Error<br>Petición no procesada<br>" + mensaje);
//         }
//     });

// }

function deleteBook(url) {
    $('#modal').load(url, function () {
        
        $(this).modal({
            backdrop: 'static',
            keyboard: false
        });
        return false;
    });
}

function openModal(url) {
    console.log(url)
    $('#modal').load(url, function () {
        $(this).modal({
            backdrop: 'static',
            keyboard: false
        });
        $(this).modal('show');

        return false;
    });
}

function closeModal() {
    $('#modal').modal('hide');
    return false;
}