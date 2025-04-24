import streamlit as st
import pandas as pd
import numpy as np
import ast
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# ---- Modern UI Styling ----
st.set_page_config(page_title="Smart Recipe Recommender", page_icon="🍽️", layout="wide")

st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .stTabs [role="tab"] {
            font-size: 18px;
            padding: 12px;
        }
        .stTextInput > div > div > input {
            border-radius: 10px;
        }
        .stButton button {
            border-radius: 8px;
            padding: 8px 16px;
            font-size: 16px;
        }
        h3 {
            margin-bottom: 0.2rem;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Load Data ----
@st.cache_data
def load_data():
    ratings = pd.read_csv("ratings.csv")
    recipes = pd.read_csv("recipes.csv")
    return ratings, recipes

ratings, recipes = load_data()

# ---- Extract Ingredients List for Filter ----
@st.cache_data
def get_all_ingredients():
    ingredient_set = set()
    for ing in recipes['ingredients']:
        try:
            items = [i.strip().lower() for i in ing.split(',')]
            ingredient_set.update(items)
        except:
            continue
    return sorted(list(ingredient_set))

all_ingredients = get_all_ingredients()

# ---- User Similarity ----
@st.cache_data
def build_user_similarity():
    matrix = ratings.pivot_table(index='user_id', columns='recipe_id', values='rating').fillna(0)
    sim = cosine_similarity(matrix)
    sim_df = pd.DataFrame(sim, index=matrix.index, columns=matrix.index)
    return matrix, sim_df

user_item_matrix, user_sim_df = build_user_similarity()

# ---- TF-IDF Model ----
@st.cache_data
def build_tfidf():
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(recipes['ingredients'])
    return tfidf_matrix, tfidf

tfidf_matrix, tfidf = build_tfidf()

# ---- Recommendation Functions ----
def user_based_recommend(user_id, n=5):
    if user_id not in user_item_matrix.index:
        return pd.DataFrame()
    sim_users = user_sim_df[user_id].sort_values(ascending=False).drop(user_id).head(3)
    weighted = user_item_matrix.loc[sim_users.index].T.dot(sim_users)
    scores = weighted / sim_users.sum()
    rated = user_item_matrix.loc[user_id]
    top = scores[rated == 0].sort_values(ascending=False).head(n)
    return recipes[recipes['recipe_id'].isin(top.index)][['title', 'cuisine', 'ingredients']]

def content_based_ingredient_recommend(ingredients, n=5):
    text = ", ".join(i.strip().lower() for i in ingredients)
    vec = tfidf.transform([text])
    sims = cosine_similarity(vec, tfidf_matrix).flatten()
    top_idx = sims.argsort()[::-1][:n]
    return recipes.iloc[top_idx][['title', 'cuisine', 'ingredients']]

def hybrid_recommend(user_id, n=5):
    cf = user_based_recommend(user_id, n=5)
    if cf.empty:
        return pd.DataFrame()
    all_ingredients = []
    for _, row in cf.iterrows():
        try:
            ing = ast.literal_eval(row['ingredients']) if isinstance(row['ingredients'], str) else []
            all_ingredients.extend(ing)
        except:
            all_ingredients.extend([i.strip() for i in row['ingredients'].split(',')])
    return content_based_ingredient_recommend(all_ingredients, n)

# ---- Fake AI Recipe Generator (No API) ----
def generate_ai_recipe(prompt):
    fake_recipe = f"""
    ### AI-Generated Recipe: {prompt.title()}
    
    **Ingredients:**
    - 1 cup of inspiration  
    - 2 tbsp of creativity  
    - A pinch of salt and spice  

    **Instructions:**
    1. Combine all ingredients in a bowl of imagination.  
    2. Stir thoroughly while thinking about {prompt}.  
    3. Serve with a smile. Enjoy!
    """
    placeholder_image = "https://cdn.pixabay.com/photo/2016/11/18/15/07/salad-1834641_960_720.jpg"
    return fake_recipe, placeholder_image

# ---- Feedback ----
def feedback_form(user_id, recipe_title, source):
    with st.expander(f"Rate: {recipe_title}"):
        rating = st.slider("Your rating", 1, 5, 3, key=f"{user_id}_{recipe_title}")
        if st.button("Submit Feedback", key=f"btn_{user_id}_{recipe_title}"):
            entry = pd.DataFrame([{
                "user_id": user_id,
                "recipe_title": recipe_title,
                "rating": rating,
                "source": source
            }])
            try:
                existing = pd.read_csv("feedback.csv")
                updated = pd.concat([existing, entry], ignore_index=True)
            except FileNotFoundError:
                updated = entry
            updated.to_csv("feedback.csv", index=False)
            st.success("Thanks for your feedback!")

# ---- Display Helper ----
def show_recipes(df, user_id, source):
    for _, row in df.iterrows():
        with st.container():
            st.markdown(f"""
                <div style='background-color: #f9f9f9; padding: 20px; border-radius: 15px; box-shadow: 2px 2px 8px rgba(0,0,0,0.05); margin-bottom: 15px;'>
                    <h3>{row['title']}</h3>
                    <p><b>Cuisine:</b> {row['cuisine']}</p>
                    <p><b>Ingredients:</b> {row['ingredients']}</p>
                </div>
            """, unsafe_allow_html=True)
            feedback_form(user_id, row['title'], source)

# ---- UI ----
st.title("🍽️ Smart Recipe Recommender + AI")
tab1, tab2, tab3, tab4 = st.tabs([
    "👥 Collaborative", "🥬 Content-Based", "⚡ Hybrid", "🧠 AI Generator"
])

# -- Collaborative --
with tab1:
    user_ids = user_item_matrix.index.tolist()
    user_id = st.selectbox("Select User ID", user_ids, key="cf_user")
    if st.button("Recommend (Collaborative)", key="cf_btn"):
        recs = user_based_recommend(user_id)
        if not recs.empty:
            show_recipes(recs, user_id, "Collaborative")
        else:
            st.warning("No collaborative recommendations found.")

# -- Content-Based --
with tab2:
    selected = st.multiselect("Select ingredients you have:", all_ingredients)
    if st.button("Find Recipes (Content-Based)", key="cb_btn"):
        if selected:
            recs = content_based_ingredient_recommend(selected)
            show_recipes(recs, user_id=0, source="Content-Based")
        else:
            st.warning("Select at least one ingredient.")

# -- Hybrid --
with tab3:
    user_ids = user_item_matrix.index.tolist()
    user_id = st.selectbox("Select User ID", user_ids, key="hy_user")
    if st.button("Recommend (Hybrid)", key="hy_btn"):
        recs = hybrid_recommend(user_id)
        if not recs.empty:
            show_recipes(recs, user_id, "Hybrid")
        else:
            st.warning("No hybrid recommendations found.")

# -- AI Generator --
with tab4:
    prompt = st.text_input("Describe your dish idea (e.g., 'vegan tacos with lentils'):", key="ai_prompt")
    if st.button("Generate AI Recipe", key="ai_btn"):
        recipe_text, image_url = generate_ai_recipe(prompt)
        if recipe_text and image_url:
            st.image(image_url, caption="AI-Generated Dish", use_column_width=True)
            st.markdown(recipe_text)
            feedback_form(user_id=999, recipe_title=f"AI: {prompt}", source="AI")

# ---- Footer ----
st.markdown("---")
st.caption("Created by Rimjhim & Raktima | Styled with ❤️ using Streamlit")
