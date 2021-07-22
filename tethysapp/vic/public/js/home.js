const home_control = (function(){
	var map_request, init_map, init_all;
	var map;
	let public_interface;

	init_map = function () {
		const raster = new ol.layer.Tile({
            source: new ol.source.OSM()
        });
        map = new ol.Map({
            layers: [raster],
            target: "map",
            view: new ol.View({
                center: [0, 0],
                zoom: 2
            })
        });
	};

	init_all = function ()  {
		init_map();
	};

	/*
    * PUBLIC INTERFACE
    */
    public_interface = {};

    /*

    * INITIALIZATIONS
    */
    $(function () {
    	init_all();
    });

    return public_interface;
}());