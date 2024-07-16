import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier


st.header(":blue[Text Classification] ",divider='blue')


file = st.file_uploader("Please upload your train dataset",type=["xlsx"],accept_multiple_files=False)
test_file = st.file_uploader("Please upload your test dataset",type=['xlsx'],accept_multiple_files=False)

if file:
    data = pd.read_excel(file)
    st.write("Your dataset :")
    st.write(data.head())

    col1,col2,col3,col4 = st.columns([1,1,1,1])

    with col1:
        buttonRF = st.button("Random Forest",use_container_width=True)
    with col2:
        buttonLR = st.button("Logistic Regression",use_container_width=True)
    with col3:
        buttonXGB = st.button("XGBoost",use_container_width=True)
    with col4:
        buttonSVC = st.button("Support Vector Classifier",use_container_width=True)

    data = data.dropna()
    data['target'] = data['target'].astype('category').cat.codes

    X= data.drop('target',axis=1)
    y = data['target']

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

    scaller = StandardScaler()
    X_train = scaller.fit_transform(X_train)
    X_test = scaller.transform(X_test)

    if buttonRF:
        model = RandomForestClassifier()
        model.fit(X_train,y_train)

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test,y_pred)

        st.info(f"The accuracy of the model using Random Forest is : {accuracy}")

        if test_file:
            test = pd.read_excel(test_file)
            st.write("Your test set : ")
            st.write(test.head())
            test = scaller.transform(test)
            rftarget = model.predict(test)
            target_labels = data['target'].astype('category').cat.categories
            rftarget_decoded = [target_labels[idx] for idx in rftarget]
            rftarget_df = pd.DataFrame(rftarget_decoded, columns=['Predicted_Target'])
            st.write(rftarget_df)



    if buttonXGB:
        ## Training a model using XG Boost Classifier
        xgb_model = XGBClassifier()
        xgb_model.fit(X_train,y_train)

        y_pred = xgb_model.predict(X_test)
        XGBaccuracy = accuracy_score(y_test, y_pred)

        st.info(f"The accuracy of the model using XGBoost model is : {XGBaccuracy}")

        if test_file:

            test = pd.read_excel(test_file)
            st.write("Your test set : ")
            st.write(test.head())
            test = scaller.transform(test)
            XGBtarget = xgb_model.predict(test)
            target_labels = data['target'].astype('category').cat.categories
            XGBtarget_decoded = [target_labels[idx] for idx in XGBtarget]
            XGBtarget_df = pd.DataFrame(XGBtarget_decoded, columns=['Predicted_Target'])
            st.write(XGBtarget_df)    
    
    if buttonLR:
        model_LR = LogisticRegression()
        model_LR.fit(X_train,y_train)

        y_pred = model_LR.predict(X_test)
        accuracy = accuracy_score(y_test,y_pred)

        st.info(f"The accuracy of the model using Logistic Regression is : {accuracy}")

        if test_file:
            test = pd.read_excel(test_file)
            st.write("Your test set : ")
            st.write(test.head())
            test = scaller.transform(test)
            LRtarget = model_LR.predict(test)
            target_labels = data['target'].astype('category').cat.categories
            LRtarget_decoded = [target_labels[idx] for idx in LRtarget]
            LRtarget_df = pd.DataFrame(LRtarget_decoded, columns=['Predicted_Target'])
            st.write(LRtarget_df)

    if buttonSVC:
        model_SVC = SVC(kernel='rbf')
        model_SVC.fit(X_train,y_train)

        y_pred = model_SVC.predict(X_test)
        accuracy = accuracy_score(y_test,y_pred)

        st.info(f"The accuracy of the model using Support Vector Classifier is : {accuracy}")

        if test_file:
            test = pd.read_excel(test_file)
            st.write("Your test set : ")
            st.write(test.head())
            test = scaller.transform(test)
            SVCtarget = model_SVC.predict(test)
            target_labels = data['target'].astype('category').cat.categories
            SVCtarget_decoded = [target_labels[idx] for idx in SVCtarget]
            SVCtarget_df = pd.DataFrame(SVCtarget_decoded, columns=['Predicted_Target'])
            st.write(SVCtarget_df)