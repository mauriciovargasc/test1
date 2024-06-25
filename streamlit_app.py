import streamlit as st
import pandas as pd

# Load the cleaned data
file_path = r"test1.csv" # Use the path to your cleaned data file
data = pd.read_csv(file_path)

# Function to calculate rewards
def calculate_rewards(selected_cards, spending):
    total_rewards = 0
    for card in selected_cards:
        card_data = data[data['Card Name'] == card].iloc[0]
        rewards = eval(card_data['Rewards'])  # Assuming rewards are stored as a list of tuples (category, rate)
        for category, rate in rewards:
            if category in spending:
                total_rewards += spending[category] * rate
    return total_rewards

# Streamlit app layout
st.title("Credit Card Rewards Optimization")

# Step 1: Select credit cards
selected_cards = st.multiselect("Select Your Credit Cards", data['Card Name'].unique())

# Step 2: Input monthly spending
st.subheader("Enter Your Monthly Spending")
categories = ['Travel', 'Dining', 'Groceries', 'Other']
spending = {}
for category in categories:
    spending[category] = st.number_input(f"{category} Spending", min_value=0.0, value=0.0)

# Step 3: Calculate and display rewards
if st.button("Calculate Rewards"):
    total_rewards = calculate_rewards(selected_cards, spending)
    st.subheader(f"Total Rewards Earned: ${total_rewards:.2f}")

# Display the selected cards and their reward structures
if selected_cards:
    st.subheader("Selected Credit Cards and Their Reward Structures")
    for card in selected_cards:
        card_data = data[data['Card Name'] == card].iloc[0]
        st.write(f"**{card}**")
        st.write(card_data['Rewards'])
