from llama_cpp import Llama
import yaml 

class VicaunaLlama:
    config = yaml.safe_load(open('config.yaml'))
    context_limit = config.get('context_limit')
    model = None
    # def __init__(self):
    #     self.config = yaml.safe_load('config.yaml')
    #     self.model = self.load_model()
    #     self.context_limit = self.config.get('context_limit')

    @classmethod
    def load_model(cls):
        if cls.model is None:
            cls.model =  Llama(
                model_path  = cls.config.get('weights'), embedding = True
            )
        return cls.model

    @classmethod
    def tokenize(cls, text: str):
        return cls.model.tokenize(b" " + text.encode('utf-8'))

    @classmethod
    def generate(cls, messages : list, temperature: float = 0.2, top_p : float = 0.95, stream: bool = False, max_tokens = 256 , stop: list = []):
        messages = cls.process_messages(messages[::-1], max_tokens)[::-1]
        return cls.model.create_chat_completion(
            messages,
            temperature=temperature,
            top_p=top_p,
            stream=stream,
            stop=stop,
            max_tokens=max_tokens,
        )

    @classmethod
    def process_messages(cls, messages, max_tokens):
        buffer_tokens = 32
        num_messages = len(messages)

        # tokenize all the messages 
        tokens = [len(cls.tokenize(m["content"])) for m in messages]

        # reduce messages if token length is greater than context size 
        token_count = sum(tokens[:num_messages])
        while token_count + max_tokens + buffer_tokens > cls.context_limit:
            num_messages -= 1
            token_count -= tokens[num_messages]
        return messages[:token_count]

    # @classmethod
    # def embeddings(cls, text):
    #     return cls.model.create_embedding(text)