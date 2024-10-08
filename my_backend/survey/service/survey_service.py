from abc import ABC, abstractmethod

class SurveyService(ABC):
    @abstractmethod
    def createSurvey(self, title, description):
        pass

    @abstractmethod
    def createSurveyQuestion(self, survey_id, question_text, survey_type):
        pass

    @abstractmethod
    def saveAnswer(self, answers, account_Id):
        pass

    @abstractmethod
    def listAnswer(self, type, survey_id=None, question_id=None, account_id=None):
        pass