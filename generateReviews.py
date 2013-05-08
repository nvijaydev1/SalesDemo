import xml.etree.ElementTree as ET
import urllib2
import csv
from random import randint
import json
import sys

f2 = open('reviewsOut.txt', 'w')

sku_arr = [];
i=0;
csvReader = csv.reader(open('sku_rating.csv', 'rb'), delimiter=' ');
for row in csvReader:
	sku_arr.append(row);
	
api_key='3xvhyc8utc852wrwhy34n8wk'
count = 1
while count < 100 :
	reviewURL='http://api.remix.bestbuy.com/v1/reviews?page=' + str(count) + '&apiKey=3xvhyc8utc852wrwhy34n8wk'
	print (reviewURL)
	try :
		reviewFile=urllib2.urlopen(reviewURL)
		reviewDoc=reviewFile.read()
		reviewDoc=reviewDoc.replace("\n", "")
		root=ET.fromstring(reviewDoc)
		for review in root.findall('review') :
			randnum = randint(0, len(sku_arr))
			review_data = {
				'sku' : str(sku_arr[randnum][0]),
				'rating' : str(review.find('rating').text),
				'id' : str(review.find('id').text),
			'name' : str(review.find('reviewer').find('name').text),
			'title' : str(review.find('title').text),
			'comment' : str(review.find('comment').text),
			'submissionTime' : str(review.find('submissionTime').text)	
			}
			json_content=json.dumps(review_data) + '\n'
			f2.write(json_content)
	except:
                e = sys.exc_info()[0]
                print( "Error: %s" % e )
	count = count +1	
f2.close	

