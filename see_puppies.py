from datetime import date
import MySQLdb
import requests
import settings

class GetDogs()
	def __init__():
		pass

	def request_url_contents(self, url):
		r = request.get(url)
		return r

	def create_filename(self, url):
		now = datetime.datetime.now()
		filename = url + now
		return filename

	def save_contents(self, url):
		r = request_url_contents(url)
		contents = r.text
		filename = create_filename(url)
		f = open(filename, 'w')
		f.write(contents)
		f.close
	
	def dog_details(self, contents):
		detail_dict = {}
		detail_dict['name'] = self.dog_name(contents)
		detail_dict['id'] = self.dog_id(contents)
		detail_dict['gender'] = self.dog_gender(contents)
		detail_dict['breed'] = self.dog_breed(contents)
		detail_dict['color'] = self.dog_color(contents)
		detail_dict['age'] = self.dog_age(contents)
		detail_dict['description'] = self.dog_description(contents)
		detail_dict['image'] = self.dog_image(contents)
		return detail_dict

	def dog_detailts_to_db(self, detail_dict):
		conn = conn = MySQLdb.connect(host= "localhost",
			                          user="root",
				                      passwd = settings.db_password,
				                      db="jewelryscraperdb")
	    cursor = conn.cursor()        
        cursor.execute (" SELECT * FROM products WHERE product_id = %s AND retailer_id = %s ", (product_dict['product_id'],product_dict['retailer_id']))
        rows = cursor.fetchall()
	    if len(rows) == 0: 
	        cursor.execute (" INSERT INTO products (name,id,gender,breed,color,age,description,image) VALUES (%s,%s,%s,%s,%s,%s) ", (product_dict['name'],product_dict['product_id'],product_dict['price'],product_dict['image'], product_dict['description'], product_dict['retailer_id']))

														
