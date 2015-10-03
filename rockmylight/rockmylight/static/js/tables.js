'use strict';

$(function () {

  $('.reservations').draggable({
    cursor: 'move',
    revert: true
  });

  $('.table-icon.available').droppable({
    accept: '.reservations',
    hoverClass: 'table-icon-reserved',
    tolerance: 'pointer',
    // On drop function
    drop: function (event, ui) {
      var $draggableElem = ui.draggable;
      var $droppableElem = $(this);

      var typeOfReservation = $draggableElem.data('type');
      var numberOfPersons = $draggableElem.data('person');
      var dateOfReservation = $draggableElem.data('date');
      var timeOfReservation = $draggableElem.data('time');

      var imageSrc;

      $droppableElem.attr('data-type', typeOfReservation);
      $droppableElem.attr('data-person', numberOfPersons);
      $droppableElem.attr('data-date', dateOfReservation);
      $droppableElem.attr('data-time', timeOfReservation);

      if (typeOfReservation === 'usual') {
        $droppableElem.find('img').addClass('table-icon-reserved');
      }
      else {
        imageSrc = '/static/images/table-' + $droppableElem.data('size') + '-primary.png';
      }

      $droppableElem.find('img').attr('src', imageSrc);
      $droppableElem.droppable('disable');
      $droppableElem.removeClass('available');
      $draggableElem.remove();
    }
  });
});
