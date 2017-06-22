hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.reduces=1 \
-input 	/user/s1669411/assignment1/task7 \
-output /user/s1669411/assignment1/task8 \
-mapper mapper.py \
-file damon_extreme_computing_cw1/task8/mapper.py \
-reducer reducer.py \
-file damon_extreme_computing_cw1/task8/reducer.py
