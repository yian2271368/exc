hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-input 	/data/assignments/ex1/uniLarge.txt \
-output /user/s1669411/assignment1/task7 \
-mapper mapper.py \
-file damon_extreme_computing_cw1/task7/mapper.py \
-reducer reducer.py \
-file damon_extreme_computing_cw1/task7/reducer.py
