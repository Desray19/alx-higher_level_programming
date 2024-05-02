$(document).ready(function () {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fg', function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
  
