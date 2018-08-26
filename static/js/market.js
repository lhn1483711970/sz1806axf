$(document).ready(function(){
    //所有类型的点击事件
    $('#alltypespan').click(function(){

         $('#alltypes').show();
         $(this).removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up');

    });

     $('#zhsortspan').click(function(){
         $('#zhsorts').show();
         $(this).removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up');

    });
    $('#alltypes').click(function(){
        $(this).hide();
        $('#alltypespan').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down');
    });

    $('#zhsort').click(function(){
        $(this).hide();
        $('#zhsortspan').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down');
    });


//添加到购物车 添加一条数据到数据库
    $('.addShopping').click(function () {
        console.info('12345');
        goodsid =$(this).val();
        spanobj = $(this).prev();
        $.ajax({
            url:'/addshopcar/',
            method:'post',
            data:{'goodsid':goodsid},
            seccess:function (obj) {
                if (obj.result == '0001'){
                    //跳转到登录页面
                    window.open('/login/','_sekf');
                }else if(obj.result == '0000'){
                    spanobj.html(obj.number); // 获取他的上一个兄弟节点

                }

            }

        })

    })

});