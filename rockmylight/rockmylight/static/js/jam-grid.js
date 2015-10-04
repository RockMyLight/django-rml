'use strict';


// $(document).ready(function() {
$(function () {

var Grid = {};
jQuery.extend(Grid, {
	// a singleton
    getInstance: function (id, cols) {
        if (window._gridTopologyInstance === undefined) {
            window._gridTopologyInstance = new Grid.Topology(id, cols);			
        }
        return window._gridTopologyInstance;
    },
});


Grid.Topology = function (id, cols) {
    // init
    this.containerId = id;
    this.container = $(id);
    this.cols = cols;
    this.cellWidth = 5;
    this.cellHeight = 5;
    this.padding = 1;
    // time rounding error
    this.eps = 0.1;
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
    },
    play: function() {
    	console.log('play jam');
    	$.ajax({
    		cache: false,
    		dataType: "json",
    		url: "/api/dj/1", 
    		success: (function( t, djdata ) {
  				this.djdata = djdata;
  				t.step = 0;
  				t.interval = setInterval((t.looper).bind({}, this),1);	
  				setInterval((t.stop).bind({}, this),5*60000);	
  			}).bind({}, this)
  		});
    },
    looper: function(t) {
    	if (t.step === undefined) {
    		t.step= 0;
    	}
    	var frame = t.djdata.frames[t.step];
    	if (frame === undefined) {
    		return;
    	}
    	if (Date.now() < frame.timestamp) {
    		console.log('waiting.. on ' + t.step);
    		console.log(Date.now());
    		console.log(frame.timestamp);
    		return;
    	}

		console.log('timestamp: ' + frame.timestamp);
		console.log('now: ' + Date.now());
		
		var delta = Math.abs(frame.timestamp - Date.now());
		console.log(delta);
		if ( delta < 300) {
			console.log('assign ' + t.step);
			//$('#thegrid div.cell').css('background-color', frame.color);
            $('body').css('background-color', frame.color);
		}
	   	t.step++;    		
    },
    transit: function() {

    },
    stop: function() {
    	console.log('stop jam')
    	clearInterval(this.interval);
    }
});

// main part
var grid = Grid.getInstance('#thegrid', 3);
// grid.align();
/*for (var i = 0; i < 12 ; i++ ) {
	grid.addElem(i);
}
grid.align();*/
var clock;
$("#jamplay").click(function(){
    $.ajax({
            cache: false,
            dataType: "json",
            url: "/api/start_jam/1", 
            success: (function( t, jamdata ) {

                // Instantiate a counter
                clock = new FlipClock($('.clock'), {
                    clockFace: 'Counter',
                    countdown: false,
                    autoStart: true,
                    time: 6,
                    minimumDigits: 4
                });
                grid.play();
                setTimeout(function(){ $('#jamaudio').trigger("play"); }, 6000);

            }).bind({}, this)
    });
	
});

$("#jamstop").click(function(){

    $.ajax({
        cache: false,
        dataType: "json",
        url: "/api/stop_jam/1", 
        success: (function( t, jamdata ) {

            clock.stop();
            grid.stop();
            $('#jamaudio').trigger("pause");

        }).bind({}, this)
    });
});

});

