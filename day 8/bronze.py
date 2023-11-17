# Databricks notebook source
# MAGIC %sql
# MAGIC create schema if not exists projectHexAD;
# MAGIC use projectHexAD;

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists projectHexAD.bronze

# COMMAND ----------

# MAGIC %sql
# MAGIC COPY INTO projectHexAD.bronze
# MAGIC FROM 'dbfs:/mnt/asadlsad/processeddata/inputproject/json'
# MAGIC FILEFORMAT = JSON
# MAGIC FORMAT_OPTIONS('multiline'='True')
# MAGIC COPY_OPTIONS ('mergeSchema' = 'true')

# COMMAND ----------

print("hello there")

# COMMAND ----------


