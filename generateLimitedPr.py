#!/usr/bin/python
import os
import json
import time
import urllib2
import sys

api_key='3xvhyc8utc852wrwhy34n8wk'

f2=open('products1Limited.txt','w')
f1=open('sku_list.csv','r')

line=f1.readline()
cnt = 1
prvsku = 'null'

while line :
	values = line.split(",")
	osku = values[0]
        relsku = values[1]
        reltype = values[2]
       	time.sleep(1)
	if osku != prvsku or cnt == 1 :
		webURL = 'http://api.remix.bestbuy.com/v1/products(sku='+str(osku)+')?format=json&apiKey=3xvhyc8utc852wrwhy34n8wk'
		cnt = cnt +1
		try:
			print("Inside original load SKU")
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
				'type' : str(json_str["type"]),
				'skutype': str("Original"),
				'parent' : str("null")
			}
			json_content=json.dumps(product_data) + '\n'
			f2.write(json_content)
			webFile.close()
		except:
			e = sys.exc_info()[0]
			print( "Error: %s" % e )
	prvsku=osku
	webURL = 'http://api.remix.bestbuy.com/v1/products(sku='+str(relsku)+')?format=json&apiKey=3xvhyc8utc852wrwhy34n8wk'
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
                        'type' : str(json_str["type"]),
                        'skutype': str(reltype),
			'parent' : str(osku)
                }
                json_content=json.dumps(product_data) + '\n'
                f2.write(json_content)
                webFile.close()
        except: 
                e = sys.exc_info()[0]
                print( "Error: %s" % e )
	
	line=f1.readline()
f2.close()
