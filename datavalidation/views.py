"""Business logic of the project."""
# from urllib import response
import os
import pandas as pd
from django.shortcuts import render, redirect
from django.http import FileResponse
from .settings import BASE_DIR
from .utils import handle_uploaded_file, process

def home(request):
    """To load the homepage"""
    return render(request, 'home.html',{})

def file_process(request):
    """Handles file processing."""
    try:
        if request.method == "POST":
            file1 = request.FILES["formFile1"]
            file2 = request.FILES["formFile2"]
            handle_uploaded_file(file1)
            handle_uploaded_file(file2)
            process(file1, file2)
            img = open('op.txt', 'rb')
            response = FileResponse(img)
            return response
        return redirect('/')
    except Exception as exc:
        return render(request,'error.html',{'error':exc})

def excel_process(request):
    """Handle excel files"""
    try:
        if request.method == "POST":
            file1 = request.FILES["formFile1"]
            file2 = request.FILES["formFile2"]
            df1 = pd.read_excel(file1)
            df2 = pd.read_excel(file2)
            merge_df = pd.merge(df1, df2, how="outer", indicator="Exist")
            compare_results = merge_df.loc[merge_df["Exist"] != "both"]
            compare_results.to_csv(os.path.join(BASE_DIR,"fileuploaded","mergereport.csv"), index=False)
            resp = open(os.path.join(BASE_DIR,"fileuploaded","mergereport.csv"),'rb')
            response = FileResponse(resp)
            return response
    except Exception as exc:
        return render(request,'error.html',{'error':exc})