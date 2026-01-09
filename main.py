from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated database (for demonstration purposes)
profiles = []
next_id = 1


@app.route("/")
def home():
    return jsonify({
        "service": "ProfileService",
        "status": "Running",
        "description": "Manages user profile data for the Trail Application"
    })


# ---------------------------
# CREATE PROFILE
# ---------------------------
@app.route("/profiles", methods=["POST"])
def create_profile():
    global next_id
    data = request.get_json()

    # Basic validation
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    required_fields = ["full_name", "email", "role_id"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # Create profile object
    profile = {
        "profile_id": next_id,
        "full_name": data["full_name"],
        "email": data["email"],
        "role_id": data["role_id"]
    }

    profiles.append(profile)
    next_id += 1

    return jsonify({
        "message": "Profile successfully created",
        "profile": profile
    }), 201


# ---------------------------
# READ ALL PROFILES
# ---------------------------
@app.route("/profiles", methods=["GET"])
def get_all_profiles():
    return jsonify({
        "count": len(profiles),
        "profiles": profiles
    })


# ---------------------------
# READ PROFILE BY ID
# ---------------------------
@app.route("/profiles/<int:profile_id>", methods=["GET"])
def get_profile(profile_id):
    for profile in profiles:
        if profile["profile_id"] == profile_id:
            return jsonify(profile)

    return jsonify({"error": "Profile not found"}), 404


# ---------------------------
# UPDATE PROFILE
# ---------------------------
@app.route("/profiles/<int:profile_id>", methods=["PUT"])
def update_profile(profile_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    for profile in profiles:
        if profile["profile_id"] == profile_id:

            # Update only provided fields
            if "full_name" in data:
                profile["full_name"] = data["full_name"]

            if "email" in data:
                profile["email"] = data["email"]

            if "role_id" in data:
                profile["role_id"] = data["role_id"]

            return jsonify({
                "message": "Profile successfully updated",
                "profile": profile
            })

    return jsonify({"error": "Profile not found"}), 404


# ---------------------------
# DELETE PROFILE
# ---------------------------
@app.route("/profiles/<int:profile_id>", methods=["DELETE"])
def delete_profile(profile_id):
    for profile in profiles:
        if profile["profile_id"] == profile_id:
            profiles.remove(profile)
            return jsonify({"message": "Profile successfully deleted"})

    return jsonify({"error": "Profile not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)

