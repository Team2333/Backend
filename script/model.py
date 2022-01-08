import torch
import warnings

from transformers import DistilBertTokenizerFast as TokenizerClass
from transformers import DistilBertForSequenceClassification as ModelClass
from transformers_interpret import SequenceClassificationExplainer
from minio_client import DEFAULT_UPDATED_SAVED_WEIGHTS
from pathlib import Path

DISTILBERT_SAVED_WEIGHTS = './distilbert_saved_weights.pt'
class Model:
    def __init__(self, current_saved_weights):
        self.cls_explainer = self.load(current_saved_weights)
    
    def load(self, current_saved_weights):
        model_name = 'distilbert-base-cased'
        tokenizer = TokenizerClass.from_pretrained(model_name)
        tokenizer.do_lower_case = False
        pt_model = ModelClass.from_pretrained(model_name, num_labels=2)
        #load weights of best model
        pt_model.load_state_dict(torch.load(current_saved_weights, map_location=torch.device('cpu')))
        # for explainable AI
        cls_explainer = SequenceClassificationExplainer(
            pt_model, 
            tokenizer)

        print("[Backend]: saved weight currently used is {}".format(current_saved_weights))

        return cls_explainer

    def reload(self, new_saved_weights):
        return self.load(new_saved_weights)

    def get_verification_result(self, news):
        word_attributions = self.cls_explainer(news)
        classification = self.cls_explainer.predicted_class_name
        # print("overall_res:{}".format(classification))
        if (classification == "LABEL_0"):
            overall_result = True
        else:
            overall_result = False
        return word_attributions, overall_result

DistilBERT_model = Model(DISTILBERT_SAVED_WEIGHTS)