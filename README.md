Recipe Recommendation System

This project is a content-based recipe recommendation system built as an interactive web application using Streamlit. It intelligently suggests new recipes to users by analyzing the ingredients and instructions of existing recipes. The recommendation engine leverages machine learning techniques to provide personalized and relevant suggestions.

✨ Features

    Content-Based Recommendation Engine: The application uses TF-IDF vectorization and cosine similarity to find recipes that are similar to each other based on their content, providing smart and relevant suggestions.

    Interactive User Interface: The app features a clean and user-friendly interface powered by Streamlit, allowing users to interact with the recommendation system easily.

    Data-Driven: The core of the system is built upon a dataset of recipes, ratings, and user feedback, allowing for further enhancements.

💻 Technologies Used

    Streamlit: The main framework used for building the interactive web application interface.

    Python: The core programming language for all logic and data processing.

    Pandas: Used for efficient data manipulation and handling the recipe datasets.

    Scikit-learn: The machine learning library that provides the TF-IDF vectorizer and cosine similarity functions for the recommendation algorithm.

    NumPy: Used for numerical operations, likely for handling the similarity matrix.

📂 Project Structure

    app.py: The primary Streamlit script that runs the application and contains the recommendation logic.

    recipes.csv: Contains a database of recipes, including their names, ingredients, and instructions.

    ratings.csv: Stores user-submitted ratings for different recipes.

    feedback.csv: A log file that records user feedback on recipes.

🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

Prerequisites

You need to have Python installed. You can install the required libraries using pip.

Installation

    Clone this repository to your local machine.
    Bash

git clone https://github.com/Rimjhim117/your-project-name.git

Navigate to the project directory.
Bash

cd your-project-name

Install the required Python packages:
Bash

    pip install streamlit pandas numpy scikit-learn

Running the Application

To start the Streamlit application, run the following command in your terminal from the project directory:
Bash

streamlit run app.py

This will open the application in your default web browser, and you can begin using the recipe recommendation system.

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

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or above
- pip (Python package installer)

### Installation and Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/Rimjhim117/Personalized_Recommendation_System.git
    cd Personalized_Recommendation_System
    ```

2. Install required Python packages:
    ```bash
    pip install streamlit pandas scikit-learn numpy
    ```

3. Run the application:
    ```bash
    streamlit run app.py
    ```

4. Open your browser and access:
    ```
    http://localhost:8501
    ```

---

## 📖 Usage Guide

1. Explore recipes listed in the app.  
2. Select a recipe you like.  
3. View recommended recipes based on similarity in ingredients and preparation.  
4. Submit a rating or feedback to refine the model over time.  

---

## 🔮 Potential Enhancements

- **Hybrid Recommendation System** → Combine content-based filtering with collaborative filtering.  
- **Personal Profiles** → Save user preferences and history for better personalization.  
- **Natural Language Search** → Query recipes like *“chicken curry with coconut milk.”*  
- **Backend API Deployment** → Separate backend for scalability and integration.  
- **Nutritional Info & Dietary Filters** → Support vegan, gluten-free, etc.  
- **User Authentication** → Add login/signup for personalized recommendations.  

---

## 🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests for new features, bug fixes, or improvements.
---

## 🙌 Acknowledgements

- Thanks to the creators of **Streamlit**, **Scikit-Learn**, **Pandas**, and **NumPy**.  
- Inspiration drawn from general recommendation system methodologies and the open-source community.


