
(function() {

var adsList = {
    container: $("#ad-list"),
    loading: $('#loading-indicator').hide(),
    base_url: '/classifieds/?',
    url: "",

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

        // Clear current results
        adsList.container.empty()

        // Reset URL
        adsList.url = adsList.base_url;

        // TODO: get values from search form and append to URL

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
                    adsList.url = next_url
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
}

adsList.init();

// Register _loadData on search button click
$("#search-button").on('click', adsList.init);

})();
