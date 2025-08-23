import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import plotly.express as px
import plotly.graph_objects as go

st.title("Football Player Clustering Dashboard")

df = pd.read_csv("/Users/deathekid/Downloads/archive-3/player_stats_s.csv")

df_gk = df[df['Sper'] > 0].copy()
df_outfield = df[df['Sper'] == 0].copy()

features_outfield = [
    'Gper','Aper','Bper','Tper','Passes per match',
    'Dper','Abper','Iper','Cper','Lbper','Tbper',
    'Recoveries','Clearances'
]
df_outfield[features_outfield] = df_outfield[features_outfield].fillna(0)

scaler = StandardScaler()
X_outfield = scaler.fit_transform(df_outfield[features_outfield])

pca = PCA(n_components=2)
X_pca_out = pca.fit_transform(X_outfield)

df_outfield['pca1'] = X_pca_out[:, 0]
df_outfield['pca2'] = X_pca_out[:, 1]

optimal_k_out = 7
kmeans_out = KMeans(n_clusters=optimal_k_out, random_state=42, n_init=50)
df_outfield['cluster'] = kmeans_out.fit_predict(X_outfield)

cluster_sizes_out = df_outfield['cluster'].value_counts()

cluster_summary = df_outfield.groupby('cluster')[features_outfield].mean()
cluster_summary_norm = (cluster_summary - cluster_summary.min()) / (cluster_summary.max() - cluster_summary.min())


loadings = pd.DataFrame(
    pca.components_.T,
    columns=['PC1','PC2'],
    index=features_outfield
)

fig_pca = px.scatter(
    df_outfield,
    x="pca1", y="pca2",
    color=df_outfield['cluster'].astype(str),
    hover_name="Name",
    title="Outfield Player Clusters (PCA)",
    labels={
        "pca1": f"PC1 ({pca.explained_variance_ratio_[0]:.2%} variance)",
        "pca2": f"PC2 ({pca.explained_variance_ratio_[1]:.2%} variance)"
    }
)
st.plotly_chart(fig_pca)

fig_sizes = go.Figure()
fig_sizes.add_trace(go.Bar(
    x=cluster_sizes_out.index.astype(str),
    y=cluster_sizes_out.values,
    marker_color=px.colors.sequential.Viridis
))
fig_sizes.update_layout(
    title="Number of Outfield Players per Cluster",
    xaxis_title="Cluster",
    yaxis_title="Count"
)
st.plotly_chart(fig_sizes)

fig_radar = go.Figure()
angles = features_outfield
for cluster_id in range(optimal_k_out):
    values = cluster_summary_norm.loc[cluster_id].values.tolist()
    values += values[:1]
    fig_radar.add_trace(go.Scatterpolar(
        r=values,
        theta=angles + [angles[0]],
        fill='toself',
        name=f'Cluster {cluster_id}'
    ))
fig_radar.update_layout(
    polar=dict(radialaxis=dict(visible=True)),
    title="Normalized Cluster Profiles (Radar Chart)"
)
st.plotly_chart(fig_radar)

fig_loadings = go.Figure()
fig_loadings.add_trace(go.Bar(x=loadings.index, y=loadings["PC1"], name="PC1"))
fig_loadings.add_trace(go.Bar(x=loadings.index, y=loadings["PC2"], name="PC2"))
fig_loadings.update_layout(
    title="Feature Loadings in PCA Components",
    yaxis_title="Loading Score",
    barmode="group"
)
st.plotly_chart(fig_loadings)
