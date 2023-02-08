# pokeberries

This repo has three endpoints:

`/health` verifies the status of the service
`/allBerryStats` gets this data structure form poke endpoint:
```
{
    "berries_names": [...],
    "min_growth_time": "",
    "median_growth_time": "",
    "max_growth_time": "",
    "variance_growth_time": "",
    "mean_growth_time": "",
    "frequency_growth_time": ""
}
```
`/histogram` returns the `HTML` code needed to see the berries data in a histogram graph. Since the endpoint has the header `Content-Type: application/json` to render the HTML correctly copy and paste the generated HTML code to a `.html` file and load it in a browser. It comes with all the resources built-in.


### Run
To execute the app:
- `make run`: builds the docker image and starts the app
- `make test`: builds the test image and runs the tests inside the container

### Goal
The objective of the project was to pull data from https://pokeapi.co/docs/v2#berries to get some stats about berries.

### Description of the implementation
The project is written in Python. The stack includes:

- `Flask` as REST framework
- `gunicorn` as web server (ready for prod)
- `requests` to fetch the endpoints where the berries information can be found
- `asyncio` & `aiohttp` to do async requests to get the data from the berries
- `marshmallow` to serialize the data from the endpoints
- `make` to automate tasks

### Architecture
- The project has the directory: `api` which holds all the code. Inside the folder `exceptions` has the `Exceptions` that could raise on the execution of the application.
`middleware` folder has the code in `berries.py` that later will be called by the middleware of the blueprints. The reasoning behind is fetch the data `before_request` has started. So to speak, this middleware fetches data (sync and async) from the endpoint to have everything ready when the requests starts processing. It is used in `@berries_endpoint.before_request` in the berries blueprint.

- The folder `model` has the model of the `Berry` that belongs to the domain regardless of the data source.

- The directory `repositories` includes `sources` folder which has the code to fetch data sync and async from the poke API. This code implemented the pattern `Strategy` since it is possible to fetch data in different ways (strategies) implementing the abstract class (interface) `FetchDataMethod`. Likewise, the `context` file is the code that has the reference to the current strategy to fetch data. The idea to use sync and async code to fetch data was, using sync code to do 4 requests and the get the list of berries endpoints. Use async code to optimize the resources and hit all the berries endpoints in a row. This strategy improves the performance of the app. It could have been possible to use sync/async code for both data sources (endpoints & berry data) However, using async code to get the 4 endpoints probably does not impact significantly in the performace. Nonetheless, using sync code to fetch data from the berries endpoints could have reduced significantly the performance of the app.

- The folder `routes` contains the Flask blueprints to organize the endpoints. The `berries` blueprint is using:
    - middleware to fetch data from the API
    - include a helper class: `BerryBlueprint` that allows the blueprint to use the data fetched in the middleware to be used in the other endpoints. Otherwise only using global variables is not possible to copy data form the middleware to outside variables.
    - the `/allBerryStats` that calls the service to do the compute of the stats
    - the `/histogram` is the endpoint that uses `render_template` function to use the `html` template with `jinja` to insert the respective data and plot the histogram in html code.

- `service` is the directory includes a parser that is using `marshmallow` for that purpose. It also includes the compute for the stats operations in `statistics_operations`.

- The folder `templates` includes the `jinja` template to render the histogram.

- Last but no least, the directory `tests` include tests for testing the endpoints and TDD to write the statistics operations. The tests are using pytests and mocks. 

In main `CORS` was also included with `Flask-Cors` to allow requests from all the sources. This could be enhances according to differents needs.

### Docker
The app is running in a docker container to make it portable. The dockerfile is enforcing the rules to go to production:
- It is not using the root user
- It is using a light and official image
- It does not copy the code into the image
- It uses the pattern multi-stage builds to reuse the same image as base for testing (dev) and production (run)

### Dependencies
It tears the dependencies apart, so that the dev dependencies are in one file and the app dependencies are in a different file. Eventually, when the docker image is build, the dependencies for dev got installed in the dev image and the app dependencies are installed in the final image. This actions produce lighter images to push to the registry when it comes to push to production.

### Makefile
This file automates the tasks so that everythiong is done with just one/two commands.
- `make run` builds the docker image and starts the app
- `make test` builds the test image and runs the tests inside the container (that becomes deleted once the tests are done)
