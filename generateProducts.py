#!/usr/bin/python
import os
import json
import time
import urllib2
import sys
from premix import ProductQuery

api_key='3xvhyc8utc852wrwhy34n8wk'

f2=open('products.txt','w')

product_query = ProductQuery.all().filter('search =', 'laptop')

results=product_query.fetch(api_key)

totalpages = results.total_pages
curpage = results.current_page

while (curpage < totalpages) :
	try:
 		cur_results = product_query.fetch(api_key, page=curpage)
        	begin = 1
		end =10 
        	curprod=begin
        	time.sleep(1)
		while curprod < end :
                	product = cur_results.products[curprod]
    			sku = product.sku
			webURL = 'http://api.remix.bestbuy.com/v1/products(sku='+str(sku)+')?format=json&apiKey=3xvhyc8utc852wrwhy34n8wk'
 			try:
				webFile = urllib2.urlopen(webURL)
				strInfo = webFile.read()
				strInfo = strInfo.replace('\n', "")
				strInfo = strInfo + '\n'
				# load  the weburl into JSON
				item = json.loads(strInfo)
				product = item["products"]
				json_str = item["products"][0]

				product_data = {
					'productTemplate' : json_str["productTemplate"],
					'sku' : json_str["sku"],
					'color' : str(json_str["color"]),
					'includedItemList' : json_str["includedItemList"],
					'description' : str(json_str["description"]),
					'department' : str(json_str["department"]),
					'relatedProducts' :  json_str["relatedProducts"],
					'regularPrice' : json_str["regularPrice"],
					'shortDescription' :  str(json_str["shortDescription"]),
					'manufacturer' : str(json_str["manufacturer"]),
					'subclass' : json_str["subclass" ],
					'technologyCode' : str(json_str["technologyCode"]),
					'modelNumber' : json_str["modelNumber"],
					'digital' : json_str["digital"],
					'salesRankMediumTerm' : str(json_str["salesRankMediumTerm"]),
					'subclassId' :  json_str["subclassId"],
					'upc' : json_str["upc"],
					'class_1' : json_str["class"],
					'classId' : json_str["classId"],
					'productId' : json_str["productId"],
					'source' : json_str["source"],
					'frequentlyPurchasedWith' : json_str["frequentlyPurchasedWith"],
					'categoryPath'  : json_str["categoryPath"],
        				'longDescription' : json_str["longDescription"],
        				'width'  : str(json_str["width"]),
        				'type' : str(json_str["type"])
				}
				json_content=json.dumps(product_data) + '\n'
				f2.write(json_content)
                		webFile.close()
			except:
				e = sys.exc_info()[0]
  				print( "Error: %s" % e )
			curprod += 1
		curpage += 1
	except:
		e2 = sys.exc_info()[0]
        	print( "Error: %s" % e2 )	
f2.close()
