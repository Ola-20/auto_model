/*
This function gets all the necessary parameters from the app.html file.
 2) creates corresponding variables and a url variable(The end point from the flask server where the model is interacted with.
 3) JQuery code is then used to send an AJAX request (Post) to the url
 4) Retrieve the estimated price in a "data" object which will now be displayed as the suggested price
*/


function place(){
    console.log("Estimate price button clicked");
    var odo = document.getElementById("uiOdo");
    var location = document.getElementById("uiLocations");
    var year = document.getElementById("uiYears");
    var transmission= document.getElementById("uiTransmissions");
    var estPrice = document.getElementById("uiActualPrice");

    var url = "http://127.0.0.1:5000/predict_used_car_price";

    $.post(url, {
        odo: parseFloat(odo.value),
        location: location.value,
        year: year.value,
        transmission: transmission.value
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML  = "<h2>" + data.estimated_price.toString() + "Dollars</h2>";
        console.log(status);
    });
}

/*
function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_location_names";
    $.get(url,function(data, status){
        console.log("got response for get_location_names request");
        if(data){
            var locations = data.locations;
            var uilocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $(#uiLocations).append(opt)
            }
        }
    }
    );
}
window.onload = onPageLoad

.innerHTML
function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_year";
    $.get(url,function(data, status){
        console.log("got response for get_location_names request");
        if(data){
            var locations = data.locations;
            var uilocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $(#uiLocations).append(opt)
            }
        }
    }
    );
}
*/


