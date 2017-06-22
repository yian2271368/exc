hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.reduces=1 \
-input 	/data/assignments/ex2/part2/stackLarge.txt \
-output /user/s1669411/assignment2/task2 \
-mapper mapper.py \
-file damon_EC_CW2/task2/mapper.py \
-combiner combiner.py \
-file damon_EC_CW2/task2/combiner.py \
-reducer reducer.py \
-file damon_EC_CW2/task2/reducer.py 

