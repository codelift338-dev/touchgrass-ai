from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

AI_URL = "http://127.0.0.1:8081/v1/chat/completions"


ACTIVITY_PROMPTS = {
    "walking": "notice something interesting along your walk",
    "exploring": "discover something you normally overlook",
    "gardening": "observe plants, soil, insects, or leaves",
    "birdwatching": "listen for or look for birds",
    "photography": "find an interesting natural detail to photograph"
}


def generate_idea(activity, minutes):

    activity_instruction = ACTIVITY_PROMPTS.get(
        activity,
        "notice something interesting in nature"
    )

    prompt = (
        f"Give ONE simple outdoor idea for {minutes} minutes. "
        f"The person is doing {activity}. "
        f"Help them {activity_instruction}. "
        f"Maximum 8 words. No explanation."
    )

    data = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 15
    }

    response = requests.post(
        AI_URL,
        json=data,
        timeout=120
    )

    response.raise_for_status()

    result = response.json()

    idea = result["choices"][0]["message"]["content"].strip()

    return idea


def create_mission(activity, minutes, idea):

    return {
        "title": f"{minutes}-Minute {activity.capitalize()} Mission",

        "steps": [
            f"Start your {activity} outdoors.",
            f"Try this local AI idea: {idea}",
            "Spend one quiet minute noticing nature."
        ],

        "reminder": (
            "📵 Put your screen away and enjoy being outside."
        )
    }


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    data = request.json or {}

    activity = data.get(
        "activity",
        "walking"
    )

    minutes = data.get(
        "minutes",
        10
    )

    try:
        minutes = int(minutes)
    except (TypeError, ValueError):
        minutes = 10

    if minutes < 5:
        minutes = 5

    if minutes > 120:
        minutes = 120

    try:

        idea = generate_idea(
            activity,
            minutes
        )

        mission = create_mission(
            activity,
            minutes,
            idea
        )

        return jsonify({
            "success": True,
            "mission": mission
        })

    except Exception as error:

        print(
            "Generation error:",
            error
        )

        return jsonify({
            "success": False,
            "error": str(error)
        }), 500


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
