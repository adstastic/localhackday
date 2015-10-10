$(document).ready(function() {
  var MAP_WIDTH = 3000;
  var MAP_HEIGHT = 3370;

  var win_width = $(window).width(),
      win_height = $(window).height();

  var position = null;

  var init = function() {
    $map = $('.map-inner');
    $map
      .css({
        width: MAP_WIDTH,
        height: MAP_HEIGHT
      })
      .draggable({
        start: function(event, ui) {
          position = ui.position;
        },
        drag: function(event, ui) {
          console.log(ui.position);
          ui.position.left = Math.min(0, ui.position.left);
          ui.position.top = Math.min(0, ui.position.top);

          ui.position.left = Math.max(win_width-MAP_WIDTH, ui.position.left);
          ui.position.top = Math.max(win_height-MAP_HEIGHT, ui.position.top);
        },
        stop: function(event, ui) {
          position = null;
        }
      });

    $('.point').on('click', function(e) {
      e.stopPropagation();

      alert('clicked point');

      return false;
    });
  };

  $(window).on('resize', function() {
    win_width = $(window).width();
    win_height = $(window).height();
  });

  init();

});