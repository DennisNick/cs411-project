// If you're adding a number of markers, you may want to drop them on the map
// consecutively rather than all at once. This example shows how to use
// window.setTimeout() to space your markers' animation.

//var neighborhoods = [
//  {lat: 52.511, lng: 13.447},
//  {lat: 52.549, lng: 13.422},
//  {lat: 52.497, lng: 13.396},
//  {lat: 52.517, lng: 13.394}
//];

//var myData = {{article_list|json}};
//console.log(myData);

//{{ "Title: " }}{{article.0}},<br> {{ "Location: " }}{{article.1}}, <br>{{ "Link: " }}{{article.2}}{{ "Coord: " }}{{ article.3 }}

var markers = [];
var map;

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 2,
    center: {lat: 52.520, lng: 13.410}
  });
}
//
function drop(neighborhood, title, url, abstract) {
  clearMarkers();
  for (var i = 0; i < 10; i++) {
      try {
          addMarkerWithTimeout(neighborhood[i], i * 200, title[i], url[i], abstract[i]);
      }
      catch(err){
          console.log("Could not find article with index " + i);
      }
  }
}

function addMarkerWithTimeout(position, timeout, title, url, abstract) {
  window.setTimeout(function() {
    var marker = (new google.maps.Marker({
      position: position,
      map: map,
      animation: google.maps.Animation.DROP,
        title: title,
        url: url,
        abstract: abstract

    }));
    markers.push(marker);
    marker.addListener('click', function() {
		clickMarkerEvent(marker, position);
	});
  }, timeout);
}

function clearMarkers() {
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(null);
  }
  markers = [];
}

function clickMarkerEvent(marker, position){
  document.getElementById("article_title").innerHTML = marker.title;
  document.getElementById("article_location").innerHTML = marker.url;
  document.getElementById("article_blurb").innerHTML = marker.abstract;
  document.getElementById("article_save").style.visibility = "visible";
  document.getElementById("article_save_button").style.visibility = "visible";
  document.getElementById("article_store").value = marker.title;
}

function save(){
    var title =  document.getElementById("article_title").innerHTML;
    var url = document.getElementById("article_location").innerHTML;

    var form = document.createElement("form");
    form.setAttribute("method", "POST");
    form.setAttribute("action", "/store_article/");
    var hiddenField = document.createElement("input");
    hiddenField.setAttribute("type", "hidden");
    hiddenField.setAttribute("name", title);
    hiddenField.setAttribute("value", url);
    form.appendChild(hiddenField);

    $.ajax({
        datatype: "json",
        type: "post",
        url: "/store_article/",
        data: {
                'title': title
              },
    success: function(msg){alert('wow ' + msg)}});
}
