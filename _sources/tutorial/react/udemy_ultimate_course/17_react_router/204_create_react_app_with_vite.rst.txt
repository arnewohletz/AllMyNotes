Create React App using Vite
===========================
#. Run

    .. code-block:: none

        $ npm create vite@latest

    .. hint::

        To use a specific version, e.g. version 4, use ``vite@4``.

#. Give a project name (here: worldwise).
#. Select the framework (here: React).
#. Select a variant (here: JavaScript).
#. Install the dependencies, here:

    .. code-block:: none

        $ cd worldwise
        $ npm install

    .. hint::

        Vite installs far less packages than create-react-app, hence installation is faster.

        Vite installs some important libraries and tools, though, including ESLint.

        The folder structure differs a bit in comparison to create-react-app.
        Also, it uses ``.jsx`` instead of ``*.js`` files.

#. To start the application run

    .. code-block:: none

        $ npm run dev

#. Install and configure ESLint (requires ESLint Plugin is installed in your IDE, e.g. VS Code):

    .. important::

        This step might not necessary when using latest version of vite, as it is
        already preconfigured.

    .. code-block:: none

        $ npm install eslint vite-plugin-eslint eslint-config-react-app

    Inside the project, delete ``.eslintrc.cjs``, create the file ``.eslintrc.cjs``
    and insert the following content:

    .. code-block:: json

        {
          "extends": "react-app"
        }

#. Add ESLint plugin inside ``vite.config.js``:

    .. code-block:: js
        :emphasize-lines: 3,7

        import { defineConfig } from "vite";
        import react from "@vitejs/plugin-react";
        import eslint from "vite-plugin-eslint";

        // https://vitejs.dev/config/
        export default defineConfig({
          plugins: [react(), eslint()],
        });

    .. hint::

        If things don't work try installing ``@nabla/vite-plugin-eslint`` instead of
        ``vite-plugin-eslint`` and use this config:

        .. code-block:: javascript
            :emphasize-lines: 3,7

            import { defineConfig } from "vite";
            import react from "@vitejs/plugin-react";
            import eslintPlugin from "@nabla/vite-plugin-eslint";

            // https://vitejs.dev/config/
            export default defineConfig({
              plugins: [react(), eslintPlugin()],
            });

