/*
Select locations that can serve point
*/
SELECT * 
FROM locations_isochrones
JOIN locations ON (locations.id = locations_isochrones.location_id)
WHERE 
    ST_Contains(
        locations_isochrones.isochrone, 
        ST_SetSRID(ST_MakePoint(-84.3143767,39.0722134),
        4326)
    );

/*
Select locations that serve the point and get the minimum time taken to do it
*/
SELECT DISTINCT id, MIN(interval)
FROM locations_isochrones
JOIN locations ON (locations.id = locations_isochrones.location_id)
WHERE 
    ST_Contains(
        locations_isochrones.isochrone, 
        ST_SetSRID(ST_MakePoint(-84.3143767,39.0722134),
        4326)
    )
GROUP BY id

/*
Select locations that serve the point within a time range
*/
SELECT id, MIN(interval)
FROM locations_isochrones
JOIN locations ON (locations.id = locations_isochrones.location_id)
WHERE 
    ST_Contains(
        locations_isochrones.isochrone, 
        ST_SetSRID(ST_MakePoint(-84.3143767,39.0722134),
        4326)
    )
	AND interval between 1800 and 3600
GROUP BY id