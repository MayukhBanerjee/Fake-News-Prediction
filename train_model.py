import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle
import re

# --- Configuration ---
FAKE_CSV_PATH = 'fake.csv'
TRUE_CSV_PATH = 'true.csv'
MODEL_SAVE_PATH = 'robust_model.pkl'
VECTORIZER_SAVE_PATH = 'robust_vectorizer.pkl'

# --- Function to clean text ---
def preprocess_text(text):
    """
    Cleans text by removing boilerplate like '(Reuters) -' and making it lowercase.
    """
    # Remove source tags like (Reuters) or (AP) at the beginning of the text
    text = re.sub(r'^\w+\s*\([^)]*\)\s*-\s*', '', text, flags=re.IGNORECASE)
    return text.lower()


# --- Main Execution ---
if __name__ == "__main__":
    # --- 1. Load and Combine Datasets ---
    print("Loading datasets...")
    df_fake = pd.read_csv(FAKE_CSV_PATH)
    df_true = pd.read_csv(TRUE_CSV_PATH)

    df_fake['target'] = 0
    df_true['target'] = 1

    df = pd.concat([df_fake, df_true], ignore_index=True)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    print(f"Datasets loaded and combined. Total articles: {len(df)}")
    
    # --- 2. Prepare Data for the Model ---
    print("Preparing and cleaning data...")
    
    # Fill any missing titles or text with empty strings
    df['title'] = df['title'].fillna('')
    df['text'] = df['text'].fillna('')

    # Combine title and text into a single feature
    df['combined_text'] = df['title'] + ' ' + df['text']
    
    # Apply the cleaning function to the combined text
    df['combined_text'] = df['combined_text'].apply(preprocess_text)
    
    labels = df['target']

    # Use 'combined_text' and IGNORE 'subject', 'date', etc., to prevent data leakage
    X_train, X_test, y_train, y_test = train_test_split(
        df['combined_text'], 
        labels, 
        test_size=0.2, 
        random_state=42
    )
    print(f"Data split into {len(X_train)} training samples and {len(X_test)} testing samples.")

    # --- 3. Vectorize the Text Data (With Tuning) ---
    print("Initializing and tuning TF-IDF Vectorizer...")
    
    # Tuned parameters to prevent overfitting:
    # max_df=0.7: ignore words that appear in more than 70% of documents.
    # min_df=5: ignore words that appear in less than 5 documents.
    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7, min_df=5)

    print("Fitting and transforming training data...")
    tfidf_train = vectorizer.fit_transform(X_train)
    print("Transforming test data...")
    tfidf_test = vectorizer.transform(X_test)
    
    # --- 4. Train a Regularized Machine Learning Model ---
    print("Training the Regularized Logistic Regression model...")
    
    # Using Logistic Regression with L2 Regularization to combat overfitting.
    # C=1.0 is the regularization strength. Lower values specify stronger regularization.
    model = LogisticRegression(C=1.0, penalty='l2', solver='liblinear', max_iter=200)
    model.fit(tfidf_train, y_train)

    # --- 5. Evaluate the More Realistic Model ---
    print("Evaluating the robust model...")
    y_pred = model.predict(tfidf_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n--- Model Evaluation Results ---")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print("(Note: A lower accuracy is expected and indicates a more robust model.)")

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("---------------------------------")
    
    # --- 6. Save the New Robust Model and Vectorizer ---
    print("\nSaving the trained robust model and vectorizer...")
    with open(MODEL_SAVE_PATH, 'wb') as model_file:
        pickle.dump(model, model_file)
        
    with open(VECTORIZER_SAVE_PATH, 'wb') as vectorizer_file:
        pickle.dump(vectorizer, vectorizer_file)
        
    print(f"Model saved to: {MODEL_SAVE_PATH}")
    print(f"Vectorizer saved to: {VECTORIZER_SAVE_PATH}")
