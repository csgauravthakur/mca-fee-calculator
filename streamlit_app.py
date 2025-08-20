import streamlit as st
import pandas as pd

# Title
st.title("📊 MCA Fee Calculator (India)")

# Load Excel safely
@st.cache_data
def load_data():
    try:
        df = pd.read_excel("MCA FEES.xlsx", sheet_name="Sheet1", engine="openpyxl")
        return df
    except Exception as e:
        st.error(f"Error loading Excel file: {e}")
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.warning("No data available. Please check the Excel file format.")
else:
    st.success("✅ Data loaded successfully!")

    # Show preview
    if st.checkbox("Show fee master sheet preview"):
        st.dataframe(df)

    # Dropdowns for search
    states = df["State"].dropna().unique().tolist()
    company_types = df["Company Type"].dropna().unique().tolist()

    selected_state = st.selectbox("Select State", states)
    selected_company = st.selectbox("Select Company Type", company_types)

    # Filter result
    result = df[
        (df["State"] == selected_state) &
        (df["Company Type"] == selected_company)
    ]

    if not result.empty:
        st.subheader("📌 Applicable Fees")
        st.table(result)
    else:
        st.warning("No matching record found. Try another selection.")
