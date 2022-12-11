from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

def prediction(lst):
    filename = 'model/RFpredictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value


def udariprediction(lst):
    filename = 'model/Churnmodel.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    Udaripred_value = model.predict([lst])
    return Udaripred_value   


def thisumprediction(lst):
    filename = 'model/elective.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    tpred_value = model.predict([lst])
    return tpred_value 

def Aprediction(lst):
    filename = 'model/RFApredictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    Apred_value = model.predict([lst])
    return Apred_value

def predictionClass(list):
    filename = 'model/RandomForestpredictor.pickle'
    with open(filename, 'rb') as file:
        model2 = pickle.load(file)
    pred_value_class = model2.predict([list])
    return pred_value_class


@app.route('/')
def interface_Home():
  return render_template('home.html')    

@app.route('/index',methods=['POST', 'GET'])
def index():
    
     pred_value = 0
     
     if request.method == 'POST':
          gpa = request.form['gpa']
          dsa = request.form['dsa']
          itp = request.form['itp']
          ps = request.form['ps']
          mad = request.form['mad']
          mc = request.form['mc']
          oop = request.form['oop']
          rate = request.form['rate']
          rp = request.form['rp']

          feature_list = []
 
          feature_list.append(float(gpa))
          feature_list.append(int(dsa))
          feature_list.append(int(itp))
          feature_list.append(int(ps))
          feature_list.append(int(mad))
          feature_list.append(int(mc))
          feature_list.append(int(oop))
          feature_list.append(int(rate))
          feature_list.append(int(rp))

          pred_value = prediction(feature_list)

          if(pred_value == 1):
            pred_value = 'information technology'

          if(pred_value == 2):
            pred_value = 'Software Engineer'

          if(pred_value == 3):
            pred_value = 'Data Science'  
          
          
     return render_template("index.html", pred_value = pred_value)

@app.route('/udari_index', methods=['POST', 'GET'])
def udari_index():
    pred = "null"
    if request.method == 'POST':
        EAP_English = request.form['EAP_English']
        IP = request.form['IP']
        mc = request.form['mc']
        OOP = request.form['OOP']
        Specialization = request.form['Specialization']
        Degree = request.form['Degree']
        scholarship = request.form['scholarship']
        InternshipJob = request.form['InternshipJob']
        RepeatProrata = request.form['RepeatProrata']
        RepeatProrataCount = request.form['RepeatProrataCount']
        GPA = request.form['GPA']
        
        udarifeature_list = []

        udarifeature_list.append(int(EAP_English))
        udarifeature_list.append(int(IP))
        udarifeature_list.append(int(mc))
        udarifeature_list.append(int(OOP))
        udarifeature_list.append(int(Specialization))
        udarifeature_list.append(int(Degree))
        udarifeature_list.append(int(scholarship))
        udarifeature_list.append(int(InternshipJob))
        udarifeature_list.append(int(RepeatProrata))
        udarifeature_list.append(int(RepeatProrataCount))
        udarifeature_list.append(float(GPA))

        pred = udariprediction(udarifeature_list)

    if(pred == 0):
        pred =' Distinctive'
    if(pred == 1):
        pred ='Very Good'
    if(pred == 2):
        pred =' Good Standing' 
    if(pred == 3):
        pred ='at Risk of dropout'
    if(pred == 4):
        pred ='near At Risk of dropout'
    if(pred == 5):
        pred ='OOps...! Try to find better suitable specialization'


    return render_template("udari_index.html",pred = pred)


