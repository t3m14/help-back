

$('.gallery').slick({
    infinite: true,
    autoplay: true,

    slidesToShow: 4,
    slidesToScroll: 4,
    prevArrow: "<img src='static/media/arrows/ap.svg' class='prev'>",
    nextArrow: "<img src='static/media/arrows/an.svg' class='next'>",
    responsive: [
        {
            breakpoint: 1200,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 3,
            }
        },
        {
            breakpoint: 840,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2
            }
        },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 3
            }
        },
        {
            breakpoint: 640,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 3
            }
        },
        {
            breakpoint: 500,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2
            }
        }

    ]

});
$('.intro-second__course-gallery').slick({
    infinite: false,
    autoplay: true,
    centerMode: true,
    slidesToShow: 3,
    slidesToScroll: 3,
    prevArrow: "<img src='static/media/arrows/apw.svg' class='prev'>",
    nextArrow: "<img src='static/media/arrows/anw.svg' class='next'>",
    responsive: [
        {
            breakpoint: 1500,
            settings: {
                slidesToShow: 2.6,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 1250,
            settings: {
                slidesToShow: 2.2,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 1150,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 980,
            settings: {
                slidesToShow: 1.7,
                slidesToScroll: 2,
            }
        },

        {
            breakpoint: 950,
            settings: {
                slidesToShow: 1.8,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 820,
            settings: {
                slidesToShow: 1.6,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 740,
            settings: {
                slidesToShow: 1.8,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 640,
            settings: {
                slidesToShow: 1.7,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 540,
            settings: {
                slidesToShow: 1.6,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 500,
            settings: {
                slidesToShow: 1.5,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 480,
            settings: {
                slidesToShow: 1.2,
                slidesToScroll: 2,
            }

        },
        {
            breakpoint: 420,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 2,
            }
        },
    ]


});