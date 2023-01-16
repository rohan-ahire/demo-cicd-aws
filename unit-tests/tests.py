# Databricks notebook source
from my_package.code1 import * 
from my_package.code2 import * 

from runtime.nutterfixture import NutterFixture, tag

class TestFixtureArbitraryFiles(NutterFixture):
  def __init__(self):
    self.code2_table_name = "my_data"
    self.code1_view_name = "my_cool_data"
    self.code1_num_entries = 100
    NutterFixture.__init__(self)
    
  def run_code1_arbitrary_files(self):
    generate_data1(spark, n = self.code1_num_entries, name = self.code1_view_name)
    
  def assertion_code1_arbitrary_files(self):
    df = spark.read.table(self.code1_view_name)
    assert(df.count() == self.code1_num_entries)
    
  def run_code2_arbitrary_files(self):
    generate_data2(table_name = self.code2_table_name)
    
  def assertion_code2_arbitrary_files(self):
    some_tbl = spark.sql(f'SELECT COUNT(*) AS total FROM {self.code2_table_name}')
    first_row = some_tbl.first()
    assert (first_row[0] == 10)

  def after_code2_arbitrary_files(self):
    spark.sql(f"drop table {self.code2_table_name}")


# COMMAND ----------

result = TestFixtureArbitraryFiles().execute_tests()
print(result.to_string())

# COMMAND ----------

is_job = dbutils.notebook.entry_point.getDbutils().notebook().getContext().currentRunId().isDefined()
if is_job:
  result.exit(dbutils)