@app.route('/tindex',methods=['POST', 'GET'])
def tindex():
    
     tpred_value = 0
     
     if request.method == 'POST':
          gpa = request.form['gpa']
          special = request.form['special']
          ra = request.form['ra']
          ia = request.form['ia']
          rate = request.form['rate']
          rp = request.form['rp']

          tfeature_list = []
 
          tfeature_list.append(float(gpa))
          tfeature_list.append(int(special))
          tfeature_list.append(int(ra))
          tfeature_list.append(int(ia))
          tfeature_list.append(int(rate))
          tfeature_list.append(int(rp))

          tpred_value = thisumprediction(tfeature_list)

          if(tpred_value == 1111):
            tpred_value = 'Internet of Things'

          if(tpred_value == 2222):
            tpred_value = 'Machine Learning'

          if(tpred_value == 3333):
            tpred_value = 'Software Quality Assurance'  

          if(tpred_value == 4444):
            tpred_value = 'Deep Learning'   

          if(tpred_value == 5555):
            tpred_value = 'Knowledge Management'  

          if(tpred_value == 6666):
            tpred_value = 'Parallel Computing'  

          if(tpred_value == 7777):
            tpred_value = 'Innovation Management & Entrepreneurship'  

          if(tpred_value == 888):
            tpred_value = 'Cloud Computing'  

          if(tpred_value == 999):
            tpred_value = 'Database Administration'
  
          

     return render_template("tindex.html", tpred_value = tpred_value)

@app.route('/Aindex', methods=['POST', 'GET'])
def Aindex():

    Apred_value = "null"
    pred_value_class = "null"


    if request.method == 'POST':
        FollowedCourses = request.form['FollowedCourses']
        OLevelScience = request.form['OLevelScience']
        OLevelMaths = request.form['OLevelMaths']
        OLevelEnglish = request.form['OLevelEnglish']
        OLevelSinhala = request.form['OLevelSinhala']
        OLevelIct = request.form['OLevelIct']
        ALevelStream = request.form['ALevelStream']
        ALevelSubject1 = request.form['ALevelSubject1']
        ALevelSubject2 = request.form['ALevelSubject2']
        ALevelSubject3 = request.form['ALevelSubject3']
        ALevelGeneralEnglish = request.form['ALevelGeneralEnglish']
        
        


        Afeature_list = []

        Afeature_list.append(len(FollowedCourses))
        Afeature_list.append(len(OLevelScience))
        Afeature_list.append(len(OLevelMaths))
        Afeature_list.append(len(OLevelEnglish))
        Afeature_list.append(len(OLevelSinhala))
        Afeature_list.append(len(OLevelIct))
        Afeature_list.append(len(ALevelStream))
        Afeature_list.append(len(ALevelSubject1))
        Afeature_list.append(len(ALevelSubject2))
        Afeature_list.append(len(ALevelSubject3))
        Afeature_list.append(len(ALevelGeneralEnglish))
        

        Apred_value = Aprediction(Afeature_list)
        print(Apred_value)


        feature_list2 = []

        feature_list2.append(len(FollowedCourses))
        feature_list2.append(len(OLevelScience))
        feature_list2.append(len(OLevelMaths))
        feature_list2.append(len(OLevelEnglish))
        feature_list2.append(len(OLevelSinhala))
        feature_list2.append(len(OLevelIct))
        feature_list2.append(len(ALevelStream))
        feature_list2.append(len(ALevelSubject1))
        feature_list2.append(len(ALevelSubject2))
        feature_list2.append(len(ALevelSubject3))
        feature_list2.append(len(ALevelGeneralEnglish))
        feature_list2.append(int(Apred_value))

        pred_value_class = predictionClass(feature_list2)
        print(pred_value_class)

        if(pred_value_class == 0):
            pred_value_class = 'First Class'
        if(pred_value_class == 1):
            pred_value_class = 'Lower Second Class'
        if(pred_value_class == 2):
            pred_value_class = 'Pass'
        if(pred_value_class == 3):
            pred_value_class = 'Upper Second Class'

        if(Apred_value == 0):
            return render_template("interface_CS.html", pred_value_class = pred_value_class)

        if(Apred_value == 1):
            return render_template("interface_DS.html", pred_value_class = pred_value_class)
            
        if(Apred_value == 2):
            return render_template("interface_ISE.html", pred_value_class = pred_value_class)
        
        if(Apred_value == 3):
            return render_template("interface_IT.html", pred_value_class = pred_value_class)

        if(Apred_value == 4):
            return render_template("interface_SE.html", pred_value_class = pred_value_class)

        

        
    return render_template("Aindex.html", Apred_value = Apred_value)

@app.route('/Stu_login')
def Stu_login():
  return render_template('Stu_login.html')  
  

if __name__ == '__main__': 
    app.run(debug=True)