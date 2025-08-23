# kmeans-r-clusters--football-data--

This project explores football player performance data using Principal Component Analysis (PCA) and K-Means clustering to identify distinct player profiles. It visualizes outfield player statistics with interactive Plotly charts, including:
PCA Scatter Plot: Shows players projected into two principal components, colored by cluster.
Cluster Sizes: A bar chart displaying the number of players in each cluster.
Radar Charts: Normalized cluster profiles highlighting strengths across key performance metrics.
PCA Feature Loadings: Shows how much each feature contributes to player separation in the PCA components.
The dashboard is implemented using Streamlit app and is ideal for portfolio demonstrations of data analysis, clustering, and interactive visualization.

Tech stack: Python, Pandas, Scikit-learn, Plotly, PCA, K-Means

Use cases:
Player performance profiling
Identifying similar player clusters for scouting
Portfolio project demonstrating data science workflow from preprocessing to visualization

Features_outfield :
    'Gper' = goals per app
    'Aper' = assits per app
    'Bper' = big chances per app
    Tper'  = tackles per app
    'Dper' = duels per app
    Abper' = aerial battles per app
    'Iper' = intercepts per app
    'Cper' = crosses per app
    'Lbper'= long balls per app
    'Tbper'= through balls per app
    'Sper' = saves per app 


Run: streamlit run /Users/{name}/{pathway}/kmeans2.py

Scatter Plot: 
Clusters 4 and 6 form the main bulk of outfield players.
Clusters 2, 3 and 5 are smaller and more extreme likely representing specialized roles.
Spread along PC1 is largest, meaning most variance is captured by a combination of goals, assists, and big chances (Gper, Aper, Bper).
Spread along PC2 is smaller. Features like tackles (Tper) or passes per match contribute more to PC2.

Cluster Sizes:
Cluster 4 is the largest (~145 players), suggesting the “average” outfield player.
Clusters 2 and 3 are tiny, probably highlighting niche roles (like defensive midfielders or high-output forwards).


Radar Chart:
Features are normalized, so we can compare clusters fairly. Using per 90 stats help.
Observations:

Cluster 0:
Small group of players, tightly packed.
Low PC1 and low PC2 values → likely low overall contributions in key stats.
Could represent support or defensive role players with limited attacking involvement.

Cluster 1:
Moderate-to-high PC1, low PC2.
Spread along PC1 → variability in one major component, but consistent on the other.
Likely attacking/goal-oriented players with higher scoring or forward metrics.

Cluster 2:
Low PC1, slightly positive PC2.
Clustered close together → consistent playing style.
Could represent midfield or defensive support players with good passing/possession stats.

Cluster 3:
Slightly negative PC1, high PC2 values.
High on PC2 → likely strong in a secondary component, possibly defensive recoveries or assists.
Could indicate creative midfielders or ball-winning players.

Cluster 4:
PC1 around 0–2, PC2 around 0–5.
Densely packed → very consistent cluster.
Likely all-round midfielders who balance attacking and defensive contributions.

Cluster 5:
Positive PC1, near-zero PC2.
Spread along PC1 → indicates variability in primary component (maybe goal scoring, attacking metrics).
Likely attacking players or wingers.

Cluster 6:
High PC1, slightly negative PC2.
Few players → outliers in attack-oriented stats.
Could represent star forwards or high-impact attackers with very strong scoring metrics.

PCA Feature Loadings:
PC1: heavily influenced by Gper, Aper, Bper → attacking output dominates first principal component.
PC2: Tper negatively loaded, passes per match positively loaded → separates defensive vs possession-oriented players.

This explains why clusters are separating based on attack vs defense and passing activity.


   

