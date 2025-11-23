from llava.model.builder import load_pretrained_model
from llava.mm_utils import get_model_name_from_path
from llava.eval.run_llava import eval_model

model_path = "liuhaotian/llava-v1.5-7b"


# Load model (first time will download)
tokenizer, model, image_processor, context_len = load_pretrained_model(
    model_path=model_path,
    model_base=None,
    model_name=get_model_name_from_path(model_path)
)



# Test with an image
args = type('Args', (), {
    "model_path": model_path,
    "model_base": None,
    "model_name": get_model_name_from_path(model_path),
    "query": "What is the color or the cat?",
    "conv_mode": None,
    "image_file": "https://llava-vl.github.io/static/images/view.jpg",
    "sep": ",",
    "temperature": 0,
    "top_p": None,
    "num_beams": 1,
    "max_new_tokens": 512
})()





eval_model(args)




# import torch
# from transformers import AutoModelForCausalLM

# m = AutoModelForCausalLM.from_pretrained("liuhaotian/llava-v1.5-7b", torch_dtype=torch.bfloat16, device_map="cpu")
# total = sum(p.numel() for p in m.parameters())
# trainable = sum(p.numel() for p in m.parameters() if p.requires_grad)
# print("name:", m.config._name_or_path)
# print("hidden_size:", m.config.hidden_size, "n_layers:", m.config.num_hidden_layers)
# print("total params:", total/1e9, "B")
# print("trainable params:", trainable/1e9, "B")