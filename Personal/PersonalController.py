from __main__ import app
from flask import Flask, jsonify, request

@app.route('/api/user/pm', methods=['POST'])
def personalMessageNotification():
    topic:str = "topic/user/pm"
    return "", 201

@app.route('/api/user/weekly-report', methods=['POST'])
def weeklyReportNotification():
    topic:str = "topic/user/weekly-report"
    return "", 201