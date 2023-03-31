
import pickle,json
import numpy as np
class Churn():

    def __init__(self,data):
        self.data = data

    def load_model(self):
        with open("churn_model.pkl","rb") as f:
            self.model = pickle.load(f)

        with open("model_data.json","r") as f:
            self.model_data = json.load(f)
        
    def predict_churn(self):
        self.load_model()


        test_array = np.zeros(len(self.model_data["Features"]))
        
        test_array[0]=int(self.data["SeniorCitizen"])

        test_array[1]=int(self.data["tenure"])

        gender_index = self.model_data["Features"].index("gender_"+self.data["gender"])
        test_array[gender_index]=1

        Partner_index = self.model_data["Features"].index("Partner_"+self.data["Partner"])
        test_array[Partner_index]=1

        Dependents_index = self.model_data["Features"].index("Dependents_"+self.data["Dependents"])
        test_array[Dependents_index]=1

        PhoneService_index = self.model_data["Features"].index("PhoneService_"+self.data["PhoneService"])
        test_array[PhoneService_index]=1

        MultipleLines_index = self.model_data["Features"].index("MultipleLines_"+self.data["MultipleLines"])
        test_array[MultipleLines_index]=1

        InternetService_index = self.model_data["Features"].index("InternetService_"+self.data["InternetService"])
        test_array[InternetService_index]=1

        OnlineSecurity_index = self.model_data["Features"].index("OnlineSecurity_"+self.data["OnlineSecurity"])
        test_array[OnlineSecurity_index]=1

        OnlineBackup_index = self.model_data["Features"].index("OnlineBackup_"+self.data["OnlineBackup"])
        test_array[OnlineBackup_index]=1

        DeviceProtection_index = self.model_data["Features"].index("DeviceProtection_"+self.data["DeviceProtection"])
        test_array[DeviceProtection_index]=1

        TechSupport_index = self.model_data["Features"].index("TechSupport_"+self.data["TechSupport"])
        test_array[TechSupport_index]=1

        StreamingTV_index = self.model_data["Features"].index("StreamingTV_"+self.data["StreamingTV"])
        test_array[StreamingTV_index]=1

        StreamingMovies_index = self.model_data["Features"].index("StreamingMovies_"+self.data["StreamingMovies"])
        test_array[StreamingMovies_index]=1

        Contract_index = self.model_data["Features"].index("Contract_"+self.data["Contract"])
        test_array[Contract_index]=1

        PaperlessBilling_index = self.model_data["Features"].index("PaperlessBilling_"+self.data["PaperlessBilling"])
        test_array[PaperlessBilling_index]=1

        PaymentMethod_index = self.model_data["Features"].index("PaymentMethod_"+self.data["PaymentMethod"])
        test_array[PaymentMethod_index]=1

        ischurn = self.model.predict([test_array])[0]

        #return test_array

        if ischurn==0:
            return "Negetive"
        else:
            return "Positive"



















            





            

        
        
        
