# CraftBuddy-backend

Copyright (C) 2025 Jacob Farnsworth

Have you ever played a game with some kind of crafting system? Have you ever found yourself struggling to plan your crafting goals in such a game? Maybe you've wondered, "How much stone do I need to make 1000 slabs?" or "How many sticks and ingots do I need to make 4 pickaxes?"

CraftBuddy is a web app that can help with a variety of crafting and resource management-related math. CraftBuddy can help with all kinds of queries related to crafting in your favorite games, and more!

This project contains the backend service of the CraftBuddy app. The backend service is built with Flask and intended to be hosted by gunicorn.

The CraftBuddy project consists of the following repositories:
* [craftbuddy-frontend](https://github.com/JFarNTIG/craftbuddy-frontend), frontend server built with React + Vite.
* [craftbuddy-backend](https://github.com/JFarNTIG/craftbuddy-backend), backend API server built with Flask.
* [craftbuddy](https://github.com/JFarNTIG/craftbuddy), environment and docker compose script for deploying the CraftBuddy app

CraftBuddy also depends on [crafterlib](https://github.com/JFarNTIG/crafterlib), a Python library that provides game item and recipe data and has a variety of functions for crafting-related math.

## Getting Started

If you want to deploy the CraftBuddy app, then it's recommended to do so via the docker compose script. See the instructions in [the main CraftBuddy repository](https://github.com/JFarNTIG/craftbuddy).

Otherwise, follow the instructions below to create a development environment for the backend service.

### Creating a Development Environment

Clone the repository:
```
git clone https://github.com/JFarNTIG/craftbuddy-backend backend && cd backend
```

It's recommended to create a Python virtual environment (venv) before installing the package:
```
python -m venv .venv
```

Next, activate the venv. Refer to the instructions for your platform.

**Terminal (Linux)**
```
source .venv/bin/activate
```

**Terminal (Windows)**
```
.venv\Scripts\activate
```

**Visual Studio Code (All Platforms)**

To activate the venv in VS Code, open the menu to select Python runtime (bottom right-hand corner). Choose the venv.


### Install Package

Install the backend service package in editable mode with dev dependencies:
```
pip install -e .[dev]
```

You can easily start the development server from within VS Code by running `src/wsgi.py`. Alternatively, to start the server from the terminal:
```
python src/wsgi.py
```

The development API server will then be available on port 8000:
```
http://localhost:8000
```

## Unit Tests

Unit tests are located in the tests/ folder.

Run all unit tests:

```
pytest
```

Run all unit tests and get a detailed coverage report, including missed lines:

```
pytest --cov-report term-missing
```

## Resources

* [Flask documentation](https://flask.palletsprojects.com/en/stable/)
* [Gunicorn reference](https://docs.gunicorn.org/en/stable/)
* [Pytest reference](https://docs.pytest.org/en/stable/)

## License

CraftBuddy is licensed under the terms of the GNU General Public License, version 2. See the file `LICENSE` for the full license text.