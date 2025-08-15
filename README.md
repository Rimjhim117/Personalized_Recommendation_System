# Personalized-Recommendation-System-

This project is a web-based recipe recommendation system built with Python and the Flask framework. It uses a simple algorithm to suggest recipes based on user ratings, providing an intuitive way for users to discover new dishes.

📋 Features

    Recipe Discovery: Users can get a list of recommended recipes directly from the home page.

    Top-Rated Recommendations: The system suggests the highest-rated recipes from a curated dataset.

    User Feedback and Ratings: The application allows users to provide ratings and submit feedback for recipes, contributing to future improvements.

    RESTful API Endpoints: A simple server provides endpoints for retrieving recommendations and submitting data.

    Data-Driven: The system is powered by three CSV files that store recipe details, user ratings, and user feedback.

💻 Technologies Used

    Python: The primary programming language for the application logic.

    Flask: A lightweight web framework used to build the web server and API endpoints.

    Pandas: A data manipulation library for reading and processing the recipe, ratings, and feedback data from CSV files.

📂 Project Structure

    app.py: The main Python script that runs the Flask server, defines the routes, and contains the recommendation logic.

    recipes.csv: Contains a database of recipes, including their names, ingredients, and instructions.

    ratings.csv: Stores user-submitted ratings for different recipes.

    feedback.csv: A log file that records user feedback on recipes.

    README.md: The file you are currently reading.

🚀 Getting Started

Follow these instructions to set up and run the project locally.

Prerequisites

You need to have Python and pip (Python package manager) installed.

Installation

    Clone this repository to your local machine:
    Bash

git clone https://github.com/Rimjhim117/your-project-name.git

Navigate to the project directory:
Bash

cd your-project-name

Install the necessary Python packages using pip:
Bash

    pip install Flask pandas

Running the Application

After installing the dependencies, you can start the server with a single command:
Bash

python app.py

The application will be running at http://127.0.0.1:5000 by default. You can access the API endpoints and view the recommendations from your web browser or an API client.

📊 Data Files

The project uses the following CSV files to store and retrieve data:

recipes.csv

This file serves as the main database for all recipe information.

    RecipeID: A unique identifier for each recipe.

    RecipeName: The name of the recipe.

    Ingredients: A list of ingredients needed for the recipe.

    Instructions: The cooking instructions for the recipe.

    Cuisine: The origin of the recipe (e.g., "Italian", "Mexican").

    DietaryPreference: Any dietary tags associated with the recipe (e.g., "Vegetarian", "Vegan").

ratings.csv

This file stores the ratings given by users.

    UserID: A unique identifier for the user.

    RecipeID: The ID of the recipe that was rated.

    Rating: The score given by the user (e.g., a number from 1 to 5).

feedback.csv

This file is used to log user feedback.

    UserID: The ID of the user who submitted the feedback.

    RecipeID: The ID of the recipe the feedback is for.

    Feedback: The text content of the feedback.


