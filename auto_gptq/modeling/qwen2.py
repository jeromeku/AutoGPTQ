from ._base import *


class Qwen2GPTQForCausalLM(BaseGPTQForCausalLM):
    layer_type = "Qwen2DecoderLayer"
    layers_block_name = "model.layers"
    outside_layer_modules = ["model.embed_tokens", "model.norm"]
    inside_layer_modules = [
        ["self_attn.k_proj", "self_attn.v_proj", "self_attn.q_proj"],
        ["self_attn.o_proj"],
        ["mlp.up_proj", "mlp.gate_proj"],
        ["mlp.down_proj"],
    ]


__all__ = ["Qwen2GPTQForCausalLM"]