hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D stream.num.map.output.key.fields=1 \
-D num.key.fields.for.partition=1 \
-D mapreduce.partition.keycomparator.options=-k1 \
-D mapreduce.partition.keypartitioner.options=-k1 \
-D mapreduce.job.reduces=1 \
-input 	/data/assignments/ex2/part1/large/ \
-output /user/s1669411/assignment2/task1 \
-mapper mapper.py \
-file damon_EC_CW2/task1/mapper.py \
-reducer reducer.py \
-file damon_EC_CW2/task1/reducer.py 
