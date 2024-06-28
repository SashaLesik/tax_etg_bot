from flask import Flask, request, jsonify, make_response
from answer_with_llm import answer
from loguru import logger
app = Flask(__name__)


# curl localhost:5005/llm_query -d '{"query": "Сколько налог в Сербии?"}' -H 'Content-Type: application/json'
@app.route('/llm_query', methods=['POST'])
def llm_query():
    logger.debug(f'instide')
    data = request.get_json()
    query = data['query']
    logger.debug(f'query {query}')
    response = answer(query)
    logger.debug(f'got response {response}')
    return jsonify(response)