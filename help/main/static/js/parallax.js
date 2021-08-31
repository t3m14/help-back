$('.parallax').on('mousemove', (e) => {
    const x = e.pageX / $(window).width();
    const y = e.pageY / $(window).height();

    $('.parallax-cont').css(
        'transform',
        'translate(-' + x * 30 + 'px, -' + y * 30 + 'px)'
    );
    $('.parallax-cont-1').css(
        'transform',
        'translate(-' + y * 40 + 'px, -' + x * 30 + 'px)'
    );

});