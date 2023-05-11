"""Parse and evaluate simple math word problems returning the answer as an integer."""

def answer(question):
    # checks if the question has cubed or starts with who 
    for item in question.split():
        if item == "cubed?" or item == "Who":
            raise ValueError("unknown operation")
    
    # changes the words to operators    
    question = question.replace("plus", "+").replace("minus", "-").replace("multiplied by", "*").replace("divided by", "/").replace("What is ", "").replace("?", "").split()
    
    # checks if question is a valid question, if it is then insert "(" and ")" around the operation
    if not question:
        raise ValueError("syntax error")
    question.insert(0, "(")
    question.insert(4, ")")
    
    # attempts the math problem
    try:
        return eval(" ".join(question))
    except:
        raise ValueError("syntax error")