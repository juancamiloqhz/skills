from pathlib import Path
import json
r=Path(__file__).parent
rules={f'category-{i}': {'minimum':i%7,'multiplier':1+i%4} for i in range(64)}
events=[{'type':f'category-{i%67}', 'amount':i%101} for i in range(80000)]
(r/'events.json').write_text(json.dumps(events,separators=(',',':'))+'\n')
(r/'rules.json').write_text(json.dumps(rules,separators=(',',':'))+'\n')
totals={};accepted=0
for event in events:
 rule=rules.get(event['type'])
 if rule and event['amount']>=rule['minimum']:
  accepted+=1;totals[event['type']]=totals.get(event['type'],0)+event['amount']*rule['multiplier']
(r/'expected.json').write_text(json.dumps({'processed':len(events),'accepted':accepted,'rejected':len(events)-accepted,'totals':totals},separators=(',',':'))+'\n')
