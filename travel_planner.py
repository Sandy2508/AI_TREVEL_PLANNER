import streamlit as st

st.set_page_config(
    page_title="AI Travel Assistant",
    page_icon="🧳",
    layout="centered"
)

TRAVEL_DATA = {
    "Airways": {
        "time": 2,        # Very fast
        "cost": 7500,     # Expensive
        "comfort": 9      # High comfort
    },
    "Railway": {
        "time": 18,       # Moderate
        "cost": 1200,     # Cheapest (Sleeper)
        "comfort": 6      # Medium comfort
    },
    "Road": {
        "time": 26,       # Slow
        "cost": 3500,     # Moderate cost
        "comfort": 4      # Low comfort
    }
}


def recommend_travel(preference):
    if preference == "🚀 Fastest":
        return min(TRAVEL_DATA, key=lambda x: TRAVEL_DATA[x]["time"])

    elif preference == "💰 Cheapest":
        return min(TRAVEL_DATA, key=lambda x: TRAVEL_DATA[x]["cost"])

    elif preference == "🛋 Most Comfortable":
        return max(TRAVEL_DATA, key=lambda x: TRAVEL_DATA[x]["comfort"])

    else:  
        scores = {}
        for mode, d in TRAVEL_DATA.items():
            score = (
                (1 / d["time"]) * 0.4 +
                (1 / d["cost"]) * 0.3 +
                (d["comfort"] / 10) * 0.3
            )
            scores[mode] = score

        return max(scores, key=scores.get)


st.markdown(
    """
    <h1 style='text-align: center;'>🧳 AI Travel Assistant</h1>
    <p style='text-align: center; color: grey;'>
    Find the best way to travel between cities in India
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

st.subheader("📍 Trip Details")

col1, col2 = st.columns(2)
with col1:
    source = st.text_input("Source City / State", placeholder="e.g. Hyderabad")
with col2:
    destination = st.text_input("Destination City / State", placeholder="e.g. Delhi")

st.markdown("")

preference = st.selectbox(
    "🎯 What matters most to you?",
    ["⚖️ Best Overall", "🚀 Fastest", "💰 Cheapest", "🛋 Most Comfortable"]
)

st.markdown("")

find_btn = st.button("🚀 Find Best Travel Option", use_container_width=True)

st.divider()

if find_btn:
    if source and destination:
        best = recommend_travel(preference)

        st.subheader("✅ Recommendation")
        st.success(
            f"**The best way to travel from {source} to {destination} is {best}.**"
        )

        st.markdown("### 🧠 Why this option?")

        if preference == "🚀 Fastest":
            st.info("✈️ Airways is recommended because it takes the least travel time.")
        elif preference == "💰 Cheapest":
            st.info("🚆 Railway (Sleeper) is the most affordable option for long distances.")
        elif preference == "🛋 Most Comfortable":
            st.info("✈️ Airways offers the highest comfort level among all travel modes.")
        else:
            st.info(
                "🚆 Railway offers the best balance of cost, travel time, and comfort "
                "for long-distance journeys in India."
            )

        st.markdown("---")
        st.markdown(
            "<p style='text-align:center; color:grey;'>"
            "Powered by intelligent travel decision logic 🇮🇳"
            "</p>",
            unsafe_allow_html=True
        )
    else:
        st.warning("⚠️ Please enter both source and destination.")