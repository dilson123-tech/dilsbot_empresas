#!/bin/bash
pip install uvicorn
cd backend/app
uvicorn main:app --host 0.0.0.0 --port 10000
