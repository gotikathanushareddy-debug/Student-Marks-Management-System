from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    return "Fail"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()
    marks = data.get("marks", [])

    if not name:
        return jsonify({"error": "Please enter the student's name."}), 400

    if not isinstance(marks, list) or len(marks) != 3:
        return jsonify({"error": "Please enter marks for all 3 subjects."}), 400

    try:
        marks = [float(mark) for mark in marks]
    except (TypeError, ValueError):
        return jsonify({"error": "Marks must be valid numbers."}), 400

    if any(mark < 0 or mark > 100 for mark in marks):
        return jsonify({"error": "Each subject mark must be between 0 and 100."}), 400

    total = sum(marks)
    average = total / 3
    grade = calculate_grade(average)

    return jsonify({
        "name": name,
        "marks": marks,
        "total": total,
        "average": round(average, 2),
        "grade": grade,
        "status": "Pass" if all(mark >= 40 for mark in marks) else "Fail"
    })

if __name__ == "__main__":
    app.run(debug=True)
