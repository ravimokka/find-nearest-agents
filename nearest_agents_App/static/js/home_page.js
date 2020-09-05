var tableData = ''
var find_tableData = ''
var row_id =''
var ag_dis = ''


$(document).ready(function(){
 $('.find_allAgents').hide();
 $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".table tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
    LoadPlaceDataAPI();
    $(document).on("click",".table_dataSet tbody tr td button.btn-find", function() { // any button
       $('.table_dataSet').hide();
        ag_dis = "";
        ag_dis = $(this).attr('ag_dis');
        var data = {}
        data['ag_dis'] = ag_dis;
        findNearestAgents(data);
        $('.find_allAgents').show();
    });

$("#btn_back").click(function() {
      $('.find_allAgents').hide();
        $('.table_dataSet').show();
    });


});

function LoadPlaceDataAPI(){
data = "test"
$.ajax({
           url: "/api/places",
           type: "GET",
           contentType: 'application/json',
           data: JSON.stringify(data),
           success: function(data, testStatus, jqXHR){
           var table_data = data.data
           tableData = data.data
           renderPlaceList(table_data)
           },
           error: function(response){
             alert("Error:" + response);
           }
        });
}

function findNearestAgents(data){
$.ajax({
           url: "/api/findAgents",
           type: "POST",
           contentType: 'application/json',
           data: JSON.stringify(data),
           success: function(data, testStatus, jqXHR){
           var table_data = data.data
           find_tableData = data.data
           renderFindList(table_data)
           alert('Find all nearest agents successfully!')

           },
           error: function(response){
             alert("Error:" + response);
           }
        });
}

function renderPlaceList(data){
       var data_view = $('.place_data');
     data_view.find('tr').remove();
       if (data.length > 0){
            var i;
            var sno = 0;
            for(i = 0; i < data.length; ++i) {
                 var clone = $('#template .place-form-list .place-row-form').clone();
                var sno = sno+1;
                $('.sno', clone).text(sno);
                $('.place_name', clone).text(data[i]['place_name']);
               var agents = '<button type="button"  class="btn btn-info btn-find"  row_id ="'+data[i]['place_id']+'" ag_dis ="'+data[i]['distance']+'"><a href="#">find nearest agents</a></button>'
                 $('.find_agents', clone).append(agents);
                data_view.append(clone);
            }
       }
}









function renderFindList(data){
     var data_view = $('.find_data');
     data_view.find('tr').remove();
       if (data.length > 0){
            var i;
            var sno = 0;
            for(i = 0; i < data.length; ++i) {
                var clone = $('#find_template .find-form-list .find-row-form').clone();
                var sno = sno+1;
                $('.sno', clone).text(sno)
                $('.id', clone).text(data[i]['ID'])
                $('.name', clone).text(data[i]['NAME'])
                $('.city', clone).text(data[i]['CITY'])
                $('.address', clone).text(data[i]['ADDRESS'])
                $('.zip_code', clone).text(data[i]['ZIPCODE'])
                $('.state', clone).text(data[i]['STATE'])
                data_view.append(clone);
            }
       }
}




