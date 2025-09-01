# 🍽️ Recipe Recommendation System

This project is a **content-based recipe recommendation system** built as an interactive web application using **Streamlit**.  
It intelligently suggests new recipes by analyzing the ingredients and instructions of existing recipes.  
The recommendation engine leverages **machine learning techniques** to provide personalized and relevant suggestions.

---

## ✨ Features

- **Content-Based Recommendation Engine**  
  Uses TF-IDF vectorization and cosine similarity to find recipes that are similar to each other based on their content, providing smart and relevant suggestions.

- **Interactive User Interface**  
  Clean and user-friendly interface powered by Streamlit, allowing users to interact with the recommendation system easily.

- **Data-Driven**  
  Built on a dataset of recipes, ratings, and user feedback, allowing for further enhancements.

---

## 💻 Technologies Used

- **Streamlit** → Framework for building the interactive web application.  
- **Python** → Core programming language for all logic and data processing.  
- **Pandas** → Efficient data manipulation and dataset handling.  
- **Scikit-learn** → TF-IDF vectorizer and cosine similarity functions for recommendations.  
- **NumPy** → Numerical operations and similarity matrix handling.  

---

## 📂 Project Structure

    app.py: The primary Streamlit script that runs the application and contains the recommendation logic.

    recipes.csv: Contains a database of recipes, including their names, ingredients, and instructions.

    ratings.csv: Stores user-submitted ratings for different recipes.

    feedback.csv: A log file that records user feedback on recipes.


---

## 📊 Data Files

### `recipes.csv`
Main database for recipe information:
- **RecipeID** → Unique identifier for each recipe  
- **RecipeName** → Name of the recipe  
- **Ingredients** → List of required ingredients  
- **Instructions** → Cooking steps  
- **Cuisine** → Origin of the recipe (e.g., Italian, Mexican)  
- **DietaryPreference** → Tags like Vegetarian, Vegan, etc.  

### `ratings.csv`
Stores ratings given by users:
- **UserID** → Unique identifier for the user  
- **RecipeID** → ID of the rated recipe  
- **Rating** → Score (e.g., 1 to 5)  

### `feedback.csv`
Logs user feedback:
- **UserID** → ID of the user giving feedback  
- **RecipeID** → Recipe being reviewed  
- **Feedback** → Text content of the feedback  

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


