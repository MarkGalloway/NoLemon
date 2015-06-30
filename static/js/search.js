var url = '/classifieds/?'


/*
 *  Window scroll function to fire off ajax requests
 *  based off of window height
 */
function scrollListener() {
    if($(window).scrollTop() + $(window).height() > $(document).height() - 200) {

        // unbind to prevent duplicate requests
        $(window).unbind('scroll');

        // make ajax request
        loadAjax();
    }
}

/*
 * Load new classified ads and update url based off of results.
 * Resets scroll listener if more results exist
 */
function loadAjax() {
    $.ajax({
        url: url,
        success: function(data) {

            // update url for next page
            url = $(data).filter('#next-link').attr('href');

            // append data(html) to list of ads
            $("#ad-list").append(data);

            if(url) {
                // Bind scroll listener is there are more results
                $(window).scroll(scrollListener);
            }

        },
        error : function(xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText);
        }

    });
}

/*
 *  Function to load initial data on document ready or search
 */
function loadData() {
    // Clear current results
    $("#ad-list").empty()

    // Reset URL
    url = '/classifieds/?';

    // TODO: get values from search form and append to URL

    loadAjax();
}

// Register loadData on document ready
$(loadData);

// Register loadData on search button click
$("#search-button").click(loadData);


// Register loading spinner
var $loading = $('#loading-indicator').hide();
$(document)
  .ajaxStart(function () {
    $loading.show();
  })
  .ajaxStop(function () {
    $loading.hide();
  });

