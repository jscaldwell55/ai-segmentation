import pandas as pd
import numpy as np

# Define parameters for data
n_samples = 200  # Number of customer samples

# Define customer categories
industries = ["Healthcare", "Finance", "Retail", "Tech", "Education"]
company_sizes = ["Small", "Medium", "Large"]
roles = ["Manager", "Engineer", "Data Scientist", "CEO"]
adoption_stages = ["Exploring", "Trial", "Pilot", "Adopted"]

# Generate random customer data
np.random.seed(42)
data = pd.DataFrame({
    "Industry": np.random.choice(industries, n_samples),
    "Company Size": np.random.choice(company_sizes, n_samples),
    "Annual Revenue (M$)": np.random.randint(1, 500, n_samples),
    "Role": np.random.choice(roles, n_samples),
    "Adoption Stage": np.random.choice(adoption_stages, n_samples),
    "Spending Score (1-100)": np.random.randint(1, 101, n_samples)
})

# Save dataset
data.to_csv("AI_Target_Customers.csv", index=False)
print("Dataset saved as AI_Target_Customers.csv")
