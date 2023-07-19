# Watch Next Program

This program suggests movies based on a given description. It calculates the similarity scores between the input description and a list of movie descriptions to recommend the most similar movie.

# Prerequisites

    - Python 3.9 or higher installed on your system
    - Docker (optional, for running the program in a container)

# Installation

    1. Clone the repository to your local machine: git clone https://github.com/DouwSteyn021/watch_next.git

    2. Change to the project directory:

    3. (Optional) If you are using Docker, build the Docker image:

docker build -t watch-next-app .

# Running the Program
## Without Docker

    1. Make sure you are in the project directory.

    2. Install the required Python packages: pip install spacy numpy python -m spacy download en_core_web_md

    3. Run the program: python watch_next.py

# Running the Program
## With Docker

    1. Make sure you have Docker installed on your system.

    2. Build the Docker image (if not already done): docker build -t watch-next-app .

    3. Run the Docker container: docker run -it watch-next-app

# Usage

    1. Enter a movie description when prompted.

    2. The program will suggest a movie based on the provided description.

    3. Repeat the process to get suggestions for different descriptions.

# Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.
