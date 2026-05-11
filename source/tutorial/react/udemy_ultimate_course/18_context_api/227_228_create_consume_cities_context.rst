Creating a CitiesContext
========================
Context files should be put into a separate ``./contexts`` folder (inside ``src``).
The new ``CitiesContext.jsx`` file will receive all state and state-updating logic
from the *App* component (``App.jsx``):

.. code-block:: jsx

    const { createContext, useState, useEffect } = require("react");

    const CitiesContext = createContext();
    const BASE_URL = "http://localhost:8000";

    function CitiesProvider({ children }) {
      const [cities, setCities] = useState([]);
      const [isLoading, setIsLoading] = useState(false);

      useEffect(function () {
        async function fetchCities() {
          try {
            setIsLoading(true);
            const res = await fetch(`${BASE_URL}/cities`);
            const data = await res.json();
            setCities(data);
          } catch {
            alert("There was an error loading data");
          } finally {
            setIsLoading(false);
          }
        }
        fetchCities();
      }, []);
    }

Next, we can remove the props that the *App* component passes down its rendering
components (it will be made available inside the context later).

And now, we make the ``CitiesProvider`` return the ``CitiesContext.Provider`` passing
along the required state variables as props and also the ``{children}`` prop (in
order to pass down any component to be enclosed into the ``<CitiesProvider>``:

.. code-block:: jsx
    :emphasize-lines: 5-9

    function CitiesProvider({ children }) {

      {/* other stuff */}

      return (
        <CitiesContext.Provider value={{ cities, isLoading }}>
          {children}
        </CitiesContext.Provider>
      );
    }

Now we are able to enclose the *App* components returning JSX into ``<CitiesProvider>``:

.. code-block:: jsx
    :emphasize-lines: 3,7

    function App() {
      return (
        <CitiesProvider>
          <BrowserRouter>
            {/* all my other JSX */}
          </BrowserRouter>
        </CitiesProvider>
      );
    }

Consuming the CitiesContext
===========================
As before, we first create the custom hook ``useCities`` to provide the ``CitiesContext``,
instead of relying on the ``useContext`` hook:

.. code-block:: jsx

    function useCities() {
      const context = useContext(CitiesContext);
      if (context === undefined)
        throw new Error("CitiesContext was used outside the CitiesProvider");
      return context;
    }

    export { CitiesProvider, useCities };

and use it in any component that relies on the ``cities`` state and/or the
``isLoading`` state-setting function, such as ``CitiesList`` and ``CountryList``,
removing the previously passed in props:

.. code-block:: jsx
    :emphasize-lines: 1,3,4

    import { useCities } from "../../contexts/CitiesContext";

    function CityList() {
      const { cities, isLoading } = useCities();

      if (isLoading) {
        return <Spinner />;
      }
      if (!cities.length)
        return (
          <Message message="Add your first city by clicking on a city on the map" />
        );
      return (
        <ul className={styles.cityList}>
          {cities.map((city) => (
            <CityItem city={city} key={city.id} />
          ))}
        </ul>
      );
    }
