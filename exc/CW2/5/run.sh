hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapred.reduce.tasks=1 \
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D mapred.text.key.comparator.options=-n \
-input 	/data/assignments/ex2/part3/webLarge.txt \
-output /user/s1669411/assignment2/task5 \
-mapper mapper.py \
-file damon_EC_CW2/task5/mapper.py \
-reducer reducer.py \
-file damon_EC_CW2/task5/reducer.py 
