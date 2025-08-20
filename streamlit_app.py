import streamlit as st
import pandas as pd

# Load Excel file
@st.cache_data
def load_data():
    return pd.read_excel("MCA FEES.xlsx")

df = load_data()

st.title("📊 MCA Fee Calculator - Company Incorporation")

# Sidebar for state selection
states = df["STATE NAME"].dropna().unique().tolist()
selected_state = st.sidebar.selectbox("Select State", states)

# Filter data for selected state
state_data = df[df["STATE NAME"] == selected_state]

st.subheader(f"Fee Structure for {selected_state}")

# Show fee table
st.dataframe(state_data)

# Optional: Search authorised capital
cap_input = st.text_input("Enter Authorised Capital to check fee (e.g. 10,00,000):")

if cap_input:
    try:
        cap_value = int(cap_input.replace(",", ""))
        # Find closest match in Authorised Capital column
        state_data["Difference"] = abs(state_data["AUTHORISED CAPITAL"] - cap_value)
        closest_row = state_data.loc[state_data["Difference"].idxmin()]
        
        st.success(
            f"For Authorised Capital ₹{cap_value:,}, "
            f"the fee is: ₹{closest_row['FEES']:,}"
        )
    except:
        st.error("⚠️ Please enter a valid number for Authorised Capital.")
