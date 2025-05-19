from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.decimal128 import Decimal128
from bson.objectid import ObjectId
from datetime import datetime


app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://kikyoumaru02:iTVGCtbBIcne2fXx@cluster0.yiutn.mongodb.net/")
db = client["sample_airbnb"]
collection = db["listingsAndReviews"]

# Convert MongoDB types to JSON-serializable Python types
def clean_mongo_document(doc):
    if isinstance(doc, dict):
        return {key: clean_mongo_document(value) for key, value in doc.items()}
    elif isinstance(doc, list):
        return [clean_mongo_document(item) for item in doc]
    elif isinstance(doc, Decimal128):
        return float(doc.to_decimal())
    elif isinstance(doc, ObjectId):
        return str(doc)
    elif isinstance(doc, datetime):
        return doc.isoformat()
    else:
        return doc

# Root endpoint
@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Airbnb Flask API is running!"})

# Get multiple listings (limit with ?limit=xx)
@app.route("/listings", methods=["GET"])
def get_listings():
    limit = int(request.args.get("limit", 50))
    raw_listings = collection.find({}, {
        "_id": 1,
        "name": 1,
        "price": 1,
        "address.country": 1,
        "description": 1,
        "review_scores.review_scores_rating": 1
    }).limit(limit)
    listings = [clean_mongo_document(doc) for doc in raw_listings]
    return jsonify(listings)

# Get detailed information for a single listing by ID
@app.route("/listings/<listing_id>", methods=["GET"])
def get_listing(listing_id):
    listing = collection.find_one({"_id": listing_id})
    if listing:
        return jsonify(clean_mongo_document(listing))
    return jsonify({"error": "Listing not found"}), 404

# Search listings
@app.route("/listings/search", methods=["GET"])
def search_listings():
    country = request.args.get("country")
    min_price = float(request.args.get("min_price", 0))

    query = {
        "address.country": country,
        "price": {"$gte": min_price}
    }

    raw_listings = collection.find(query, {
        "_id": 1,
        "name": 1,
        "price": 1,
        "address.country": 1,
        "review_scores.review_scores_rating": 1
    }).limit(50)

    listings = [clean_mongo_document(doc) for doc in raw_listings]
    return jsonify(listings)

# Get reviews for a listing
@app.route("/listings/<listing_id>/reviews", methods=["GET"])
def get_reviews(listing_id):
    listing = collection.find_one({"_id": listing_id}, {"_id": 0, "reviews": 1})
    if listing and "reviews" in listing:
        return jsonify(clean_mongo_document(listing["reviews"]))
    return jsonify({"error": "No reviews found or listing does not exist"}), 404

# Add a review (mock implementation)
@app.route("/reviews", methods=["POST"])
def post_review():
    data = request.json
    listing_id = data.get("listing_id")
    reviewer_name = data.get("reviewer_name", "Anonymous")
    comments = data.get("comments", "")
    review_id = str(ObjectId())
    review_date = datetime.utcnow()

    if not listing_id or not comments:
        return jsonify({"error": "listing_id and comments are required"}), 400

    new_review = {
        "_id": review_id,
        "date": review_date,
        "reviewer_name": reviewer_name,
        "comments": comments
    }

    result = collection.update_one(
        {"_id": listing_id},
        {"$push": {"reviews": new_review}}
    )

    if result.modified_count == 1:
        return jsonify({"message": "Review added successfully", "review": clean_mongo_document(new_review)}), 201
    else:
        return jsonify({"error": "Listing not found or review not added"}), 400


# Delete the review
@app.route("/listings/<listing_id>/reviews/<review_id>", methods=["DELETE"])
def delete_review(listing_id, review_id):
    result = collection.update_one(
        {"_id": listing_id},
        {"$pull": {"reviews": {"_id": review_id}}}
    )

    if result.modified_count == 1:
        return jsonify({"message": "Review deleted successfully"}), 200
    else:
        return jsonify({"error": "Review not found or already deleted"}), 404


# Start the server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
