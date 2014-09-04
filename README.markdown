Shibboleth python integration demo
==================================

What is where
-------------

* The `app.wsgi` file is the wsgi application loaded by apache's `mod_wsgi`
* The `contrib` folder contains configurations file to override the default
  configuration of the container.
* The `demo.py` file contains the whole Flask based demo web app.
* The `Dockerfile` file is used to create the server image with Apache and the
  Shibboleth daemon preinstalled and configured. The demo python webapp is
  expected to be available at `/src/pyshib/app.wsgi`.
* `ibe-check-divio-testing` is the sample metadata which was loaded to
  https://www.testshib.org
* The `templates` folder contains the html templates used by the demo webapp.


How to build and run
--------------------

Just build the image using docker:

    docker build -t shibdemo .

And then run it:

    docker run -it -p 80:80 -v $(pwd):/src/pyshib shibdemo

You can now access the demo at http://dev/

Note: the demo is configured to be available at the `dev` hostname. Changes
are needed to the apache and shibboleth configuration in `contrib` to make
everything work from `localhost`.
