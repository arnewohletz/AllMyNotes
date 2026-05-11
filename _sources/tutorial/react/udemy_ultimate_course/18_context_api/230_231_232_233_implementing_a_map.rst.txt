Include a map using the Leaflet library
=======================================
Install ``react-leaflet`` and ``leaflet``:

.. code-block::

    $ npm i react-leaflet leaflet

    .. hint::

        `Leaflet`_ is the most popular JavaScript library for implementing maps.
        `React Leaflet`_ is built on top of Leaflet.

On the `Installation`_ page refers to `Leaflet's Quick Start Guide`_, which states
that the following CSS code must be added to the project's main CSS file (``index.css``):

.. code-block:: css

     <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
     integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
     crossorigin=""/>

Next, we take the sample code from `React Leaflet`_ main page and copy it into our
*Map* component:

.. code-block:: jsx

    import { useNavigate, useSearchParams } from "react-router-dom";
    import styles from "./Map.module.css";
    import { MapContainer } from "react-leaflet/MapContainer";
    import { TileLayer } from "react-leaflet/TileLayer";
    import { Marker } from "react-leaflet/Marker";
    import { Popup } from "react-leaflet/Popup";
    import { useState } from "react";

    function Map() {
      const navigate = useNavigate();
      const [mapPosition, setMapPosition] = useState([40, 0]);
      const [searchParams, setSearchParams] = useSearchParams();
      const lat = searchParams.get("lat");
      const lng = searchParams.get("lng");

      return (
        <div className={styles.mapContainer}>
          <MapContainer
            center={mapPosition}
            zoom={13}
            scrollWheelZoom={true}
            className={styles.map}
          >
            <TileLayer
              attribution='&copy; <a href="https://www.openstreetmap.fr/hot/copyright">OpenStreetMap</a> contributors'
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <Marker position={mapPosition}>
              <Popup>
                A pretty CSS3 popup. <br /> Easily customizable.
              </Popup>
            </Marker>
          </MapContainer>
        </div>
      );
    }

    .. hint::

        By default the map element has a height of 0, so we assign our CSS class
        ``map`` to the ``<MapContainer>`` element which has an appropriate rule
        defined, to fix that.

.. _Leaflet: https://leafletjs.com/
.. _React Leaflet: https://react-leaflet.js.org/
.. _Installation: https://react-leaflet.js.org/docs/start-installation/
.. _Leaflet's Quick Start Guide: https://leafletjs.com/examples/quick-start/


Display city markers on map
---------------------------
The *CitiesContext* provides us the coordinates of our cities as global state.
We use it to create a marker on the map for each city, while also making the
*Popup* element on each marker show some meaningful data:

.. code-block:: jsx
    :emphasize-lines: 3,21,23-24,27-28,31

    function Map() {
      const navigate = useNavigate();
      const { cities } = useCities();
      const [mapPosition, setMapPosition] = useState([40, 0]);
      const [searchParams, setSearchParams] = useSearchParams();
      const lat = searchParams.get("lat");
      const lng = searchParams.get("lng");

      return (
        <div className={styles.mapContainer}>
          <MapContainer
            center={mapPosition}
            zoom={13}
            scrollWheelZoom={true}
            className={styles.map}
          >
            <TileLayer
              attribution='&copy; <a href="https://www.openstreetmap.fr/hot/copyright">OpenStreetMap</a> contributors'
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            {cities.map((city) => (
              <Marker
                position={[city.position.lat, city.position.lng]}
                key={city.id}
              >
                <Popup>
                  <span>{city.emoji}</span>
                  <span>{city.cityName}</span>
                </Popup>
              </Marker>
            ))}
          </MapContainer>
        </div>
      );
    }

