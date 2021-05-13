# Kohaku - Web Backend
## Requierements
This project uses Python 3.9 and Poetry as a package manager.
You can also skip poetry and install every package yourself. Poetry is therefore optional.

## Project Structure

```
.
├── src                     # Main directory (Holds whole backend logic)
|   ├── games               # Sub-directory for games
|   |   ├── gameA           # Each game need a folder of it's own (get's automatically imported)
|   |   |   ├── models      
|   |   |   ├── schemes
|   |   |   ├── main.py     # (Required!)
|   |   |   ├── ...
|   |   |   ...
|   |   ...
|   ├── app.py              # Application
|   ├── constants.py        # Stores & Convert general constants 
|   └── database.py         # Database structures            
├── .gitignore                    
├── LICENSE                   
├── poetry.lock             # Fast package management
├── pyproject.toml
└── README.md
```

## Project setup
To work on this project, clone this repository and execute the following steps:
1. Install packages
    1. Poetry: <br>
        `poetry install` **(Recommended)**
    2. Non-Poetry:<br>
        Install every package yourself via `pip install <package>`. You can look them up in [pyproject.toml](pyproject.toml)
2. Execute
    1. Poetry: **(Recommended)**
        ```
        cd src
        poetry run uvicorn app:app
        ```
    2. Non-Poetry:
        ```
        cd src
        uvicorn app:app
        ```
On Default you can now find the server on `localhost:8000`.

## Development Setup
To create a development environment follow the steps above and add the option `--reload` to the `uvicorn app:app` command. <br>
This will allow uvicorn to reload on code changes.

## Build Image for Production
TODO