$.getJSON('https://code.org/schools.json', function (data) {
    console.log(data);




    // This is obtaining the information from a URL that has a page in JSON format. Variables are being assigned to the keys through
    //  a  for loop to iterate through each element and group the information accordingly to placed in a table which is shown below
    //  in the function "searchFunction()".

    for (i = 0; i <= data.schools.length; i++) {
        var name = data.schools[i].name,
            levels = data.schools[i].levels[i],
            website = data.schools[i].website,
            contact_number = data.schools[i].contact_number,
            contact_email = data.schools[i].contact_email,
            street = data.schools[i].street,
            city = data.schools[i].city,
            state = data.schools[i].state,
            zip = data.schools[i].zip;



        var tr = $('<tr/>');
        tr.append("<td class='schoolName'>" + "<a   target='_blank' href='" + website + "'>" + name + "</a>" + "</td>");
        tr.append("<td class='schoolStreet'>" + street + "</td>");
        tr.append("<td class='schoolCity'>" + city + "</td>");
        tr.append("<td class='schoolState'>" + state + "</td>");
        tr.append("<td class='schoolZip'>" + zip + "</td>");
        $('#myTable').append(tr);


    }

});

// This searchFunction is the same concept as the housetable.js function. The table is being made on a certain set of parameters
// for the columns. However, the function allows the table to be filtered in a dynamic way as the user si typing in the search input.

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