.. hint::

    The ``<Popup>`` elements receive a classname from Leaflet that you can use to
    customize its style, for example:

    .. code-block:: css

        :global(.leaflet-popup .leaflet-popup-content-wrapper) {
          background-color: var(--color-dark--1);
          color: var(--color-light--2);
          border-radius: 5px;
          padding-right: 0.6rem;
        }

    The ``:global(...)`` operator is used to make the style apply to **all** components
    which may use this class, not just the one component the CSS module is assigned
    to. Without it, in our case, the rules will not apply to any of the ``<Popup>``
    elements.

    As mentioned in :ref:`tutorial_react_ultimate_use_css_modules`, by default
    the compiler attaches a random ID to the classname of the CSS rule as well as
    the rendered component, effectively preventing the style to apply to any other
    equally named rules in other component's CSS classes. Using ``:global`` prevent
    this *mangling*, applying the style to all other components assigned to this class
    (here: ``.leaflet-popup .leaflet-popup-content-wrapper``).

Interacting with the map
------------------------
First, we'll use the latitude and longitude from the URL, which is to center the map
to the currently selected city:

.. code-block:: jsx
    :emphasize-lines: 6-7,12

    function Map() {
      const navigate = useNavigate();
      const { cities } = useCities();
      const [mapPosition, setMapPosition] = useState([40, 0]);
      const [searchParams, setSearchParams] = useSearchParams();
      const mapLat = searchParams.get("lat");
      const mapLng = searchParams.get("lng");

      return (
        <div className={styles.mapContainer}>
          <MapContainer
            center={[mapLat, mapLng]}
            zoom={6}
            scrollWheelZoom={true}
            className={styles.map}
          >
          {/* more stuff */}
          </MapContainer>
        </div>
      );
    }

But when selecting a different city, the map does not update, as the ``mapLat`` and
``mapLng`` are not reactive, so not updating after selecting another city.

