hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-input 	/user/s1669411/assignment1/task1 \
-output /user/s1669411/assignment1/task2 \
-mapper mapper.py \
-file damon_extreme_computing_cw1/task2/mapper.py \
-reducer reducer.py \
-file damon_extreme_computing_cw1/task2/reducer.py
