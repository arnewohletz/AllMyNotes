Creating a reusable Component
=============================
A reusable component must

    * be independent from other components
    * contain its own style (no external CSS)

It is created by the **component creator** and consumed by the **component consumer**,
which usually are different persons.

The creator decides which **props** the component accepts (defines the public API of
the component), allowing some configuration, for which the consumer chooses the
**values** when using it.

Too few props

    * make the component not **flexibel** enough
    * making it **useless**

Too many props

    * make the component too **hard to use**
    * exposes **too much complexity**
    * having a hard-to-write code
    * requires setting default values

**Right amount of props is important**.

.. important::

    **Initialize state variable from a prop value**

    It is allowed to initialize state variables using prop values, if this state
    variable **is not** supposed to stay in sync with the props. For instance,

    .. code-block:: jsx
        :emphasize-lines: 6, 8

        export default function StarRating({
          maxRating = 5,
          color = "#fcc419",
          size = 48,
          className = "",
          messages = [],
          defaultRating = 0,
        }) {
          const [rating, setRating] = useState(defaultRating);
          const [tempRating, setTempRating] = useState(0);

    sets the initial value of ``rating`` to the value passed into the ``defaultRating``
    prop. This is fine, as the state variable is not supposed to update, if the
    prop value is updated. It is only supposed to be set once, as long a no value
    for ``rating`` is set.

**Passing a state setter function as prop**

It may be necessary to pass a state setter function into a component in order to
allow some state outside the component to be updated as well, e.g. in this example
the ``movieRating`` state variable needs to be updated as well (the ``rating`` state
variable is only available inside the component``):

.. code-block:: jsx
    :emphasize-lines: 2,7

    function Test() {
      const [movieRating, setMovieRating] = useState(0);

      return (
        <div>
          <StarRating color="blue" maxRating={10} onSetRating={setMovieRating} />
          <p>This movie was rated {movieRating} stars.</p>
        </div>
      );
    }

To do so, the component must accept a ``onSetRating`` prop (value must be a function)
and call the function when calling its own rating setter method:

.. code-block:: jsx
    :emphasize-lines: 8,16

    export default function StarRating({
      maxRating = 5,
      color = "#fcc419",
      size = 48,
      className = "",
      messages = [],
      defaultRating = 0,
      onSetRating,
    }) {

      const [rating, setRating] = useState(defaultRating);
      const [tempRating, setTempRating] = useState(0);

      function handleRating(rating) {
        setRating(rating);
        onSetRating(rating);
      }

    /* more stuff */
    }