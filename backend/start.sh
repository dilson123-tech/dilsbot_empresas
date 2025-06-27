#!/bin/bash
pip install uvicorn  # Garante que uvicorn esteja instalado no ambiente global
cd app
uvicorn main:app --host 0.0.0.0 --port 10000
