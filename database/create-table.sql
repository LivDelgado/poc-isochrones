/*
Setting up database
*/

CREATE EXTENSION IF NOT EXISTS postgis;

SELECT postgis_full_version();

-- We are not using pgrouting in this version
-- CREATE EXTENSION IF NOT EXISTS pgrouting;

/*
Information table
*/
CREATE TABLE Stores (
  id integer PRIMARY KEY, 
  address_street varchar(50),
  zip_code varchar(10),
  address_state varchar(5),
  address_city varchar(50),
  coordinates Geometry(Point, 4326)
);

/*
Isochrone table
*/
CREATE TABLE Stores_Isochrones (
  location_id integer REFERENCES Stores (id),
  interval integer,
  isochrone Geometry(Polygon, 4326),
  PRIMARY KEY (location_id, interval)
)