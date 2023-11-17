# Databricks notebook source
# MAGIC %sql
# MAGIC Create or replace table projectHexAD.gold as (select product_name, sum(quantity) as totalquantity from projectHexAD.silver group by all order by totalquantity desc)

# COMMAND ----------

print("hello there")

# COMMAND ----------


