from flask import Flask, request, abort, Response
import json
from businessLogic import business
import sys

app = Flask(__name__)
if len(sys.argv)>1 and sys.argv[1] == "-test":
	ob = business(True)
else:
	ob = business()

@app.route("/menusection", methods = ['GET'])
def get_menu():
	return ob.get_menu()

@app.route("/menusection", methods = ['POST'])
def add_menu():
	data, err_code = ob.add_menu_section(request.get_json())
	if not data:
		return Response(json.dumps({'success':False}, indent=4), status=err_code)
	else:
		return data

@app.route("/menusection/<section_id>", methods = ['GET', 'PUT','DELETE'])
def operations(section_id):
	if request.method == 'GET':
		res = ob.get_menu_by_id(section_id)
		if not res:
			return Response(json.dumps({'success':False}, indent=4), status=400)
		else:
			return res

	if request.method == 'DELETE':
		res = ob.delete_menu_by_id(section_id)
		if not res:
			return Response(json.dumps({'success':False}, indent=4), status=400)
		else:
			return res

	if request.method == 'PUT':
		data , err_code = ob.update_menu_by_id(section_id, request.get_json())
		if not data:
			return Response(json.dumps({'success':False}, indent=4), status=err_code)
		else:
			return data

if __name__ == '__main__':
	app.run(debug = True, port=ob.get_port())