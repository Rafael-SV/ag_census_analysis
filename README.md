# ag_census_analysis

This is a 2 month long project started at the end of october. 

In order to predict the best ways a new Ag tech startup can market to earlyvangelist farmers, the growers most likely to adopt new technology need to be identified.

This project will take change in crop type in an area as a proxy for willingness of the local farmers to try new technology.

Until the project is finished, multiple jupyter notebooks will be used, also added at the end will be a function to download the raw data and turn it into parquet.

The first notebook uses pyspark to read parquet files then explores and cleans with spark.sql.  

The second notebook reads the output from the first into a dask dataframe for further processing, followed by machine learning algorithms. 

The ML starts with unsupervised learning to cluster areas based on crop types, (these clusters are visualized on a united states map using plotly.) The the features identified in the clustering will be used in a classifier to bin later data. Finally areas that are in different clusters will be identified.

This repo contains some analysis of United States Department of Agriculture census data. The USDA ag census occurs every 5 years.
The data can be downloaded from here: ftp://ftp.nass.usda.gov/quickstats/ 
