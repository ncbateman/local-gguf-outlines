from transformers.modeling_outputs import CausalLMOutputWithPast
from transformers import PretrainedConfig, PreTrainedModel
import torch

class Model(PreTrainedModel):
    def __init__(self, config: PretrainedConfig, llm):
        config.vocab_size = llm.vocab_size
        config.eos_token_id = llm.eos_token_id
        config.pad_token_id = llm.eos_token_id
        super().__init__(config)
        self._llm = llm
        self._past = []

    def prepare_inputs_for_generation(
        self,
        input_ids,
        attention_mask=None,
        **kwargs,
    ):
        return {"input_ids": input_ids}

    def forward(
        self,
        input_ids=None,
        return_dict=None,
        **kwargs,
    ):
        llm = self._llm
        tokens = input_ids.flatten().tolist()
        n_past = len(self._past)
        if tokens[:n_past] == self._past:
            self._past = tokens
            tokens = tokens[n_past:]
        else:
            self._past = tokens
            llm.reset()
        llm.eval(tokens)
        logits = torch.tensor(llm.logits).reshape([1, 1, -1])
        if not return_dict:
            return (logits,)
        return CausalLMOutputWithPast(logits=logits)

    @property
    def device(self) -> torch.device:
        return torch.device("cpu")