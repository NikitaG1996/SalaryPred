import pickle
import json
import numpy as np
import config2

class SalaryPrediction():
    def __init__(self, Total_Experience, Team_Lead_Experience,Project_Manager_Experience,Certifications):
        self.Total_Experience = Total_Experience
        self.Team_Lead_Experience = Team_Lead_Experience
        self.Project_Manager_Experience = Project_Manager_Experience
        self.Certifications = Certifications
        
    def load_model(self):
        with open(config2.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)
            
        with open(config2.JSON_FILE_PATH,'r') as f:
            self.project_data = json.load(f)
            
    def get_predicted_salary(self):
        self.load_model()
        
        test_array = np.zeros(len(self.project_data['columns']))
        test_array[0] = self.Total_Experience
        test_array[1] = self.Team_Lead_Experience
        test_array[2] = self.Project_Manager_Experience
        test_array[3] = self.Certifications
        
        print('Test Array:', test_array)
        predicted_salary = self.model.predict([test_array])[0]
        print(f'Predicted Salary is: RS. {round(predicted_salary,2)}')
        return predicted_salary
    
if __name__ == '__main__':
    Total_Experience = 4
    Team_Lead_Experience = 3
    Project_Manager_Experience = 4
    Certifications = 2
    salary_pred = SalaryPrediction(Total_Experience,Team_Lead_Experience,Project_Manager_Experience,Certifications)
    salary_pred.get_predicted_salary()        