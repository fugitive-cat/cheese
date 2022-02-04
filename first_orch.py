from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline

class orchestrator:
    def __init__(self, name: str, qfile: str, cfile: str, model_name: str, task: str):
        self.name = name
        self.questiondb = database(qfile)
        self.contextdb = database(cfile)
        self.inferencepipeline = inferencepipeline(model_name,model_name, task)

    def answerQuestion(self, number: int): #execute
        return self.inferencepipeline.answer(self.questiondb.getstory(number), self.contextdb.getstory(number))
        
class database:
    """
        this just assumes stories
        are in a txt file seperated
        by line breaks... WIP
    """
    
    def __init__(self, base: str):
        self.base = base

    def infile(self):
        with open(self.base, 'r', encoding='utf-8') as file:
            all_data = file.read()
        return all_data

    def splitstories(self):
            return self.infile().split('\n')
        
    def getstory(self, number: int):
        return self.splitstories()[number]

class inferencepipeline:
    def __init__(self, tokenizer: str, model: str, pipelineName: str):
        
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer)
        self.model = AutoModelForQuestionAnswering.from_pretrained(model)
        self.nlp = pipeline(pipelineName, model=self.model, tokenizer=self.tokenizer)

    def answer(self, question: str, context: str):
        QAinput = {
            'question': question,
            'context': context
            }
        return self.nlp(QAinput)
        
a = orchestrator('name','questions.txt','context.txt',"deepset/roberta-base-squad2",'question-answering')
print(a.answerQuestion(1)) # put this in a webpage
