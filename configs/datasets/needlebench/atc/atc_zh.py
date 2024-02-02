from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.datasets.needlebench.atc import NeedleBenchATCDataset
from opencompass.datasets.needlebench.origin import NeedleBenchOriginEvaluator
from opencompass.datasets.needlebench.origin import needlebench_postprocess
from opencompass.datasets.needlebench.origin import needlebench_dataset_postprocess

needlebench_reader_cfg = dict(input_columns=['prompt'], output_column='answer')

needlebench_infer_cfg = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            round=[
                dict(role='HUMAN', prompt='{prompt}'),
                dict(role='BOT', prompt='{answer}\n'),
            ]
        )
        ),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=GenInferencer))

needlebench_eval_cfg = dict(
    evaluator=dict(type=NeedleBenchOriginEvaluator),
    pred_postprocessor=dict(type=needlebench_postprocess),
    dataset_postprocessor=dict(type=needlebench_dataset_postprocess),
    pred_role='BOT')

needle_num_list = list(range(2, 50, 3))
document_depth_percent_intervals = 20
repeats = 10

needlebench_atc_datasets = []

for num_needles in needle_num_list:
    dataset_dict = {
        'abbr': f'needlebench_atc_challenge'
                f'needle_{num_needles}_zh',
        'type': NeedleBenchATCDataset,
        # 'path': base_path,
        'num_needles': num_needles,
        'language': 'Chinese',
        'repeats': repeats,
        'reader_cfg': needlebench_reader_cfg,
        'infer_cfg': needlebench_infer_cfg,
        'eval_cfg': needlebench_eval_cfg
    }
    needlebench_atc_datasets.append(dataset_dict)
