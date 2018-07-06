$(document).on('ready', function () {
    $(".headshotsGallery").slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3500,
        pauseOnHover: true,
        adaptiveHeight: true,
        arrows: true,
    });
});

$(document).on('ready', function () {
    $(".optimizerCarousel").slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        pauseOnHover: true,
        adaptiveHeight: true,
        arrows: true,
        dots: true,
    });
});
