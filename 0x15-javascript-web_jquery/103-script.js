$(document).ready(function() {
    function fetchTranslation() {
        var languageCode = $('#language_code').val();
        var url = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode;
        $.getJSON(url, function(data) {
            $('#hello').text(data.hello);
        }).fail(function() {
            $('#hello').text('Translation not found');
        });
    }

    $('#btn_translate').click(fetchTranslation);
    $('#language_code').keypress(function(e) {
        if (e.which == 13) { // 13 is the ENTER key code
            fetchTranslation();
        }
    });
});

