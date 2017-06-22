hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-input /data/assignments/ex1/webLarge.txt \
-output /user/s1669411/assignment1/task1 \
-mapper mapper.py \
-file damon_extreme_computing_cw1/task1/mapper.py

