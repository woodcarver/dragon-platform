# install
python3 setup.py install
# config
1. 替换application.py 的setting，使用线上配置好的setting文件
2. 

# start up
python3 application.py

# how to write sql directly
files_info = session.execute("select * from simulation_files")
basic_info['files'] = format_sql_result(files_info)