*react-leaflet* provides a ``useMap`` hook (https://react-leaflet.js.org/docs/api-map/#usemap),
which returns a ``Map`` component. We will use it to create a custom Map component,
which uses ``mapLat`` and ``mapLng`` as state:

.. code-block:: jsx
    :emphasize-lines: 1,20,26-30

    import { useMap } from 'react-leaflet/hooks'

    function Map() {
      const navigate = useNavigate();
      const { cities } = useCities();
      const [mapPosition, setMapPosition] = useState([40, 0]);
      const [searchParams, setSearchParams] = useSearchParams();
      const mapLat = searchParams.get("lat");
      const mapLng = searchParams.get("lng");

      return (
        <div className={styles.mapContainer}>
          <MapContainer
            center={[mapLat, mapLng]}
            zoom={6}
            scrollWheelZoom={true}
            className={styles.map}
          >
            {/* other stuff */}
            <ChangeCenter position={[mapLat, mapLng]} />
          </MapContainer>
        </div>
      );
    }

    function ChangeCenter({ position }) {
      const map = useMap();
      map.setView(position);
      return null;
    }

Although the ``ChangeCenter`` does not return any JSX (``null``, which is a valid
return value), it makes the ``mapLat`` and ``mapLng`` become state variables of the
``ChangeCenter``, which is rendered by ``Map``.

The problem is, that ``mapLat`` and ``mapLng`` are **not** remembered, as the URL
does not include them when going back to the ``/cities`` endpoint. We want them to
stay saved inside the ``mapPosition``. For this, we create an effect, which runs
whenever either ``mapLat`` or ``mapLng`` changes (if those exits, so are not ``null``),
updating the ``mapPosition`` state:

.. code-block:: jsx
    :emphasize-lines: 3-8,13

    function Map() {
      {/* other stuff */}
      useEffect(
        function () {
          if (mapLat && mapLng) setMapPosition([mapLat, mapLng]);
        },
        [mapLat, mapLng],
      );

      return (
        <div className={styles.mapContainer}>
          <MapContainer
            center={mapPosition}
            zoom={6}
            scrollWheelZoom={true}
            className={styles.map}
          >
            {/* other stuff */}
            <ChangeCenter position={[mapLat, mapLng]} />
          </MapContainer>
        </div>
      );
    }

The last feature we want is to display the form whenever we click on some point
on the map. As the ``<MapContainer>`` component does **not** include a ``onClick``
handler, we must create yet another custom component, which provides the functionality.
For this, we use the ``useMapEvents`` hook from *leaflet-react*:

.. code-block:: jsx
    :emphasize-lines: 1,16,22-25

    import { useMap, useMapEvents } from "react-leaflet/hooks";

    function Map() {
      {/* other stuff */}

      return (
        <div className={styles.mapContainer}>
          <MapContainer
            center={mapPosition}
            zoom={6}
            scrollWheelZoom={true}
            className={styles.map}
          >
            {/* other stuff */}
            <ChangeCenter position={[mapLat, mapLng]} />
            <DetectClick />
          </MapContainer>
        </div>
      );
    }

    function DetectClick() {
      const navigate = useNavigate();
      useMapEvents({ click: (e) => navigate(`form`) });
    }

We move the ``useNavigate()`` hook from the *<Map>* component into the *<DetectClick>*
component, as we want to navigate to the form at the event of a click.

As we want the form to have the position information of the current click. For this,
we will include this information in the ``/form`` URL so the form can read it
(it is far more less work than saving the position in a temporary global variable):

.. code-block:: jsx
    :emphasize-lines: 4

    function DetectClick() {
      const navigate = useNavigate();
      useMapEvents({
        click: (e) => navigate(`form/?lat=${e.latlng.lat}&lng=${e.latlng.lng}`),
      });
    }

The event-object provides the ``latlng`` property, containing the latitude and
longitude of the click. The data will be written into the form later.

Setting map position with geolocation
-------------------------------------
Modern browsers natively support provision of the current geolocation, using the
:javascript:`navigator.geolocation` attribute. Previously, we defined the custom
``useGeolocation`` hook in a challenge:

.. code-block:: jsx
    :emphasize-lines: 3,5

    import { useState } from "react";

    export function useGeolocation(defaultPosition = null) {
      const [isLoading, setIsLoading] = useState(false);
      const [position, setPosition] = useState(defaultPosition);
      const [error, setError] = useState(null);

      function getPosition() {
        if (!navigator.geolocation)
          return setError("Your browser does not support geolocation");

        setIsLoading(true);
        navigator.geolocation.getCurrentPosition(
          (pos) => {
            setPosition({
              lat: pos.coords.latitude,
              lng: pos.coords.longitude,
            });
            setIsLoading(false);
          },
          (error) => {
            setError(error.message);
            setIsLoading(false);
          },
        );
      }

      return { error, isLoading, position, getPosition };
    }

The only difference is that we add the ``default_position`` argument to be the
initial ``position``.

We can now use the hook to be called inside the *<Map>* component, adding a button,
which triggers the hook's ``getPosition`` function:

.. code-block:: jsx
    :emphasize-lines: 1-2,8-12,18-20

    import Button from "./Button";
    import { useGeolocation } from "../hooks/useGeolocation";

    function Map() {
      const { cities } = useCities();
      const [mapPosition, setMapPosition] = useState([40, 0]);
      const [searchParams, setSearchParams] = useSearchParams();
      const {
        isLoading: isLoadingPosition,
        position: geolocationPosition,
        getPosition,
      } = useGeolocation();
      const mapLat = searchParams.get("lat");
      const mapLng = searchParams.get("lng");

      return (
        <div className={styles.mapContainer}>
          <Button type="position" onClick={getPosition}>
            {isLoadingPosition ? "Loading..." : "Use your position"}
          </Button>
          {/* more stuff */}
        </div>
      );
    }

The state is already set, now this state is supposed to navigate to the map to
this position by updating the ``mapPosition`` state. As we use our custom hook,
we create another effect to do that:

.. code-block:: jsx
    :emphasize-lines: 5-11

    function Map() {

      {/* more stuff */}

      useEffect(
        function () {
          if (geolocationPosition)
            setMapPosition([geolocationPosition.lat, geolocationPosition.lng]);
        },
        [geolocationPosition],
      );

      {/* more stuff */}

    }

    .. hint::

        Generally, it is recommended to use as little effects as possible, as each
        forces a re-render. More on this in the next chapter.
