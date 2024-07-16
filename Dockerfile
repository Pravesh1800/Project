# Use the official Python image from the Docker Hub
FROM python:3.11-slim

ENV PYTHONUNBUFFERED = 1

# Set the working directory
WORKDIR /app

RUN python -m pip install --upgrade pip
RUN pip install virtualenv
RUN python -m venv .venv
RUN . .venv/bin/activate

COPY . .

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

# Copy the rest of the application code

# Expose the port Streamlit will run on
EXPOSE 8502

# Command to run the application
CMD ["streamlit", "run", "app.py", "--server.port=8502", "--server.enableCORS=false"]

