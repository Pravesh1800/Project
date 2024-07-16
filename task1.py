import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import io

st.header(":blue[Clustering] ",divider='blue')


file = st.file_uploader("Please upload your dataset",type="xlsx",accept_multiple_files=False)
text = st.text_input("please enter the data row in form of a list")
if text:
    from io import StringIO
    csv_file= pd.read_csv(StringIO(text),header=None)
    st.write(csv_file,)
    csv_file = csv_file.values.tolist()



if file:
    data = pd.read_excel(file)
    data  = data.drop('target',axis=1)
    st.write("This is your dataset")
    st.write(data)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    pca = PCA(n_components=2)
    data_pca = pca.fit_transform(scaled_data)
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(scaled_data)
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.scatter(data_pca[:, 0], data_pca[:, 1], c=kmeans.labels_, s=20)
    ax.set_xlabel('PCA Component 1')
    ax.set_ylabel('PCA Component 2')
    ax.set_title('Data Visualization using PCA')
    plt.tight_layout()
    plt.plot()
    st.write("On plotting the cluster we get")
    st.pyplot(fig)


    def predict_cluster(new_data_point):
        # Scale the new data point
        new_data_point_scaled = scaler.transform([new_data_point])
        
        # Predict the cluster
        cluster = kmeans.predict(new_data_point_scaled)[0]
        
        # Find the closest cluster center
        closest_center = kmeans.cluster_centers_[cluster]
        
        # Calculate the distance to the closest center
        distance = np.linalg.norm(new_data_point_scaled - closest_center)
        
        explanation = f"The data point belongs to cluster {cluster} because it is closest to the cluster center {closest_center}, with a distance of {distance:.4f}."
        
        return cluster, explanation
    
    print(text)
    cluster, explanation = predict_cluster(csv_file[0])
    st.info(f"Cluster: {cluster}")
    st.info(f"Explanation: {explanation}")