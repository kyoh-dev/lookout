<script>
	import { onMount } from 'svelte';
	import mapboxgl from 'mapbox-gl';

	mapboxgl.accessToken = process.env.MAPBOX_ACCESS_TOKEN;
	onMount(() => {
		const map = new mapboxgl.Map({
			container: 'map', // container ID
			style: 'mapbox://styles/mapbox/streets-v11', // style URL
			center: [-74.5, 40], // starting position [lng, lat]
			zoom: 9 // starting zoom
		});
	});
</script>

<svelte:head>
	<title>Lookout</title>
</svelte:head>

<div id="map"></div>

<style>
	#map {
		position: absolute;
		top: 0;
		bottom: 0;
		width: 100%;
	}
</style>
