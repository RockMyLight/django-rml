'use strict';

$(function () {

var Grid = {};
jQuery.extend(Grid, {
	// a singleton
    getInstance: function (id) {
        if (window._gridTopologyInstance === undefined) {
            window._gridTopologyInstance = new Grid.Topology(id);
        }
        return window._gridTopologyInstance;
    },
});


Grid.Topology = function (id) {
    // init
    this.containerId = id;
    this.container = $(id);
    this.cols = 2;
    this.cellWidth = 5;
    this.cellHeight = 5;
    this.padding = 1;
    return this;
};

jQuery.extend(Grid.Topology.prototype, {
    align: function() {
		var x = 0;
		var y = 0;
		var count = 1;
		var cols = this.cols;
		var cellWidth = this.cellWidth;
		var cellHeight = this.cellHeight;
		var padding = this.padding;
		jQuery(this.containerId).each(function() {
			jQuery(this).css("position", "relative");		    
		    jQuery(this).children("div").each((function(index, el) {
		        jQuery(el).css("width", cellWidth + "em");
		        jQuery(el).css("height", cellHeight + "em");
		        jQuery(el).css("position", "absolute");
		        jQuery(el).css("left", x + "em");
		        jQuery(el).css("top", y + "em");
		        
		        if ((count % cols) == 0) {
		            x = 0;
		            y += cellHeight + padding;
		        } else {
		            x += cellWidth + padding;
		        }
		        
		        count++;
		    }).bind({}));
		});

    },
    addElem: function(devnum) {
    	var cellId = 'cell' + devnum;
    	var html = '<div id="' + cellId + '" class="cell">' + devnum +'</div>';
    	$(this.containerId).append(html);
    }
});

// main part
var grid = Grid.getInstance('#thegrid');
// grid.align();
grid.addElem(1);
grid.addElem(2);
grid.addElem(3);
grid.addElem(4);
grid.align();

});
