# now in here files spark_exports are converted to zip file
# then these all format files are download from there
# step7 
!zip -r spark_exports.zip spark_exports > /dev/null 

# step8
from google.colab import files
files.download("spark_exports.zip")
