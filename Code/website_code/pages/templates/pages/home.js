const attractions = {{ Attractions | safe }}; // Assuming attractions is a list of Django model objects

var CartoDB_Voyager = L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    subdomains: 'abcd',
    maxZoom: 20
});

const osm_options = {
    maxZoom: 19,
    noWrap: true,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
};

const osmMap = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', osm_options);

// Define the bounds for Salzburg
const bounds = L.latLngBounds(
    L.latLng(47.60949000, 13.35501000),   // Southwest corner of the bounding box
    L.latLng(47.86, 12.801000) // Northeast corner of the bounding box
);

const mapElement = 'map'; // Change var to const for better scoping
// My Map 
const mymap = L.map(mapElement, {
    center: [47.811195, 13.033229],
    zoom:11,
    minZoom: 12,
    zoomSnap: 0.25,
    zoomDelta: 0.25,
    easelinearity: 0.2,
    worldcopyjump: true,
    layers: [CartoDB_Voyager],
    maxBounds: bounds // Set the maximum bounds
});

// Add a marker for the user's current position
function onLocationFound(e) {
    const radius = e.accuracy / 2;

    L.marker(e.latlng).addTo(mymap)
        .bindPopup("You are here").openPopup();

    L.circle(e.latlng, radius).addTo(mymap);
}

// Handle errors if geolocation is not supported or user denies permission
function onLocationError(e) {
    alert(e.message);
}

// Request user's location
mymap.on('locationfound', onLocationFound);
mymap.on('locationerror', onLocationError);

mymap.locate({ setView: true, maxZoom: 13 }); // Request the user's location and set the map's view
// Loop through all attractions
attractions.forEach(function(attraction) {
    const address = attraction.address;
    fetch('https://nominatim.openstreetmap.org/search?format=json&q=' + encodeURIComponent(address))
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            if (data.length > 0 && data[0].lat && data[0].lon) {
                const lat = data[0].lat;
                const lon = data[0].lon;
                const marker = L.marker([lat, lon]).addTo(mymap)
                   
                    .bindTooltip(attraction.title); // Show the attraction title as popup content
                    

                // Construct the URL dynamically based on the title
                const attractionSlug = attraction.title.toLowerCase().replace(/\s+/g, '-');
                const attractionDetailURL = '/attractions/' + attractionSlug + '/';

                // Add event listener for click event
                marker.on('click', function() {
                    // Redirect to the attraction detail page URL
                    window.location.href = attractionDetailURL;
                });
            } else {
                console.log('Invalid address:', address);
            }
        })
        .catch(function(error) {
            console.log('Error fetching address coordinates:', error);
        });
});