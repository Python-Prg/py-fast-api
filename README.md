# py-fast-api

A FastAPI project setup.

## Setup

1. **Hands-on project setup create foder structure first**
   ```bash
   mkdir py-fast-api
   cd py-fast-api
   python -m venv pfaenv

# Windows:
   ```bash
      pfaenv\Scripts\activate.bat
   ``` 
# macOS/Linux:
   ```bash
     source pfaenv/bin/activate
   ```
### Install fastApi dependencies in current project directory
   ```bash
      pip install "fastapi[standard]"
      uvicorn main:app --reload
  ```

### Run new way
   ```bash
      fastapi run main.py
  ``` 

### Swagger link
   ```
   http://127.0.0.1:8000/docs
  ```
   

### Project structure look like
py-fast-api/
├── .pfaenv/         # Virtual environment (excluded via .gitignore)
├── main.py        # Example FastAPI app
└── README.md      # Project documentation

