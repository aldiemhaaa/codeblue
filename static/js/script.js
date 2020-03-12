$(document).ready(function () {
  let getiplocal = 'http://127.0.0.1:8000/getroom/';
  let updateiplocal = 'http://192.168.20.5:8000/updateroom/';
  let ipclient = 'http://192.168.20.150:8001';
  
  setInterval(
    function () {
      $.get(getiplocal, function (data) {
        $.each(data, function (i, item) {
          $('#status-room-' + item.room).html(item.status);
          if (item.status === "1") {
            $('#alert-button-' + item.room).css('background-color', 'blue')
          }
        })
      })
    },
    5000  /* 10000 ms = 10 sec */
  ),
    $.get(getiplocal, function (data) {

      $.each(data, function (i, item) {
        // ini untuk mereset button ke localhost
        $('#btn-post-' + item.room).click(function () {
          $.ajax({
            url:updateiplocal,
            type: 'POST',
            data: JSON.stringify({
              "room": item.room,
              "status": 0,
            }),
            dataType:'json',
            headers: { 
              'Accept': 'application/json',
              'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': '*'
            },
            success: function(response){
              $('#alert-button-'+item.room).css('background-color','transparent')
            }
          }),
          $.ajax({
            url:ipclient,
            type: 'POST',
            data: JSON.stringify({
              "room": item.room,
              "status": 0,
            }),
            dataType:'json',
            success: function(response){
            }
          })
        })
      })
    })
})
