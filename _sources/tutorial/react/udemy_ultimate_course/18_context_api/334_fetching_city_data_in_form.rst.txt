Fetching city data in the form
==============================
To fetch the form data from the URL to populate the *Form* component whenever we
click on the *Map*, we will create a new custom hook:

.. code-block:: jsx

    import { useSearchParams } from "react-router-dom";

    export function useUrlPosition() {
      const [searchParams, setSearchParams] = useSearchParams();
      const lat = searchParams.get("lat");
      const lng = searchParams.get("lng");

      return [lat, lng];
    }

.. note::

    The ``useUrlPosition`` hook relies on the ``useSearchParam()`` hook, provided
    by React-Router. The hook is supposed to be generic and reusable, whenever we
    need the position from the URL.

We import this function into our *App* component, replacing the previous lines,
which are now moved to ``useUrlPosition``:

.. code-block:: jsx
    :emphasize-lines: 10

    function Map() {
      const { cities } = useCities();
      const [mapPosition, setMapPosition] = useState([40, 0]);
      const {
        isLoading: isLoadingPosition,
        position: geolocationPosition,
        getPosition,
      } = useGeolocation();
      const [mapLat, mapLng] = useUrlPosition();

      {/* other stuff */}

    }

same as to the *Form* component:

.. code-block:: jsx
    :emphasize-lines: 2

    function Form() {
      const [latPos, lngPos] = useUrlPosition

      {/* other stuff */}

    }

In the *Form* component, we then define an effect function to fetch the data:

.. code-block:: jsx
    :emphasize-lines: 1,9,10-19

    const BASE_URL = "https://api.bigdatacloud.net/data/reverse-geocode-client";

    function Form() {
      const [lat, lng] = useUrlPosition();
      const navigate = useNavigate();
      const [cityName, setCityName] = useState("");
      const [country, setCountry] = useState("");
      const [date, setDate] = useState(new Date());
      const [notes, setNotes] = useState("");
      const [isLoadingGeolocation, setIsLoadingGeolocation] = useState();
      useEffect(
        function () {
          async function fetchCityData() {
            try {
              setIsLoadingGeolocation(true);
              console.log(lat, lng);
              const res = await fetch(
                `${BASE_URL}?latitude=${lat}&longitude=${lng}`,
              );
              const data = await res.json();
              setCityName(data.city || data.locality || "");
              setCountry(data.countryName);
            } catch (err) {
            } finally {
              setIsLoadingGeolocation(false);
            }
          }
          fetchCityData();
        },
        [lat, lng],
      );

      {/* other stuff */}

    }
