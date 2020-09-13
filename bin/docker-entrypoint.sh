#!/bin/sh
exec uvicorn --host 0.0.0.0 --port $PORT main:app