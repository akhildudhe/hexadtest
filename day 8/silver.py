# Databricks notebook source
# MAGIC %python
# MAGIC from pyspark.sql.functions import *

# COMMAND ----------

# MAGIC %python
# MAGIC df=spark.read.table("projectHexAD.bronze")
# MAGIC df_final=df.withColumn("products",explode("products"))\
# MAGIC .withColumn("price",col("products.price"))\
# MAGIC .withColumn("product_id",col("products.product_id"))\
# MAGIC .withColumn("product_name",col("products.product_name"))\
# MAGIC .withColumn("quantity",col("products.quantity"))\
# MAGIC .withColumn("timestamp",col("timestamp").cast("timestamp"))\
# MAGIC .drop("products")
# MAGIC df_final.write.mode("overwrite").saveAsTable("projectHexAD.silver")

# COMMAND ----------

print("hello there")

# COMMAND ----------


