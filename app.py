import streamlit as st
import pandas as pd
import plotly.express as px

# Load segmented data
data = pd.read_csv("Segmented_AI_Customers.csv")

# Convert Cluster column to a string to ensure discrete colors
data['Cluster'] = data['Cluster'].astype(str)

# Define mappings for industry and company size
industry_mapping = {0: "Healthcare", 1: "Finance", 2: "Retail", 3: "Tech", 4: "Education"}
company_size_mapping = {0: "Small", 1: "Medium", 2: "Large"}

# Feature definitions
feature_definitions = {
    'Adoption Stage': {
        'Exploring': "Exploring chatbot solutions but not yet trialing.",
        'Trial': "Testing chatbot solutions in a limited capacity.",
        'Pilot': "Running chatbots in a real-world environment on a smaller scale.",
        'Adopted': "Fully integrated chatbots into their workflows."
    },
    'Industry': {
        'Healthcare': "Medical, biotech, or pharmaceutical companies.",
        'Finance': "Banks, investment firms, and insurance companies.",
        'Retail': "Businesses in retail looking for customer support solutions.",
        'Tech': "Technology and software companies.",
        'Education': "Educational institutions or EdTech companies."
    },
    'Company Size': {
        'Small': "Fewer than 50 employees, looking for affordable solutions.",
        'Medium': "50-250 employees, with moderate resources for scaling.",
        'Large': "Over 250 employees, needing robust, customizable solutions."
    }
}

# Dashboard title and description
st.title("AI Chatbot Deployment Platform - Customer Segmentation")
st.write("Explore customer segments for companies interested in a chatbot deployment platform. This segmentation helps understand the adoption stage, industry type, and company size for better targeting.")

# Display feature definitions
with st.expander("Feature Definitions"):
    st.write("**Adoption Stage**")
    for key, desc in feature_definitions['Adoption Stage'].items():
        st.write(f"- **{key}**: {desc}")
    st.write("**Industry**")
    for key, desc in feature_definitions['Industry'].items():
        st.write(f"- **{key}**: {desc}")
    st.write("**Company Size**")
    for key, desc in feature_definitions['Company Size'].items():
        st.write(f"- **{key}**: {desc}")

# Dropdowns for selecting x and y axes
x_axis = st.selectbox("X-axis", options=['Annual Revenue (M$)', 'Spending Score (1-100)', 'Industry', 'Company Size', 'Adoption Stage'])
y_axis = st.selectbox("Y-axis", options=['Annual Revenue (M$)', 'Spending Score (1-100)', 'Industry', 'Company Size', 'Adoption Stage'])

# Filter by Cluster
cluster_filter = st.selectbox("Select Cluster", options=['All'] + sorted(data['Cluster'].unique().tolist()))

# Filter data based on selected cluster
if cluster_filter != 'All':
    data = data[data['Cluster'] == cluster_filter]

# Define a custom color palette with distinct colors for each cluster
color_palette = ['#FF5733', '#33FF57', '#3357FF', '#FF9933']  # Red, Green, Blue, Orange

# Plot clusters using Plotly with the custom color palette
fig = px.scatter(data, x=x_axis, y=y_axis, color='Cluster', 
                 title="Customer Segments for AI Chatbot Deployment Platform",
                 color_discrete_sequence=color_palette)
st.plotly_chart(fig)

# Cluster summary
cluster_labels = {
    "0": "Budget-Conscious Tech SMEs",
    "1": "Healthcare and Finance Giants",
    "2": "Early Adopters in Retail and Education",
    "3": "Large Enterprises with High Spend Potential"
}

st.subheader("Cluster Summary Statistics")
for cluster, label in cluster_labels.items():
    cluster_data = data[data['Cluster'] == cluster]
    most_common_industry = industry_mapping.get(cluster_data['Industry'].mode()[0], "Unknown")
    most_common_company_size = company_size_mapping.get(cluster_data['Company Size'].mode()[0], "Unknown")
    
    st.write(f"**Cluster {cluster} - {label}**")
    st.write(f"- Average Annual Revenue: ${cluster_data['Annual Revenue (M$)'].mean():,.2f}M")
    st.write(f"- Average Spending Score: {cluster_data['Spending Score (1-100)'].mean():.2f}")
    st.write(f"- Most Common Industry: {most_common_industry}")
    st.write(f"- Most Common Company Size: {most_common_company_size}")
    st.write("---")
