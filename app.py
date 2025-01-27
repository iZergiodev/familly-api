from flask import Flask, request, jsonify
from models import FamilyStructure

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo_list.db"

jackson_family = FamilyStructure('Jackson')

@app.route('/members', methods = ['GET'])
def get_all_members():
    data = jackson_family.get_all_members()
    response_body = {
        "family": data
    }

    return jsonify(response_body), 200



@app.route('/member/<int:id>', methods = ['GET'])
def get_member_by_id(id):
    data = jackson_family.get_member(id)

    return jsonify(data), 200




@app.route('/members', methods = ['POST'])
def create_member():
    try:
        data = request.get_json()

        response = {
            "id": jackson_family._generate_id(),
            "first_name": data['first_name'],
            "age": data['age'],
            "lucky_numbers": data['lucky_numbers']
        }

        jackson_family.add_member(response)

        return jsonify(response), 201

    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500



@app.route('/member/<int:id>', methods = ['DELETE'])
def delete_member(id):
    result = jackson_family.delete_member(id)
    
    if "error" in result:
        return jsonify(result), 404
    else:
        return jsonify(result), 200

