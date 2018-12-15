/**
 * Website: util js
 *
 * Version : 1.0
 *
 * Created by cyx on 2018-11-27
 */

$(function () {
    // console.log(235468)
    var tableCont = $('#table-cont');

    /**
     * scroll handle
     * @param {event} e -- scroll event
     */
    function scrollHandle(e) {
        var scrollTop = this.scrollTop;
        console.log(scrollTop)
        $('#table-cont thead').css("transform", 'translateY(' + scrollTop + 'px)');
    }

    tableCont.scroll(scrollHandle)
});
