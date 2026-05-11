Sorting items
=============
Sorting the items of an Array. This is not React specific, but mostly JavaScript.

See ``04-travel-list`` project.

We want to implement a sorting selector, which lets the items on the packing list
to be sorted by

    * input order
    * description
    * packed status

Solution:

.. code-block:: jsx
    :linenos:
    :emphasize-lines: 4, 6-14, 19

    function PackingList({ items, onDeleteItem, onToggleItem }) {
      const [sortBy, setSortBy] = useState("packed");

      let sortedItems = [];

      if (sortBy === "input") sortedItems = items;
      else if (sortBy === "description")
        sortedItems = items
          .slice()
          .sort((a, b) => a.description.localeCompare(b.description));
      else if (sortBy === "packed")
        sortedItems = items
          .slice()
          .sort((a, b) => Number(a.packed) - Number(b.packed));

      return (
        <div className="list">
          <ul>
            {sortedItems.map((item) => (
              <Item
                item={item}
                key={`item_${item.id}`}
                onDeleteItem={onDeleteItem}
                onToggleItem={onToggleItem}
              />
            ))}
          </ul>
          <div className="actions">
            <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
              <option value="input">Sort by input order</option>
              <option value="description">Sort by description</option>
              <option value="packed">Sort by packed status</option>
            </select>
          </div>
        </div>
      );
    }

:line 4:

    Using a new mutable variable for sorted items (``sortedItems``). This will be
    rendered in line 19.

:line 6 - 14:

    Create the elements for ``sortedItems``. If ``"input"``, use original order
    (which is by input order, oldest to newest). If ``"description"``, the items
    array is copied with ``slice()``, then the copy is sorted by the description
    value using the ``localCompare`` function. If it is ``"packed"``, the copy is
    sorted according to the numerical representation of the boolean values (
    True == 1, False == 0)  in ascending order, where ``False`` comes before ``True``.

.. hint::

    In ``sort((a, b) => {function})`` the ``function`` works as follows:

    ``a`` and ``b`` which are two consecutive values from the array, starting from
    first one, are fed to the function:

    * if it returns a **positive number** it means that **swapping is needed**,
      hence ``a`` must come after ``b``
    * if it returns a **negative number** it means that **no swapping is needed**,
      hence ``a`` stays before ``b``
    * if it returns **zero** both values are equal and their order remains as is
