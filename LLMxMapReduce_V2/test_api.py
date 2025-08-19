from request import RequestWrapper


request_pool = RequestWrapper(
    model="qwen-plus-latest", infer_type="OpenAI"
)

prompt = "What is the capital of France?"

response = request_pool.completion(prompt)
print(response)
