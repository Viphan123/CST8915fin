import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize an empty staff data list
staff_data = []

# Load the staff data from staff.json into memory
with open('staff.json') as f:
    staff_data = json.load(f)

# Define the CRUD endpoints
@app.route('/staff', methods=['GET'])
def get_all_staff():
    return jsonify(staff_data)

@app.route('/staff/<int:id>', methods=['GET'])
def get_staff(id):
    staff = next((s for s in staff_data if s['id'] == id), None)
    if staff:
        return jsonify(staff)
    return jsonify({'message': 'Staff not found'}), 404

@app.route('/staff', methods=['POST'])
def create_staff():
    new_staff = request.json
    staff_data.append(new_staff)
    return jsonify(new_staff), 201

@app.route('/staff/<int:id>', methods=['PUT'])
def update_staff(id):
    staff = next((s for s in staff_data if s['id'] == id), None)
    if staff:
        staff.update(request.json)
        return jsonify(staff)
    return jsonify({'message': 'Staff not found'}), 404

@app.route('/staff/<int:id>', methods=['DELETE'])
def delete_staff(id):
    staff = next((s for s in staff_data if s['id'] == id), None)
    if staff:
        staff_data.remove(staff)
        return jsonify({'message': 'Staff deleted'})
    return jsonify({'message': 'Staff not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
