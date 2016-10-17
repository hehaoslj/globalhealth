$(function(){

    var md_content = $("#markdown-content").prop("innerHTML");
    var html_content = markdown.toHTML( md_content, 'Maruku');
    $("#markdown-result").prop("innerHTML", html_content);
    $("#markdown-content").prop("innerHTML", "");
});
