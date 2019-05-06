import csv

def get_month_stats(provided_file, month):
  with open(provided_file, 'r') as data_file:
    csv_data = csv.DictReader(data_file)
    play_dict = {}
    rev_dict = {}
    for item in csv_data:
      if item['DAY'].split('-')[1] == month:
        if item['WORK_ID'] in play_dict:
          play_dict[item['WORK_ID']] += int(item['PLAYS'])
          rev_dict[item['WORK_ID']] += float(item['REVENUE'])
        else:
          play_dict[item['WORK_ID']] = int(item['PLAYS'])
          rev_dict[item['WORK_ID']] = float(item['REVENUE'])

  ds = [play_dict, rev_dict]
  d = {}
  for k in play_dict.keys():
    d[k] = tuple(d[k] for d in ds)

  # print(d)

  with open(f'MERGED_METRICS_{month}.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["WORK_ID", "PLAYS", "REVENUE",'MONTH'])
    for key in d.keys():
        f.write("%s,%s\n"%(key,f"{d[key][0]},{d[key][1]},{month}"))

#FUNCTION CALL BELOW
# -CSV FILE YOU WISH TO PARSE CAN BE PLACED AS FIRST PARAMETER AS LONG AS ITS SET AS header is WORK_ID,REVENUE,PLAYS,DAY
# -MONTH CAN BE PLACED AS SECOND PARAMETER AS LONG AS IT IS DAY-MONTH FORMAT IN FILE

#for july stats
get_month_stats('DATA_MERGED.CSV', 'Jul')
#for jun stats
# get_month_stats('DATA_MERGED.CSV', 'Jun')