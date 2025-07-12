# install java,spark,findspark,pymysql
!apt-get install openjdk-11-jdk-headless -qq > /dev/null
!wget -q https://archive.apache.org/dist/spark/spark-3.4.1/spark-3.4.1-bin-hadoop3.tgz
!tar -xzf spark-3.4.1-bin-hadoop3.tgz
!pip install -q findspark
!pip install pymysql