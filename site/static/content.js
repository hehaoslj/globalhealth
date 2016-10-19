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
