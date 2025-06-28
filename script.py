import openai
import azure.functions as func
import json

openai.api_key = "8KNRfvH4kolBGavFRRvWBXlfF0aK84vgBrDxWPHY5da2TsNzFzDHJQQJ99BFAC5RqLJXJ3w3AAAAACOGbD5o"
endpoint = "https://albertodiogoproject-exa-resource.cognitiveservices.azure.com/openai/deployments/albertodiogogpt-35-turbo_exame/chat/completions?api-version=2025-01-01-preview"
deployment_id = "albertodiogogpt-35-turbo_exame"

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
        prompt = body.get("message", "")

        response = openai.ChatCompletion.create(
            engine=deployment_id,
            messages=[{"role": "user", "content": prompt}],
            api_base=endpoint,
            api_version="2023-05-15",
        )

        reply = response['choices'][0]['message']['content']
        return func.HttpResponse(json.dumps({"reply": reply}), mimetype="application/json")

    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
