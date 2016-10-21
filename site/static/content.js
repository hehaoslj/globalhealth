$(function(){

    //var md_content = $("div #markdown-content").html();
    //var html_content = markdown.toHTML( md_content);
    //$("#markdown-result").html(html_content);
    //$("#markdown-content").html("");

    var converter = new showdown.Converter(),
        text      = $("div #markdown-content").html().replace( /\\n/g, "\n" ),
        html_ctx  = converter.makeHtml(text);
    $("#markdown-result").html(html_ctx);
    $("#markdown-content").html("");
});

$(function(){
    var current_tile_area_scheme = localStorage.getItem('tile-area-scheme') || "tile-area-scheme-darkViolet";
    $(".tile-area").removeClass (function (index, css) {
        return (css.match (/(^|\s)tile-area-scheme-\S+/g) || []).join(' ');
    }).addClass(current_tile_area_scheme);
    $(".app-bar").removeClass(function(index, css){
        return( css.match(/(^|\s)navy\s+/g) || []).join(' ');
    }).removeClass (function (index, css) {
        return (css.match (/(^|\s)tile-area-scheme-\S+/g) || []).join(' ');
    }).addClass(current_tile_area_scheme);

    $(".schemeButtons .button").hover(
            function(){
                var b = $(this);
                var scheme = "tile-area-scheme-" +  b.data('scheme');
                $(".tile-area").removeClass (function (index, css) {
                    return (css.match (/(^|\s)tile-area-scheme-\S+/g) || []).join(' ');
                }).addClass(scheme);
            },
            function(){
                $(".tile-area").removeClass (function (index, css) {
                    return (css.match (/(^|\s)tile-area-scheme-\S+/g) || []).join(' ');
                }).addClass(current_tile_area_scheme);
            }
    );

    $(".schemeButtons .button").on("click", function(){
        var b = $(this);
        var scheme = "tile-area-scheme-" +  b.data('scheme');

        $(".tile-area").removeClass (function (index, css) {
            return (css.match (/(^|\s)tile-area-scheme-\S+/g) || []).join(' ');
        }).addClass(scheme);

        $(".app-bar").removeClass(function(index, css){
            return( css.match(/(^|\s)navy\s+/g) || []).join(' ');
        }).removeClass (function (index, css) {
            return (css.match (/(^|\s)tile-area-scheme-\S+/g) || []).join(' ');
        }).addClass(scheme);

        current_tile_area_scheme = scheme;
        localStorage.setItem('tile-area-scheme', scheme);

        //showSettings();
    });


    $("a[href='/options'").attr("onclick", "showCharms('#charmSettings')").removeAttr("href")
     ;


});
