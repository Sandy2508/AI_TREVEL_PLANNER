import streamlit as st
import openai
import requests

# Set OpenAI API key (Replace 'your-api-key' with your actual key)
openai.api_key = "your-api-key"

# Function to get travel suggestions
def get_travel_suggestions(destination):
    search_url = f"https://www.googleapis.com/customsearch/v1?q=top+attractions+in+{destination}&key=your-google-api-key"
    response = requests.get(search_url)
    if response.status_code == 200:
        return response.json()["items"][:5]  # Get top 5 suggestions
    return ["No suggestions available."]

# Function to generate itinerary
def generate_itinerary(user_input):
    prompt = f"""
    You are an AI travel assistant. Create a {user_input['trip_duration']}-day itinerary for {user_input['destination']}
    based on the following preferences:
    - Budget: {user_input['budget']}
    - Interests: {user_input['interests']}
    - Accommodation type: {user_input['accommodation']}
    - Dietary preferences: {user_input['diet']}
    Provide a detailed, day-by-day travel plan.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

# Streamlit UI
st.title("AI Travel Planner")

# Collect User Inputs
destination = st.text_input("Enter your destination:")
trip_duration = st.number_input("Number of days:", min_value=1, max_value=30)
budget = st.selectbox("Budget:", ["Low", "Mid-range", "Luxury"])
interests = st.text_area("What are your interests? (e.g., history, nature, nightlife)")
accommodation = st.selectbox("Accommodation Type:", ["Hostel", "Hotel", "Resort"])
diet = st.text_input("Dietary Preferences (optional):")

# Generate Plan
if st.button("Generate Itinerary"):
    user_input = {
        "destination": destination,
        "trip_duration": trip_duration,
        "budget": budget,
        "interests": interests,
        "accommodation": accommodation,
        "diet": diet
    }
    
    itinerary = generate_itinerary(user_input)
    suggestions = get_travel_suggestions(destination)

    st.subheader("Suggested Attractions:")
    for item in suggestions:
        st.write(f"- {item}")

    st.subheader("Your Personalized Itinerary:")
    st.write(itinerary)
