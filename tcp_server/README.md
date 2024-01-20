# TCP Server

For the duration of the project and the tools we have at our disposal, we've decided against bluetooth.
Using HTTP requests for something dynamic also seems antithetical. We've decided to go with websockets, which allow for a constant stream of information. We've decided to use FastAPI, a python package for running our server