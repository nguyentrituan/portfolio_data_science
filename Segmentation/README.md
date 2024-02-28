# Hands-on: Online-Retail analytics pipeline

We will sit together and hands-on to put together what we have learnt to build a "workable" analytics pipeline. 
Besides, we learn by hands-on with several analytics techniques: Cohort analysis, RFM analysis, and Clustering.


## 🚩 Toolings

- `dvc` to version and collaborate on datasets (raw, intermediate, metrics/insight layers)
- `Python` + `Jupyter Notebook` to do analysis, visualization, and modeling
- `git`: versioning code and collaborate
- `elyra`: create an analytics workflow


## 🧬 Analytics techniques

- [Cohort analysis](../03-hands-on-01/01_OnlineRetail_Cohort.ipynb)
- [RFM analysis](../03-hands-on-01/02_OnlineRetail_RFM.ipynb)
- [K-means clustering](../03-hands-on-01/03_OnlineRetail_KMeans.ipynb)


## 📝 TODO

> Work in pairs. Your final goal is to build end-to-end pipeline (from loading, cleaning to analysis) to provide insights from cohort, RFM, and K-means clustering analysis in an meaningful ways for business

1. Init a repo to work with your peer
2. Now, the dataset is in `data/online-retail.csv`, it is not a good practice to keep the raw data in git repo. Use `dvc` to version and collaborate on the raw data (See: [dvc-assigment.md](../02-reproducibility/dvc-assignment.md))
    - Init `dvc`
    - Config `dvc-remote`
    - Version data with `dvc`
3. Please go through 03 notebooks and complete TODO
4. Restructure notebooks into Elyria pipeline with:
    - Load / cleaning / transform data (from primary => intermediate)
    - Generate tables input into visualization (from intermediate => insight layer)
    - Visualize and comments
