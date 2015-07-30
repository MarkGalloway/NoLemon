
(function() {

// Detect browser version
var div = document.createElement("div");
div.innerHTML = "<!--[if lt IE 9]><i></i><![endif]-->";
var isIeLessThan9 = (div.getElementsByTagName("i").length == 1);

/*
 *  Object for managing AJAX loading of the ads data
 */
var adsList = {
    container: $("#ad-list"),
    loading: $('#loading-indicator').hide(),
    url: '/search/',

    config: {
        effect: 'fadeIn',
        speed: 1300
    },

    init: function(config) {
        $.extend(adsList.config, config);

        // Register _loading spinner
        $(document)
            .ajaxStart(function() {
                adsList.loading.show();
            })
            .ajaxStop(function() {
                adsList.loading.hide();
            });

        // unbind possible previous listener
        $(window).unbind('scroll');

        // Clear current results
        adsList.container.empty();

        // Register browser URL for ajax
        adsList.url = $(location).attr('href');

        adsList._load();
    },
    /*
    * load new classified ads and update url based off of results.
    * Resets scroll listener if more results exist
    */
    _load: function() {
        $.ajax({
            url: adsList.url,
            success: function(data) {

                // Update url for next page
                next_url = $(data).filter('#next-link').attr('href');

                // Strip the next-link from the html
                ads = $(data).not('#next-link');

                // Apply effect
                ads.hide()[adsList.config.effect](adsList.config.speed);

                // append ads(html) to list of ads
                ads.appendTo(adsList.container);

                if(next_url) {
                    adsList.url = next_url;
                    // Bind scroll listener is there are more results
                    $(window).scroll(adsList._listen);
                }
            },
            error : function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }

        });
    },
    /*
     *  Window scroll function to fire off ajax requests
     *  based off of window height
     */
    _listen: function() {
        if($(window).scrollTop() + $(window).height() > $(document).height() - 200) {
            // unbind to prevent duplicate requests
            $(window).unbind('scroll');

            // load new data
            adsList._load();
        }
    }
};


// Start Adlist Ajax
adsList.init();


/*
 * Price Range slider setup
 */
$("#price-range").slider({
    animate: 'fast',
    range: true,
    min: 0,
    max: 50000,
    step: 500,
    values: [0, 50000],
    slide: function( event, ui ) {
      (ui.values[1] > 0)? $("#min-price").val(ui.values[0])
                        : $("#min-price").val('');
      (ui.values[1] < 49999)? $("#max-price").val(ui.values[1])
                            : $("#max-price").val('');
      (ui.values[1] < 49999)? $("#price-display").val("$" + ui.values[0] + " - $" + ui.values[1])
                            : $("#price-display").val("$" + ui.values[0] + " - $" + ui.values[1] + " +");
    }
});

/*
 * Year Range slider setup
 */
$("#year-range").slider({
    animate: 'fast',
    range: true,
    min: 1900,
    max: 2016,
    step: 1,
    values: [1900, 2016],
    slide: function( event, ui ) {
      (ui.values[0] > 1900)? $("#min-year").val(ui.values[0])
                           : $("#min-year").val('');
      (ui.values[1] < 2016)? $("#max-year").val(ui.values[1])
                           : $("#max-year").val('');

      if(ui.values[0] < 1901 && ui.values[1] > 2015) {
        $("#year-display").val("Any");
      } else {
        $("#year-display").val((ui.values[0] > 1900? ui.values[0] : "")
                                + " - " +
                               (ui.values[1] < 2016? ui.values[1] : ""));
      }

    }
});

/*
 * Mileage Range slider setup
 */
$("#mileage-range").slider({
    animate: 'fast',
    range: true,
    min: 0,
    max: 300000,
    step: 10000,
    values: [0, 300000],
    slide: function( event, ui ) {
      (ui.values[0] > 0)? $("#min-mileage").val(ui.values[0])
                        : $("#min-mileage").val('');
      (ui.values[1] < 300000)? $("#max-mileage").val(ui.values[1])
                             : $("#max-mileage").val('');

      if(ui.values[0] < 0 && ui.values[1] > 300000) {
        $("#mileage-display").val("Any");
      } else {
        $("#mileage-display").val((ui.values[0] > 0? ui.values[0] : "")
                                   + " - " +
                                  (ui.values[1] < 300000? ui.values[1] : ""));
      }

    }
});


/*
 *  Sets initial/default slider settings
 */
function sliderDefaults(){
    $("#price-display").val("$" + $("#price-range").slider("values", 0) +
          " - $" + $("#price-range").slider("values", 1));
    $("#year-display").val("Any");
    $("#mileage-display").val("Any");

    $("#min-price").val('');
    $("#max-price").val('');
    $("#min-year").val('');
    $("#max-year").val('');
    $("#min-mileage").val('');
    $("#max-mileage").val('');
}

// Register initial slider settings
sliderDefaults();

/*
 *  Handles search form manipulations
 */
$("#search-form").on("submit", function(event) {
    // Prevent form submission
    event.preventDefault();

    // Build the querystring
    var querystring = $("#search-form :input")
        .filter(function(index, element) {
            return $(element).val() !== "";
        })
        .serialize();

    // Set the browser URL
    isIeLessThan9 ? window.location.search = querystring
                  : window.history.replaceState({}, document.title,'?' + querystring);

    // Reset the ads list
    adsList.init();

    // Scroll down to results
    $('html, body').animate({
        scrollTop: $("#ad-list").offset().top
    }, 300);
});

/*
 *  Handles search form reset
 */
$("#search-form").on("reset", function(event) {
    // Reset the browser URL
    isIeLessThan9 ? window.location.search = '?'
                  : window.history.replaceState({}, document.title,'?');

    // Reset the ads list
    adsList.init();

    // Reset Sliders
    setTimeout(function() {
        $("#price-range").slider("option", "values", [0, 50000]);
        $("#year-range").slider("option", "values", [1900, 2016]);
        $("#mileage-range").slider("option", "values", [0, 300000]);
        sliderDefaults();
    });

});

})();

