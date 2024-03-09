from flask import Flask, jsonify, render_template, request
from utils import SalaryPrediction
import config2

app = Flask(__name__)

########################################################################################
################################## Home API ############################################
########################################################################################

@app.route('/')
def salary_pred_model():
    print('Welcome to the Salary Prediction Model')
    return render_template('index2.html')

########################################################################################
################################## Model API ############################################
########################################################################################

@app.route('/predict_salary', methods = ['POST','GET'])
def get_required_info():
    if request.method == 'POST':
        print('We are in POST method')
        data = request.form
        Total_Experience = eval(data['Total_Experience'])
        Team_Lead_Experience = eval(data['Team_Lead_Experience'])
        Project_Manager_Experience = eval(data['Project_Manager_Experience'])
        Certifications =  eval(data['Certifications'])
        print(f'Total_Experience={Total_Experience},Team_Lead_Experience={Team_Lead_Experience},Project_Manager_Experience={Project_Manager_Experience},Certifications={Certifications}')
        
        salary = SalaryPrediction(Total_Experience,Team_Lead_Experience,Project_Manager_Experience,Certifications)
        salary_pred = salary.get_predicted_salary()
        # return jsonify({'Result':f'Predicted Salary is: RS. {round(salary_pred,2)}'})
        prediction_text = round(salary_pred,2)
        return render_template('index2.html',prediction_text='Predicted Salary is RS: {}'.format(prediction_text))
    
    else:
        print('We are in GET method')
        data1 = request.args
        Total_Experience = eval(data1.get('Total_Experience'))
        Team_Lead_Experience = eval(data1.get('Team_Lead_Experience'))
        Project_Manager_Experience = eval(data1.get('Project_Manager_Experience'))
        Certifications =  eval(data1.get('Certifications'))
        print(f'Total_Experience={Total_Experience},Team_Lead_Experience={Team_Lead_Experience},Project_Manager_Experience={Project_Manager_Experience},Certifications={Certifications}')
        
        salary1 = SalaryPrediction(Total_Experience,Team_Lead_Experience,Project_Manager_Experience,Certifications)
        salary_pred1 = salary1.get_predicted_salary()
        return jsonify({'Result':f'Predicted Salary is: RS. {round(salary_pred1,2)}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=config2.PORT_NUMBER, debug=True)    