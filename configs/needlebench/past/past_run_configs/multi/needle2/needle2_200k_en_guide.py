from mmengine.config import read_base
with read_base():
    from ...base import needle2_datasets_200k_en
    from ...base import chat_models_200k_en
    from ...base import infer, eval

datasets = [*needle2_datasets_200k_en]
models = [*chat_models_200k_en]