'use strict';

$(function () {
  (function SidebarPanel() {
    // Function for searching open and open first panels
    function findOpenPanel(openClass) {
      var $alertsPanel = $('#alerts-sidebar-panel');
      var $messengerPanel = $('#messenger-sidebar-panel');

      if ($alertsPanel.hasClass(openClass)) {
        return $alertsPanel;
      }
      else if ($messengerPanel.hasClass(openClass)) {
        return $messengerPanel;
      }
      else {
        return false;
      }
    }

    // Function for sidebar panels animation
    function sidebarPanelAnimate($sidebarPanel, rightValue, animationSpeed) {
      animationSpeed = animationSpeed || 250;

      $sidebarPanel.animate({
        right: rightValue
      }, animationSpeed);
    }

    // Function for reducing z-index
    function reduceZIndex($sidebarPanel) {
      var currentZIndex = $sidebarPanel.zIndex();

      $sidebarPanel.zIndex(currentZIndex - 1);
    }

    // Function for open sidebar panels
    function sidebarPanelOpen($sidebarPanel) {
      var sidebarPanelWidth = $sidebarPanel.outerWidth();
      var $firstOpenPanel = findOpenPanel('open');

      if ($firstOpenPanel) {
        $firstOpenPanel.addClass('open-first');

        // If open sidebar panel exists move it to the left of current opened panel
        sidebarPanelAnimate($firstOpenPanel, sidebarPanelWidth);
      }

      $sidebarPanel.addClass('open');

      // Open current sidebar panel
      sidebarPanelAnimate($sidebarPanel, 0);
    }

    function sidebarPanelClose($sidebarPanel) {
      var sidebarPanelWidth = $sidebarPanel.outerWidth();
      var $firstOpenPanel = findOpenPanel('open-first');

      $sidebarPanel.removeClass('open open-first');

      if ($firstOpenPanel) {
        // If user close first opened sidebar panel move it behind the second opened panel
        if ($sidebarPanel.is($firstOpenPanel)) {
          sidebarPanelAnimate($sidebarPanel, 0);
          sidebarPanelAnimate($sidebarPanel, -sidebarPanelWidth, 0);
        }
        else {
          sidebarPanelAnimate($sidebarPanel, -sidebarPanelWidth);
          // If user close second opened sidebar panel move the first opened panel to the right
          sidebarPanelAnimate($firstOpenPanel, 0);

          $firstOpenPanel.removeClass('open-first');
        }
      }
      else {
        sidebarPanelAnimate($sidebarPanel, -sidebarPanelWidth);
      }
    }

    $('#alerts-sidebar-button')
      .click(function (event) {
        event.preventDefault();

        var $alertsPanel = $('#alerts-sidebar-panel');

        if ($alertsPanel.hasClass('open')) {
          sidebarPanelClose($alertsPanel);
          reduceZIndex($alertsPanel);
        }
        else {
          sidebarPanelOpen($alertsPanel);
          $alertsPanel.zIndex('');
        }
      })
      .mouseenter(function () {
        $(this).children('img').attr('src', '/static/images/nailed-table-white-icon.png');
      })
      .mouseleave(function () {
        $(this).children('img').attr('src', '/static/images/nailed-table-grey-icon.png');
      });

    $('#messenger-sidebar-button').click(function (event) {
      event.preventDefault();

      var $messengerPanel = $('#messenger-sidebar-panel');

      if ($messengerPanel.hasClass('open')) {
        sidebarPanelClose($messengerPanel);
        reduceZIndex($messengerPanel);
      }
      else {
        sidebarPanelOpen($messengerPanel);
        $messengerPanel.zIndex('');
      }
    });

    $('#alerts-sidebar-close').click(function (event) {
      event.preventDefault();
      sidebarPanelClose($('#alerts-sidebar-panel'));
    });

    $('#messenger-sidebar-close').click(function (event) {
      event.preventDefault();
      sidebarPanelClose($('#messenger-sidebar-panel'));
    });
  })();
});