from vllm import LLM, SamplingParams
prompts = [
    "<s><|im_start|>user\nHello, my name is<|im_end|>\n<|im_start|>assistant\n",
    "<s><|im_start|>user\nThe president of the United States is<|im_end|>\n<|im_start|>assistant\n",
    "<s><|im_start|>user\nThe capital of France is<|im_end|>\n<|im_start|>assistant\n",
    "<s><|im_start|>user\nThe future of AI is<|im_end|>\n<|im_start|>assistant\n",
]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
llm = LLM(model="WizardLM/WizardLM-70B-V1.0", trust_remote_code=True,
          tensor_parallel_size=4,
          download_dir=)
outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")


# export HF_EVALUATE_OFFLINE=0
# export TRANSFORMERS_OFFLINE=0
# export HF_DATASETS_OFFLINE=0