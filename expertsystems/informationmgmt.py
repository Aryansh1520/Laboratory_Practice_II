knowledge_base = {
    "question_1":"answer_1",
    "question_2":"answer_2",
    "question_3":"answer_3",
    "question_4":"answer_4"

}
def return_answer(question):
    for kb_ques in knowledge_base:
        if question in kb_ques:
            return knowledge_base[kb_ques]
    return None
def main():
    while True:
        question = input("What do you want to know about information management? ")
        answer = return_answer(question)
        if answer is not None:
            print(answer)
        else:
            print("I don't know the answer to that question.")
main()
