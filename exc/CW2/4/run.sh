##first mapreduce without reducer. 
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.reduces=1 \
-input 	/data/assignments/ex2/part2/stackLarge.txt \
-output /user/s1669411/assignment2/task_4_1 \
-mapper mapper1.py \
-file damon_EC_CW2/task4/mapper1.py
##copy acceptedid to local in order to improve the effeciency
hdfs dfs -copyToLocal /user/s1669411/assignment2/task_4_1
#second M/P job
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D stream.num.map.output.key.fields=1 \
-D num.key.fields.for.partition=1 \
-D mapreduce.partition.keypartitioner.options=-k1 \
-D mapreduce.job.reduces=15 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-input 	/data/assignments/ex2/part2/stackLarge.txt \
-output /user/s1669411/assignment2/task_4_2 \
-mapper mapper2.py \
-file damon_EC_CW2/task4/mapper2.py \
-reducer reducer1.py \
-file damon_EC_CW2/task4/reducer1.py \
-file damon_EC_CW2/task4/AC_list.txt
####third mapreduce job
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D stream.num.map.output.key.fields=1 \
-D mapreduce.partition.keycomparator.options="-k 1nr" \
-D mapreduce.job.reduces=1 \
-input 	/user/s1669411/assignment2/task_4_2 \
-output /user/s1669411/assignment2/task4 \
-mapper mapper3.py \
-file damon_EC_CW2/task4/mapper3.py \
-reducer reducer2.py \
-file damon_EC_CW2/task4/reducer2.py
