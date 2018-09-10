$('#subBtn').on('click', function (e) {
    e.preventDefault();
    $('#myTable').empty();
    var city = $("#cityselect").val();
    var state = $("#stateselect").val();




    // Variables have been defined above, and not the information is called using the ".get" to obtain the Zillow API
    $.get('http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz18fvjq3ltsb_6ttia&state=' + state + '&city=' + city + '&childtype=neighborhood')
        .done(function (response) {
            myFunction(response);
            console.log(response);

        })

        .fail(function (error) {
            console.log(error);
        })


// This function below is assigning which piece of the XML file is going to go to which column in the table being generated.
// This function also allows the table to filter the information based on what the user is typing.

    function myFunction(response) {
        var $xmlResponse = $(response);

        $xmlResponse.find('region').each(function () {
            var $region = $(this);
            var name = $region.find('name').text(),
                medianValue = $region.find('zindex').text(),
                url = $region.find('url').text(),
                lt = $region.find('latitude').text(),
                ln = $region.find('longitude').text(),
                lat = parseFloat(lt),
                lng = parseFloat(ln);

            var tr = $('<tr/>');
            tr.append("<td class='schoolName'>" + "<a   target='_blank' href='" + url + "'>" + name + "</a>" + "</td>");
            tr.append("<td class='schoolStreet'>" + medianValue + "</td>");
            $('#myTable').append(tr);

        })
    }




  

});

function searchFunction() {
    var input, filter, table, tr, td, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}