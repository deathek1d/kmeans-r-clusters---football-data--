Football Player Performance Analysis
This project explores football player performance data using Principal Component Analysis (PCA) and K-Means clustering to identify distinct player profiles. It visualizes outfield player statistics with interactive Plotly charts and is implemented on Streamlit.

🔧 Tech Stack
Python
Pandas
Scikit-learn
Plotly
PCA & K-Means
Streamlit

🎯 Use Cases
Player performance profiling
Identifying similar player clusters for scouting

⚙️ Features (Outfield Player Stats)
Feature	Description
Gper:	Goals per appearance
Aper:	Assists per appearance
Bper:	Big chances per appearance
Tper:	Tackles per appearance
Dper:	Duels per appearance
Abper:	Aerial battles per appearance
Iper:	Intercepts per appearance
Cper:	Crosses per appearance
Lbper:	Long balls per appearance
Tbper:	Through balls per appearance
Sper:	Saves per appearance

📊 Visualizations

1️⃣ PCA Scatter Plot
Shows players projected into two principal components, colored by cluster.
Observations:
Clusters 4 & 6: Main bulk of outfield players
Clusters 2, 3 & 5: Smaller, specialized roles
PC1: Largest variance, driven by Gper, Aper, Bper
PC2: Smaller variance, influenced by defensive and passing stats

2️⃣ Cluster Sizes
Bar chart displaying the number of players in each cluster
Observations:
Cluster 4: Largest (~145 players) = “average” outfield player
Clusters 2 & 3: Small groups = niche roles

3️⃣ Radar Charts
Normalized cluster profiles for fair comparison
Cluster Profiles:
Cluster 0: Low PC1 & PC2 = support/defensive role players
Cluster 1: High PC1, low PC2 = attacking/goal-oriented players
Cluster 2: Low PC1, slightly positive PC2 = consistent midfield/defensive support
Cluster 3: Negative PC1, high PC2 = creative midfielders or ball-winning players
Cluster 4: PC1 ~0–2, PC2 ~0–5 = all-round midfielders
Cluster 5: Positive PC1, near-zero PC2 = attacking players or wingers
Cluster 6: High PC1, slightly negative PC2 = star forwards or high-impact attackers

4️⃣ PCA Feature Loadings
PC1: Dominated by attacking output (Gper, Aper, Bper)
PC2: Separates defensive vs possession-oriented players (Tper negatively, passes positively)

🚀 Running the App
streamlit run /Users/{name}/{pathway}/kmeans2.py
