$(document).ready(function () {
   var mySwiper = new Swiper('#topSwiper',{
        autoplay:2000,
        pagination:'.swiper-pagination'

    });

    var menuSwiper = new Swiper('#swiperMenu',{

        // pagination:'.swiper-pagination',
        slidesPerView: 3
    });

});