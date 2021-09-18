from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *

if __name__ == '__main__':
	sc = SparkContext(appName='TSV2Parquet')
	sqlContext = SQLContext(sc)

	schema = StructType([
		StructField("SOURCE_DESC", StringType(), True),
		StructField("SECTOR_DESC", StringType(), True),
		StructField("GROUP_DESC", StringType(), True),
		StructField("COMMODITY_DESC", StringType(), True),
		StructField("CLASS_DESC", StringType(), True),
		StructField("PRODN_PRACTICE_DESC", StringType(), True),
		StructField("UTIL_PRACTICE_DESC", StringType(), True),
		StructField("STATISTICCAT_DESC", StringType(), True),
		StructField("UNIT_DESC", StringType(), True),
		StructField("SHORT_DESC", StringType(), True),
		StructField("DOMAIN_DESC", StringType(), True),
		StructField("DOMAINCAT_DESC", StringType(), True),
		StructField("AGG_LEVEL_DESC", StringType(), True),
		StructField("STATE_ANSI", IntegerType(), True),
		StructField("STATE_FIPS_CODE", IntegerType(), True),
		StructField("STATE_ALPHA", StringType(), True),
		StructField("STATE_NAME", StringType(), True),
		StructField("ASD_CODE", IntegerType(), True),
		StructField("ASD_DESC", StringType(), True),
		StructField("COUNTY_ANSI", IntegerType(), True),
		StructField("COUNTY_CODE", IntegerType(), True),
		StructField("COUNTY_NAME", StringType(), True),
		StructField("REGION_DESC", IntegerType(), True),
		StructField("ZIP_5", IntegerType(), True),
		StructField("WATERSHED_CODE", IntegerType(), True),
		StructField("WATERSHED_DESC", IntegerType(), True),
		StructField("CONGR_DISTRICT_CODE", IntegerType(), True),
		StructField("COUNTRY_CODE", IntegerType(), True),
		StructField("COUNTRY_NAME", StringType(), True),
		StructField("LOCATION_DESC", StringType(), True),
		StructField("YEAR", IntegerType(), True),
		StructField("FREQ_DESC", StringType(), True),
		StructField("BEGIN_CODE", IntegerType(), True),
		StructField("END_CODE", IntegerType(), True),
		StructField("REFERENCE_PERIOD_DESC", StringType(), True),
		StructField("WEEK_ENDING", IntegerType(), True),
		StructField("LOAD_TIME", StringType(), True),
		StructField("VALUE", StringType(), True),
		StructField("CV_%", IntegerType(), True)
		])
	rdd = sc.textFile('~/ag_census_analysis/truncated_ag_census_2002.txt') 
	df = sqlContext.createDataFrame(rdd, schema)
	df.write.parquet('~/ag_census_analysis/truncated_ag_census_2002-parquet')
