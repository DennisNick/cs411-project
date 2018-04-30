// If you're adding a number of markers, you may want to drop them on the map
// consecutively rather than all at once. This example shows how to use
// window.setTimeout() to space your markers' animation.

var neighborhoods = [
  {lat: 52.511, lng: 13.447},
  {lat: 52.549, lng: 13.422},
  {lat: 52.497, lng: 13.396},
  {lat: 52.517, lng: 13.394}
];


var markers = [];
var map;

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 12,
    center: {lat: 52.520, lng: 13.410}
  });
}

function drop() {
  clearMarkers();
  for (var i = 0; i < neighborhoods.length; i++) {
    addMarkerWithTimeout(neighborhoods[i], i * 200, i.toString(),"http://something", i.toString());
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
   document.getElementById("article_title").innerHTML = "News Article: " + marker.title;
  document.getElementById("article_location").innerHTML = marker.url;
  document.getElementById("article_blurb").innerHTML = marker.abstract;
  document.getElementById("article_save").style.visibility = "visible";
  document.getElementById("article_save_button").style.visibility = "visible";
}

function save(){

}
