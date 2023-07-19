# Use the official Python image as the base
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the script and requirements.txt file into the container
COPY watch_next.py .
COPY movies.txt .

# Install the required packages
RUN pip install spacy numpy

# Download the spaCy language model
RUN python -m spacy download en_core_web_md

# Specify the command to run the script
CMD ["python", "watch_next.py"]

