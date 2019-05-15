import csv  
import json  
    
# Open the CSV  
f = open( 'final_data.csv', 'rU' )  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "description","sentiment"))  
# Parse the CSV into JSON  
out = json.dumps( [ row for row in reader ] )  
print("JSON parsed!")  
# Save the JSON  
f = open( 'final_data.json', 'w')  
f.write(out)  
print("JSON saved!") 