function advanceArt(artId) {
    $.getJSON('/art/advance/' + artId +'/',function (data) {
        alert(data.msg);
        if(data.status == 201){
            queryAdvanceArt(artId);
        }

    })
}

//定时查询抢读的结果
function queryAdvanceArt(artId) {
    tid = setInterval(function () {
        $.getJSON('/art/qAdvance/' + artId +'/', function(data) {

            $('#advanceBtn').text(data.msg);
            if(data.status =202 || 200){
                clearInterval(tid)
            }
        })

    },2000)
}