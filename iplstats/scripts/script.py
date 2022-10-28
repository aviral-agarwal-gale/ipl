import json
import csv  
from datetime import datetime
from stats.models import Native
import csv
from djqscsv import write_csv
import timeit

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
start_date = data['date']['start_date']
end_date = data['date']['end_date']
print("start_date: ",start_date)
print("end_date", end_date)

sort = data['sort']
order_list=[]
for i in sort:
    name = i['name']
    order = i['order']
    if order == 'ASC':
        order_list.append(name)
    else:
        order_list.append("-"+name)        

print(order_list)    
dim_met = dimensions + metrics
   
def run():
    with open(input_file) as file:
        reader = csv.reader(file, dialect='excel')
        next(reader)  # Advance past the header

        Native.objects.all().delete()

        for row in reader:
            new_date = datetime.strptime(row[0], '%d/%m/%Y').date()
            print(new_date)
            native = Native(DATE = new_date,
                PCC_SITENAME = row[1],
                PCC_AUDIENCE = row[2],
                PCC_UNIT_TYPE = row[3],
                PCC_PLATFORM_DEVICE = row[4],
                CREATIVE_NAME = row[5],
                CREATIVE_TYPE = row[6],
                CREATIVE_PLACEMENT = row[7],
                CAMPAIGN_GROUP = row[8],
                HEADLINE = row[9],
                BODY = row[10],
                COST = row[11],
                CLICKS = row[12],
                IMPRESSIONS = row[13],
                ENGAGEMENTS = row[14],
                LIKES = row[15],
                SHARES = row[16],
                LEADS = row[17],
                FOLLOWS = row[18],
                COMMENTS = row[19],
                REACTIONS = row[20],
                LANDING_PAGE_CLICKS = row[21])
            native.save() 
            
            
    timer_start = timeit.default_timer()
    
    if output_file_type == 'CSV':
        print("-------")
        query_set = Native.objects.filter(DATE__range=[start_date, end_date], PCC_AUDIENCE__in=filters['PCC_AUDIENCE'],
                                        PCC_PLATFORM_DEVICE__in=filters['PCC_PLATFORM_DEVICE'], PCC_SITENAME__in=filters['PCC_SITENAME'],
                                        PCC_UNIT_TYPE__in=filters['PCC_UNIT_TYPE']).values(*dim_met).order_by(*order_list)
        process_time = timeit.default_timer() - timer_start
        print(process_time)
        with open(output_file, 'wb') as csv_file:
            write_csv(query_set, csv_file)
    else:        
        query_set1 = Native.objects.filter(DATE__range=[start_date, end_date], PCC_AUDIENCE__in=filters['PCC_AUDIENCE'],
                                        PCC_PLATFORM_DEVICE__in=filters['PCC_PLATFORM_DEVICE'], PCC_SITENAME__in=filters['PCC_SITENAME'],
                                        PCC_UNIT_TYPE__in=filters['PCC_UNIT_TYPE']).only(*dim_met)
    
        qs_json = serializers.serialize('json', query_set1)
        process_time = timeit.default_timer() - timer_start
        print(process_time)
        with open(output_file, 'w') as outfile:
            outfile.write(qs_json)
            