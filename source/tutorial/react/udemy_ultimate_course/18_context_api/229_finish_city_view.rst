Finish the city view
====================
The cities data is supposed to be requested from ``http://localhost:8000/cities/<CITY_ID>``.
The data **cannot be stored as local state** using ``useState()`` inside each displayed
``City`` component, as the state needs to be available outside of the component
as well to mark the *currentCity* in the list of cities (green border) -> it is *global state*,
**as multiple components need it**.

.. hint::

    If state is only used inside one component, always make it local state, not global.

We add it to our ``CityContext.jsx`` and pass it into the context:

.. code-block:: jsx
    :emphasize-lines: 4,9

    function CitiesProvider({ children }) {
      const [cities, setCities] = useState([]);
      const [isLoading, setIsLoading] = useState(false);
      const [currentCity, setCurrentCity] = useState({});

      {/* other stuff */}

      return (
        <CitiesContext.Provider value={{ cities, isLoading, currentCity }}>
          {children}
        </CitiesContext.Provider>
      );
    }

Next, we create a ``getCity()`` function inside our ``CitiesProvider`` to load the
city data (very similar to the ``fetchCities()`` function) and pass it into the
*Provider* via ``value``:

.. code-block::
    :emphasize-lines: 5-16,19

    function CitiesProvider({ children }) {

      {/* other stuff */}

      async function getCity(id) {
        try {
          setIsLoading(true);
          const res = await fetch(`${BASE_URL}/cities/${id}`);
          const data = await res.json();
          setCurrentCity(data);
        } catch {
          alert("There was an error loading data");
        } finally {
          setIsLoading(false);
        }
      }

      return (
        <CitiesContext.Provider value={{ cities, isLoading, currentCity, getCity }}>
          {children}
        </CitiesContext.Provider>
      );

    }

.. hint::

    The ``getCity()`` could also be put into the ``City`` component, but it is
    considered cleaner to have the state-updating logic at one place.

Next, we can use the getter-function and ``currentCity`` state variable inside the
*City* component (replacing the placeholder data):

.. code-block:: jsx
    :emphasize-lines: 1,5

    import { useCities } from "../contexts/CitiesContext";

    function City() {
      const { id } = useParams();
      const { getCity, currentCity } = useCities();

      // TEMP DATA
      // const currentCity = {
      //   cityName: "Lisbon",
      //   emoji: "🇵🇹",
      //   date: "2027-10-31T15:59:59.138Z",
      //   notes: "My favorite city so far!",
      // };

      {/* other stuff */}
    }

The ``getCity`` function is then called inside an effect (the ``id`` comes from the URL),
which runs when the component is initially rendered:

.. code-block:: jsx
    :emphasize-lines: 7-12

    import { useCities } from "../contexts/CitiesContext";

    function City() {
      const { id } = useParams();
      const { getCity, currentCity } = useCities();

      useEffect(
        function () {
          getCity(id);
        },
        [id],
      );

      {/* other stuff */}
    }

Relying the effect to re-run, once the ``id`` changes is important, so that when
a different city is selected, it fetches the data for the new city.

To optimize, as the previous ``currentCity`` data is still displayed until the data
of the new city has been fetched, we want to add a loading spinner.

For this, we will use the ``isLoading`` state from our ``useCities`` hook:

.. code-block:: jsx
    :emphasize-lines: 3,7

    function City() {
      const { id } = useParams();
      const { getCity, currentCity, isLoading } = useCities();

      {/* other stuff */}

      if (isLoading) return <Spinner />;

      return (
        {/* regular return JSX */}
      )
    }

.. important::

    The second ``return`` statement must be put **after** the effect, as close to
    the regular ``return`` as possible.

Next up, we want to mark the current city via a colored border in the cities list
(the reason we made ``currentCity`` global state in the first place).

Inside the *CityItem* component, we add a conditional styling in case the ``id``
matches ``currentCity``'s id:

.. code-block:: jsx
    :emphasize-lines: 3,7

    function CityItem({ city }) {
      const { cityName, emoji, date, id, position } = city;
      const { currentCity } = useCities();
      return (
        <li>
          <Link
            className={`${styles.cityItem} ${id === currentCity.id ? styles["cityItem--active"] : ""}`}
            to={`${id}?lat=${position.lat}&lng=${position.lng}`}
          >
            <span className={styles.emoji}>{emoji}</span>
            <h3 className={styles.name}>{cityName}</h3>
            <time className={styles.date}>{formatDate(date)}</time>
            <button className={styles.deleteBtn}>&times;</button>
          </Link>
        </li>
      );
    }

.. note::

    Here we cannot use dot-notation (:javascript:`${styles.cityItem--active}`)
    due to the dashes (``--``), but we must refer to it via
    :javascript:`styles["cityItem--active"]`.

Lastly, we want to make a *BackButton* component (we already defined such a button
inside ``Form.jsx``, but we probably need it more often). The new ``BackButton.jsx``:

.. code-block:: jsx

    import { useNavigate } from "react-router-dom";
    import Button from "./Button";

    function BackButton() {
      const navigate = useNavigate();

      return (
        <Button
          type="back"
          onClick={(e) => {
            e.preventDefault();
            navigate(-1);
          }}
        >
          &larr; Back
        </Button>
      );
    }

    export default BackButton;

The we use it in both ``Form.jsx`` and ``City.jsx`` via ``<BackButton />``.
