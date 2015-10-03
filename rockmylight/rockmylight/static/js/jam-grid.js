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
    return this;
};

jQuery.extend(Grid.Topology.prototype, {
    align: function() {
		var x = 0;
		var y = 0;
		var count = 1;
		jQuery("#" + id).each(function() {
		    jQuery(this).css("position", "relative");		    
		    jQuery(this).children("div").each(function() {
		        jQuery(this).css("width", cellWidth + "em");
		        jQuery(this).css("height", cellHeight + "em");
		        jQuery(this).css("position", "absolute");
		        
		        jQuery(this).css("left", x + "em");
		        jQuery(this).css("top", y + "em");
		        
		        if ((count % cols) == 0) {
		            x = 0;
		            y += cellHeight + padding;
		        } else {
		            x += cellWidth + padding;
		        }
		        
		        count++;
		    });
		});

    },
    addElem: function() {
    	var html = '<div class="cell">1</div>';
    	this.container.append(html);
    }
});

// main part
var grid = Grid.getInstance('the-grid');
// grid.align();
grid.addElem();

});
