from sanic import Sanic
from sanic.response import json

app = Sanic()
users = [{
    "id": 1,
    "name": "Homere Sobtka",
    "email": "hsobtka0@sphinn.com",
    "pass": "gj0wbmQT"
}, {
    "id": 2,
    "name": "Georgeta Vasiliev",
    "email": "gvasiliev1@squidoo.com",
    "pass": "MNPoFNQvK"
}, {
    "id": 3,
    "name": "Alister Bygrove",
    "email": "abygrove2@miitbeian.gov.cn",
    "pass": "Zo2LnC"
}, {
    "id": 4,
    "name": "Gaylene Dumbleton",
    "email": "gdumbleton3@google.com.au",
    "pass": "qrgdyx8fqAY"
}, {
    "id": 5,
    "name": "Owen Choppin",
    "email": "ochoppin4@uiuc.edu",
    "pass": "0YSjpCu"
}, {
    "id": 6,
    "name": "Simonne Simioni",
    "email": "ssimioni5@senate.gov",
    "pass": "qJylD3J"
}, {
    "id": 7,
    "name": "Wilmette Mackness",
    "email": "wmackness6@people.com.cn",
    "pass": "7UlwKXHxn"
}, {
    "id": 8,
    "name": "Ev Surgenor",
    "email": "esurgenor7@rediff.com",
    "pass": "gEifQ6M1s"
}, {
    "id": 9,
    "name": "Joly Vero",
    "email": "jvero8@apache.org",
    "pass": "srzJyoofGhO"
}, {
    "id": 10,
    "name": "Urbano Horbart",
    "email": "uhorbart9@cnet.com",
    "pass": "TuHyPvlZ82"
}]


@app.route("/users")
async def test(request):
    return json(users)


@app.route('/users/<id:int>')
async def get_user_by_id(request, id):
    for user in users:
        if user["id"] == id:
            return json(user)

    return json("")

@app.route("/users", methods=['POST'])
async def add_usr(request):   
    raw = request.json # Hứng POST định dạng application/json phải dùng request.json

    next_id = users[-1]["id"] + 1
    user = {
        'id': next_id,
        'name': raw["name"],
        'email': raw['email'],
        'pass': raw['pass']    
    }
    users.append(user)
    return json({"id": next_id})


@app.route('/users/<str:string>')
async def get_user_by_keyword(request, str):
    str = str.strip().lower()
    if "@" in str:
        for user in users:
            if user["email"].lower() == str:
                return json(user)
    else:
        for user in users:
            if str in user["name"].lower():
                return json(user)
    return json("")


@app.route('/users/<delete_id:int>', methods=['DELETE'])
async def delete_user_by_id(request, delete_id):
    print("delete_id", delete_id)
    for user in users:
        if user["id"] == int(delete_id):
            users.remove(user)
            return json(True)
    return json(False)


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


# Change password
@app.route('/users/change_pass', methods=['POST'])
async def change_pass(request):
    raw = request.json
    user_email = raw["email"].lower()
    new_pass = raw["pass"]
    if len(new_pass) < 6:
        return json({"status": False, "message": "password is too short"})
    
    if not hasNumbers(new_pass):
        return json({"status": False, "message": "password does not contain numerics"})
    
    for user in users:
        if user["email"].lower() == user_email:
            user["pass"] = new_pass
            return json({"status": True, "message": "success"})
    
    # Chạy hết vòng lặp for mà không tìm được thì mới báo lỗi
    return json({"status": False, "message": "user not found"})
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True, auto_reload=True)