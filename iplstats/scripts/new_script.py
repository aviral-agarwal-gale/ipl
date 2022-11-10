import json
import csv  
from itertools import groupby
from operator import itemgetter
from datetime import datetime
from stats.models import Native
import csv
from djqscsv import write_csv
import timeit
from collections import defaultdict
from django.core import serializers
from django.http import HttpResponse
# Opening JSON file
f = open('/Users/aviralagarwal/gale/ipl/iplstats/scripts/input_data.json')
  
data = json.load(f)
f.close()
input_file = data['input_file_path']

output_file = data['output_file_path']
output_file_type = data['output_file_type']

dimensions = data['dimensions']
metrics = data['metrics']
filters = data['filters']
old_start_date = data['date']['start_date']
old_end_date = data['date']['end_date']
print("start_date: ",old_start_date)
print("end_date", old_end_date)
start_date = datetime.strptime(old_start_date, '%Y-%m-%d').date()
end_date = datetime.strptime(old_end_date, '%Y-%m-%d').date()
print(start_date)
print(end_date)
sort = data['sort']

pagination = data['pagination']
limit = pagination['limit']
page = pagination['page']

dim_met = dimensions + metrics
dim_met.insert(0,'\ufeffdate')   
def run():
    timer_start = timeit.default_timer()
    with open(input_file,'r',newline='') as fin,open(output_file,'w',newline='') as fout:
        final = []
        # skip needed because sample data had spaces after comma delimiters.
        reader = csv.DictReader(fin, skipinitialspace=True)

        # Output file will have these fieldnames
        writer = csv.DictWriter(fout,fieldnames=dim_met)
        writer.writeheader()
        for i in reader:
            dat = i['\ufeffdate']
            new_date = datetime.strptime(dat, '%d/%m/%Y').date()
            temp = {}
            if ((new_date > start_date and new_date < end_date) and (i[key] in value for key,value in filters.items())):
                for k in i:
                    if k in dim_met: 
                        temp[k] = i[k]
                final.append(temp)
        for i in sort:
            name = i['name']
            order = i['order']
            if order == 'ASC':
                final = sorted(final, key=itemgetter(name))
            else:
                final = sorted(final, key=itemgetter(name), reverse=True)
                
        end_range = limit*page  
        start_range = end_range - limit 
        json_opt = []
        if end_range < len(final):
            for row in range(start_range, end_range):
                writer.writerow(final[row])
                json_opt.append(final[row])  
        else:
            end_range = len(final)
            for row in range(start_range, end_range):
                writer.writerow(final[row])
                json_opt.append(final[row])
        if output_file_type == 'json':
            jsn = json.dumps({'results': json_opt})
            with open(output_file, 'w') as outfile:
                outfile.write(jsn)                                            
        process_time = timeit.default_timer() - timer_start
        print(process_time)                