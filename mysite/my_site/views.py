from django.shortcuts import render
from django.http import HttpResponse
import pickle
from xgboost import XGBRegressor,XGBClassifier, plot_importance
import tensorflow as tf
import sklearn
import numpy as np
# Create your views here.
def index1(request):
    val=request.POST
    y=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    x=[]
    x.append(21)
    for i in val:
        if val[i].lower()=="yes" or val[i].lower()=="y":
            x.append(1)
        elif val[i].lower()=="no" or val[i].lower()=="no":
            x.append(0)
        else:
            continue
    if len(y)!=len(x):
        x=y
    model=pickle.load(open("model.sav","rb"))
    y=pickle.load(open("scalar.sav","rb"))
    # x=np.array(x)
    # print(x.shape)
    # x=y.transform(x.reshape(-1,1)
    y_pred=model.predict([x])

    model=tf.keras.models.load_model("my_site/model1.h5")
    pred=model.predict([x])
    print(pred)
    pred=int(np.round(pred[0,0]))
    target_names = ['YOU MIGHT NOT BE DIABETIC', 'YOU MIGHT BE DIABTETIC']
    z=False
    if target_names[pred]=='YOU MIGHT BE DIABTETIC':
        z=True
    context={"val":val,"user":True,"ans":target_names[pred],"z":z}
    print(context)
    return render(request,"index.html",context=context)
