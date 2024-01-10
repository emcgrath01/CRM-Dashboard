document.addEventListener('DOMContentLoaded', function() {
    var map = L.map('map').setView([0, 0], 2); // Initialize the map

    // Add a tile layer to display the map
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
        maxZoom: 18,
    }).addTo(map);

    // Fetch your GeoJSON file (replace 'your_geojson_file.json' with the actual file path)
    fetch('.venv/templates/output.geojson')
        .then(response => response.json())
        .then(data => {
            // Loop through each feature in the GeoJSON file
            data.features.forEach(feature => {
                // Extract polygon coordinates
                var polygonCoordinates = feature.geometry.coordinates[0][0]; // Access the coordinates from the nested structure
                
                // Log the coordinates to check
                console.log('Coordinates:', polygonCoordinates);

                // Create a Leaflet polygon layer
                var polygon = L.polygon(polygonCoordinates, {
                    color: 'red', // Set the color of the polygon border
                    fillColor: 'orange', // Set the fill color
                    fillOpacity: 0.5 // Set the opacity of the fill
                }).addTo(map);
            });

            // Fit the map view to the bounds of all polygons
            var group = new L.featureGroup(Object.values(map._layers));
            map.fitBounds(group.getBounds());
        })
        .catch(error => {
            console.error('Error fetching GeoJSON:', error);
        });
});
