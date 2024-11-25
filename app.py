from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

# List of funny fortunes
funny_fortunes = [
    "You will find a missing sock today.",
    "A surprise is waiting for you... in the fridge.",
    "You will achieve great things... unless you nap first.",
    "Your pet secretly judges you. Just kidding! Or am I?",
    "Don’t trust the next person who offers you cake.",
    "A fortune cookie app told me to say hi. So, hi!",
    "You’ll soon realize you’re reading this instead of working.",
    "A random stranger thinks you’re cool. (It’s me.)",
    "Today is your lucky day. Tomorrow? Maybe not.",
    "An exciting journey awaits... probably to the snack aisle."
]

# HTML template
template = """
<!DOCTYPE html>
<html>
<head>
    <title>Funny Fortune App</title>
</head>
<body>
    <h1>Welcome to the Funny Fortune App!</h1>
    <form method="POST">
        <button type="submit">Get Your Fortune!</button>
    </form>
    {% if fortune %}
        <h2>Your Fortune: {{ fortune }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def fortune():
    fortune = None
    if request.method == "POST":
        # Generate a random funny fortune
        fortune = random.choice(funny_fortunes)
    return render_template_string(template, fortune=fortune)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
