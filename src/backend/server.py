from flask import Flask, request, jsonify
from controller import SapientiaLuxController

from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch

model = AutoModelForTokenClassification.from_pretrained("google/mobilebert-uncased")
tokenizer = AutoTokenizer.from_pretrained("google/mobilebert-uncased")
dummy_input = tokenizer("He go to school", return_tensors="pt")
torch.onnx.export(model, (dummy_input['input_ids'], dummy_input['attention_mask']),
                  "models/mobilebert.onnx", opset_version=11)

app = Flask(__name__)
controller = SapientiaLuxController()

@app.route('/correct', methods=['POST'])
def correct():
    data = request.json
    result = controller.process_request("grammar", data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5000)