$(function() {  


	var url = "http://api.openweathermap.org/data/2.5/weather?q=";
    var apiKey = "09bdee17cd2205c0566182970e86ed8a"; // Replace "APIKEY" with your own API key;
   


    $('#button-addon2').on('click' , (i) => {
        var city = $("#cityID").val();
        i.preventDefault();



    $.get(url + city + '&appid=' + apiKey)
    .done(function(response) {

		console.log(response);
        updateUISuccess(response)
		
    })
    .fail(function(error) {
        console.log(error);
        
        updateUIError()
			
    });
    
	function updateUISuccess(response) {

        var condition = response.weather[0].main;
        console.log(condition);
        
        var degC = response.main.temp - 273.15;

        console.log(degC);
        
        var degCInt = Math.floor(degC);
        
        console.log(degCInt);

        var degF = degC * 1.8 + 32;
        
        console.log(degF);
        var degFInt = Math.floor(degF);
        console.log(degFInt);
        
		
        var weatherBox = document.getElementById("weather");
        weatherBox.innerHTML = "<p>" + degCInt + "&#176; C / " + degFInt + "&#176; F" + " <br> Weather Condition: " + condition + "</p>"
        // weatherBox.innerHTML = "<p>" + "img" + ;
	}

	// handle XHR error
	function updateUIError() {
		var $weatherBox = $('#weather');
		$weatherBox.addClass('hidden');
	}
})
})();