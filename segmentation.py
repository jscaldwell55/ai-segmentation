import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans

# Load the generated dataset
data = pd.read_csv("AI_Target_Customers.csv")

# Encode categorical variables
label_encoders = {}
for column in ['Industry', 'Company Size', 'Role', 'Adoption Stage']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le  # Save encoder for future reference

# Select features for clustering
X = data[['Industry', 'Company Size', 'Annual Revenue (M$)', 'Role', 'Adoption Stage', 'Spending Score (1-100)']]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=4, random_state=0)
data['Cluster'] = kmeans.fit_predict(X_scaled)

# Save segmented data to a new CSV file
data.to_csv("Segmented_AI_Customers.csv", index=False)
print("Customer segmentation complete and saved as Segmented_AI_Customers.csv")

# Optional: Print the first few rows of the segmented data for confirmation
print(data.head())
