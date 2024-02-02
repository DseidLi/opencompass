from mmengine.config import read_base
with read_base():
    from ..base import cdme4kto8k_parallel_datasets_cn
    from ..base import chat_models_8k_cn, chat_models_32k_cn
    from ..base import parallel_infer as infer
    from ..base import eval as eval

datasets = [*cdme4kto8k_parallel_datasets_cn]
models = [*chat_models_8k_cn, *chat_models_32k_cn]